# Scrapy 使い方

# インストール
pip install scrapy
scrapy startproject postscrape
cd postscrape
create posts_spider.py file in spiders folder
scrapy crawl posts



# Scrapy shellを遊んで見る
scrapy shell https://blog.scrapinghub.com/

-----------------------------------------
response.css('title')
#[<Selector xpath='descendant-or-self::title' data='<title>THE SCRAPINGHUB BLOG</title>'>]

response.css('title').get()
#'<title>THE SCRAPINGHUB BLOG</title>'

response.css('title::text').get()
#'THE SCRAPINGHUB BLOG'

response.css('h3::text').get()
#'Keep up to date with web scraping  and data tips...'

response.css('h3::text')[1].get()
#'Keep up to date with web scraping  and data tips...'

response.css('h3::text')[2].get()
#'\n  Crawl web data at scale without Bottlenecks or slowdowns.\n'

response.css('h3::text').getall()
#['Keep up to date with web scraping  and data tips...', '\n  Crawl web data at scale without Bottlenecks or slowdowns.\n', 'Follow Us', 'Popular Posts', 'Recent Posts', 'Categories', 'Archives']

response.css('h3').getall()
#['<h3 id="hs_cos_wrapper_module_1577809707375810_title" class="hs_cos_wrapper form-title" 
# data-hs-cos-general-type="widget_field" data-hs-cos-type="text">Keep up to date with web scraping  
# and data tips...</h3>', '<h3 style="text-align:center;">
# <a href="https://blog.scrapinghub.com/web-scraping-basics-tools" 
# rel=" noopener">Web Scraping Basics: A Developer's Guide to Reliably Extract Data</a></h3>', 
# '<h3>\n  Crawl web data at scale without Bottlenecks or slowdowns.\n</h3>', '<h3>Follow Us</h3>', 
# '<h3>Popular Posts</h3>', '<h3>Recent Posts</h3>', '<h3>Categories</h3>', '<h3>Archives</h3>']

