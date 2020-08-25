import requests

url = 'http://code.tarena.com.cn/AIDCode/aid1905/13_redis/'
headers = {'User-Agent':'Mozilla/5.0'}

response = requests.get(url=url,headers=headers).text

print(response)

print(response.url)
# https://example.com/

print(response.status_code)
# 200

print(response.headers)
# {'Content-Encoding': 'gzip', 'Accept-Ranges': 'bytes', 'Cache-Control': 'max-age=604800', 'Content-Type': 'text/html', 'Date': 'Thu, 12 Jul 2018 11:58:54 GMT', 'Etag': '"1541025663"', 'Expires': 'Thu, 19 Jul 2018 11:58:54 GMT', 'Last-Modified': 'Fri, 09 Aug 2013 23:54:35 GMT', 'Server': 'ECS (oxr/8313)', 'Vary': 'Accept-Encoding', 'X-Cache': 'HIT', 'Content-Length': '606'}

print(type(response.headers))
# <class 'requests.structures.CaseInsensitiveDict'>

print(response.headers['Content-Type'])
# text/html

print(response.encoding)
# ISO-8859-1

print(response.content)
# b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 50px;\n        background-color: #fff;\n        border-radius: 1em;\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        body {\n            background-color: #fff;\n        }\n        div {\n            width: auto;\n            margin: 0 auto;\n            border-radius: 0;\n            padding: 1em;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is established to be used for illustrative examples in documents. You may use this\n    domain in examples without prior coordination or asking for permission.</p>\n    <p><a href="http://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'

print(type(response.content))
# <class 'bytes'>