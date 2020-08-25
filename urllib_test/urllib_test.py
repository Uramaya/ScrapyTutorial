from urllib import request

class getHTML():
    def __init__(self):
        self.url = 'https://www.gnavi.co.jp/'

    def get_html(self):
        url = self.url
        headers = {'User-Agent':'Mozilla/5.0'}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

if __name__ == '__main__':
    html = getHTML()
    result = html.get_html()
    print(result)