response.css('.post-header').getall()
#['<div class="post-header">\n<h2>
# <a href="https://blog.scrapinghub.com/scrapy-cloud-secrets-hub-crawl-frontier-and-how-to-use-it">
# Scrapy Cloud Secrets: Hub Crawl Frontier and How To Use It</a></h2>\n<div class="byline">\n<span class="dat
# e">\n<i class="fa fa-calendar-o"></i>\n<a href="https://blog.scrapinghub.com/sc
# rapy-cloud-secrets-hub-crawl-frontier-and-how-to-use-it">August 06, 2020 </a>\n
# </span>\n<span class="author">\n<i class="fa fa-user"></i>\n<a href="https://bl
# og.scrapinghub.com/author/j%C3%BAlio-c%C3%A9sar-batista">Júlio César Batista</a
# >\t\n</span>\n<span class="custom_listing_comments">\n<i class="fa fa-comments-
# o"></i>\n<a href="https://blog.scrapinghub.com/scrapy-cloud-secrets-hub-crawl-f
# rontier-and-how-to-use-it#comments-listing">0 Comment</a>\n</span>\n</div>\n</d
# iv>', '<div class="post-header">\n<h2><a href="https://blog.scrapinghub.com/blo
# g-comments-api-beta-release">Blog Comments API (BETA):\xa0Extract Blog Comment
# DATA At Scale</a></h2>\n<div class="byline">\n<span class="date">\n<i class="fa
#  fa-calendar-o"></i>\n<a href="https://blog.scrapinghub.com/blog-comments-api-b
# eta-release">July 30, 2020 </a>\n</span>\n<span class="author">\n<i class="fa f
# a-user"></i>\n<a href="https://blog.scrapinghub.com/author/john-campbell">John
# Campbell</a>\t\n</span>\n<span class="custom_listing_comments">\n<i class="fa f
# a-comments-o"></i>\n<a href="https://blog.scrapinghub.com/blog-comments-api-bet
# a-release#comments-listing">0 Comment</a>\n</span>\n</div>\n</div>', '<div clas
# s="post-header">\n<h2><a href="https://blog.scrapinghub.com/price-intelligence-
# questions-answered">Your Price Intelligence Questions Answered</a></h2>\n<div c
# lass="byline">\n<span class="date">\n<i class="fa fa-calendar-o"></i>\n<a href=
# "https://blog.scrapinghub.com/price-intelligence-questions-answered">July 28, 2
# 020 </a>\n</span>\n<span class="author">\n<i class="fa fa-user"></i>\n<a href="
# https://blog.scrapinghub.com/author/himanshi-bhatt">Himanshi Bhatt</a>\t\n</spa
# n>\n<span class="custom_listing_comments">\n<i class="fa fa-comments-o"></i>\n<
# a href="https://blog.scrapinghub.com/price-intelligence-questions-answered#comm
# ents-listing">0 Comment</a>\n</span>\n</div>\n</div>', '<div class="post-header
# ">\n<h2><a href="https://blog.scrapinghub.com/data-center-proxies-vs.-residenti
# al-proxies">Data Center Proxies vs. Residential Proxies</a></h2>\n<div class="b
# yline">\n<span class="date">\n<i class="fa fa-calendar-o"></i>\n<a href="https:
# //blog.scrapinghub.com/data-center-proxies-vs.-residential-proxies">July 21, 20
# 20 </a>\n</span>\n<span class="author">\n<i class="fa fa-user"></i>\n<a href="h
# ttps://blog.scrapinghub.com/author/attila-t%C3%B3th">Attila Tóth</a>\t\n</span>
# \n<span class="custom_listing_comments">\n<i class="fa fa-comments-o"></i>\n<a
# href="https://blog.scrapinghub.com/data-center-proxies-vs.-residential-proxies#
# comments-listing">0 Comment</a>\n</span>\n</div>\n</div>', '<div class="post-he
# ader">\n<h2><a href="https://blog.scrapinghub.com/how-to-get-high-success-rates
# -with-proxies-3-steps-to-scale-up">How to Get High Success Rates With Proxies:
# 3 Steps to Scale Up</a></h2>\n<div class="byline">\n<span class="date">\n<i cla
# ss="fa fa-calendar-o"></i>\n<a href="https://blog.scrapinghub.com/how-to-get-hi
# gh-success-rates-with-proxies-3-steps-to-scale-up">July 14, 2020 </a>\n</span>\
# n<span class="author">\n<i class="fa fa-user"></i>\n<a href="https://blog.scrap
# inghub.com/author/attila-t%C3%B3th">Attila Tóth</a>\t\n</span>\n<span class="cu
# stom_listing_comments">\n<i class="fa fa-comments-o"></i>\n<a href="https://blo
# g.scrapinghub.com/how-to-get-high-success-rates-with-proxies-3-steps-to-scale-u
# p#comments-listing">0 Comment</a>\n</span>\n</div>\n</div>', '<div class="post-
# header">\n<h2><a href="https://blog.scrapinghub.com/job-postings-api-stable-rel
# ease">Job Postings API: Stable release</a></h2>\n<div class="byline">\n<span cl
# ass="date">\n<i class="fa fa-calendar-o"></i>\n<a href="https://blog.scrapinghu
# b.com/job-postings-api-stable-release">July 09, 2020 </a>\n</span>\n<span class
# ="author">\n<i class="fa fa-user"></i>\n<a href="https://blog.scrapinghub.com/a
# uthor/john-campbell">John Campbell</a>\t\n</span>\n<span class="custom_listing_
# comments">\n<i class="fa fa-comments-o"></i>\n<a href="https://blog.scrapinghub
# .com/job-postings-api-stable-release#comments-listing">0 Comment</a>\n</span>\n
# </div>\n</div>', '<div class="post-header">\n<h2><a href="https://blog.scraping
# hub.com/web-scraping-basics-tools">Web Scraping Basics: A Developer's Guide To
#  Reliably Extract Data</a></h2>\n<div class="byline">\n<span class="date">\n<i
# class="fa fa-calendar-o"></i>\n<a href="https://blog.scrapinghub.com/web-scrapi
# ng-basics-tools">July 07, 2020 </a>\n</span>\n<span class="author">\n<i class="
# fa fa-user"></i>\n<a href="https://blog.scrapinghub.com/author/chira-mircea">Ch
# ira Mircea</a>\t\n</span>\n<span class="custom_listing_comments">\n<i class="fa
#  fa-comments-o"></i>\n<a href="https://blog.scrapinghub.com/web-scraping-basics
# -tools#comments-listing">0 Comment</a>\n</span>\n</div>\n</div>', '<div class="
# post-header">\n<h2><a href="https://blog.scrapinghub.com/news-api-blog-importan
# ce-of-article-quality">Extracting Article &amp; News Data: The Importance of Da
# ta Quality</a></h2>\n<div class="byline">\n<span class="date">\n<i class="fa fa
# -calendar-o"></i>\n<a href="https://blog.scrapinghub.com/news-api-blog-importan
# ce-of-article-quality">June 23, 2020 </a>\n</span>\n<span class="author">\n<i c
# lass="fa fa-user"></i>\n<a href="https://blog.scrapinghub.com/author/attila-t%C
# 3%B3th">Attila Tóth</a>\t\n</span>\n<span class="custom_listing_comments">\n<i
# class="fa fa-comments-o"></i>\n<a href="https://blog.scrapinghub.com/news-api-b
# log-importance-of-article-quality#comments-listing">0 Comment</a>\n</span>\n</d
# iv>\n</div>', '<div class="post-header">\n<h2><a href="https://blog.scrapinghub
# .com/price-gouging-or-economics-at-work-price-intelligence-to-track-consumer-se
# ntiment">Price Gouging or Economics at Work: Price Intelligence to Track Consum
# er Sentiment</a></h2>\n<div class="byline">\n<span class="date">\n<i class="fa
# fa-calendar-o"></i>\n<a href="https://blog.scrapinghub.com/price-gouging-or-eco
# nomics-at-work-price-intelligence-to-track-consumer-sentiment">June 11, 2020 </
# a>\n</span>\n<span class="author">\n<i class="fa fa-user"></i>\n<a href="https:
# //blog.scrapinghub.com/author/robert-cosgrave">Robert Cosgrave</a>\t\n</span>\n
# <span class="custom_listing_comments">\n<i class="fa fa-comments-o"></i>\n<a hr
# ef="https://blog.scrapinghub.com/price-gouging-or-economics-at-work-price-intel
# ligence-to-track-consumer-sentiment#comments-listing">0 Comment</a>\n</span>\n<
# /div>\n</div>', '<div class="post-header">\n<h2><a href="https://blog.scrapingh
# ub.com/web-data-qa-part-iii-combining-manual-and-automated-techniques-for-holis
# tic-data-validation">A Practical Guide to Web Data QA Part III: Holistic Data V
# alidation Techniques</a></h2>\n<div class="byline">\n<span class="date">\n<i cl
# ass="fa fa-calendar-o"></i>\n<a href="https://blog.scrapinghub.com/web-data-qa-
# part-iii-combining-manual-and-automated-techniques-for-holistic-data-validation
# ">June 09, 2020 </a>\n</span>\n<span class="author">\n<i class="fa fa-user"></i
# >\n<a href="https://blog.scrapinghub.com/author/ivan-ivanov-and-warley-ferreira
# -lopes">Ivan Ivanov and Warley Ferreira Lopes</a>\t\n</span>\n<span class="cust
# om_listing_comments">\n<i class="fa fa-comments-o"></i>\n<a href="https://blog.
# scrapinghub.com/web-data-qa-part-iii-combining-manual-and-automated-techniques-
# for-holistic-data-validation#comments-listing">0 Comment</a>\n</span>\n</div>\n
# </div>']

