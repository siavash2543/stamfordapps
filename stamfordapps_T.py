import requests
from bs4 import BeautifulSoup
import mysql.connector
 
db =mysql.connector.connect(user='siavashtajaddini', password='admin123', host='localhost', database='stamfordapps_1')

url ='https://stamfordapps.org/restaurantratings/ListRestaurants.aspx?SType=All&slabel=est_id&sdir=Asc'
r= requests.get(url)
contents = BeautifulSoup(r.text,"html.parser",encoding='utf-8')

tables=[]
datas_table=contents.findAll("table",{"cellspacing":"0","cellpadding":"5","align":"Center","rules":"all","border":"1","id":"grdData"})
for table in datas_table:
    headers=[]
    rows=table.findAll('tr')
    
    for header in table.find('tr').findAll('th'):
        headers.append(header.text)
    
    for row in table.findAll('tr')[1: ]:
        values=[]
        for col in row.findAll('td'):
            values.append(col.text)
        if values:
            tablesDict={headers[i]:values[i] for i in range(len(values))}
            tables.append(tablesDict)
for data in tables:
    print(data)

sql = "INSERT INTO Restaurants(ID,Name,Address,Zip,Contact,Type,Date,Rating,Grade) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(ID,Name,Address,Zip,Contact,Type,Date,Rating,Grade)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    db.close()




