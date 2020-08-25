# URLに複数のParamを入れる場合

from urllib import request
from urllib import parse

params = {
	'wd' : '美女',
	'pn' : '50'
}
params = parse.urlencode(query_string_dict)
url = 'http://www.baidu.com/s?{}'.format(params)
print(url)


# ParamとURLを結合する方法
# 1
  baseurl = 'http://www.baidu.com/s?'
  params = 'wd=%E7XXXX&pn=20'
  url = baseurl + params
# 2
  params = 'wd=%E7XXXX&pn=20'
  url = 'http://www.baidu.com/s?%s'% params
# 3
  url = 'http://www.baidu.com/s?{}'
  params = 'wd=#E7XXXX&pn=20'
  url = url.format(params)


  # Paramのみエンコードする場合
  string = '美女'
  print(parse.quote(string))
  # 结果: %E7%BE%8E%E5%A5%B3