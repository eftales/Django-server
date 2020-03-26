import requests
url = 'http://eftales.pythonanywhere.com/SNSC/ClassNumChange/'
BuildingID = 'PC'
BuildingID = '107'
Num = '233'

r = requests.get(url + BuildingID + ':' + BuildingID + ':' + Num)
print(r.text)
