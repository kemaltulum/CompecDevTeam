from urllib import request
import re

res = request.urlopen('http://www.hurriyetemlak.com/konut-satilik/istanbul-sariyer-rumeli-hisari/listeleme')
res = res.read().decode("UTF-8")
result = re.findall(r"<strong class=\"ellipsis\">([a-zA-Z0-9]+) *<i>", res)
print(result)