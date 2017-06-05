# API

## Общая информация

Общение сервера и приложения происходит зашифрованными json сообщениями:

# Шифрование

RC4 with SHA256 >> BASE64 utf8

**Только такие кавычки в**  **json** **строке считаются валидными! (как в примере далее)**

Методы decode и encodeapi только для теста, валидация json строки не производится, данные кодируются как есть. Другие методы api проверяют правильность json строки.

**Тест**** кодирования**

{%22name%22:%22test%22,%22pass%22:%22test%22}

```javascript
/encode?data={"name":"test","pass":"test"}
```

**Ответ**** :**

```javascript
TCLCgsK7CsOpw4kMHcOuwpEiwo7Cq8KewoHDhFQmBGPCg8KzOsK2fcOjwooE
```

**Тест**** декодирования**

```javascript
/decode?data=TCLCgsK7CsOpw4kMHcOuwpEiwo7Cq8KewoHDhFQmBGPCg8KzOsK2fcOjwooE
```

**Ответ**** :**

```javascript
{"name":"test","pass":"test"}
```

## Авторизация

```javascript
/userAuth?data=<шиврованный json>
```

```javascript
{
	"name": <string>,
	"pass": <string>
}
```

**Ответ**** :**

```javascript
{
	"sid": <string uuid4>
}
```

**Пример**** :**

_Запрос__:_

```javascript
/userAuth?data=TCLCgsK7CsOpw4kMHcOuwpEiwo7Cq8KewoHDhFQmBGPCg8KzOsK2fcOjwooE
```

Ответ:

```javascript
TCLCn8KzA8Kuw5EWHcKswpBmwpnCusOQwpXDlxhjRCTCjcK8esOiOcKgwoVAC8KTNwjCn2QXHktSZsK8ScOuwrPDt8Kvw4s=
```

## Данные пользователя

```javascript
/userData?data=<шиврованный json>
```

```javascript
{
	"sid": string,
}

```
Ответ** :**

```javascript
{
"user": <string>,
"robot": [
	{
		"battle_count": <int>,
		"recid": <int>,
		"attribs": <long string>,
		"sell_flag": <0 or 1>,
		"user_recid": <int>,
		"robot_status_recid": <int>,
		"name": <string>,
		"rank": <float>
		"win_count": <int>,
		"model": <long string>,
	}]
}
```

**Пример**** :**

_Запрос__:_

```javascript
/userData?data=TCLCn8KzA8Kuw5EWHcKpw41kw4LCvsOWwpHDkRhlQ3DDm8K8esKxNsKhwoVBCMOCbwjCmmURQB4APcK6ScOiwrzDsMKvw4s%3D
```

Ответ:

```javascript
TCLCmcKpAsO%2Bw4kMH8K4wpowwpfDrMKQwo%2FClBcnGCPDlsOlbMOpLsOMw5NbWMOFelHClTV8GxVEa8O7WsOgwqXDscKhwpZua0tqwqrDrn7CmGw8f09rFQzDocOSw4d4w4VyXQkGfsKZEEPDs8KCw6A0FwlTXh9ZL8OdwrLCnMKSaXA4w4TCk8KGFHfDscOQSWLDqWbDsDLCmsO1Mikrwq1ywrzCvsK5wpYFwoguwq1GZlh3CMKjSzA%2Fw74LaV5FwoLDpF3DrMOBdcKPw5g4wpsxcsOKwrwWZsOQwpnChzYRwpFhBRJMwpjDlRXDrjgTw6fColdhHmPDvl3DlRrClcOOKkcGVARPwoTDkxTCgMOrBG9GwqUpwqrCncKAw7PDsg%3D%3D
```





## Коды ошибок

При возникновении любой ошибки будет возвращен ответ с соответствующим кодом

{&quot;err&quot;:&lt;error code&gt;}

| Код | Расшифровка |
| --- | --- |
| -1 | Неизвестная ошибка ) |
| 0 | Данные не расшифрованы (сообщение не соответствует требованиям шифрования) |
| 1 | Ошибка авторизации (пользователь с полученным логином или паролем не существует) |
| 2 | Ошибка аутентификации (нет авторизованного пользователя с полученным sid) |
| 3 | Переданы не все параметры, либо параметры не соответствуют методу |
| 4 | Данные не зашифрованы (баг на сервере 99%) |
