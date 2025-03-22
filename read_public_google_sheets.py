###
# Read Public Google Sheets
# 
# 
# ###

# import pandas

# url_sheet1 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"
# url_sheet2 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2014"
# data1 = pandas.read_csv(url_sheet1)
# data2 = pandas.read_csv(url_sheet2)

# print(data1)
# print(data2)

import pandas

url_sheet1 = "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"

data1 = pandas.read_csv(url_sheet1)
# data1_df = pandas.DataFrame(url_sheet1)

print(data1)