import requests as r
import re

goodUA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"

def getItemList(res : str) -> list:
  return re.findall(r"<a title=\"(.+)\" class=\"overlay-link\" href=\"(.+)\"></a>", res)

def getItemProps(res : str) -> dict:
  props_list = {
    'price':r"<li class=\"price-line clearfix\">\s*<span>(.+)<\/span>\s*<\/li>",
    'coordinates':r"<input id=\"hdnRealtyCoordinates\" name=\"hdnRealtyCoordinates\" type=\"hidden\" value=\"(.+?)\" \/>",
    'numroom':r"<span><span>Oda \+ Salon<\/span>(.+?)<\/span>",
    'm2':r"<span><span>Metrekare<\/span>(.+?)<\/span>",
    'age':r"<span><span>Bina Ya..<\/span>(.+?)<\/span>",
    'heating':r"<span><span>Is.nma Tipi<\/span>(.+?)<\/span>",
    'floor':r"<span>Bulundu.u Kat<\/span><span>(.+?)<\/span>",
    'furnished':r"<span>E.yal.<\/span><span>(.+?)<\/span>"
  }
  props = {}
  for (key, ptn) in props_list.items():
    try:
      props[key] = re.findall(ptn, res)[0]
    except Exception as e:
      print('Caught exception while trying to parse', key, ':', e)
      props[key] = 'UNK'
  props['location'] = "/".join(re.findall(r"<a href='.+?listeleme'>(.+?)<\/a>\/?", res)[:3])
  return props

def dictToCSV(d : dict) -> str:
  s = ""
  keys = list(d.keys())
  keys.sort()
  for key in keys[:-1]:
    s += d[key] + ","
  s += d[keys[-1]]
  return s

url = "https://www.hurriyetemlak.com/konut-satilik/istanbul-sariyer-rumeli-hisari/listeleme"
f = open("database.txt", "a")
pageStart = int(input("Which page to start from : "))
itemStart = int(input("Which item to start from (in the starting page) : "))
for i in range(pageStart, 50):
  print('Page', i)
  items = getItemList(r.get(url, headers={'User-Agent' : goodUA}, params={'page':str(i)}).text)
  for (itemid, item) in enumerate(items[itemStart:], itemStart):
    print('Page', i, 'item', itemid)
    print(item)
    link = "https://www.hurriyetemlak.com" + item[1]
    while True:
      try:
        ress = getItemProps(r.get(link, headers={'User-Agent' : goodUA}).text)
      except Exception as e:
        print('Caught exception', e)
        continue
      else:
        break
    if ress != None:
      csvres=dictToCSV(ress)
      print(csvres)
      f.write(csvres + "\r\n")
      f.flush()
  itemStart = 0 # itemStart is only valid for the starting page
