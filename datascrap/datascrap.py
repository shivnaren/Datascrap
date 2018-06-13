import requests as r
import bs4 as bs

r = r.get('https://connect.data.com/company/view/vNTDYqDD4A0r9ybX1QtHXg/')
c = r.content
soup = bs.BeautifulSoup(c, "html.parser")

data = soup.findAll("div", {"class":"seo-company-info"})
tables = data[0].findAll('table')
# print(tables)
#
# for i in range(len(tables)):
#     tr = tables[i].find_all('tr')
#     for i in range(len(tr)):
#         td = tr[i].find_all('td')
#         for i in range(len(td)):
#             data = td[i].get_text()
#             print(data)


for i in range(len(tables)):
    tr = tables[i].find_all('tr')
    for i in range(len(tr)):
        data = tr[i].get_text()
        if "Phone" in data:
            print(data)