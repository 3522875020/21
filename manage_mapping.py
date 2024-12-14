import logging
import click
from utils.mapping_manager import mapping_manager

# 配置日志
logging.basicConfig(level=logging.INFO)

@click.group()
def cli():
    """微信-飞书映射管理工具"""
    pass

@cli.command()
@click.argument('source_id')
@click.argument('name')
@click.option('--type', default='group', type=click.Choice(['group', 'user']))
def add(source_id, name, type):
    """添加新的映射关系"""
    chat_id = mapping_manager.add_mapping(source_id, name, type)
    if chat_id:
        click.echo(f"映射添加成功: {source_id} -> {chat_id}")
    else:
        click.echo("映射添加失败")

@cli.command()
def list():
    """列出所有映射关系"""
    import sqlite3
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT source_id, target_id, name, type FROM chat_mappings")
    mappings = cursor.fetchall()
    
    if not mappings:
        click.echo("没有找到任何映射关系")
        return
        
    click.echo("\n当前映射关系:")
    for mapping in mappings:
        click.echo(f"[{mapping[3]}] {mapping[2]}")
        click.echo(f"  微信: {mapping[0]}")
        click.echo(f"  飞书: {mapping[1]}\n")
    
    conn.close()

@cli.command()
def import_default():
    """导入默认映射关系"""
    from config.mappings import DEFAULT_MAPPINGS
    
    for mapping in DEFAULT_MAPPINGS:
        chat_id = mapping_manager.add_mapping(
            mapping['source_id'],
            mapping['name'],
            mapping['type']
        )
        if chat_id:
            click.echo(f"导入映射成功: {mapping['source_id']} -> {chat_id}")
        else:
            click.echo(f"导入映射失败: {mapping['source_id']}")

if __name__ == '__main__':
    cli() 