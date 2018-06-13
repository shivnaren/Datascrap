from html_file import raw_html_text

import requests as re
from bs4 import BeautifulSoup

# raw_html_file = re.get('https://connect.data.com/company/view/vNTDYqDD4A0r9ybX1QtHXg/')


soup_html = BeautifulSoup(raw_html_text, "html.parser")
# print(soup_html.prettify())

div_html = soup_html.findAll("div", {"class":"seo-company-info"})
tables = div_html[0].findAll('table')

# def find_tables_html(raw_div_html):
#     for i in range(len(raw_div_html)):
#         tables_html = raw_div_html[i].findAll('table')
#     return tables_html
#
#
# def find_rows_html(raw_tables_html):
#     for i in range(len(tables)):
#         row_html = raw_tables_html[i].findAll('tr')
#     return row_html
#
#
# # print(tables)
# #
# # for i in range(len(tables)):
# #     tr = tables[i].find_all('tr')
# #     for i in range(len(tr)):
# #         td = tr[i].find_all('td')
# #         for i in range(len(td)):
# #             data = td[i].get_text()
# #             print(data)
#
# def find_phone_row_html(raw_row_html):
#     for i in range(len(raw_row_html)):
#         row_data = raw_row_html[i].get_text()
#         if "Phone" in row_data:
#             row_phone_html = raw_row_html[i].find_all('td')
#     return row_phone_html
#

def find_phone_td_html(raw_row_phone_html):
    phone_list = list()
    for i in range(len(raw_row_phone_html)):
        phone_list.append(raw_row_phone_html[i].get_text())
    return phone_list
#
#
#

for i in range(len(tables)):
    tr = tables[i].find_all('tr')
    for i in range(len(tr)):
        data = tr[i].get_text()
        if "Phone" in data:
            td = tr[i].find_all('td')




#
#
#
