---
title: Gewechat copy
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# Gewechat copy

Base URLs:

# Authentication

# 基础API/登录模块

## POST 获取登录二维码(步骤2) 

POST /login/getLoginQrCode

- appId参数为设备ID，首次登录传空，会自动触发创建设备，掉线后重新登录则必须传接口返回的appId，注意**同一个号避免重复创建设备**，以免触发官方风控
- **取码时传的appId需要与上次登录扫码的微信一致，否则会导致登录失败**
- 响应结果中的qrImgBase64为微信二维码图片的base64，前端需要**将二维码图片展示给用户并进行手机扫码操作**（PS: **扫码后调用步骤2，手机上才显示登录**）。（或使用响应结果中的qrData生成二维码）

> Body 请求参数

```json
{
  "appId": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID，首次登录传空，之后传接口返回的appId|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "appId": "wx_wR_U4zPj2M_OTS3BCyoE4",
    "qrData": "http://weixin.qq.com/x/4dmHZZMtoLbHoLZwd1wE",
    "qrImgBase64": "data:image/jpg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/wAALCAJaAloBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/AP1Toooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooor8gP29f29fjt8Fv2sfHPg3wb45/sbw3pv2H7JZf2RYT+X5lhbyv88sDOcvI55Y4zgcACvAP+Ho/7Tv8A0U3/AMoGl/8AyNR/w9H/AGnf+im/+UDS/wD5Go/4ej/tO/8ARTf/ACgaX/8AI1H/AA9H/ad/6Kb/AOUDS/8A5Go/4ej/ALTv/RTf/KBpf/yNR/w9H/ad/wCim/8AlA0v/wCRqP8Ah6P+07/0U3/ygaX/API1H/D0f9p3/opv/lA0v/5Go/4ej/tO/wDRTf8AygaX/wDI1H/D0f8Aad/6Kb/5QNL/APkaj/h6P+07/wBFN/8AKBpf/wAjV9//APBKT9qP4n/tKf8AC0f+Fj+Jv+Ej/sX+y/sH+gWtr5Pn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",
    "uuid": "4dmHZZMtoLbHoLZwd1wE"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||响应数据|
|»» qrData|string|true|none||二维码内包含的信息（可用二维码生成工具结合值生成可扫描的微信二维码）|
|»» appId|string|true|none||设备ID|
|»» qrImgBase64|string|true|none||二维码图片base64|
|»» uuid|string|true|none||二维码的uuid|

## POST 获取Token(步骤1)

POST /tools/getTokenId

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": ""
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|string|true|none||token|

## POST 执行登录(步骤3)

POST /login/checkLogin

- 获取到登录二维码后需每间隔5s调用本接口来判断是否登录成功
- 新设备登录平台，次日凌晨会掉线一次，重新登录时需调用[获取二维码且传appId取码](/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196794502)，登录成功后则可以长期在线
- 登录成功后请保存appId与wxid的对应关系，后续接口中会用到

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "uuid": "4cHBcs6XMZ_Px2sEguJh"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» uuid|body|string| 是 |取码返回的uuid|
|» captchCode|body|string| 是 |扫码后手机提示输入的验证码|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "uuid": "AZ0yN8d1wJmiNfQBKFgu",
    "headImgUrl": "http://wx.qlogo.cn/mmhead/ver_1/ZYUmcl1UNzyB2onM08Ij901TaUOLIjHj2UicK3XGDsjEWl4XgQN5IjodunHicBVsZiaZc1iaGCRfluAxkzyibbiau3WBfFj2nprzKp2KryicMjGIvDbWOQGmibwVK648a3o4A8hD/0",
    "nickName": "G",
    "expiredTime": 225,
    "status": 1,
    "loginInfo": null
  }
}
```

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "uuid": "4YHmGvoXvgmS1MqWVtQ2",
    "headImgUrl": "http://wx.qlogo.cn/mmhead/ver_1/ZYUmcl1UNzyB2onM08Ij901TaUOLIjHj2UicK3XGDsjEWl4XgQN5IjodunHicBVsZiaZc1iaGCRfluAxkzyibbiau3WBfFj2nprzKp2KryicMjGIvDbWOQGmibwVK648a3o4A8hD/0",
    "nickName": "G",
    "expiredTime": 230,
    "status": 2,
    "loginInfo": {
      "uin": 4077276085,
      "wxid": "wxid_0xsqb3o0tsvz22",
      "nickName": "G",
      "mobile": "17114312382",
      "alias": null
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||响应数据|
|»» uuid|string|true|none||二维码的uuid|
|»» headImgUrl|string|true|none||头像地址|
|»» nickName|string|true|none||昵称|
|»» expiredTime|integer|true|none||二维码超时时间|
|»» status|integer|true|none||状态|
|»» loginInfo|object|true|none||登录成功信息|
|»»» uin|integer|true|none||uin|
|»»» wxid|string|true|none||微信ID，返回此值则是登录成功|
|»»» nickName|string|true|none||昵称|
|»»» mobile|string|true|none||绑定的手机号|
|»»» alias|string|true|none||微信号|

## POST 设置消息回调地址

POST /tools/setCallback

> Body 请求参数

```json
{
  "token": "55d143207c5e4ab8ad19e0f729f54ab4",
  "callbackUrl": "http://192.168.29.1:8080/v2/api/callback/collect"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» token|body|string| 是 |token|
|» callbackUrl|body|string| 是 |回调接收地址|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "uuid": "4YHmGvoXvgmS1MqWVtQ2",
    "headImgUrl": "http://wx.qlogo.cn/mmhead/ver_1/ZYUmcl1UNzyB2onM08Ij901TaUOLIjHj2UicK3XGDsjEWl4XgQN5IjodunHicBVsZiaZc1iaGCRfluAxkzyibbiau3WBfFj2nprzKp2KryicMjGIvDbWOQGmibwVK648a3o4A8hD/0",
    "nickName": "G",
    "expiredTime": 230,
    "status": 2,
    "loginInfo": {
      "uin": 4077276085,
      "wxid": "wxid_0xsqb3o0tsvz22",
      "nickName": "G",
      "mobile": "17114312382",
      "alias": null
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

# 基础API/联系人模块

## POST 获取通讯录列表

POST /contacts/fetchContactsList

- 本接口为长耗时接口，耗时时间根据好友数量递增，若接口返回超时可通过[获取通讯录列表缓存接口](https://apifox.com/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196794505)获取响应结果
- 本接口返回的群聊仅为[保存到通讯录中的群聊](https://zhidao.baidu.com/question/144774265918920605/answer/4326874247.html)，若想获取会话列表中的所有群聊，需要通过[消息订阅](https://apifox.com/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196884570)做二次处理。原因：当未获取的群有成员在群内发消息的话会有消息回调， 开发者此刻调用[获取群详情接口](https://apifox.com/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196794513)查询群信息入库保存即可，比如说手机上三年前不说话的群，侧滑删除了，用户手机上也不会看到被删除的群聊的 ，但是有群成员说了话他会显示，原理就是各个终端（Android、IOS、桌面版微信）取得了消息回调，又去获取群详情信息，本地数据库缓存了下来，显示的手机群聊，让用户感知的。

> Body 请求参数

```json
{
  "appId": "{{appid}}"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "friends": [
      "tmessage",
      "medianote",
      "qmessage",
      "qqmail",
      "wxid_910acevfm2nb21",
      "qqsafe",
      "wxid_9299552988412",
      "weixin",
      "exmail_tool",
      "wxid_mp05xmje0ctn22",
      "wxid_09oq4f4j4wg912",
      "wxid_6bfguz79h8n122",
      "wxid_lyuq4hr4lrjq22",
      "wxid_a1zqyljsrsdu12",
      "wxid_lv3pb3zhna3522",
      "wxid_k2biq6fuinsr22",
      "wxid_ujredjhxz9y712",
      "wxid_uwb7989u0jea12",
      "wxid_in46ey732vxu12",
      "wxid_3rvervwohj6921",
      "wxid_4wkls7tu62ua12",
      "wxid_g0bdknnotx2f12",
      "wxid_ce5fgp0icb3y21",
      "wxid_1482424825211",
      "wxid_vw3p4f6jy7bm12",
      "wxid_o2m8xm71c23522",
      "wxid_bclqpc2ho6o412",
      "wxid_98pjjzpiisi721",
      "wxid_noq2wsn5c8h222"
    ],
    "chatrooms": [
      "2180313478@chatroom",
      "14358945067@chatroom",
      "17362526147@chatroom",
      "11685224357@chatroom",
      "17522822550@chatroom"
    ],
    "ghs": [
      "gh_7aac992b0363",
      "gh_d7293b5f14f4",
      "gh_f51ce3ef83a4",
      "gh_7d20df86e26b",
      "gh_69bfb92a3e43"
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» friends|[string]|true|none||好友的wxid|
|»» chatrooms|[string]|true|none||保存到通讯录中群聊的ID|
|»» ghs|[string]|true|none||关注的公众号ID|

## POST 获取通讯录列表缓存

POST /contacts/fetchContactsListCache

通讯录列表数据缓存10分钟，超时则需要重新调用[获取通讯录列表接口](https://apifox.com/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196794504)

> Body 请求参数

```json
{
  "appId": "{{appid}}"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 搜索好友

POST /contacts/search

搜索的联系人信息若已经是好友，响应结果的v3则为好友的wxid
本接口返回的数据可通过[添加联系人接口](https://apifox.com/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196794507)发送添加好友请求

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "contactsInfo": "zhangch"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» contactsInfo|body|string| 是 |搜索的联系人信息，微信号、手机号...|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "v3": "v3_020b3826fd030100000000006c20217514f7f2000000501ea9a3dba12f95f6b60a0536a1adb690dcccc9bf58cc80765e6eb16bc2678a36a0ed264e1b22596f787de6acc71a4beb20b69ab88bfd6d71aa1858b3@stranger",
    "nickName": "zhang",
    "sex": 1,
    "signature": "学习、成长、锻炼",
    "bigHeadImgUrl": "http://wx.qlogo.cn/mmhead/ver_1/yoYJGtDmGicz9QGOFRb71Ns6onQO63bnfJibicBwEmO73m18N7BicrGzeYsdxOrUf5qwJq9mMaQbDwEBA92uPOuibZg/0",
    "smallHeadImgUrl": "http://wx.qlogo.cn/mmhead/ver_1/yoYJGtDmGicz9QGOFRb71Ns6onQO63bnfJibicBwEmO73m18N7BicrGzeYsdxOrUf5qwJq9mMaQbDwEBA92uPOuibZg/132",
    "v4": "v4_000b708f0b04000001000000000056d3690365e0eefe00ef467a8e651000000050ded0b020927e3c97896a09d47e6e9ec65e1f9d32b06f86df4790587a6308149b3c8a90185e824efccd5b41bd75f6240ab020f9dd4b5915a083c6784a5cfcb806f53ca340b4c95b24f474d6e3fc0661301b3b3b741aac3eb5@stranger"
  }
}
```

```json
{
  "ret": 500,
  "msg": "搜索联系人失败",
  "data": {
    "code": "-4",
    "msg": "用户不存在"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» v3|string|true|none||搜索好友的v3，添加好友时使用|
|»» nickName|string|true|none||搜索好友的昵称|
|»» sex|integer|true|none||搜索好友的性别|
|»» signature|null|true|none||搜索好友的签名|
|»» bigHeadImgUrl|string|true|none||搜索好友的大尺寸头像|
|»» smallHeadImgUrl|string|true|none||搜索好友的小尺寸头像|
|»» v4|string|true|none||搜索好友的v4，添加好友时使用|

## POST 添加联系人/同意添加好友

POST /contacts/addContacts

本接口建议在线3天后再进行调用。
好友添加成功后，会通过回调消息推送一条包含v3的消息，可用于判断好友是否添加成功。

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "scene": 3,
  "content": "hallo",
  "v4": "v4_000b708f0b04000001000000000054a9e826263634356493c57b8e651000000050ded0b020927e3c97896a09d47e6e9e455d674c2544e251e77c7cba08cc6cef8f7df9e52d2bd4a3cef771c8661331fa1939fbe54f4e479d6d9d4522d70aeba057ffd0dd82398730da44ee57332a7bdea4862304d4799758ba@stranger",
  "v3": "v3_020b3826fd030100000000003a070e7757675c000000501ea9a3dba12f95f6b60a0536a1adb690dcccc9bf58cc80765e6eb16bffa5996420bb1b2577634516ff82090419d8bdcd5689df8dfb21d40af93d286f72c3a0e8cfa6dcb68afed39226f008c6@stranger",
  "option": 2
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» scene|body|integer| 是 |添加来源，同意添加好友时传回调消息xml中的scene值。|
|» option|body|integer| 是 |操作类型，2添加好友 3同意好友 4拒绝好友|
|» v3|body|string| 是 |通过搜索或回调消息获取到的v3|
|» v4|body|string| 是 |通过搜索或回调消息获取到的v4|
|» content|body|string| 是 |添加好友时的招呼语|

#### 详细说明

**» scene**: 添加来源，同意添加好友时传回调消息xml中的scene值。
添加好友时的枚举值如下：
3 ：微信号搜索
4 ：QQ好友
8 ：来自群聊
15：手机号

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 删除好友

POST /contacts/deleteFriend

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "wxid": "wxid_phyyedw9xap22"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» wxid|body|string| 是 |删除好友的wxid|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 上传手机通讯录

POST /contacts/uploadPhoneAddressList

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "phones": [
    "18616561632",
    "18134173174"
  ],
  "opType": 1
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» phones|body|[string]| 是 |需要上传的手机号|
|» opType|body|integer| 是 |操作类型，1:上传  2:删除|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 获取群/好友简要信息

POST /contacts/getBriefInfo

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "wxids": [
    "wxid_phyyedw9xap22"
  ]
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» wxids|body|[string]| 是 |好友的wxid|

> 返回示例

```json
{
  "ret": 200,
  "msg": "获取联系人信息成功",
  "data": [
    {
      "userName": "wxid_phyyedw9xap22",
      "nickName": "Ashley",
      "pyInitial": "ASHLEY",
      "quanPin": "Ashley",
      "sex": 2,
      "remark": "",
      "remarkPyInitial": "",
      "remarkQuanPin": "",
      "signature": null,
      "alias": "zero-one_200906",
      "snsBgImg": null,
      "country": "AD",
      "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/buiaXybHTBK3BuGr1edN72zBDermWVFJ7YC8Jib2RcCSdiauAtZcPgUQpdhE9KY5NsumDAWD16fsg3A6OKuhdEr97VAHdTGgk6R1Eibuj7ZNwJ4/0",
      "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/buiaXybHTBK3BuGr1edN72zBDermWVFJ7YC8Jib2RcCSdiauAtZcPgUQpdhE9KY5NsumDAWD16fsg3A6OKuhdEr97VAHdTGgk6R1Eibuj7ZNwJ4/132",
      "description": null,
      "cardImgUrl": null,
      "labelList": "",
      "province": "",
      "city": "",
      "phoneNumList": null
    }
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|[object]|true|none||none|
|»» userName|string|false|none||none|
|»» nickName|string|false|none||none|
|»» pyInitial|string|false|none||none|
|»» quanPin|string|false|none||none|
|»» sex|integer|false|none||none|
|»» remark|string|false|none||none|
|»» remarkPyInitial|string|false|none||none|
|»» remarkQuanPin|string|false|none||none|
|»» signature|null|false|none||none|
|»» alias|string|false|none||none|
|»» snsBgImg|null|false|none||none|
|»» country|string|false|none||none|
|»» bigHeadImgUrl|string|false|none||none|
|»» smallHeadImgUrl|string|false|none||none|
|»» description|null|false|none||none|
|»» cardImgUrl|null|false|none||none|
|»» labelList|string|false|none||none|
|»» province|string|false|none||none|
|»» city|string|false|none||none|
|»» phoneNumList|null|false|none||none|

## POST 获取群/好友详细信息

POST /contacts/getDetailInfo

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "wxids": [
    "yc-081726"
  ]
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» wxids|body|[string]| 是 |好友的wxid|

> 返回示例

```json
{
  "ret": 200,
  "msg": "获取联系人信息成功",
  "data": [
    {
      "userName": "wxid_phyyedw9xap22",
      "nickName": "Ashley",
      "pyInitial": null,
      "quanPin": "Ashley",
      "sex": 2,
      "remark": null,
      "remarkPyInitial": null,
      "remarkQuanPin": null,
      "signature": "山林不向四季起誓 枯荣随缘。",
      "alias": "zero-one_200906",
      "snsBgImg": "http://shmmsns.qpic.cn/mmsns/UaAfqYic92wm7ZCrsEwlQMXSmBLs8dpwBzrXnrOyyP3B8bDibCCFInJ9PicC9LPYY17uWH1yIOmBYQ/0",
      "country": "AD",
      "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/buiaXybHTBK3BuGr1edN72zBDermWVFJ7YC8Jib2RcCSdiauAtZcPgUQpdhE9KY5NsumDAWD16fsg3A6OKuhdEr97VAHdTGgk6R1Eibuj7ZNwJ4/0",
      "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/buiaXybHTBK3BuGr1edN72zBDermWVFJ7YC8Jib2RcCSdiauAtZcPgUQpdhE9KY5NsumDAWD16fsg3A6OKuhdEr97VAHdTGgk6R1Eibuj7ZNwJ4/132",
      "description": null,
      "cardImgUrl": null,
      "labelList": null,
      "province": null,
      "city": null,
      "phoneNumList": null
    }
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|[object]|true|none||none|
|»» userName|string|false|none||好友的wxid|
|»» nickName|string|false|none||好友的昵称|
|»» pyInitial|null|false|none||好友昵称的拼音首字母|
|»» quanPin|string|false|none||好友昵称的全拼|
|»» sex|integer|false|none||好友的性别|
|»» remark|null|false|none||好友备注|
|»» remarkPyInitial|null|false|none||好友备注的拼音首字母|
|»» remarkQuanPin|null|false|none||好友备注的全拼|
|»» signature|string|false|none||好友的签名|
|»» alias|string|false|none||好友的微信号|
|»» snsBgImg|string|false|none||朋友圈背景图链接|
|»» country|string|false|none||国家|
|»» bigHeadImgUrl|string|false|none||大尺寸头像链接|
|»» smallHeadImgUrl|string|false|none||小尺寸头像链接|
|»» description|null|false|none||好友的描述|
|»» cardImgUrl|null|false|none||好友描述的图片链接|
|»» labelList|null|false|none||好友的标签ID|
|»» province|null|false|none||省份|
|»» city|null|false|none||城市|
|»» phoneNumList|null|false|none||好友的手机号码|

## POST 设置好友仅聊天

POST /contacts/setFriendPermissions

设置完好友仅聊天后若发现手机展示不是设置的结果，可能是手机缓存未刷新，重新进入页面刷新查看

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "wxid": "wxid_phyyedw9xap22",
  "onlyChat": true
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» wxid|body|string| 是 |好友的wxid|
|» onlyChat|body|boolean| 是 |设置好友是否仅聊天|

> 返回示例

```json
{
  "ret": 200,
  "msg": "设置好友权限成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 设置好友备注

POST /contacts/setFriendRemark

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "wxid": "wxid_phyyedw9xap22",
  "remark": "备注"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» wxid|body|string| 是 |好友的wxid|
|» remark|body|string| 是 |备注的备注|

> 返回示例

```json
{
  "ret": 200,
  "msg": "设置好友权限成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 获取手机通讯录

POST /contacts/getPhoneAddressList

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "phones": []
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» phones|body|[string]| 否 |获取哪些手机号的好友详情，不传获取所有|

> 返回示例

```json
{
  "ret": 200,
  "msg": "获取手机通讯录成功",
  "data": [
    {
      "userName": "wxid_ddgsghdfafaphh22",
      "v4": null,
      "nickName": null,
      "sex": 1,
      "phoneMd5": "d36f4cc1c8bca1ef41b93d2215133cdb",
      "signature": "......",
      "alias": null,
      "country": "CN",
      "bigHeadImgUrl": "http://wx.qlogo.cn/mmhead/ver_1/vwGdLRK5jtpXagA7dfXlUiaU9VayWNSqia1c2Wib7icJNhPd6WHhqMIVuYuNDfEqPRC2TnmlRSkfYrib9fHyYONwdccv17gibCls7ia8elaunvgMmYicAw22wUJQ3CDw0Cm5ibrOT/0",
      "smallHeadImgUrl": "http://wx.qlogo.cn/mmhead/ver_1/vwGdLRK5jtpXagA7dfXlUiaU9VayWNSqia1c2Wib7icJNhPd6WHhqMIVuYuNDfEqPRC2TnmlRSkfYrib9fHyYONwdccv17gibCls7ia8elaunvgMmYicAw22wUJQ3CDw0Cm5ibrOT/132",
      "province": "Jiangsu",
      "city": "Xuzhou",
      "personalCard": 0
    }
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|[object]|true|none||none|
|»» userName|string|false|none||none|
|»» v4|null|false|none||none|
|»» nickName|null|false|none||none|
|»» sex|integer|false|none||none|
|»» phoneMd5|string|false|none||none|
|»» signature|string|false|none||none|
|»» alias|null|false|none||none|
|»» country|string|false|none||none|
|»» bigHeadImgUrl|string|false|none||none|
|»» smallHeadImgUrl|string|false|none||none|
|»» province|string|false|none||none|
|»» city|string|false|none||none|
|»» personalCard|integer|false|none||none|

# 基础API/群模块

## POST 创建微信群

POST /group/createChatroom

创建微信群时最少要选择两位微信好友

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "wxids": [
    "wxid_0xsqb3o0tsvz22",
    "wxid_phyyedw9xap22"
  ]
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» wxids|body|[string]| 是 |好友的wxid列表|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "headImgBase64": "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",
    "chatroomId": "34757816141@chatroom"
  }
}
```

```json
{
  "ret": 500,
  "msg": "创建群聊失败",
  "data": {
    "code": "0",
    "msg": "MemberList are wrong"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» headImgBase64|string|true|none||群头像的base64图片|
|»» chatroomId|string|true|none||群ID|

## POST 修改群名称

POST /group/modifyChatroomName

修改完群名称后若发现手机未展示修改后的名称，可能是手机缓存未刷新，手机聊天框多切换几次会刷新。

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomName": "GeWe test",
  "chatroomId": "34757816141@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomName|body|string| 是 |群名称|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 修改群备注

POST /group/modifyChatroomRemark

群备注仅自己可见
修改完群备注后若发现手机未展示修改后的备注，可能是手机缓存未刷新，手机聊天框多切换几次会刷新。

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomRemark": "GeWe test private",
  "chatroomId": "34757816141@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomRemark|body|string| 是 |群备注|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 修改我在群内的昵称

POST /group/modifyChatroomNickNameForSelf

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "nickName": "廖静",
  "chatroomId": "34757816141@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» nickName|body|string| 是 |群昵称|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 邀请/添加 进群

POST /group/inviteMember

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "wxids": "wxid_8pvka4jg6qzt22",
  "chatroomId": "34757816141@chatroom",
  "reason": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» wxids|body|string| 是 |邀请进群的好友wxid，多个英文逗号分隔|
|» chatroomId|body|string| 是 |群ID|
|» reason|body|string| 是 |邀请进群的说明|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 删除群成员

POST /group/removeMember

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "wxids": "wxid_8pvka4jg6qzt22",
  "chatroomId": "34757816141@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» wxids|body|string| 是 |删除的群成员wxid，多个英文逗号分隔|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 退出群聊

POST /group/quitChatroom

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "21425161836@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 解散群聊

POST /group/disbandChatroom

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "21425161836@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 获取群信息

POST /group/getChatroomInfo

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "chatroomId": "34757816141@chatroom",
    "nickName": "GeWe test",
    "pyInitial": "GEWETEST",
    "quanPin": "GeWetest",
    "sex": 0,
    "remark": "GeWe test private",
    "remarkPyInitial": "GEWETESTPRIVATE",
    "remarkQuanPin": "GeWetestprivate",
    "chatRoomNotify": 1,
    "chatRoomOwner": "zhangchuan2288",
    "smallHeadImgUrl": "https://wx.qlogo.cn/mmcrhead/PiajxSqBRaEJEIII6n6NUHudK1r5a29cMDlW0Ef7b1ibzksfrwIcRkTicPRoWm7Km3ZQIpq8xp65nD6yUm8BHxzqhV1ic1jQvvnv/0",
    "memberList": [
      {
        "wxid": "zhangchuan2288",
        "nickName": "朝夕。",
        "inviterUserName": null,
        "memberFlag": 1,
        "displayName": null,
        "bigHeadImgUrl": null,
        "smallHeadImgUrl": null
      },
      {
        "wxid": "wxid_phyyedw9xap22",
        "nickName": "Ashley",
        "inviterUserName": "zhangchuan2288",
        "memberFlag": 1,
        "displayName": null,
        "bigHeadImgUrl": null,
        "smallHeadImgUrl": null
      },
      {
        "wxid": "wxid_0xsqb3o0tsvz22",
        "nickName": "G",
        "inviterUserName": "zhangchuan2288",
        "memberFlag": 1,
        "displayName": null,
        "bigHeadImgUrl": null,
        "smallHeadImgUrl": null
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» chatroomId|string|true|none||群ID|
|»» nickName|string|true|none||群名称|
|»» pyInitial|string|true|none||群名称的拼音首字母|
|»» quanPin|string|true|none||群名称的全拼|
|»» sex|integer|true|none||none|
|»» remark|string|true|none||群备注，仅自己可见|
|»» remarkPyInitial|string|true|none||群备注的拼音首字母|
|»» remarkQuanPin|string|true|none||群备注的全拼|
|»» chatRoomNotify|integer|true|none||群消息是否提醒|
|»» chatRoomOwner|string|true|none||群主的wxid|
|»» smallHeadImgUrl|string|true|none||群头像链接|
|»» memberList|[object]|true|none||群成员列表|
|»»» wxid|string|true|none||群成员的wxid|
|»»» nickName|string|true|none||群成员的昵称|
|»»» inviterUserName|string¦null|true|none||邀请人的wxid|
|»»» memberFlag|integer|true|none||标识|
|»»» displayName|null|true|none||在本群内的昵称|
|»»» bigHeadImgUrl|null|true|none||大尺寸头像|
|»»» smallHeadImgUrl|null|true|none||小尺寸头像|

## POST 获取群成员列表

POST /group/getChatroomMemberList

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "memberList": [
      {
        "wxid": "zhangchuan2288",
        "nickName": "朝夕。",
        "inviterUserName": null,
        "memberFlag": 1,
        "displayName": null,
        "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/T0MtLBu618rUlZqaAiaWfucmVibiawiciaSibPfz11siaLZr0qSxQTAR9lu7YicDwYAHNia1je79icxul6bzQ4LLZopiaM9EdYAEublPCLV29QKLv26ictBHjWsWnE0lvYGjibB9DkE6q/0",
        "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/T0MtLBu618rUlZqaAiaWfucmVibiawiciaSibPfz11siaLZr0qSxQTAR9lu7YicDwYAHNia1je79icxul6bzQ4LLZopiaM9EdYAEublPCLV29QKLv26ictBHjWsWnE0lvYGjibB9DkE6q/132"
      },
      {
        "wxid": "wxid_phyyedw9xap22",
        "nickName": "Ashley",
        "inviterUserName": "zhangchuan2288",
        "memberFlag": 1,
        "displayName": null,
        "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/5ibSibfNKwpv0TLLuSFv2hibEBqShib4BKsaxHZ2v10y9F93ibO5lK4bwib47qtuwsLZD8HY7fVicibWlWvehCLDCdicy38NaIbVupuMZMDwiaXozjUhk/0",
        "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/5ibSibfNKwpv0TLLuSFv2hibEBqShib4BKsaxHZ2v10y9F93ibO5lK4bwib47qtuwsLZD8HY7fVicibWlWvehCLDCdicy38NaIbVupuMZMDwiaXozjUhk/132"
      },
      {
        "wxid": "wxid_0xsqb3o0tsvz22",
        "nickName": "G",
        "inviterUserName": "zhangchuan2288",
        "memberFlag": 2049,
        "displayName": "G1",
        "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/FMkteDauMN35F3lhfavibDYpGibfHqrsMICtqBbWDfwfQOnIYfgHBpOJLLbac0Wf3odowXcePFHMzj954EeFOiaKcsgIaMedw5KWZhBpaLsFfSK5HNAE7AQODQ1FfrPiaTCh/0",
        "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/FMkteDauMN35F3lhfavibDYpGibfHqrsMICtqBbWDfwfQOnIYfgHBpOJLLbac0Wf3odowXcePFHMzj954EeFOiaKcsgIaMedw5KWZhBpaLsFfSK5HNAE7AQODQ1FfrPiaTCh/132"
      },
      {
        "wxid": "wxid_8pvka4jg6qzt22",
        "nickName": "白开水加糖",
        "inviterUserName": "wxid_phyyedw9xap22",
        "memberFlag": 2049,
        "displayName": null,
        "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/3d34Q9DWL6pHiaASIBMIG3J9deRhwz4yKpZxGibDqiaRGmF6XckV0VSeRTGHSTq55bSwK1qF4Sy1JVXIkB7tYHpR4qPh3ECcodpkqRQjSwKUa4/0",
        "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/3d34Q9DWL6pHiaASIBMIG3J9deRhwz4yKpZxGibDqiaRGmF6XckV0VSeRTGHSTq55bSwK1qF4Sy1JVXIkB7tYHpR4qPh3ECcodpkqRQjSwKUa4/132"
      }
    ],
    "chatroomOwner": "zhangchuan2288",
    "adminWxid": [
      "wxid_8pvka4jg6qzt22"
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» memberList|[object]|true|none||群成员列表|
|»»» wxid|string|true|none||群成员的wxid|
|»»» nickName|string|true|none||群成员昵称|
|»»» inviterUserName|string¦null|true|none||邀请人的wxid|
|»»» memberFlag|integer|true|none||标识|
|»»» displayName|string¦null|true|none||在本群内的昵称|
|»»» bigHeadImgUrl|string|true|none||大尺寸头像|
|»»» smallHeadImgUrl|string|true|none||小尺寸头像|
|»» chatroomOwner|null|true|none||群主的wxid|
|»» adminWxid|null|true|none||管理的wxid|

## POST 获取群成员详情

POST /group/getChatroomMemberDetail

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom",
  "memberWxids": [
    "wxid_0xsqb3o0tsvz22",
    "wxid_phyyedw9xap22"
  ]
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|
|» memberWxids|body|[string]| 是 |none|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": [
    {
      "userName": "wxid_0xsqb3o0tsvz22",
      "nickName": "G",
      "pyInitial": "G",
      "quanPin": "G",
      "sex": 0,
      "remark": null,
      "remarkPyInitial": null,
      "remarkQuanPin": null,
      "chatRoomNotify": 0,
      "signature": null,
      "alias": null,
      "snsBgImg": "http://shmmsns.qpic.cn/mmsns/s5BUfupeMYsJx3WHf6RyTxAqLUpGZPsgD9l68D5iaf7qibkcjz08RwNwDxj9ToFvnaicFD2X8CtPe4/0",
      "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/tmlG7SpZJMJEh0dA14icl4CWnliaI8pKvVicEMaowRywgVpljBK3nmBib0jHG4eVo5hiaqS7Gg0p7GwCuHopGYqdNBu9WVtxMB8icSFGUjibCDPoGXicPic1r3gx3PQ4YMf3GPfXj/0",
      "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/tmlG7SpZJMJEh0dA14icl4CWnliaI8pKvVicEMaowRywgVpljBK3nmBib0jHG4eVo5hiaqS7Gg0p7GwCuHopGYqdNBu9WVtxMB8icSFGUjibCDPoGXicPic1r3gx3PQ4YMf3GPfXj/132",
      "description": null,
      "cardImgUrl": null,
      "labelList": null,
      "country": "CN",
      "province": "Guangdong",
      "city": "Foshan",
      "phoneNumList": null,
      "friendUserName": "wxid_0xsqb3o0tsvz22",
      "inviterUserName": "zhangchuan2288",
      "memberFlag": 0
    },
    {
      "userName": "wxid_phyyedw9xap22",
      "nickName": "Ashley",
      "pyInitial": "ASHLEY",
      "quanPin": "Ashley",
      "sex": 2,
      "remark": "小号",
      "remarkPyInitial": "XH",
      "remarkQuanPin": "xiaohao",
      "chatRoomNotify": 0,
      "signature": "山林不向四季起誓 枯荣随缘。",
      "alias": "zero-one_200906",
      "snsBgImg": "http://shmmsns.qpic.cn/mmsns/UaAfqYic92wm7ZCrsEwlQMXSmBLs8dpwBzrXnrOyyP3B8bDibCCFInJ9PicC9LPYY17uWH1yIOmBYQ/0",
      "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/buiaXybHTBK3BuGr1edN72zBDermWVFJ7YC8Jib2RcCSdiauAtZcPgUQpdhE9KY5NsumDAWD16fsg3A6OKuhdEr97VAHdTGgk6R1Eibuj7ZNwJ4/0",
      "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/buiaXybHTBK3BuGr1edN72zBDermWVFJ7YC8Jib2RcCSdiauAtZcPgUQpdhE9KY5NsumDAWD16fsg3A6OKuhdEr97VAHdTGgk6R1Eibuj7ZNwJ4/132",
      "description": null,
      "cardImgUrl": null,
      "labelList": "27",
      "country": "AD",
      "province": null,
      "city": null,
      "phoneNumList": [
        "\n\u000b14752126220"
      ],
      "friendUserName": "wxid_phyyedw9xap22",
      "inviterUserName": null,
      "memberFlag": null
    }
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|[object]|true|none||none|
|»» userName|string|true|none||群成员的wxid|
|»» nickName|string|true|none||群成员的昵称|
|»» pyInitial|string|true|none||群成员昵称的拼音首字母|
|»» quanPin|string|true|none||群成员昵称的全拼|
|»» sex|integer|true|none||性别|
|»» remark|string¦null|true|none||备注|
|»» remarkPyInitial|string¦null|true|none||备注的拼音首字母|
|»» remarkQuanPin|string¦null|true|none||备注的全拼|
|»» chatRoomNotify|integer|true|none||消息通知|
|»» signature|string¦null|true|none||签名|
|»» alias|string¦null|true|none||微信号|
|»» snsBgImg|string|true|none||朋友圈背景图链接|
|»» bigHeadImgUrl|string|true|none||大尺寸头像|
|»» smallHeadImgUrl|string|true|none||小尺寸头像|
|»» description|null|true|none||描述|
|»» cardImgUrl|null|true|none||描述的图片链接|
|»» labelList|string¦null|true|none||标签列表，多个英文逗号分隔|
|»» country|string|true|none||国家|
|»» province|string¦null|true|none||省份|
|»» city|string¦null|true|none||城市|
|»» phoneNumList|[string]|true|none||手机号码|
|»» friendUserName|string|true|none||好友的wxid|
|»» inviterUserName|string¦null|true|none||邀请人的wxid|
|»» memberFlag|integer¦null|true|none||标识|

## POST 获取群公告

POST /group/getChatroomAnnouncement

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "announcement": "群公告哈",
    "announcementEditor": "zhangchuan2288",
    "publishTime": 1703839509
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» announcement|string|true|none||群公告内容|
|»» announcementEditor|string|true|none||群公告作者的wxid|
|»» publishTime|integer|true|none||群公告发布时间|

## POST 设置群公告

POST /group/setChatroomAnnouncement

仅群主或管理员可以发布群公告

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom",
  "content": "群公告哈"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|
|» content|body|string| 是 |公告内容|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 同意进群

POST /group/agreeJoinRoom

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "url": "https://support.weixin.qq.com/cgi-bin/mmsupport-bin/addchatroombyinvite?ticket=A%2FtYjg2L%2FGB%2FHYqOwzWNMQ%3D%3D"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» url|body|string| 是 |邀请进群回调消息中的url|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "chatroomId": "19189253160@chatroom"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» chatroomId|string|true|none||群ID|

## POST 添加群成员为好友

POST /group/addGroupMemberAsFriend

添加群成员为好友，若对方关闭从群聊添加的权限则添加失败

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom",
  "content": "hallo",
  "memberWxid": "wxid_phyyedw9xap22"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|
|» memberWxid|body|string| 是 |群成员的wxid|
|» content|body|string| 是 |加好友的招呼语|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "v3": "v3_020b3826fd030100000000003a070e7757675c000000501ea9a3dba12f95f6b60a0536a1adb690dcccc9bf58cc80765e6eb16bffa5996420bb1b2577634516ff82090419d8bdcd5689df8dfb21d40af93d286f72c3a0e8cfa6dcb68afed39226f008c6@stranger"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» v3|string|true|none||添加群成员的v3，通过好友后会通过回调消息返回此值|

## POST 获取群二维码

POST /group/getChatroomQrCode

### 注意
- 在新设备登录后的1-3天内，无法使用本功能。在此期间，如果尝试进行获取，您将收到来自微信团队的提醒。请注意遵守相关规定。
- 生成的群二维码图片7天有效

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "qrBase64": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/wAALCAG4AbgBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/AP1Tooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooor+Veiiiiiiv6qK/lXr+qiiiv5V6/qor+Vev6qKKKKK/lXoooooor+qiiiv5V6KK/qoor+Veiv6qKKK/lXr+qiv5V6KKKKKK/qoooooor+Vev6qKKKKK/lXr+qiiiv5V6KKKKKK/qor+Veiiiv6qKK/lXor+qiiv5V6K/qoor+Veiv6qKK/lXr+qiv5V6KK/qor+Vev6qKKKKK/lXr+qiiiiiiv5V6/qor+Veiiv6qK/lXr+qiiv5V6K/qoor+Veiiv6qK/lXor+qiv5V6/qoor+Veiv6qK/lXor+qiiv5V6/qor+Veiv6qKKKKK/lXor+qiv5V6/qor+Veiiv6qK/lXr+qiiiiiiv5V6/qor+Veiiv6qK/lXr+qiiv5V6K/qor+Veiiiv6qKK/lXor+qiiv5V6/qor+Veiiiv6qKK/lXr+qiiiiv5V6KK/qor+Vev6qKK/lXr+qiv5V6KK/qor+Vev6qKKKKKK/lXr+qiv5V6KK/qor+Vev6qK/lXr+qiiv5V6K/qooor+Veiiiv6qKK/lXoooor+qiv5V6KK/qor+Vev6qKK/lXoor+qiiiiv5V6/qor+Veiiv6qK/lXr+qiiiiiiv5V6/qooooor+Vev6qK/lXr+qiv5V6K/qoor+Vev6qK/lXr+qiiv5V6/qoor+Vev6qKKK/lXoor+qiv5V6KK/qoor+Veiv6qK/lXr+qiiiv5V6/qooooor+Vev6qKKKKKK/lXoooooor+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6/qor+Vev6qK/lXoooooor+qiiiiiiiiiiiiiiiiiiiv5V6/qor+Veiiiv6qKKK/lXr+qiiiv5V6/qor+Veiv6qK/lXr+qiv5V6/qor+Veiv6qK/lXor+qiiiiiiiiiiiiiiiiv5V6KKKKKK/qor+Veiiv6qK/lXooooooor+qiv5V6KKKK/qoooooor+Veiv6qK/lXor+qiv5V6/qooor+Veiv6qKKK/lXr+qiiiiiiv5V6KKK/qor+Vev6qK/lXr+qiiv5V6/qor+Vev6qK/lXoor+qiv5V6K/qor+Veiiv6qKKK/lXr+qiv5V6KK/qooor+Veiiv6qKKK/lXor+qiiv5V6/qooooooooor+Vev6qK/lXoor+qiv5V6/qor+Veiiv6qKKK/lXoor+qiiiv5V6KKK/qor+Veiiv6qKK/lXr+qiiv5V6/qoor+Veiv6qKK/lXor+qiv5V6/qor+Veiiiv6qKKKKKKK/lXoor+qiv5V6/qooor+Vev6qKKKK/lXoor+qiiv5V6/qooooor+Vev6qKK/lXr+qiiv5V6/qoor+Veiiv6qKKK/lXooor+qiiiv5V6/qooooooor+Vev6qK/lXr+qiiv5V6K/qor+Vev6qK/lXoor+qiv5V6K/qor+Vev6qKKKK/lXr+qiiv5V6K/qor+Vev6qK/lXor+qiiv5V6KKK/qor+Veiv6qK/lXor+qiiiiv5V6/qoooooor+Vev6qK/lXoor+qiiiv5V6K/qor+Vev6qKKKK/lXor+qiiiiv5V6KKK/qooor+Veiv6qKKKKK/lXor+qiv5V6/qoor+Vev6qKKK/lXr+qiiiiiiiiv5V6K/qor+Vev6qK/lXoor+qiv5V6K/qor+Vev6qKKK/lXr+qiiv5V6/qor+Veiv6qK/lXoor+qiv5V6/qooooor+Veiiv6qKK/lXoor+qiiv5V6KKKK/qooooooor+Veiiv6qK/lXr+qiv5V6/qoooor+Veiv6qK/lXoor+qiv5V6K/qoor+Vev6qKKK/lXr+qiv5V6/qoooor+Veiiiiiiv6qK/lXr+qiv5V6/qor+Veiiv6qKKKKKK/lXr+qiv5V6/qoor+Veiiiv6qK/lXoooor+qiiv5V6K/qor+Veiiv6qK/lXor+qiiv5V6/qoor+Vev6qK/lXooor+qiv5V6/qoor+Veiv6qKK/lXr+qiiiiiiiiiv5V6/qooor+Vev6qKK/lXr+qiiiiv5V6K/qoor+Vev6qKKKKKK/lXr+qiiiiiv5V6/qoor+Vev6qK/lXr+qiv5V6KKK/qoor+Veiv6qK/lXor+qiiiiiiiiiv5V6/qor+Vev6qK/lXoor+qiiiv5V6K/qooooor+Veiiiiv6qK/lXor+qiiv5V6/qor+Vev6qKK/lXr+qiiiiiiiv5V6KKKK/qor+Veiv6qKKKKKKK/lXr+qiiv5V6/qooor+Vev6qK/lXr+qiv5V6/qor+Veiiiv6qK/lXoor+qiiv5V6K/qoor+Veiv6qK/lXoooor+qiv5V6KK/qoor+Veiiv6qKKKKKKKKKKKKKKK/lXoor+qiv5V6/qor+Vev6qKKKKKK/lXor+qiiv5V6K/qor+Vev6qKK/lXr+qiiv5V6/qoooor+Veiiiiv6qK/lXor+qiiv5V6K/qooooooooor+Vev6qK/lXor+qiiv5V6/qoor+Veiiv6qK/lXoor+qiv5V6KKK/qooor+Veiiiiv6qK/lXr+qiiv5V6K/qoooor+Veiv6qKK/lXr+qiiiiiiiiiv5V6KK/qor+Veiiiiiv6qKK/lXor+qiv5V6KKKK/qor+Veiiiiiv6qKK/lXr+qiv5V6/qoor+Vev6qKKK/lXr+qiv5V6KKKK/qor+Veiiv6qKKKKKKKK/lXoor+qiiiv5V6/qoor+Vev6qK/lXor+qiiiv5V6/qor+Vev6qK/lXr+qiiiv5V6/qooor+Vev6qKK/lXr+qiiv5V6/qoor+Veiv6qKKK/lXr+qiiiv5V6/qoooooooooor+Vev6qK/lXr+qiv5V6K/qoor+Veiv6qK/lXr+qiiv5V6/qoor+Veiv6qK/lXr+qiv5V6K/qor+Veiiv6qKKK/lXoor+qiiv5V6/qor+Vev6qK/lXoor+qiiiiiiiiiiiiv5V6/qooor+Veiiiv6qKKK/lXr+qiiv5V6KKKK/qooor+Vev6qKK/lXor+qiv5V6/qoor+Veiiv6qKK/lXr+qiiiv5V6KKKK/qooooooor+Veiiiiiiiiiv6qKK/lXr+qiv5V6/qor+Vev6qK/lXr+qiv5V6KKKKKK/qoor+Vev6qK/lXor+qiiiv5V6/qoor+Veiiiiiiv6qK/lXr+qiiiiiiv5V6/qooor+Veiv6qK/lXoor+qiv5V6/qor+Veiv6qKK/lXoor+qiv5V6/qor+Vev6qK/lXoor+qiiiiv5V6K/qooor+Veiv6qK/lXor+qiv5V6/qor+Vev6qK/lXor+qiiiiiiv5V6K/qor+Veiiiiv6qK/lXor+qiiiiv5V6K/qoor+Veiiiv6qK/lXor+qiiv5V6KKK/qor+Vev6qK/lXoor+qiv5V6KK/qoooor+Vev6qK/lXr+qiiiiiiv5V6KK/qoooor+Veiiv6qKK/lXoor+qiv5V6KKK/qooor+Vev6qKK/lXooooor+qiv5V6/qor+Vev6qK/lXr+qiiiv5V6/qor+Veiiv6qK/lXr+qiiiiiiiiiiiv5V6KKK/qor+Vev6qKKK/lXr+qiiv5V6/qooooor+Vev6qKK/lXor+qiv5V6K/qoor+Vev6qK/lXoooooooor+qiv5V6KK/qor+Vev6qKKKKKK/lXr+qiv5V6/qor+Veiv6qKKK/lXor+qiv5V6/qor+Veiv6qKK/lXr+qiv5V6KK/qoor+Veiiv6qK/lXr+qiiiiv5V6/qor+Vev6qKK/lXor+qiiv5V6K/qooooooooooooor+Vev6qK/lXor+qiiiiv5V6K/qor+Veiv6qKKK/lXr+qiiv5V6K/qoor+Vev6qK/lXooooooor+qiv5V6/qor+Veiiiiiiiiv6qKKKKKKKK/lXr+qiiiv5V6/qor+Veiiv6qK/lXr+qiv5V6/qoor+Vev6qKK/lXr+qiv5V6K/qor+Vev6qKK/lXooor+qiv5V6/qoooor+Vev6qKK/lXr+qiiv5V6/qooor+Vev6qKKKKKKKK/lXoor+qiv5V6KKKK/qor+Vev6qK/lXr+qiiiiiiv5V6KK/qooooor+Vev6qKK/lXoooor+qiiiiiv5V6K/qor+Veiv6qKK/lXr+qiiiiiiiv5V6KKK/qooooor+Vev6qK/lXr+qiv5V6KK/qooooor+Veiv6qK/lXr+qiv5V6/qor+Vev6qK/lXor+qiiiv5V6K/qooooor+Veiv6qKKKKKKKKKK/lXor+qiv5V6K/qor+Vev6qK/lXr+qiiiv5V6K/qor+Vev6qKKK/lXor+qiv5V6/qor+Vev6qKK/lXr+qiv5V6KK/qooor+Veiv6qK/lXoor+qiiv5V6/qor+Veiiv6qKKKKKKKKK/lXr+qiv5V6K/qor+Vev6qK/lXr+qiiiv5V6/qoooor+Veiv6qKK/lXr+qiiv5V6K/qoor+Veiv6qK/lXr+qiiv5V6KK/qoor+Vev6qKK/lXr+qiv5V6/qor+Vev6qKKKKKKKK/lXr+qiiiv5V6KK/qor+Vev6qK/lXoooor+qiiiiiv5V6K/qooor+Veiiv6qKK/lXr+qiiiiv5V6KKKKKKKK/qooor+Vev6qKKKKKKK/lXoor+qiiiv5V6KK/qooor+Vev6qKKK/lXoor+qiiiiiv5V6KKK/qor+Veiiiv6qK/lXr+qiiiiiv5V6/qor+Vev6qK/lXr+qiv5V6K/qoooooor+Veiiv6qKKK/lXor+qiv5V6K/qor+Vev6qKK/lXooor+qiiv5V6KKKKK/qoor+Veiv6qKKKK/lXoor+qiv5V6KKKKK/qooor+Vev6qKKKKKKKKKKKKKK/lXor+qiv5V6/qoor+Veiiiv6qKK/lXoor+qiiiv5V6K/qoor+Veiiiv6qK/lXor+qiiiv5V6/qooor+Vev6qKKKKKKKKKK/lXoooooor+qiv5V6/qoor+Vev6qK/lXor+qiiv5V6KKKKK/qor+Vev6qK/lXoooor+qiv5V6/qoor+Vev6qK/lXr+qiiv5V6/qor+Vev6qK/lXor+qiiv5V6/qoooooor+Vev6qKKKKK/lXr+qiv5V6/qooor+Vev6qKK/lXor+qiv5V6/qooor+Vev6qKKK/lXor+qiiv5V6/qor+Veiiiiiiiiv6qKKK/lXr+qiiv5V6K/qoooooor+Vev6qK/lXoor+qiv5V6/qor+Vev6qK/lXooor+qiv5V6/qor+Veiv6qKKK/lXoooor+qiiv5V6KK/qor+Vev6qK/lXooooooooor+qiv5V6/qor+Vev6qKKKKKK/lXr+qiv5V6KK/qor+Vev6qK/lXor+qiv5V6/qoooooor+Veiv6qK/lXor+qiiiiiv5V6KK/qor+Vev6qKK/lXr+qiv5V6/qor+Vev6qK/lXor+qiv5V6/qor+Veiiv6qKKKKKK/lXr+qiv5V6KK/qor+Vev6qK/lXr+qiv5V6KKKKKKK/qoor+Veiv6qK/lXor+qiv5V6K/qor+Vev6qKKK/lXor+qiv5V6KK/qor+Veiv6qK/lXr+qiiv5V6KK/qoooooor+Vev6qKKKKK/lXr+qiv5V6K/qoor+Vev6qKK/lXoor+qiv5V6K/qor+Vev6qKKKK/lXr+qiv5V6/qoor+Veiv6qK/lXor+qiiv5V6K/qor+Vev6qK/lXr+qiiiv5V6/qoooooor+Veiiiiiiv6qKK/lXr+qiiv5V6KK/qooor+Vev6qKK/lXoor+qiv5V6K/qoooor+Vev6qKKK/lXoor+qiiv5V6/qoooor+Veiiiv6qKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK//2Q==",
    "qrTips": "该二维码7天内(1月5日前)有效，重新进入将更新"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» qrBase64|string|true|none||群二维码图片的base64|
|»» qrTips|string|true|none||群二维码的提示|

## POST 群保存到通讯录

POST /group/saveContractList

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom",
  "operType": 3
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|
|» operType|body|integer| 是 |操作类型  3保存到通讯录  2从通讯录移除|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 管理员操作

POST /group/adminOperate

添加、删除群管理员，转让群主

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom",
  "operType": 1,
  "wxids": [
    "wxid_0xsqb3o0tsvz22"
  ]
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|
|» operType|body|integer| 是 |操作类型  1：添加群管理（可添加多个微信号） 2：删除群管理（可删除多个） 3：转让（只能转让一个微信号）|
|» wxids|body|[string]| 是 |none|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 聊天置顶

POST /group/pinChat

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom",
  "top": true
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|
|» top|body|boolean| 是 |是否置顶|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 设置消息免打扰

POST /group/setMsgSilence

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom",
  "silence": true
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|
|» silence|body|boolean| 是 |是否免打扰|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 扫码进群

POST /group/joinRoomUsingQRCode

qrUrl是通过解析群二维码图片获得的内容

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "qrUrl": "https://weixin.qq.com/g/AwYAALLELoeKLg-qWAtkYtBdyTg_i2TG22w1GS-cL1GFO9J4AemIyZAw7RSuIpZw"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» qrUrl|body|string| 是 |二维码的链接|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "chatroomName": "GeWe-test-room(2)",
    "html": null,
    "chatroomId": "34559815390@chatroom"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» chatroomName|string|true|none||群名称|
|»» html|null|true|none||none|
|»» chatroomId|string|true|none||群ID|

## POST 确认进群申请

POST /group/roomAccessApplyCheckApprove

群聊开启邀请确认后，有人申请进群时群主和管理员会收到进群申请，本接口用于确认进群申请

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "chatroomId": "34757816141@chatroom",
  "msgContent": "<sysmsg type=\"NewXmlChatRoomAccessVerifyApplication\">\n\t<NewXmlChatRoomAccessVerifyApplication>\n\t\t<text> <![CDATA[\"Ashley\"想邀请1位朋友加入群聊]]></text>\n\t\t <link>\n\t\t\t<scene>roomaccessapplycheck_approve</scene>\n\t\t\t<text> <![CDATA[ 去确认]]></text>\n\t\t\t<ticket> <![CDATA[AwAAAAEAAAAVxQT9t2UOmpKWhJUViezAdSPKcaOLjP8JydTTWGHXiByZInpCp71HDoXAui/u7ByQVOutX93UlKBpkA2/3FoSAET1nA==]]> </ticket>\n\t\t\t<invitationreason> <![CDATA[进一下]]> </invitationreason>\n\t\t\t<inviterusername> <![CDATA[wxid_phyyedw9xap22]]> </inviterusername>\n\t\t\t<memberlist>\n\t\t\t\t<memberlistsize>1</memberlistsize>\n\t\t\t\t<member>\n\t\t\t\t\t<username> <![CDATA[wxid_8pvka4jg6qzt22]]> </username>\n\t\t\t\t\t<nickname> <![CDATA[白开水加糖]]> </nickname>\n\t\t\t\t\t<headimgurl> <![CDATA[http://wx.qlogo.cn/mmhead/ver_1/b6BQ3ibU4I5hDEtSyR1unAOaQMymjgk6gE9bUmteJUY6JAaJeMKJvibkLEia8PpbvuDo96bC5JKhydyLJWia7yTmahwwb0ZfjGZy9jMsibbQBVmU/96]]> </headimgurl>\n\t\t\t\t\t<quitchatroominfo> <![CDATA[曾被移出群聊,建议谨慎通过,]]> </quitchatroominfo>\n\t\t\t\t</member>\n\t\t\t</memberlist>\n\t\t</link>\n\t\t<RoomName> <![CDATA[34757816141@chatroom]]> </RoomName>\n\t</NewXmlChatRoomAccessVerifyApplication>\n</sysmsg>",
  "newMsgId": "8866462780395237368"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» chatroomId|body|string| 是 |群ID|
|» newMsgId|body|string| 是 |消息ID|
|» msgContent|body|string| 是 |消息内容|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

# 基础API/消息模块

## POST 发送文字消息

POST /message/postText

#### 注意
在群内发送消息@某人时，content中需包含@xxx

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "wxid_tdkou97nquqz22",
  "ats": "wxid_phyyedw9xap22",
  "content": "@猿猴 我在测试艾特内容"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» content|body|string| 是 |消息内容|
|» ats|body|string| 否 |@的好友，多个英文逗号分隔。群主或管理员@全部的人，则填写'notify@all'|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1703841160,
    "msgId": 0,
    "newMsgId": 3768973957878705000,
    "type": 1
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 发送文件消息

POST /message/postFile

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "fileName": "a909.xls",
  "fileUrl": "https://scrm-1308498490.cos.ap-shanghai.myqcloud.com/pkg/a909-99066ce80e03.xls?q-sign-algorithm=sha1&q-ak=AKIDmOkqfDUUDfqjMincBSSAbleGaeQv96mB&q-sign-time=1703841209;1703848409&q-key-time=1703841209;1703848409&q-header-list=&q-url-param-list=&q-signature=2a60b0f8d9169550cd83c4a3ca9cd18138b4bb88"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» fileUrl|body|string| 是 |文件链接|
|» fileName|body|string| 是 |文件名|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1703841225,
    "msgId": 769523509,
    "newMsgId": 4399037329770756000,
    "type": 6
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 发送图片消息

POST /message/postImage

#### 注意
发送图片接口会返回cdn相关的信息，如有需求同一张图片发送多次，第二次及以后发送时可使用接口返回的cdn信息拼装xml调用[转发图片接口](https://apifox.com/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196794551)，这样可以缩短发送时间

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "imgUrl": "http://dummyimage.com/400x400"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» imgUrl|body|string| 是 |图片链接|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 0,
    "msgId": 640355969,
    "newMsgId": 8992614056172360000,
    "type": null,
    "aesKey": "7678796e6d70626e6b626c6f7375616b",
    "fileId": "3052020100044b30490201000204e49785f102033d11fd0204136166b4020465966eea042437646265323234362d653662662d343464392d393363362d3139313661363863646266390204052418020201000400",
    "length": 1096,
    "width": 400,
    "height": 400,
    "md5": "e6355eab0393facbd6a2cde3f990ef60"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|null|true|none||消息类型|
|»» aesKey|string|true|none||cdn相关的aeskey|
|»» fileId|string|true|none||cdn相关的fileid|
|»» length|integer|true|none||图片文件大小|
|»» width|integer|true|none||图片宽度|
|»» height|integer|true|none||图片高度|
|»» md5|string|true|none||图片md5|

## POST 发送语音消息

POST /message/postVoice

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "voiceUrl": "https://scrm-1308498490.cos.ap-shanghai.myqcloud.com/pkg/response.silk?q-sign-algorithm=sha1&q-ak=AKIDmOkqfDUUDfqjMincBSSAbleGaeQv96mB&q-sign-time=1703841529;1703848729&q-key-time=1703841529;1703848729&q-header-list=&q-url-param-list=&q-signature=781831fe71ad4bbb582715bf197a9cf86ec80c97",
  "voiceDuration": 2000
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» voiceUrl|body|string| 是 |语音文件的链接，仅支持silk格式|
|» voiceDuration|body|integer| 是 |语音时长，单位毫秒|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1704357563,
    "msgId": 640355967,
    "newMsgId": 2321462558768366600,
    "type": null
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 发送视频消息

POST /message/postVideo

#### 注意
发送视频接口会返回cdn相关的信息，如有需求同一个视频发送多次，第二次及以后发送时可使用接口返回的cdn信息拼装xml调用[转发视频接口](https://apifox.com/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196794552)，这样可以缩短发送时间

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "videoUrl": "https://scrm-1308498490.cos.ap-shanghai.myqcloud.com/pkg/436fa030-18a45a6e917.mp4?q-sign-algorithm=sha1&q-ak=AKIDmOkqfDUUDfqjMincBSSAbleGaeQv96mB&q-sign-time=1703841673;1703848873&q-key-time=1703841673;1703848873&q-header-list=&q-url-param-list=&q-signature=2527904720ee07fd5bfc6cfffa001b415fd08329",
  "thumbUrl": "https://scrm-1308498490.cos.ap-shanghai.myqcloud.com/pkg/hhh.jpeg?q-sign-algorithm=sha1&q-ak=AKIDmOkqfDUUDfqjMincBSSAbleGaeQv96mB&q-sign-time=1703841885;1703849085&q-key-time=1703841885;1703849085&q-header-list=&q-url-param-list=&q-signature=c0a3837bde236636c342373e19551e332c40d847",
  "videoDuration": 10
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» videoUrl|body|string| 是 |视频的链接|
|» thumbUrl|body|string| 是 |缩略图的链接|
|» videoDuration|body|integer| 是 |视频的播放时长，单位秒|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": null,
    "msgId": 769523567,
    "newMsgId": 945590746179451500,
    "type": null,
    "aesKey": "687a636f627579667a756a7168717968",
    "fileId": "3052020100044b304902010002043904752002033d11ff02045dd79b240204658e9072042466633131376136662d366566632d343638662d613633662d3536316139616133383362350204012400040201000400",
    "length": 1315979
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|null|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|null|true|none||消息类型|
|»» aesKey|string|true|none||cdn相关的aeskey|
|»» fileId|string|true|none||cdn相关的fileid|
|»» length|integer|true|none||视频文件大小|

## POST 发送链接消息

POST /message/postLink

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "title": "澳门这一夜",
  "desc": "39岁郭碧婷用珠圆玉润的身材，狠狠打脸了白幼瘦女星",
  "linkUrl": "https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_8864265500294006781%22%7D&n_type=-1&p_from=-1",
  "thumbUrl": "https://pics3.baidu.com/feed/0824ab18972bd407a9403f336648d15c0db30943.jpeg@f_auto?token=d26f7f142871542956aaa13799ba1946"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» title|body|string| 是 |链接标题|
|» desc|body|string| 是 |链接描述|
|» linkUrl|body|string| 是 |链接地址|
|» thumbUrl|body|string| 是 |链接缩略图地址|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1703841982,
    "msgId": 769523572,
    "newMsgId": 3358797740318931000,
    "type": 5
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 发送名片消息

POST /message/postNameCard

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "nickName": "谭艳",
  "nameCardWxid": "wxid_0xsqb3o0tsvz22"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» nickName|body|string| 是 |名片的昵称|
|» nameCardWxid|body|string| 是 |名片的wxid|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1703842036,
    "msgId": 0,
    "newMsgId": 3285058507819179500,
    "type": 42
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 发送emoji消息

POST /message/postEmoji

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "emojiMd5": "4cc7540a85b5b6cf4ba14e9f4ae08b7c",
  "emojiSize": 102357
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» emojiMd5|body|string| 是 |emoji图片的md5|
|» emojiSize|body|integer| 是 |emoji的文件大小|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": null,
    "msgId": 769523643,
    "newMsgId": 891398861855787000,
    "type": null
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 发送appmsg消息

POST /message/postAppMsg

#### 注意
本接口可用于发送所有包含<appmsg>节点的消息，例如：音乐分享、视频号、引用消息等等

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "appmsg": "<appmsg appid=\"\" sdkver=\"0\">\n\t\t<title>一审宣判！蔡鄂生被判死缓</title>\n\t\t<des />\n\t\t<action />\n\t\t<type>5</type>\n\t\t<showtype>0</showtype>\n\t\t<soundtype>0</soundtype>\n\t\t<mediatagname />\n\t\t<messageext />\n\t\t<messageaction />\n\t\t<content />\n\t\t<contentattr>0</contentattr>\n\t\t<url>http://mp.weixin.qq.com/s?__biz=MjM5MjAxNDM4MA==&amp;mid=2666774093&amp;idx=1&amp;sn=aa405094dd00034d004f6e8287f86e9b&amp;chksm=bcc9d903635a9c284591edda1f027c467245d922d7d66c32d3cd2c6af1c969a7ea0896aa7639&amp;scene=0&amp;xtrack=1#rd</url>\n\t\t<lowurl />\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<appattach>\n\t\t\t<totallen>0</totallen>\n\t\t\t<attachid />\n\t\t\t<emoticonmd5 />\n\t\t\t<fileext />\n\t\t\t<cdnthumburl>3057020100044b304902010002048399cc8402032f57ed02041388e6720204658e922d042462666538346165322d303035382d343262322d616538322d3337306231346630323534360204051408030201000405004c53d900</cdnthumburl>\n\t\t\t<cdnthumbmd5>ea3d5e8d4059cb4db0a3c39c789f2d6f</cdnthumbmd5>\n\t\t\t<cdnthumblength>93065</cdnthumblength>\n\t\t\t<cdnthumbwidth>1080</cdnthumbwidth>\n\t\t\t<cdnthumbheight>459</cdnthumbheight>\n\t\t\t<cdnthumbaeskey>849df42ab37c8cadb324fe94ba46d76e</cdnthumbaeskey>\n\t\t\t<aeskey>849df42ab37c8cadb324fe94ba46d76e</aeskey>\n\t\t\t<encryver>0</encryver>\n\t\t</appattach>\n\t\t<extinfo />\n\t\t<sourceusername>gh_363b924965e9</sourceusername>\n\t\t<sourcedisplayname>人民日报</sourcedisplayname>\n\t\t<thumburl>https://mmbiz.qpic.cn/sz_mmbiz_jpg/xrFYciaHL08DCJtwQefqrH8JcohbOHhTpyCPab8IgDibkTv3Pspicjw8TRHnoic2tmiafBtUHg7ObZznpWocwkCib6Tw/640?wxtype=jpeg&amp;wxfrom=0</thumburl>\n\t\t<md5 />\n\t\t<statextstr />\n\t\t<mmreadershare>\n\t\t\t<itemshowtype>0</itemshowtype>\n\t\t</mmreadershare>\n\t</appmsg>"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» appmsg|body|string| 是 |回调消息中的appmsg节点内容|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1703842453,
    "msgId": 769523712,
    "newMsgId": 3090682956820882400,
    "type": 0
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 发送小程序消息

POST /message/postMiniApp

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "miniAppId": "wx1f9ea355b47256dd",
  "userName": "gh_690acf47ea05@app",
  "title": "最快29分钟 好吃水果送到家",
  "coverImgUrl": "https://che-static.vzhimeng.com/img/2023/10/30/67d55942-e43c-4fdb-8396-506794ddbdbc.jpg",
  "pagePath": "pages/homeDelivery/index.html",
  "displayName": "百果园+"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» miniAppId|body|string| 是 |小程序ID|
|» displayName|body|string| 是 |小程序名称|
|» pagePath|body|string| 是 |小程序打开的地址|
|» coverImgUrl|body|string| 是 |小程序封面图链接|
|» title|body|string| 是 |小程序标题|
|» userName|body|string| 是 |归属的用户ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1704162674,
    "msgId": 769533691,
    "newMsgId": 3190424380344821000,
    "type": 33
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 转发文件

POST /message/forwardFile

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "xml": "<?xml version=\"1.0\"?>\n<msg>\n\t<appmsg appid=\"\" sdkver=\"0\">\n\t\t<title>info.json</title>\n\t\t<des />\n\t\t<action />\n\t\t<type>6</type>\n\t\t<showtype>0</showtype>\n\t\t<soundtype>0</soundtype>\n\t\t<mediatagname />\n\t\t<messageext />\n\t\t<messageaction />\n\t\t<content />\n\t\t<contentattr>0</contentattr>\n\t\t<url />\n\t\t<lowurl />\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<appattach>\n\t\t\t<totallen>63</totallen>\n\t\t\t<attachid>@cdn_3057020100044b304902010002043904752002032f7d6d02046bb5bade02046593760c042433653765306131612d646138622d346662322d383239362d3964343665623766323061370204051400050201000405004c53d900_f46be643aa0dc009ae5fb63bbc73335d_1</attachid>\n\t\t\t<emoticonmd5 />\n\t\t\t<fileext>json</fileext>\n\t\t\t<cdnattachurl>3057020100044b304902010002043904752002032f7d6d02046bb5bade02046593760c042433653765306131612d646138622d346662322d383239362d3964343665623766323061370204051400050201000405004c53d900</cdnattachurl>\n\t\t\t<aeskey>f46be643aa0dc009ae5fb63bbc73335d</aeskey>\n\t\t\t<encryver>0</encryver>\n\t\t\t<overwrite_newmsgid>594239960546299206</overwrite_newmsgid>\n\t\t\t<fileuploadtoken>v1_0bgfyCkUmoZYYyvXys0cCiJdd2R/pKPdD2TNi9IY6FOt+Tvlhp3ijUoupZHzyB2Lp7xYgdVFaUGL4iu3Pm9/YACCt20egPGpT+DKe+VymOzD7tJfsS8YW7JObTbN8eVoFEetU5HSRWTgS/48VVsPZMoDF6Gz1XJDLN/dWRxvzrbOzVGGNvmY4lpXb0kRwXkSxwL+dO4=</fileuploadtoken>\n\t\t</appattach>\n\t\t<extinfo />\n\t\t<sourceusername />\n\t\t<sourcedisplayname />\n\t\t<thumburl />\n\t\t<md5>d16070253eee7173e467dd7237d76f60</md5>\n\t\t<statextstr />\n\t</appmsg>\n\t<fromusername>zhangchuan2288</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname></appname>\n\t</appinfo>\n\t<commenturl></commenturl>\n</msg>"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» xml|body|string| 是 |文件消息的xml|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1704162866,
    "msgId": 769533740,
    "newMsgId": 6455486805605396000,
    "type": 6
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 转发图片

POST /message/forwardImage

#### 注意
若通过发送图片消息获取cdn信息后可替换xml中的aeskey、cdnthumbaeskey、cdnthumburl、cdnmidimgurl、length、md5等参数来进行转发

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "xml": "<?xml version=\"1.0\"?>\n<msg>\n\t<img aeskey=\"294774c8ac2ca8f8114e4d58d2ba78a5\" encryver=\"1\" cdnthumbaeskey=\"294774c8ac2ca8f8114e4d58d2ba78a5\" cdnthumburl=\"3057020100044b304902010002043904752002032f7d6d02046bb5bade020465937656042436626431373937632d613430642d346137662d626230352d3832613335353935333130630204051818020201000405004c543d00\" cdnthumblength=\"2253\" cdnthumbheight=\"120\" cdnthumbwidth=\"111\" cdnmidheight=\"0\" cdnmidwidth=\"0\" cdnhdheight=\"0\" cdnhdwidth=\"0\" cdnmidimgurl=\"3057020100044b304902010002043904752002032f7d6d02046bb5bade020465937656042436626431373937632d613430642d346137662d626230352d3832613335353935333130630204051818020201000405004c543d00\" length=\"4061\" md5=\"799ee4beed51720525232aef6a0d2ec4\" />\n\t<platform_signature></platform_signature>\n\t<imgdatahash></imgdatahash>\n</msg>"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» xml|body|string| 是 |文件消息的xml|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 0,
    "msgId": 769533749,
    "newMsgId": 7003061792458481000,
    "type": null,
    "aesKey": "294774c8ac2ca8f8114e4d58d2ba78a5",
    "fileId": "3057020100044b304902010002043904752002032f7d6d02046bb5bade020465937656042436626431373937632d613430642d346137662d626230352d3832613335353935333130630204051818020201000405004c543d00",
    "length": null,
    "width": null,
    "height": null,
    "md5": null
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|null|true|none||消息类型|
|»» aesKey|string|true|none||cdn相关的aeskey|
|»» fileId|string|true|none||cdn相关的fileid|
|»» length|integer|true|none||图片文件大小|
|»» width|integer|true|none||图片宽度|
|»» height|integer|true|none||图片高度|
|»» md5|string|true|none||图片md5|

## POST 转发视频

POST /message/forwardVideo

#### 注意
若通过发送视频消息获取cdn信息后可替换xml中的aeskey、cdnthumbaeskey、cdnvideourl、cdnthumburl、length等参数来进行转发

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "xml": "<?xml version=\"1.0\"?>\n<msg>\n\t<videomsg aeskey=\"5c5163d06757faae44eacc2146ba0575\" cdnvideourl=\"3057020100044b304902010002043904752002032f7d6d02046bb5bade0204659376a6042465623261663836382d336363332d346131332d383037642d3464626162316638303634360204051800040201000405004c56f900\" cdnthumbaeskey=\"5c5163d06757faae44eacc2146ba0575\" cdnthumburl=\"3057020100044b304902010002043904752002032f7d6d02046bb5bade0204659376a6042465623261663836382d336363332d346131332d383037642d3464626162316638303634360204051800040201000405004c56f900\" length=\"490566\" playlength=\"7\" cdnthumblength=\"8192\" cdnthumbwidth=\"135\" cdnthumbheight=\"240\" fromusername=\"zhangchuan2288\" md5=\"8804c121e9db91dd844f7a34035beb88\" newmd5=\"\" isplaceholder=\"0\" rawmd5=\"\" rawlength=\"0\" cdnrawvideourl=\"\" cdnrawvideoaeskey=\"\" overwritenewmsgid=\"0\" originsourcemd5=\"\" isad=\"0\" />\n</msg>"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» xml|body|string| 是 |文件消息的xml|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": null,
    "msgId": 769533762,
    "newMsgId": 2099537549112929300,
    "type": null,
    "aesKey": "5c5163d06757faae44eacc2146ba0575",
    "fileId": null,
    "length": 490566
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|null|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|null|true|none||消息类型|
|»» aesKey|string|true|none||cdn相关的aeskey|
|»» fileId|string|true|none||cdn相关的fileid|
|»» length|integer|true|none||视频文件大小|

## POST 转发链接

POST /message/forwardUrl

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "xml": "<?xml version=\"1.0\"?>\n<msg>\n\t<appmsg appid=\"\" sdkver=\"0\">\n\t\t<title>“李在明遇袭，颈部出血”</title>\n\t\t<des />\n\t\t<action />\n\t\t<type>5</type>\n\t\t<showtype>0</showtype>\n\t\t<soundtype>0</soundtype>\n\t\t<mediatagname />\n\t\t<messageext />\n\t\t<messageaction />\n\t\t<content />\n\t\t<contentattr>0</contentattr>\n\t\t<url>http://mp.weixin.qq.com/s?__biz=MjM5MzI5NTU3MQ==&amp;mid=2652294920&amp;idx=1&amp;sn=ad415f5d83e1471b845b2cb3fca7c3ce&amp;chksm=bce58367ee6ae84b711255705422d1554ee96b92d75648751316639d4aa09289d7827ff1cc85&amp;scene=0&amp;xtrack=1#rd</url>\n\t\t<lowurl />\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<appattach>\n\t\t\t<totallen>0</totallen>\n\t\t\t<attachid />\n\t\t\t<emoticonmd5 />\n\t\t\t<fileext />\n\t\t\t<cdnthumburl>3057020100044b304902010002048399cc8402032f7d6d020468b5bade0204659376ec042463663234636366642d323736612d343533342d623734342d3864623065633235636135390204051808030201000405004c56f900</cdnthumburl>\n\t\t\t<cdnthumbmd5>8e32cafa882f9b4f7c51fb568c0c4f8e</cdnthumbmd5>\n\t\t\t<cdnthumblength>38637</cdnthumblength>\n\t\t\t<cdnthumbwidth>658</cdnthumbwidth>\n\t\t\t<cdnthumbheight>280</cdnthumbheight>\n\t\t\t<cdnthumbaeskey>accc71cbe8ff795a94583fc514d198a8</cdnthumbaeskey>\n\t\t\t<aeskey>accc71cbe8ff795a94583fc514d198a8</aeskey>\n\t\t\t<encryver>0</encryver>\n\t\t</appattach>\n\t\t<extinfo />\n\t\t<sourceusername>gh_d29e0d22a6f9</sourceusername>\n\t\t<sourcedisplayname>澎湃新闻</sourcedisplayname>\n\t\t<thumburl>https://mmbiz.qpic.cn/mmbiz_jpg/yl6JkZAE3SibWvw5icQJpv87X084SRJOVeS3k7KMscRzov1nwicjMYzicyBIpRdJchWKTGPf4eN2H07Jicl11zMK2Pw/640?wxtype=jpeg&amp;wxfrom=0</thumburl>\n\t\t<md5 />\n\t\t<statextstr />\n\t\t<mmreadershare>\n\t\t\t<itemshowtype>0</itemshowtype>\n\t\t</mmreadershare>\n\t</appmsg>\n\t<fromusername>zhangchuan2288</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname></appname>\n\t</appinfo>\n\t<commenturl></commenturl>\n</msg>"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» xml|body|string| 是 |文件消息的xml|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1704163083,
    "msgId": 769533781,
    "newMsgId": 1947412320722133800,
    "type": 5
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 转发小程序

POST /message/forwardMiniApp

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "xml": "<?xml version=\"1.0\"?>\n<msg>\n\t<appmsg appid=\"\" sdkver=\"0\">\n\t\t<title>👇晒出新年第一杯，点赞赢饮茶月卡</title>\n\t\t<des />\n\t\t<action />\n\t\t<type>33</type>\n\t\t<showtype>0</showtype>\n\t\t<soundtype>0</soundtype>\n\t\t<mediatagname />\n\t\t<messageext />\n\t\t<messageaction />\n\t\t<content />\n\t\t<contentattr>0</contentattr>\n\t\t<url>https://mp.weixin.qq.com/mp/waerrpage?appid=wxafec6f8422cb357b&amp;type=upgrade&amp;upgradetype=3#wechat_redirect</url>\n\t\t<lowurl />\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<appattach>\n\t\t\t<totallen>0</totallen>\n\t\t\t<attachid />\n\t\t\t<emoticonmd5 />\n\t\t\t<fileext />\n\t\t\t<cdnthumburl>3057020100044b30490201000204573515c902032f7d6d020416b7bade020465922a53042437383139393934652d323662652d346430662d396466362d3466303137346139616362390204051408030201000405004c53d900</cdnthumburl>\n\t\t\t<cdnthumbmd5>33cf0a1101e7f8cd3057cd417a691f0b</cdnthumbmd5>\n\t\t\t<cdnthumblength>96673</cdnthumblength>\n\t\t\t<cdnthumbwidth>600</cdnthumbwidth>\n\t\t\t<cdnthumbheight>500</cdnthumbheight>\n\t\t\t<cdnthumbaeskey>6f3098f2ee8b351b6cc9b1818d580356</cdnthumbaeskey>\n\t\t\t<aeskey>6f3098f2ee8b351b6cc9b1818d580356</aeskey>\n\t\t\t<encryver>0</encryver>\n\t\t</appattach>\n\t\t<extinfo />\n\t\t<sourceusername>gh_e9d25e745aae@app</sourceusername>\n\t\t<sourcedisplayname>霸王茶姬</sourcedisplayname>\n\t\t<thumburl />\n\t\t<md5 />\n\t\t<statextstr />\n\t\t<weappinfo>\n\t\t\t<username><![CDATA[gh_e9d25e745aae@app]]></username>\n\t\t\t<appid><![CDATA[wxafec6f8422cb357b]]></appid>\n\t\t\t<type>2</type>\n\t\t\t<version>193</version>\n\t\t\t<weappiconurl><![CDATA[]]></weappiconurl>\n\t\t\t<pagepath><![CDATA[/pages/page/page.html?code=JKD6DA55_3&channelCode=scrm_t664sgg5mrzxkqa]]></pagepath>\n\t\t\t<shareId><![CDATA[0_wxafec6f8422cb357b_25984983017778987@openim_1704162955_0]]></shareId>\n\t\t\t<pkginfo>\n\t\t\t\t<type>0</type>\n\t\t\t\t<md5><![CDATA[]]></md5>\n\t\t\t</pkginfo>\n\t\t\t<appservicetype>0</appservicetype>\n\t\t</weappinfo>\n\t</appmsg>\n\t<fromusername>zhangchuan2288</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname></appname>\n\t</appinfo>\n\t<commenturl></commenturl>\n</msg>",
  "coverImgUrl": "http://dummyimage.com/400x400"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» xml|body|string| 是 |文件消息的xml|
|» coverImgUrl|body|string| 是 |小程序封面图链接|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "toWxid": "34757816141@chatroom",
    "createTime": 1704163145,
    "msgId": 769533801,
    "newMsgId": 5271007655758710000,
    "type": 33
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» toWxid|string|true|none||接收人的wxid|
|»» createTime|integer|true|none||发送时间|
|»» msgId|integer|true|none||消息ID|
|»» newMsgId|integer|true|none||消息ID|
|»» type|integer|true|none||消息类型|

## POST 撤回消息

POST /message/revokeMsg

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "toWxid": "34757816141@chatroom",
  "msgId": "769533801",
  "newMsgId": "5271007655758710001",
  "createTime": "1704163145"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» toWxid|body|string| 是 |好友/群的ID|
|» msgId|body|string| 是 |发送类接口返回的msgId|
|» newMsgId|body|string| 是 |发送类接口返回的newMsgId|
|» createTime|body|string| 是 |发送类接口返回的createTime|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

# 基础API/消息模块/下载

## POST 下载图片

POST /message/downloadImage

**注意** 如果下载图片失败，可尝试下载另外两种图片类型，并非所有图片都会有高清、常规图片

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "type": 2,
  "xml": "<?xml version=\"1.0\"?>\n<msg>\n\t<img aeskey=\"83721f32eeab053f06317c1de5138461\" encryver=\"1\" cdnthumbaeskey=\"83721f32eeab053f06317c1de5138461\" cdnthumburl=\"3057020100044b30490201000204a2b473b402032f7efd02045b04d83a020466bb1a2c042464303334643966392d363639312d343439632d393463302d373033346237333331396561020405150a020201000405004c505500\" cdnthumblength=\"5785\" cdnthumbheight=\"120\" cdnthumbwidth=\"120\" cdnmidheight=\"0\" cdnmidwidth=\"0\" cdnhdheight=\"0\" cdnhdwidth=\"0\" cdnmidimgurl=\"3057020100044b30490201000204a2b473b402032f7efd02045b04d83a020466bb1a2c042464303334643966392d363639312d343439632d393463302d373033346237333331396561020405150a020201000405004c505500\" length=\"9557\" md5=\"db3de4c78bc00837a32ed753a179c336\" hevc_mid_size=\"9557\" originsourcemd5=\"d5314bba593a09f61df100ba635b440e\" />\n\t<platform_signature />\n\t<imgdatahash />\n\t<ImgSourceInfo>\n\t\t<ImgSourceUrl />\n\t\t<BizType>0</BizType>\n\t</ImgSourceInfo>\n</msg>\n"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» xml|body|string| 是 |回调消息中的XML|
|» type|body|integer| 是 |下载的图片类型 1:高清图片  2:常规图片  3:缩略图|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "fileUrl": "/download/20240720/wx_BTVoJ_o_r6DpxNCNiycFE/0ca5b675-8e2c-4dc1-b288-3c44a40086ec4"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» fileUrl|string|true|none||图片链接地址，7天有效|

# 基础API/标签模块

## POST 添加标签

POST /label/add

#### 注意
标签名称不存在则是添加标签，如果标签名称已经存在，此接口会直接返回标签名及ID

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "labelName": "testtest"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» labelName|body|string| 是 |标签名称|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "labelName": "testtest",
    "labelId": 31
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» labelName|string|true|none||标签名称|
|»» labelId|integer|true|none||标签ID|

## POST 删除标签

POST /label/delete

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "labelIds": "31"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» labelIds|body|string| 是 |标签ID，多个逗号分隔|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 标签列表

POST /label/list

> Body 请求参数

```json
{
  "appId": "{{appid}}"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "labelList": [
      {
        "labelName": "朋友",
        "labelId": 1
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» labelList|[object]|true|none||none|
|»»» labelName|string|false|none||标签名称|
|»»» labelId|integer|false|none||标签ID|

## POST 修改好友标签

POST /label/modifyMemberList

#### 注意
由于好友标签信息存储在用户客户端，因此每次在修改时都需要进行全量修改。举例来说，考虑好友A（wxid_asdfaihp123），该好友已经被标记为标签ID为1和2。

在添加标签ID为3时，传递的参数如下：labelIds：1,2,3，wxIds：[wxid_asdfaihp123]。这表示要给好友A添加标签ID为3，同时保留已有的标签ID 1和2。

而在删除标签ID为1时，传递的参数如下：labelIds：2,3 ，wxIds：[wxid_asdfaihp123]。这表示要将好友A的标签ID 1删除，而保留标签ID 2。

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "labelIds": "15",
  "wxIds": [
    "zhangchuan2288"
  ]
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» labelIds|body|string| 是 |标签ID，多个逗号分隔|
|» wxIds|body|[string]| 是 |修改的好友wxid|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

# 基础API/个人模块

## POST 获取个人资料

POST /personal/getProfile

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "proxyIp": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "alias": null,
    "wxid": "zhangchuan2288",
    "nickName": "朝夕。",
    "mobile": "18761670817",
    "uin": 1042679712,
    "sex": 1,
    "province": "Jiangsu",
    "city": "Xuzhou",
    "signature": ".......",
    "country": "CN",
    "bigHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/REoLX7KfdibFAgDbtoeXGNjE6sGa8NCib8UaiazlekKjuLneCvicM4xQpuEbZWjjQooSicsKEbKdhqCOCpTHWtnBqdJicJ0I3CgZumwJ6SxR3ibuNs/0",
    "smallHeadImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/REoLX7KfdibFAgDbtoeXGNjE6sGa8NCib8UaiazlekKjuLneCvicM4xQpuEbZWjjQooSicsKEbKdhqCOCpTHWtnBqdJicJ0I3CgZumwJ6SxR3ibuNs/132",
    "regCountry": "CN",
    "snsBgImg": "http://shmmsns.qpic.cn/mmsns/FzeKA69P5uIdqPfQxp59LvOohoE2iaiaj86IBH1jl0F76aGvg8AlU7giaMtBhQ3bPibunbhVLb3aEq4/0"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» alias|string|true|none||微信号|
|»» wxid|string|true|none||微信ID|
|»» nickName|string|true|none||昵称|
|»» mobile|string|true|none||绑定的手机号|
|»» uin|integer|true|none||uin|
|»» sex|integer|true|none||性别|
|»» province|string|true|none||省份|
|»» city|string|true|none||城市|
|»» signature|string|true|none||签名|
|»» country|string|true|none||国家|
|»» bigHeadImgUrl|string|true|none||大尺寸头像|
|»» smallHeadImgUrl|string|true|none||小尺寸头像|
|»» regCountry|string|true|none||注册国家|
|»» snsBgImg|string|true|none||朋友圈背景图|

## POST 获取自己的二维码

POST /personal/getQrCode

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "proxyIp": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "qrCode": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT/2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT/wAARCAIAAgADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD5kooor8XP6jCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKK1tP03biWUc9lPb61+7FfUYXIaten7SpLlv0tf9UfAZhxdQwlZ0aFP2lt3eyv5aO5+CNFfvdRXZ/q5/wBPv/Jf+CeZ/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRX73UUf6uf9Pv/ACX/AIIf67/9Q3/k/wD9qfgjRX73UUf6uf8AT7/yX/gh/rv/ANQ3/k//ANqfgjRRRXxZ+pBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRSqpdgqjJPQCmk27IltRV3sABYgAZJ7Vr6fpwhxJKMv2HpT7DTxbgO/Mn8qu193leUKlaviF73RdvXz/ACPyPiDiR4i+EwT9zrLv5Ly/P03K/cavw5r9xq+sPzo/A/xF4ixutbVvZ5Af0Fc7Z2ct/OsMK7nP5D3NFnZy386wwruc/kPc1/QlSSsU227s/CjSdJi0qDYnzSH7745P/wBasbxF4ixutbVvZ5Af0FfvhRSsU56WR/PbZ2ct/OsMK7nP5D3Nd3pOkxaVBsT5pD998cn/AOtX7r0U2rijJR6H4H+IvEWN1rat7PID+gr98K/nts7OW/nWGFdzn8h7mv6EqFoKTctWFFfgf4i8RY3Wtq3s8gP6Cv3woQSSTsj+e2zs5b+dYYV3OfyHua/oSr8KNJ0mLSoNifNIfvvjk/8A1q/dehO45R5Uj8D/ABF4ixutbVvZ5Af0FfvhRX4EeHvDxuitzcriHqqH+L3+lGwazZ++9fhZqGoQ6XbGSQ4A4VR1J9BX7p0UNXCMuU/nx1HUZdTuDLKfZVHRRWv4e8PG6K3NyuIeqof4vf6V++9fhZqGoQ6XbGSQ4A4VR1J9BSemxUFd3YahqEOl2xkkOAOFUdSfQV+6dfz46jqMup3BllPsqjoorX8PeHjdFbm5XEPVUP8AF7/ShaA3zuyP33r8LNQ1CHS7YySHAHCqOpPoKNQ1CHS7YySHAHCqOpPoK4TUdRl1O4Msp9lUdFFL4h/ww1HUZdTuDLKfZVHRRWv4e8PG6K3NyuIeqof4vf6V++9FUZp63Z+FmoahDpdsZJDgDhVHUn0FcJqOoy6ncGWU+yqOiiv6DqKErDlNyPwI8PeHjdFbm5XEPVUP8Xv9K6TUNQh0u2MkhwBwqjqT6Cv3TopNXGp8qskfz46jqMup3BllPsqjoor+g6vwI8PeHjdFbm5XEPVUP8Xv9K/femS092fhZqGoQ6XbGSQ4A4VR1J9BXCajqMup3BllPsqjooo1HUZdTuDLKfZVHRRX9B1JKxUpcx+BHh7w8borc3K4h6qh/i9/pXSahqEOl2xkkOAOFUdSfQV+6dFDVwU+VWSP58dR1GXU7gyyn2VR0UVr+HvDxuitzcriHqqH+L3+lfvvRTJT1uz8LNQ1CHS7YySHAHCqOpPoK/dOv58dR1GXU7gyyn2VR0UV/QdQlYc5czPwRooor8YP6gCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKfFC87hEGWNVGLm1GKu2ROcacXObsluxI42lcKoyx7Vt2Ngtqu4/NIep9KfZ2S2iernq1WK/QcrylYZKtW1n+X/BPxnP+IpY9vDYV2pdX1l/wPL7wooor6U+FCv3Gr8Oa/cagD8KNJ0mLSoNifNIfvvjk/wD1q/devwP8ReIsbrW1b2eQH9BX74VKNJtbI/nMooor8+P6/Cv6M6/nMr+jOvoso/5efL9T8d8Qv+YX/t//ANsPwo0nSYtKg2J80h+++OT/APWr916/A/xF4ixutbVvZ5Af0FfvhXvo/IptbIK/CjSdJi0qDYnzSH7745P/ANav3Xr8D/EXiLG61tW9nkB/QUPUINK7Z++FFFFUZhX4WahqEOl2xkkOAOFUdSfQUahqEOl2xkkOAOFUdSfQV+6dT8Rt/DCvwI8PeHjdFbm5XEPVUP8AF7/Sv33r8LNQ1CHS7YySHAHCqOpPoKGyYJPVn7p1/PjqOoy6ncGWU+yqOiiv6DqKozCiiv58dR1GXU7gyyn2VR0UUAf0HUV+BHh7w8borc3K4h6qh/i9/pXSahqEOl2xkkOAOFUdSfQVLZooXV2funX8+Oo6jLqdwZZT7Ko6KK/oOoqjM/Ajw94eN0VublcQ9VQ/xe/0r996K/nx1HUZdTuDLKfZVHRRSKbVj+g6ivwI8PeHjdFbm5XEPVUP8Xv9K6TUNQh0u2MkhwBwqjqT6Ck2UoXV2GoahDpdsZJDgDhVHUn0FfunX8+Oo6jLqdwZZT7Ko6KK/oOppWFOXMz8CPD3h43RW5uVxD1VD/F7/Sv33r8LNQ1CHS7YySHAHCqOpPoK/dOkncc0o2SP5zKKKK/Pj+vwr+jOv5zK/ozr6LKP+Xny/U/HfEL/AJhf+3//AGw/A/w74dxturpfdIyP1NfvhX4Uatq0WlQb3+aQ/cTPJ/8ArV+69e+tT8jmkrJH4I0UUV+Mn9PBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUVNbWr3Um1Rx3bsK0p051ZKEFdsxrVqeHpurVlaK3YkFu9zIEQZPc+lbtraJapheWPVvWlt7ZLaPag+p7mpa/RcsyuGDXtJ6zf4en+Z+JZ7xBUzOTo0vdpLp1fm/0QUUUV758eFFFFABX7jV+HNfuNQB/PbZ2ct/OsMK7nP5D3Nf0JV+E+k6VFpUGxPmkP33xya/dikncuUeVI/nMor+jOivn/AOyP+nn4f8E/Xv8AiIX/AFC/+T//AGh/OZX9GdFFehhMJ9V5veve3Q+P4h4h/t72X7rk5Ob7V73t5Lsfz22dnLfzrDCu5z+Q9zX9CVfhPpOlRaVBsT5pD998cmv3Yr0E7nyMo8qQV/PPRXQeH/D5uStzcr+56qh/i/8ArUbEpNuyF8PeHjdFbm5XEPVUP8Xv9K6TUNQh0u2MkhwBwqjqT6Cv3Tr+fHUdRl1O4Msp9lUdFFJq5opqK0DUdRl1O4Msp9lUdFFf0HV+A/h/w+bkrc3K/ueqof4v/rV+/FMhp7s/CzUNQh0u2MkhwBwqjqT6CuE1HUZdTuDLKfZVHRRRqOoy6ncGWU+yqOiitbw/4fNyVublf3PVUP8AF/8AWpJWLbc3ZH78UUUVRkfz46jqMup3BllPsqjoorX8PeHjdFbm5XEPVUP8Xv8ASk8P+Hzclbm5X9z1VD/F/wDWr9+KXki9tWfhZqGoQ6XbGSQ4A4VR1J9BXCajqMup3BllPsqjooo1HUZdTuDLKfZVHRRWt4f8Pm5K3Nyv7nqqH+L/AOtSSsU25uyF8PeHjdFbm5XEPVUP8Xv9K/fevwrv9Ri0y2MkhwBwqjqT6Cv3UoTuKaUbJBX4EeHvDxuitzcriHqqH+L3+lJ4f8Pm5K3Nyv7nqqH+L/61dJf6jFplsZJDgDhVHUn0FDfRFRj1Z+6lfz46jqMup3BllPsqjoor+g6iqMQor8K7/UYtMtjJIcAcKo6k+gr91KSdy5R5T+fHUdRl1O4Msp9lUdFFf0HV+A/h/wAPm5K3Nyv7nqqH+L/61fvxQJp7s/nMor+jOivn/wCyP+nn4f8ABP1//iIX/UL/AOT/AP2h/OZX9GdFFehhMJ9V5veve3Q+P4h4h/t72X7rk5Ob7V73t5Lsfz23l5LfztNM25z+Q9hX9CVfgd4e8PY23V0vPVIyP1NfvjXoHyDTWrPwRooor8YP6hCiiigAooooAKKKKACiiigAooooAKKKKACiirVlYtdNk/LGOrVtRo1MRNU6au2cuKxVHB0nWrytFf19420s3u3wOEHVq3YYEt4wiDA/nSxxrCgRBhR2p1fpOXZbDAxu9Zvd/oj8NzrPK2bVOVe7TWy/V+f5BRRRXsnzAUUUUAFFFFABX7jV+HNfuNQB+B3iHxDjda2rc9HkB/QVz1nZy306xRLuY/kPev6EqKVrFOXM7s/CbStKi0uDYnzSH7745NY/iHxDjda2rc9HkB/QV++NFKxTnpZH89tnZy306xRLuY/kPeu50rSotLg2J80h+++OTX7s0U2rijJR6H4HeIfEON1ratz0eQH9BX740UUJWFJuTuz8BvD/AIfNyVublcQ9VQ/xf/Wr9+a/Cq/1CHTLYySHAHCqOpPoK/dWkncqaUbJH8+Oo6jLqVwZZT7Ko6KK/oOr8BvD/h/7SVubkYi6qh/i/wDrV0l/qEOmWxkkOAOFUdSfQUXtoNQb1YX9/DplsZJDgDhVHUn0FfurRX4DeH/D/wBpK3NyMRdVQ/xf/Wo2E25uyDw/4fNyVublcQ9VQ/xf/Wr9+aK/nx1HUZdSuDLKfZVHRRTJbVg1HUZdSuDLKfZVHRRX9B1fgN4f8P8A2krc3IxF1VD/ABf/AFq/fmgGnuz8Kr+/h0y2MkhwBwqjqT6Cv3Vr+fHUdRl1K4Msp9lUdFFavh/w/wDaStzcjEXVUP8AF/8AWpLQtvndkHh/w+bkrc3K4h6qh/i/+tX780V/PjqOoy6lcGWU+yqOiimQ2rBqOoy6lcGWU+yqOiiv6Dq/Abw/4f8AtJW5uRiLqqH+L/61dJf6hDplsZJDgDhVHUn0FK9tC1BvVhf38OmWxkkOAOFUdSfQV+6tFFNKxMpcx+A3h/w+bkrc3K4h6qh/i/8ArV+/NfhVf6hDplsZJDgDhVHUn0FfurSTuOaUbJH8+Oo6jLqVwZZT7Ko6KK/oOooqjPc/Cq/v4dMtjJIcAcKo6k+grhtR1GXUrgyyn2VR0UV/QdRSSsXKbkfgd4e8PY23V0vPVIyP1NbGq6rFpcG9/mkP3Ezya/dmila5SnZWSP57by8lvp2llbcx/Ie1dD4e8PY23V0vPVIyP1NfvjRTZCdndn4TarqsWlwb3+aQ/cTPJr92aKKErDlLmPwRooor8YP6gCiiigAooooAKKKKACiiigAooooAKKKv2GnGciSQYj7D1rqw2GqYqoqdJXZwY3HUMvouvXdkvvb7LzGWOntcnc3EY7+tbaIsahVACjoBSqoUAAYA7Civ0rAYCngYWjrJ7v8ArofhOb5xXzarzT0gto9v835hRRRXqHghRRRQAUUUUAFFFFABX7jV+HNfuNQAUV+BniDxBjdbWzezyA/oKwLS0lvZ1iiXcx/T3pFNWdkf0JUV+EmlaVFpcG1fmkP3n9a/duhO45R5bH4GeIPEGN1tbN7PID+grmqK3tA0A3JW4uFxF1VD/F/9ajYNZsNA0A3JW4uFxF1VD/F/9aujv7+HTbcySHAHCqOpPoK/dev58NQ1CXUrgyyn/dUdFFJq5SmorQ/oPor8BdA0A3JW4uFxF1VD/F/9av36pmbTSuFfz4ahqEupXBllP+6o6KK/oPopiCvwov7+HTbcySHAHCqOpPoK/dev58NQ1CXUrgyyn/dUdFFJq5cZcqYahqEupXBllP8AuqOiiv6D6KKZG4UUUUAfgLoGgG5K3FwuIuqof4v/AK1fv1RX8+GoahLqVwZZT/uqOiikU2rBqGoS6lcGWU/7qjoor+g+ivwov7+HTbcySHAHCqOpPoKG7DS5rtsL+/h023MkhwBwqjqT6Cv3Xor8BdA0A3JW4uFxF1VD/F/9alsNtzZ+/VfhRf38Om25kkOAOFUdSfQUX9/DptuZJDgDhVHUn0FfuvR8RX8MK/AXQNANyVuLhcRdVQ/xf/Wo0DQDclbi4XEXVUP8X/1q6O/v4dNtzJIcAcKo6k+gob6IIR6s/deiv58NQ1CXUrgyyn/dUdFFf0H1RifgZ4f8P423NyvukZH6mtjVdVi0uDc3zSH7qetGq6rFpcG5vmkP3U9a/duoSvqbtqCsgor8DPD/AIfxtublfdIyP1NbGq6rFpcG5vmkP3U9adyVDS7P3br+e27u5b2dpZW3Mf09q/oSr8DPD/h/G25uV90jI/U03oRFOWiP3zor8JNV1WLS4NzfNIfup61+7dCdxyjyn4I0UUV+MH9QBRRRQAUUUUAFFFFABRRRQAUUUUAaWn6b5mJJRhey+tawGBRRX6zg8FSwVPkp79X3P5zzPNK+aVva1np0XRL+t2FFFFd55AUUUUAFFFFABRRRQAUUUUAFfuNX4c1+41AH89tpaS3s6xRLuY/kPev6EqK/AvXtfxutrZvZ5B/IUikk0Gv6/jdbWzc9HkH8hXN0V/QxQlYJNyd2fgLoOgm4K3Fwv7rqqH+L/wCtX79UV/PhqGoS6jOZJD7Ko6KKAbVg1DUJdRnMkh9lUdFFf0H0UUydz8Jr6+i023MkhwBwqjqT6CuJ1DUJdRnMkh9lUdFFf0H0UkrFym5H4C6DoJuCtxcL+66qh/i/+tX79UV/PhqGoS6jOZJD7Ko6KKBNqwahqEuozmSQ+yqOiitXQdBNwVuLhf3XVUP8X/1q/fqigE9bs/Ca+votNtzJIcAcKo6k+gr92aKKErDlLmCvwmvr6LTbcySHAHCqOpPoK/dmihq4Rlyn8+GoahLqM5kkPsqjoor+g+vwE0HQTcFbi4X911VD/F7/AErob6+i023MkhwBwqjqT6Cle2hSg3qxb6+i023MkhwBwqjqT6Cv3Zor8BNB0E3BW4uF/ddVQ/xe/wBKNhNubsj9+6/Ca+votNtzJIcAcKo6k+gr92aKbVxRlyhX4C6DoJuCtxcL+66qh/i/+tX79UUEppPU/Ca+votNtzJIcAcKo6k+gridQ1CXUZzJIfZVHRRRqGoS6jOZJD7Ko6KK/oPpJWLlLmCvwi1TVItMg3N80h+6nc1+7tfz23d3LeztLK25j+Q9qbVxRlypn9CVFFfhFqmqRaZBub5pD91O5obsEY3DVNUi0yDc3zSH7qdzXFXd3LeztLK25j+Q9q/oSr8C9A0HG25uV90jP8zS2Kbc3YNA0DG25uV56pGf5mv30r8ItU1SLTINzfNIfup3Nfu7QtQmkrJBRRRVGR+CNFFFfi5/UYUUUUAFFFFABRRRQAUUUUAFFFFAHUUUUV+0H8uBRRRQAUUUUAFFFFABRRRQAUUUUAFfuNX4c1+41AH4F69r/wB62tm9nkH8hX76UV+AehaEbkrcXC/uuqof4v8A61LYvWbP38r8Jb6/h063MknA6Ko6n2FNvr6LTrcySHA6Ko6n2Ffu5S+Iv+GFfgHoOh/aCtxcL+66qh/i/wDrUaFoRuStxcL+66qh/i/+tX7+U9yEuXVn4S31/Dp1uZJOB0VR1PsK4rUNQl1GcyyH/dUdFFf0H1+AehaEbkrcXC/uuqof4v8A61K1im3N2R+/lFFFUZBRRRQAUV/Pff38uoTmSQ/7qjoorU0LQjclbi4X911VD/F/9alexSV3ZBoOh/aCtxcL+66qh/i/+tX7+V+Ed9fRadbmSQ4HRVHU+wr93KSdyppRskFFFFUZhRRRQAV+Et9fw6dbmSTgdFUdT7Cm319Fp1uZJDgdFUdT7CuLv7+XUJzJIf8AdUdFFR8Rt/DP6EK/APQdD+0Fbi4X911VD/F/9av38oqjJNJ6n4S31/Dp1uZJOB0VR1PsK/dqiihKxUpcwUUV/PZdXUl5M0srbmP6UyD+hOvwK0HQgNtzcr7pGR+po0LQsbbm5X3SM/zNa2p6nHpsO5vmkP3U9alvojaMbe9IXU9Vi02Hc3zSH7qetfu9RRTSsRKXMfgVoOhAbbm5X3SMj9TWvqeqxabDub5pD91PWk1PU49Nh3N80h+6nrX7v1KV9TRtQVkfz23d3LeztLK25j+Q9q3dB0IDbc3K+6RkfqaNC0LG25uV90jP8zX761W+iI+HVn4Q6nqsWmw7m+aQ/dT1r93qKKErClLmPwRooor8YP6gCiiigAooooAKKKKACiiigAooooA6iiiiv2g/lwKKKKACiiigAooooAKKKKACiiigAr9xq/Dmv3GoAKKK/nvvr6XUJzJIfoo6AUAf0IV+AWh6GbgrcXC/uuqof4v/AK1fv7X4QXt9Fp8Bd+AOFUd/YVLZpBJ6s/d+v577+/l1CcySH/dXsBRfX0uoTmSQ/RR0Ar+hCqI8kfgFoehm4K3Fwv7rqqH+L/61b97fR6fbmSQ4A4VR1PsK/d6ipauWp8qskfz339/LqE5kkP8Aur2Ar+hCiiqM9z8Ib2+j0+3MkhwBwqjqfYV+71fz3319LqE5kkP0UdAK0tE0X7QVnuF/ddVQ/wAX/wBapWhq3zuyF0PQzcFbi4X911VD/F/9at+9vo9PtzJIcAcKo6n2FJe30WnwF34A4VR39hX7v0tym1BWR/Pff38uoTmSQ/7q9gK/oQr8AdE0X7QVnuF/ddVQ/wAX/wBav3+qjJp7s/CG9vo9PtzJIcAcKo6n2Fcbf38uoTmSQ/7q9gKL6+l1CcySH6KOgFaWiaL9oKz3C/uuqof4v/rUkrFtubshdD0M3BW4uF/ddVQ/xf8A1q372+j0+3MkhwBwqjqfYUl7fRafAXfgDhVHf2Ffu/S3KbUFZBX4BaHoZuCtxcL+66qh/i/+tX7+0VRimk9Qor+e++vpdQnMkh+ijoBX9CFMQV+D2papHpsO5jukP3U9a/eGik1cuMuU/nsurqS8maWVtzH9K3NC0PG25uF90Q/zNGh6JjbcXC+6If5mv33o30Q/h1YV/PZdXUl5M0srbmP6UXV1JeTNLK25j+lf0J0yAr8HtS1SPTYdzHdIfup61+8Nfz2XV1JeTNLK25j+lJq5UZcqZ/QnX4EaFoeNtzcL7oh/ma/feihiTSd2fg9qWqR6bDuY7pD91PWv3hr+ey6upLyZpZW3Mf0r+hOhKw5S5mFFfg7qWpx6dDub5nP3U9a/eKhO4Sjyn4I0UUV+MH9QBRRRQAUUUUAFFFFABRRRQAUUUUAdRRRRX7Qfy4FFFFABRRRQAUUUUAFFFFABRRRQAV+41fhzX7jUAFfgDomifaCJ5x+66qp/i/8ArUmi6L9oInnH7rqqn+L/AOtX7/0ty0uXVn4P3t7Fp8BkkOB0VR1PsK4++vpL+cySH6KOgFf0IUUJWCU3I/AHRNE+0ETzj911VT/F/wDWrevb2LT4DJIcDoqjqfYUy8vIrCDe/A6BR39q/eOp3NG1BWR/PffX0l/OZJD9FHQCtLRNE+0ETzj911VT/F/9av3+oqjJPW7Cv5776+kv5zJIfoo6AUXt7JfzGSQ/RewFaOi6L9oInnH7rqqn+L/61AJNuyP3/oor+e+9vZL+YySH6L2Apkn9CFfgDomifaCJ5x+66qp/i/8ArUmi6L9oInnH7rqqn+L/AOtW5eXkVhBvfgdAo7+1S30RtCPVn7x0UUVRiFfg/e3sWnwGSQ4HRVHU+wr94KKTVy4y5Qr8AdE0T7QRPOP3XVVP8X/1qTRdF+0ETzj911VT/F/9aty8vIrCDe/A6BR39qTfRFwj1Y+9vYtPgMkhwOiqOp9hX7wUUU0rESlzH4D6JomNtxcL7oh/ma1NS1KPTodzfM5+6nrTdR1GPT4dzcufup61yVzcyXczSSNlj+lTuatqCsgurqS8maWVssf0r+hOivwZ1HUY9Ph3Ny5+6nrVN2Mkua7bP3mor+ey5uZLuZpJGyx/StrRdFxtuLhfdEP8zQ3YSjzOyP35r8G9S1KPTodzfM5+6nrTdR1GPT4dzcufup61yVzcyXczSSNlj+lLc0/h6ILq6kvJmllbLH9K29E0TG24uF90Q/zNfvxRTZmnZ3YV/PZdXUl5M0srZY/pRc3Ml3M0kjZY/pW1oui423FwvuiH+ZobsCTbshdE0TG24uF90Q/zNampalHp0O5vmc/dT1r95KKVrlqdlZI/nsurqS8maWVssf0r+hOiiqMj8EaKKK/Fz+owooooAKKKKACiiigAooooAKKKKAOoooor9oP5cCiiigAooooAKKKKACiiigAooooAK/cavw5r9xqACv57r29kvpjJIfoo6AUXt7JfTGSQ/RewFaGj6R55E84/d9VU/wAX/wBakUk27IXRtH88iecfu+qqf4v/AK1f0AUV/Pde3sl9MZJD9F7AUA2rH9CNfz/6No/nkTzj931VT/F/9ak0fSPPInnH7vqqn+L/AOtX9ANG40uXVn4N3l7HYQb34HQKO/tX7yUV/P8AaPpHnkTzj931VT/F/wDWpbDbc2Lo2j+eRPOP3fVVP8X/ANav6AKK/nuvb2S+mMkh+i9gKZLasf0I1/P/AKNo/nkTzj931VT/ABf/AFqTR9I88iecfu+qqf4v/rVt3d5FYwF3PHQKO9Jvoi4x6s/eav57r29kvpjJIfoo6AV/QjRVGQUV+DN3eRWMBdzx0CjvXKXt7JfTGSQ/RewFJO5coqPU/oRr+f8A0bR/PInnH7vqqn+L/wCtSaPpHnkTzj931VT/ABf/AFq/oBo3BLl1Z+Dd5ex2EG9+B0Cjv7VyV7eyX0xkkP0UdAKL29kvpjJIfovYCtbRtHAxPcD3VD/M0tim3N2QaNo2NtxOvuqH+ZrU1DUksIdzYLn7qetJqGox2EO5uXP3U9a5S5uZLuYySHLH9KW5TagrILm5ku5mkkbLH9K/oTr8BNG0cDE9wPdUP8zWnqGox2EO5uXP3U9ad+iJULq7F1DUksIdzYLn7qetcnc3Ml3M0kjZY/pX9CdFNKxMpOQV+DGoaklhDubBc/dT1pNQ1GOwh3Ny5+6nrX70Uty/4eiP57Lm5ku5mkkbLH9K2NG0bG24nX3VD/M1+/dFNmadndhRX89lzcyXcxkkOWP6V/QnTJCivwX1DUY7CHc3Ln7qetfvRSTuXKPKfz2XNzJdzNJI2WP6V/QnX4CaNo4GJ7ge6of5mtPUNRjsIdzcufup60r9EUoXV2fvRRRRVGR+CNFFFfi5/UYUUUUAFFFFABRRRQAUUUUAFFFFAHUUUUV+0H8uBRRRQAUUUUAFFFFABRRRQAUUUUAFfuNX4c1+41ABX4MXd3HYw734HQKO9Mu7uOyh3ueOgUd65i8vJL2YvIfoOwFR8Rt/DC8vJL2Yu5+i9gK0NI0jzyJph+76qp/i/wDrV/QDX4K3d3HZQ73PHQKO9N6bCgk3dn71V/PdeXkl7MXc/RewFF5eSXsxeQ/QdgKv6TpPnETTD93/AAqf4v8A61MhJvRC6RpHnkTTD931VT/F/wDWr+gGiv57ry8kvZi8h+g7AUA2rH9CNFfz+6TpPnETTD93/Cp/i/8ArV/QFQJppXCv57ry8kvZi7n6L2Ar+hGv5/dJ0nziJph+7/hU/wAX/wBah6DSb0QukaR55E0w/d9VU/xf/Wr+gGiv57ry8kvZi8h+g7AUA2rBeXkl7MXc/RewFaGkaR55E0w/d9VU/wAX/wBav6Aa/BW7u47KHe546BR3pPTYuCTd2Pu7uOxh3vwOgUd6/eeivwB0jSOk8491Q/zNGwNubsj9/qK/BO/v0sYtzHLn7q561y9xcSXUpkkOWP6U07kyio9T+hSvwD0fR8bZ5191Q/zNN0jSOk8491Q/zNfv9RuC93Vo/BW/v47CLc3Ln7q+tcrc3Ml1KZJDlj+lf0KUUJWCUnI/APR9HxtnnX3VD/M1+/lfgnf36WMW5jlz91c9a5e4uJLqUySHLH9KS1KmkrJBc3Ml1KZJDlj+lbGj6PjbPOvuqH+Zr9/K/BO/v0sYtzHLn7q560Psggk7tn72V/PXc3Ml1KZJDlj+lf0KUVRkfgHo+j42zzr7qh/ma/fyiikU2mrIKK/AHSNI6Tzj3VD/ADNfv9RcGmldn4K39/HYRbm5c/dX1rlbm5kupTJIcsf0r+hSihKw5Scgor8E7+/Sxi3McufurnrX72UJ3CUeU/BGiiivxg/qAKKKKACiiigAooooAKKKKACiiigDqKKKK/aD+XAooooAKKKKACiiigAooooAKKKKACv3Gr8Oa/cagD+e27u5LyUu5+g7AVf0nSvOImmH7v8AhU/xV/QHX4J3V1HZw736dAo71L02NIpN3Z+9lFfz23d295KXc/QdhX9CVUZhRRX89t3dveSl3P0HYUAF3dyXkpdz9B2Aq/pOlecRNMP3f8Kn+Kv6A6KRSet2FFFFMk/n80nSvOImmH7v+FT/ABVs3V5HZQ73PHQKO9fvVRUtXNFKyskfz23d3JeSl3P0HYCr+k6V5xE0w/d/wqf4qTStK84iaYfu+yn+Kv6BKfkhbas/BW6vI7KHe546BR3rl7u7kvJS7n6DsBRd3b3kpdz9B2Ff0JUkrBKVz8AdJ0kcTzj3VD/M1+/1fghfXyWUW5uXP3V9a/e+hajmkrJBRX4AaTpXSaYe6of5mtC+vksotzcufur60XBQ0ux19fx2MW5uXP3V9a/e2iimlYmUuY/AHSdJHE8491Q/zNfv9X4IX18llFublz91fWv3vpLUqaSskFfgDpOkjiece6of5mv3+opshNLc/BK+v47GLc3Ln7q+tcxcXD3UpkkOWP6UXFw9zKZJDlj+lf0KUJWKlK5+AOk6SOJ5x7qh/ma/f6vwQvr5LKLc3Ln7q+tfvfSWo5pKyR/PXcXD3UpkkOWP6V/QpRX4IX18llFublz91fWm3YSV9Wz976/nruLh7qUySHLH9K/oUopkH4A6TpI4nnHuqH+Zr9/q/BC+vksotzcufur61zVxcPcymSQ5Y/pUrU0kktEf0KUV+AGk6V0mmHuqH+Zr9/6dyGrH4I0UUV+MH9RBRRRQAUUUUAFFFFABRRRQAUUUUAdRRRRX7Qfy4FFFFABRRRQAUUUUAFFFFABRRRQAV+41fhzX7jUAfgjdXSWcW9zx0CjvXN3V295KXc/QdhRdXT3cpdz9B2FXNM0zzSJZR8nZT3qUrGrbm7IXS9L84iWUfu+ynv8A/WrXurpLOLe546BR3ptzdpaRb36dAB3rnbq6e7lLufoOwpblNqCsj+hKiivwPubtLSLe/ToAO9U3YzjG466uks4t7njoFHeuburt7yUu5+g7Cv6Eq/n50zTPNIllHydlPelaw23N2P6Bq/BG6uks4t7njoFHev3uoptXFGXKfz23V295KXc/QdhV3S9L84iWUfu+ynv/APWpNM0zzSJZR8nZT3rWubtLSLe/ToAO9Jvoiox+0z98K/nturt7yUu5+g7Cv6EqKoyP5/8AS9L6TTD3VT/M1fvb5LKLcxyx+6vrSXt8tnHk4LH7q+tfvlUJX1Nm+TRH89c873MpkkOWP6VqaXpfSaYe6qf5mv6AKKpmadndn4HXt8llFuY5Y/dX1rnJ53uZTJIcsf0onne5lLucsf0r+hShKw5S5gor8Db2+WzjycFj91fWv3yoTuKUeU/nrnne5lMkhyx/Sv6FKKKZJ+B17fJZRbmOWP3V9a/fGv56553uZS7nLH9K09L0zGJph7qp/manY0bc3ZH9ANfgde3yWUW5jlj91fWkvb5bOPJwWP3V9a/fKjcfwaI/nrnne5lMkhyx/StTS9L6TTD3VT/M0ml6ZjE0w91U/wAzX9ANPfRE/Dqz8Dr2+Syi3Mcsfur61zk873MpkkOWP6UTzvcyl3OWP6V/QpQlYJS5gr8Dr2+Syi3Mcsfur60l7fLZx5OCx+6vrXOzzvcyl3OWP6Utyvg2Ced7mUySHLH9K1NL0vpNMPdVP8zX9AFFNkJ2d2fgde3yWUW5jlj91fWv3xr+eued7mUu5yx/Sv6FKErDlLmPwRooor8YP6gCiiigAooooAKKKKACiiigAooooA6iiiiv2g/lwKKKKACiiigAooooAKKKKACiiigAr9xq/Dmv3GoAKKKKAP57Lq6e6lLufoPSv6E6KKAPwOubqO0i3N+AHeudurp7qUu5+g9KLm5e6kLufoPSrmm6b5pEso+TsvrUpWNG3N2Qum6b5pEso+TsvrX9A1FFUQ2fz2XV091KXc/Qelf0J1/Pxpum+aRLKPk7L61qXNylpFub8AO9Te2hajfVn751/PZdXT3Updz9B6V/QnX8/mm6b0llHuqn+dN6EpN6I/oDor8Cry8S0jyeWPRfWv31oTuElYK/n90zTRxNMPdVP86TTdN6Syj3VT/Or15eJaR5PLHovrSb6IuMbas/fWv56p53uJC7nJNf0K0VRkFfgXeXqWkeTyx6L60l5eJaR5PLHovrXPzTPcSF3OSanc1+A/oVor+fzTdN6Syj3VT/ADr+gOnczasfgXeXqWkeTyx6L61z0873Ehdzkmv6Fa/n803Tekso91U/zpbF3c3YXTNNHE0w91U/zr+gKiimQ2fz1TzvcSF3OSa09M00cTTD3VT/ADpNN03pLKPdVP8AOr15eJaR5PLHovrSb6I0jHqz99a/nqnne4kLuck1/QrRVGQV+Bd5epaR5PLHovrSXl4lpHk8sei+tc/NM9xIXc5JqdzX4D+hWv5/dM00cTTD3VT/ADr+gKimzNOx+Bd5epaR5PLHovrX76V/PVNM9xIXc5Jr+hWhKxUpcwUV+BltbJaRbV/EnvX750J3E48p+CNFFFfjB/UIUUUUAFFFFABRRRQAUUUUAFFFFAHUUUUV+0H8uBRRRQAUUUUAFFFFABRRRQAUUUUAFfuNX4c1+41AH89lzcPcyFmP0HpVvTtO83Ekg+TsvrX9BFFIpPW7Cv57Lm4e5kLMfoPSv6E6KZIUUUUAfz2XNw9zIWY/Qelf0J0UUAFFfz2XFw9zIWc/Qelf0J0Afz96dp3SWUf7qmv6BKK/nqmmaeQu5yTSKbVj+hWv5+9O07pLKP8AdU1/QJX4DXV4trHknLHovrSZUEt2fvzRX89U0zTyF3OSa/oVqjMKKK/nqmmaeQu5yTQATTNPIXc5Jr+hWiigD8CLu7W0jyeWPRfWv33or+fnT9P6Syj3VTU7Gjbmz+gaiiiqMz+eqaZp5C7nJNf0K0UUAfgRd3a2keTyx6L61gzTNPIXc5JommaeQu5yTV/T9P6Syj3VTU7Gjbm7Idp2ndJZR/uqau3d2tpHk8sei+tNurxbWPJOWPRfWv35pLXVlN8miP56ppmnkLuck1o6dp3SWUf7qmv6BKKpmaet2fgRd3a2keTyx6L61++9fz1TTNPIXc5Jpbe3e5kCqPqfShKw5PmYtvbvcyBVH1PpW7b26Wse1fxJ71++1fz7ahqBlzHGfk7n1pNXHFpan9BNFFFUZn4I0UUV+Ln9RhRRRQAUUUUAFFFFABRRRQAUUUUAdRRRRX7Qfy4FFFFABRRRQAUUUUAFFFFABRRRQAV+41fhzX7jUAfgNPcpbR7m/ADvWJcXD3MhZj9B6UTztcSFmP0HpX9ClSlYuUrn8+thY+YRJIPk7D1rRnuUto9zfgB3r9+aKGrjUrLRH89dxcPcyFmP0HpVqwsfMIkkHydh61/QVRTJT1uz8Bp7lLaPc34Ad6/fmv56552uJCzH6D0r+hShKw5Sufz8afY9JZR/uqa/oHr8A7m5W2TJ5Y9B61jSytO5ZzkmktRySWgTTNPIXc5Jq9p9j0llH+6posLDpJIPopq3c3K2yZPLHoPWk30Q4x6s/fyv56ppmnkLuck0SytO5Zzkmr1hYdJJB9FNU3YhK+iP6B6K/AO5uVtkyeWPQetY0srTuWc5JoTuOSsE0zTyF3OSavafY9JZR/uqa/oHooYk9bsK/nqmmaeQu5yTRLK07lnOSavWFh0kkH0U0N2BK+iP6B6/AW6u1to8nlj0HrTbm5W2TJ5Y9B61+/lLcv4Ar+fjT7HpLKP91TRYWHSSQfRTX9A9Pcn4dWFFFFMg/n40+x6Syj/dU1/QPX4B3NytsmTyx6D1r9/Klamkkloj+eqaZp5C7nJNf0K1/PxYWHSSQfRTX9A9Mlp7s/AW6u1to8nlj0HrX79UUUJWCUuY/nrgga4kCqPqfStu3hS2j2r+J9aSCBLaPav4k96/fqp+Iv4D+fa/1Dzcxxn5O59a/oJr+euCBriQKo+p9K2oIEto9q/iT3p3sJJz1P36or+fW+vvMzHGfl7n1r+gqmQ1Y/BGiiivxg/qIKKKKACiiigAooooAKKKKACiiigDqKKKK/aD+XAooooAKKKKACiiigAooooAKKKKACv3Gr8Oa/cagD+fSysvMxJIPl7D1r+guvwAmmWBNzfgPWv3/pIuSS0P5zKKKK/PT+wAr+jOv5zK/ozr6LKP+Xny/U/HfEL/AJhf+3//AGw/n3sbLpJIPotf0EV/P/cXC26ZPJPQV/QBX0CPyKSS0R/PTLK0zlmOSa/oWor+f+4uFt0yeSegoJSvqz+gCv56ZZWmcsxyTX9C1fz62Vn0kkH0WgEm9B1jZdJJB9Fr+giiv56ZJGlcsxyTQDasf0LUUV/P/cXC26ZPJPQUAlcdc3K2yZPLHoPWv3+oooSsEpcx/PvY2XSSQfRa/oIoooE2FFfz62Vn0kkH0Wv6CqYNWPwBublbZMnlj0HrWPLK0zlmOSa/oWopJDlLmCiiv56ZJGlcsxyTTJCWVpnLMck1/QtX8+tlZ9JJB9Fq1cXC26ZPJPQUrmnLpdjrm5W2TJ5Y9B61jyytM5Zjkmv6FqKEiZS5j+euCBp32r+J9K2IYVt49q/iT3pkMKwJtX8T61+/9Lcv4D+fS9vfMzHGfl7n1qtBA077V/E+lJDC077V/E+lf0K0yG76s/AOGFbePav4k96oXt75mY4z8vc+tf0F0UJDcrqyCiiimQfgjRRRX4uf1GFFFFABRRRQAUUUUAFFFFABRRRQB1FFFFftB/LgUUUUAFFFFABRRRQAUUUUAFFFFABX7jV+HNfuNQB/PVNM077m/Aelf0K1/PjaWu/Dv93sPWv6DqRTT3Z/OZRX9GdFfP8A9kf9PPw/4J+v/wDEQv8AqF/8n/8AtD+cyv6M6KK9DCYT6rze9e9uh8fxDxD/AG97L91ycnN9q9728l2P56ZJGlcsxyTX9C1fz6Wlp0d/wBr+guvQPkGnuwooopkhRX8/k9wsC5PJ7CsySRpXLMck0k7lSVgkkaVyzHJNf0LUV/P5PcLAuTyewo2GlfVjp7lYEyeSegr+gGiv59LS06O/4A0bDbc2f0F1/P8AT3KwJk8k9BTZ7hYFyeT2Ff0B0tw+DRH89MkjSuWY5Jq3Z2mMSSD6LX9BdFMlPW7Civ56ZJGlcsxyTVu0tOjv+ANGwJXegWdpjEkg+i1anuVgTJ5J6Cmz3CwLk8nsKzJJGlcsxyTS3NG1BWQSSNK5Zjkmv6FqKKoxP5/p7lYEyeSegr+gGiv56oommfav4n0pJWLbcmf0K0UUUyD+fK8vPMyicL3PrVeGFpn2r+J9K/oVopDbu7sKK/nxu7vzMoh+XufWv6DqYNWCv5/4Y1gTao+p9aSKJYE2j8T61Su7vzMoh+XufWp3NUuTVn9B1FFFUYn4I0UUV+Ln9RhRRRQAUUUUAFFFFABRRRQAUUUUAdRRRRX7Qfy4FFFFABRRRQAUUUUAFFFFABRRRQAV+41fhzX7jUAfz+SyrCmT+ArNllaZtzfgPSv6FaKVi5Sufz52tr0dx9BU886wrk8nsK/oFoosNSsrI/npkkaRizHJq1a2vR3H0Ff0GUUyU7O7P5+p51hXJ5PYV/QLRRSCUuYK/n6nnWFcnk9hX9AtFAKVj+emSRpGLMcmrVra9HcfQV/QZRTBOzuz+fqedYVyeT2Ff0C0UUglLmP587W16O4+gqeedYVyeT2Ff0C0UWKUrKyCv587W16O4+gr+gyimQnYKKKKBBX8/U86wrk8nsK/oFopFKVgooopkn8/U86wrk8nsK/oFoopFSlzBRRRTJCiiigD+fyKJYUwPxNU7q635RD8vc+tf0H0UrFuV1ZH89UUTTNtX8T6V/QrRRTIP58Lq635RD8vc+tQxRNM21fxPpX9CtFA27u7P5/IolhTA/E1/QHRRSG3c/BGiiivxg/qEKKKKACiiigAooooAKKKKACiiigDqKKKK/aD+XAooooAKKKKACiiigAooooAKCQASTgCmzTJbxPLK6xxoCzO5wFA6kmvnr4sfGN9dM2kaJIY9N5Wa5Xhp/UD0X+dIZo/Fj40GbzdG8PzYj5We+jb73+yh9P9r8q8ToooC4UUUUxBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUU+CCS5mSKJGklchVRRkk+gFG2rGk27Iaql2CqCWJwAOpr2T4bfCoWnlaprUWZ+GhtHHCf7Te/t2q98OPhdHoSx6lqiCTUT80cR5WH/Fv5V6PXw2aZxz3oYZ6dX39P8z9X4f4aVK2Lx0fe3Ue3m/Py6dddiiiivkD9LCiiigAooooAKKKKACiiigAooooA6iiiiv2g/lwKKKKACiiigAooooAKhvb2DTrWW5uZUgt4lLPI5wFFRarqtpolhNe30629tENzyOeB/wDXr5m+J3xUu/HF01rbFrbR42+SHoZSP4n/AKDtQMvfFT4uz+LpZNN0xmg0dThj0a4PqfRfb868zoooEFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUVb0nSLvXL+OzsoWmnkOAo7e59BUykopyk7JFwhKpJQgrtkdjYz6ldxW1rE008h2oiDJJr3r4efDWDwrCl5eBZ9VYct1WL2X396ueA/h9aeDrQSMFn1J1/eT4+7/sr6D+ddbXwGaZu8RejQdodX3/4B+xZBw5HBJYnFq9Toukf+D+QUUUV8wffBRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAHUUUUV+0H8uBRRRQAUUUUAFZ2v6/Y+GdMlv8AUJxBbxjqerHsAO5NQeKvFen+DtKe/wBRl2RjhI15eRv7qjua+WvHXj3UPHepm4umMVshPkWqtlYx/U+poAufEX4k33jy/O4tb6ZG37i1B/8AHm9W/lXHUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUVteFfCd94u1EW1mmEXBlmYfLGPU/wCFZ1KkaUXObskbUaNSvUVKlG8nskV/D/h698TailnYxeZI3LMfuoPUnsK+hvBngmy8HWIjhAlu3A865I+Zj6D0HtVnwt4UsfCWnC1s0+Y4MkzD5pD6n/CtmvzvM81ljH7OnpD8/X/I/a8i4fp5ZFVq3vVX90fJfqwooor58+yCiiigAooooAKKKKACiiigAooooAKKKKACiiigDqKKKK/aD+XAooooAK57xr4407wNpRu7198rZENsp+eVvQe3qe1VPiD8RLDwHpxeYie/kU+Rag8sfU+i+9fLviTxLf8AivVJL/UZjLO/AH8KL2VR2FAFjxf4x1HxpqrXuoSZxkRwr9yJfRRWHRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRXXeAvh7deMLoSyBrfTEb95Pjlv9lff37VhWrU8PB1KjskdWFwtbGVVRoRvJ/19xU8F+CL3xlfBIgYrNCPOuSOF9h6n2r6G0HQLLw3pyWVjEI4l5JP3nPqT3NTaVpVrotjFZ2cKwQRjAVf5n1NW6/N8xzKpjpWWkFsv1Z+5ZLkdHKafM/eqPd/ovL8wooorxj6cKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigDqKKKK/aD+XArh/iV8T7LwJZtFGVudWkXMVvnhf9p/Qe3eqXxR+LNt4Mt3sbFkuNZccL1WEH+Jvf0FfNWoajc6rezXd3M9xcytueRzkk0AS6zrV54g1Ga+v52uLmU5Z2/kPQe1UqKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK9I+G/wufW2j1LVUMenj5o4Tw03v7L/OuXE4mnhKbqVXp+Z6GBwNfMayoUFd/gl3ZS+Hfw0n8USpe3qtBpanOejTey+3vXvNlZQadax21tEsMEY2oiDAAp8MMdvEkUSLHGgCqijAA9AKfX5pjsfUx0+aWkVsv66n7rlOT0MppcsNZPeXV/5LyCiiivMPeCiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAOoryz4r/GCLwykulaQ6y6sflklHK2/wDi3t2rP+LPxlXSxNo+gyhrzlJ7tTxF6qvq3v2/l4C7tI7O7F3Y5LMckn1NftB/Lg+5uZby4knnkaaaRizyOcsxPUk1HRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRSqpdgqgsxOAAMkmvZvht8KhY+Vqmsx7rnhobVhxH/tN7+3auDGYylgqfPUfourPXyzLK+aVvZUVp1fRL+tkZ/w3+FJuPL1TWosRcNDaOPvf7Tj09q9jACgADAHAAoor80xeMq42pz1H6Loj92y3LKGV0fZUV6vq35/5BRRRXCesFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH//2Q=="
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» qrCode|string|true|none||二维码图片的base64|

## POST 获取设备记录

POST /personal/getSafetyInfo

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "proxyIp": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "list": [
      {
        "uuid": "087b139951b776e0416b5015d0b98109",
        "deviceName": "iPhone 13 Pro",
        "deviceType": "iPhone iOS17.2",
        "lastTime": 1703218815
      },
      {
        "uuid": "f7e4bda161f7a6a7361ca62141cded23",
        "deviceName": "张传的MacBook Pro",
        "deviceType": "iMac MacBookPro17,1 OSX OSX 13.3.1 build(22E261)",
        "lastTime": 1703206819
      },
      {
        "uuid": "80d6218be93f570a971d8c605fa542c3",
        "deviceName": "iPad",
        "deviceType": "iPad iOS14.5.1",
        "lastTime": 1703065642
      },
      {
        "uuid": "197e97585d02c9cd6e6de68c74c81780",
        "deviceName": "iPad",
        "deviceType": "iPad iOS14.5.1",
        "lastTime": 1701300706
      },
      {
        "uuid": "bf5eb4d8498f4affac1cbfb8aa936d2a",
        "deviceName": "iPad",
        "deviceType": "iPad iPadOS14.3",
        "lastTime": 1696729849
      },
      {
        "uuid": "33ac7f39ed3d7115d9c15f07981a264a",
        "deviceName": "iPad",
        "deviceType": "iPad iPadOS14.5.1",
        "lastTime": 1695050733
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» list|[object]|true|none||设备记录|
|»»» uuid|string|true|none||设备ID|
|»»» deviceName|string|true|none||设备名称|
|»»» deviceType|string|true|none||设备类型|
|»»» lastTime|integer|true|none||最后操作时间|

## POST 隐私设置

POST /personal/privacySettings

**option 说明**
- 4: 加我为朋友时需要验证
- 7: 向我推荐通讯录朋友
- 8: 添加我的方式 手机号
- 25: 添加我的方式 微信号
- 38: 添加我的方式 群聊
- 39: 添加我的方式 我的二维码
- 40: 添加我的方式 名片

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "open": true,
  "option": 4
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» option|body|integer| 否 |隐私设置的选项|
|» open|body|boolean| 是 |开关|

#### 详细说明

**» option**: 隐私设置的选项
     4: 加我为朋友时需要验证
     7: 向我推荐通讯录朋友
     8: 添加我的方式 手机号
     25: 添加我的方式 微信号
     38: 添加我的方式 群聊
     39: 添加我的方式 我的二维码
     40: 添加我的方式 名片

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 修改个人信息

POST /personal/updateProfile

**注意** 修改个人信息需要单独设置每一项
比如修改昵称则参数仅传appId和nickName
修改地区则参数可传appId、country、province、city

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "city": "",
  "country": "",
  "nickName": "",
  "province": "",
  "sex": 1,
  "signature": "......"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» city|body|string| 否 |城市|
|» country|body|string| 是 |国家|
|» nickName|body|string| 是 |昵称|
|» province|body|string| 是 |省份|
|» sex|body|string| 是 |性别 1:男 2:女|
|» signature|body|string| 是 |签名|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 修改头像

POST /personal/updateHeadImg

**注意** 修改头像后需要将手机的微信进程关掉，然后重启查看最新头像

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "headImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/REoLX7KfdibFAgDbtoeXGNjE6sGa8NCib8UaiazlekKjuLneCvicM4xQpuEbZWjjQooSicsKEbKdhqCOCpTHWtnBqdJicJ0I3CgZumwJ6SxR3ibuNs/0"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» headImgUrl|body|string| 否 |头像的图片地址|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

# 基础API/收藏夹模块

## POST 同步收藏夹

POST /favor/sync

#### 注意:
响应结果中会包含已删除的的收藏夹记录，通过flag=1来判断已删除

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "syncKey": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» syncKey|body|string| 否 |翻页key，首次传空，获取下一页传接口返回的syncKey|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "syncKey": "CAESCAgBEJyi9e4C",
    "list": [
      {
        "favId": 2,
        "type": 1,
        "flag": 1,
        "updateTime": 1448465918
      },
      {
        "favId": 1,
        "type": 2,
        "flag": 1,
        "updateTime": 1448465922
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» syncKey|string|true|none||翻页key|
|»» list|[object]|true|none||none|
|»»» favId|integer|true|none||收藏夹ID|
|»»» type|integer|true|none||收藏内容类型|
|»»» flag|integer|true|none||收藏夹标识|
|»»» updateTime|integer|true|none||收藏时间|

## POST 获取收藏夹内容

POST /favor/getContent

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "favId": 179
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» favId|body|integer| 是 |收藏夹ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "favId": 179,
    "status": 0,
    "flag": 0,
    "updateTime": 1703235210,
    "content": "<favitem type=\"1\"><desc>没说呢</desc><source sourceid=\"1838546569535807562\" sourcetype=\"21\"><createtime>1703217521</createtime><tousr>wxid_cy6buf12nf6921</tousr><fromusr>zhangchuan2288</fromusr><msgid>1838546569535807562</msgid></source><ctrlflag>127</ctrlflag><taglist></taglist><tagidlist></tagidlist></favitem>"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|object|true|none||none|
|»» favId|integer|true|none||收藏夹ID|
|»» status|integer|true|none||状态|
|»» flag|integer|true|none||收藏夹标识|
|»» updateTime|integer|true|none||更新时间|
|»» content|string|true|none||收藏的内容|

## POST 删除收藏夹

POST /favor/delete

> Body 请求参数

```json
{
  "appId": "{{appid}}",
  "favId": 179
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|
|» favId|body|integer| 是 |收藏夹ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

# 基础API/账号管理

## POST 断线重连

POST /login/reconnection

- 当系统返回账号已离线，但是手机顶部还显示ipad在线，可用此接口尝试重连，若返回错误/失败则必须重新调用[步骤一登录](https://apifox.com/apidoc/shared-69ba62ca-cb7d-437e-85e4-6f3d3df271b1/api-196794502)
- 本接口非常用接口，可忽略

> Body 请求参数

```json
{
  "appId": "{{appid}}"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": {
    "uuid": "4YHmGvoXvgmS1MqWVtQ2",
    "headImgUrl": "http://wx.qlogo.cn/mmhead/ver_1/ZYUmcl1UNzyB2onM08Ij901TaUOLIjHj2UicK3XGDsjEWl4XgQN5IjodunHicBVsZiaZc1iaGCRfluAxkzyibbiau3WBfFj2nprzKp2KryicMjGIvDbWOQGmibwVK648a3o4A8hD/0",
    "nickName": "G",
    "expiredTime": 230,
    "status": 2,
    "loginInfo": {
      "uin": 4077276085,
      "wxid": "wxid_0xsqb3o0tsvz22",
      "nickName": "G",
      "mobile": "17114312382",
      "alias": null
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 退出

POST /login/logout

> Body 请求参数

```json
{
  "appId": ""
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|

## POST 检查是否在线

POST /login/checkOnline

响应结果的data=true则是在线，反之为离线

> Body 请求参数

```json
{
  "appId": "{{appid}}"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|X-GEWE-TOKEN|header|string| 是 |none|
|body|body|object| 否 |none|
|» appId|body|string| 是 |设备ID|

> 返回示例

```json
{
  "ret": 200,
  "msg": "操作成功",
  "data": true
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» ret|integer|true|none||none|
|» msg|string|true|none||none|
|» data|boolean|true|none||none|

# 数据模型

