# API

## Общая информация

Общение сервера и приложения происходит зашифрованными json сообщениями:

# RC4

BASE64 utf-8

Key:

SHA256

**Только такие кавычки в**  **json** **строке считаются валидными! (как в примере далее)**

Методы decode и encodeapi только для теста, валидация json строки не производится, данные кодируются как есть. Другие методы api проверяют правильность json строки.

**Тест**** кодирования**

{%22name%22:%22test%22,%22pass%22:%22test%22}

/encode?data={&quot;name&quot;:&quot;test&quot;,&quot;pass&quot;:&quot;test&quot;}

**Ответ**** :**

TCLCgsK7CsOpw4kMHcOuwpEiwo7Cq8KewoHDhFQmBGPCg8KzOsK2fcOjwooE

**Тест**** декодирования**

/decode?data=TCLCgsK7CsOpw4kMHcOuwpEiwo7Cq8KewoHDhFQmBGPCg8KzOsK2fcOjwooE

**Ответ**** :**

{&quot;name&quot;:&quot;test&quot;,&quot;pass&quot;:&quot;test&quot;}

## Авторизация

/userAuth?data=&lt;шиврованный json&gt;

{

&quot;name&quot;: &lt;string&gt;,

&quot;pass&quot;: &lt;string&gt;

}

**Ответ**** :**

{

&quot;sid&quot;: &lt;string uuid4&gt;

}

**Пример**** :**

_Запрос__:_

/userAuth?data=TCLCgsK7CsOpw4kMHcOuwpEiwo7Cq8KewoHDhFQmBGPCg8KzOsK2fcOjwooE

Ответ:

TCLCn8KzA8Kuw5EWHcKswpBmwpnCusOQwpXDlxhjRCTCjcK8esOiOcKgwoVAC8KTNwjCn2QXHktSZsK8ScOuwrPDt8Kvw4s=

## Данные пользователя

/userData?data=&lt;шиврованный json&gt;

{

&quot;sid&quot;: string,

}

**Ответ**** :**

{

&quot;user&quot;: &lt;string&gt;,

 &quot;robot&quot;: [

{

&quot;battle\_count&quot;: &lt;int&gt;,

 &quot;recid&quot;: &lt;int&gt;,

 &quot;attribs&quot;: &lt;long string&gt;,

&quot;sell\_flag&quot;: &lt;0 or 1&gt;,

 &quot;user\_recid&quot;: &lt;int&gt;,

&quot;robot\_status\_recid&quot;: &lt;int&gt;,

&quot;name&quot;: &lt;string&gt;,

&quot;rank&quot;: &lt;float&gt;

&quot;win\_count&quot;: &lt;int&gt;,

&quot;model&quot;: &lt;long string&gt;,

}

]

}

**Пример**** :**

_Запрос__:_

/userData?data=TCLCn8KzA8Kuw5EWHcKpw41kw4LCvsOWwpHDkRhlQ3DDm8K8esKxNsKhwoVBCMOCbwjCmmURQB4APcK6ScOiwrzDsMKvw4s%3D

Ответ:

TCLCmcKpAsO%2Bw4kMH8K4wpowwpfDrMKQwo%2FClBcnGCPDlsOlbMOpLsOMw5NbWMOFelHClTV8GxVEa8O7WsOgwqXDscKhwpZua0tqwqrDrn7CmGw8f09rFQzDocOSw4d4w4VyXQkGfsKZEEPDs8KCw6A0FwlTXh9ZL8OdwrLCnMKSaXA4w4TCk8KGFHfDscOQSWLDqWbDsDLCmsO1Mikrwq1ywrzCvsK5wpYFwoguwq1GZlh3CMKjSzA%2Fw74LaV5FwoLDpF3DrMOBdcKPw5g4wpsxcsOKwrwWZsOQwpnChzYRwpFhBRJMwpjDlRXDrjgTw6fColdhHmPDvl3DlRrClcOOKkcGVARPwoTDkxTCgMOrBG9GwqUpwqrCncKAw7PDsg%3D%3D





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
