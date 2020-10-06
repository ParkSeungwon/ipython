#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import sqlalchemy as sq

conn = sq.create_engine('mysql://zeta:cockcodk0@localhost/email?charset=utf8')
drv = webdriver.PhantomJS()
interval = 0

def get_url(url):
    global interval, drv
    interval += 1
    if interval == 20:
        interval = 0
        drv.close()#due to memory usage problem
        drv = webdriver.PhantomJS()#executable_path
    drv.get(url)
    return drv.page_source.encode('utf-8')

def extract_info(doc):
    soup = bs(doc, 'lxml')
    result = []
    product = soup.find('h1', {'class', 'title'})
    if product is not None: result.append(product.string)
    else : return result
    
    for caption in soup.find_all('caption'):
        if caption.get_text() == '판매자정보 테이블':
            for row in caption.find_parent('table').find_all('tr'):
                for td in row.find_all('td'):
                    result.append(td.string)
    return result


def extract_link(doc):
    soup = bs(doc, 'lxml')
    return soup.find_all('a')

def insert_to_db(result):
    if len(result) > 8:
        command = "insert into crawl values ('" + result[7] + "', '" + result[0] + "', '" + result[1] + "', '" + result[4].strip() + "', " + result[5] + ", '" + result[8] + "', '" + result[2] + "');"
        print(command)
    try: conn.execute(command)
    except sq.exc.SQLAlchemyError: pass
    
def write_file(result):
    if len(result) > 4 : result[4] = result[4].strip()
    f = open('11st.txt', 'a')
    for i in result: f.write(i + '\n')
    f.write('\n')
    f.close()

def crawl(url, depth):
    if depth == 0: return
    print(url)
    doc = get_url(url)
    if doc == '': return
    data = extract_info(doc)
    print(data)
    if len(data) != 0: write_file(data)
    for a in extract_link(doc):
        link = a.get('href')
        if(link is not None and link.find('product') is not -1): crawl(link, depth - 1)
        
eleven = 'https://www.11st.co.kr'
crawl(eleven, 3)
drv.quit()
