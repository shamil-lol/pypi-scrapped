r = "\u001b[91m"
g = "\u001b[92m"
y = "\u001b[93m"
db = "\u001b[94m"
p = "\u001b[95m"
b = "\u001b[96m"
w = "\u001b[97m"
rr = 0
try:
  import requests
  from bs4 import BeautifulSoup as bs
  from os import system as sys
  import sys as syst
  sys("clear")
  print (f"{r}[{y}!{r}]{p} checking your internet connection{w}")
  try:
    requests.get("https://google.com/")
  except Exception:
    sys("clear")
    print (f"{r}[{y}!{r}]{p} please turn on internet connection{w}")
    syst.exit()
  sys("clear")
  pn = input(f"{db}[{b}?{db}]{w}:{b} ")
  print ()
  r = requests.get(f"https://pypi.org/search/?q={pn}")
  s = bs(r.text, "html.parser")
  i = s.find_all(class_="package-snippet__name")
  for i in i:
    print (f'{y}[{g}-{y}]{db} name:\t\t {y}{i.text}{w}')
    url = f"https://pypi.org/project/{i.text}"
    l = requests.get(url).text
    sp = bs(l, "html.parser")
    print (f'{y}[{g}-{y}]{db} pip command:\t {y}{sp.find(id="pip-command").text}{w}')
    print (f'{y}[{g}-{y}]{db} description:\t {y}{sp.find(property="og:description")["content"]}{w}')
    print (f'{y}[{g}-{y}]{db} url:\t\t {y}{sp.find(property="og:url")["content"]}{w}')
    try:
      rep = sp.find(class_="github-repo-info hidden")["data-url"]
      rep = rep.replace("https://api.github.com/repos", "https://github.com")
    except Exception:
      rep = "Null"
    print (f'{y}[{g}-{y}]{db} repo:\t\t {y}{rep}{w}')
    rr += 1
    print ()
  print (f"{b}{rr} {y}results{w}")
  print (f"{g}[{y}✓{g}] {b}Done{w}")
except:
  pass
