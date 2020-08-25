s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))
# 结果: ['A B','C D']
p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))
# 结果: ['A','C']
p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))
# 结果: [('A','B'),('C','D')]
```