response.css('.post-header a').get()
#'<a href="https://blog.scrapinghub.com/scrapy-cloud-secrets-hub-crawl-frontier-
# and-how-to-use-it">Scrapy Cloud Secrets: Hub Crawl Frontier and How To Use It</
# a>'

response.css('.post-header a::text').get()
#'Scrapy Cloud Secrets: Hub Crawl Frontier and How To Use It'

response.css('.post-header a::text')[1].get()
#'August 06, 2020 '


[Scrapy 正規表現の使い方]
response.css('p::text')
#[<Selector xpath='descendant-or-self::p/text()' data='Imagine a long crawling p
# rocess, like...'>, <Selector xpath='descendant-or-self::p/text()' data='We are
# excited to announce our newest...'>, <Selector xpath='descendant-or-self::p/tex
# t()' data=' is now publicly available as a BETA ...'>, <Selector xpath='descend
# ant-or-self::p/text()' data='Price Intelligence is leveraging web ...'>, <Selec
# tor xpath='descendant-or-self::p/text()' data='We are excited to announce our n
# ewest...'>, <Selector xpath='descendant-or-self::p/text()' data=' is now out of
#  BETA and publicly avai...'>, <Selector xpath='descendant-or-self::p/text()' da
# ta='The web is complex and constantly cha...'>, <Selector xpath='descendant-or-
# self::p/text()' data='Article and news data extraction is b...'>, <Selector xpa
# th='descendant-or-self::p/text()' data='As the COVID-19 pandemic took hold, w..
# .'>, <Selector xpath='descendant-or-self::p/text()' data='© 2020'>]

