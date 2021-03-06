from bs4 import BeautifulSoup

# こちらで用意したHTML

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# BeautifulSoupの初期化

soup = BeautifulSoup(html_doc, 'html.parser')  # BeautifulSoupの初期化

print(soup.prettify())  # HTMLをインデントすることができます。

soup.title
#<title>The Dormouse's story</title>が抽出される

soup.title.string
# The Dormouse's storyが出力される

soup.find_all("a")
#[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>] が出力される


soup.find("p", attrs={"class", "title"})
# The Dormouse's storyが出力される


# BeautifulSoupでHTMLを見やすくする (soup.prettify())
print(soup.prettify())