response.css('p::text').re(r's\w+')
#['ss', 'site', 'start', 'sults', 'something', 'site', 'some', 'sort', 'server',
#  'some', 'st', 'se', 'siness', 'sions', 'sically', 'se', 'strategy', 'sing', 's
# iness', 'st', 'stable', 'se', 'stantly', 'sons', 'specially', 'ssary', 'stand',
#  'site', 'spection', 'show', 'some', 'singly', 'sed', 'sure', 'se', 'succeed',
# 'siness', 'sk', 'specially', 'stant', 'something', 'seful']

response.css('p::text').re(r'\w+ you \w+')
#['before you try', 'show you some']

response.css('p::text').re(r'(\w+) you (\w+)')
#['before', 'try', 'show', 'some']

[Scrapy：css selectorの使い方]

post = response.css('div.post-item')[0]
post
#<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normal
# ize-space(@class), ' '), ' post-item ')]" data='<div class="post-item">\n<div c
# lass="h...'>

title = post.css('.post-header h2 a::text')[0].get()
title
#'Scrapy Cloud Secrets: Hub Crawl Frontier and How To Use It'

date = post.css('.post-header a::text')[1].get()
date

author = post.css('.post-header a::text')[2].get()
author


[Scrapy:Loopの使い方]
for post in response.css('div.post-item'):
   title = post.css('.post-header h2 a::text')[0].get()
   date = post.css('.post-header a::text')[1].get()
   author = post.css('.post-header a::text')[2].get()
   print(dict(title=title,date=date,author=author))
   
#{'title': 'Scrapy Cloud Secrets: Hub Crawl Frontier and How To Use It', 'date':
# 'August 06, 2020 ', 'author': 'Júlio César Batista'}
# {'title': 'Blog Comments API (BETA):\xa0Extract Blog Comment DATA At Scale', 'da
# te': 'July 30, 2020 ', 'author': 'John Campbell'}
# {'title': 'Your Price Intelligence Questions Answered', 'date': 'July 28, 2020 '
# , 'author': 'Himanshi Bhatt'}
# {'title': 'Data Center Proxies vs. Residential Proxies', 'date': 'July 21, 2020
# ', 'author': 'Attila Tóth'}
# {'title': 'How to Get High Success Rates With Proxies: 3 Steps to Scale Up', 'da
# te': 'July 14, 2020 ', 'author': 'Attila Tóth'}
# {'title': 'Job Postings API: Stable release', 'date': 'July 09, 2020 ', 'author'
# : 'John Campbell'}
# {'title': 'Web Scraping Basics: A Developer's Guide To Reliably Extract Data',
# 'date': 'July 07, 2020 ', 'author': 'Chira Mircea'}
# {'title': 'Extracting Article & News Data: The Importance of Data Quality', 'dat
# e': 'June 23, 2020 ', 'author': 'Attila Tóth'}
# {'title': 'Price Gouging or Economics at Work: Price Intelligence to Track Consu
# mer Sentiment', 'date': 'June 11, 2020 ', 'author': 'Robert Cosgrave'}
# {'title': 'A Practical Guide to Web Data QA Part III: Holistic Data Validation T
# echniques', 'date': 'June 09, 2020 ', 'author': 'Ivan Ivanov and Warley Ferreira
#  Lopes'}

[Scrapy Json出力コマンド]
scrapy crawl posts -o posts.json
scrapy crawl posts -o postsnext.json