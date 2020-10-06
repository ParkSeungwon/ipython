
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs


# In[2]:


drv = webdriver.Firefox()
interval = 0


# In[44]:


def get_url(url):
    global drv, interval
    #time.sleep(5)
    interval += 1
    if interval == 20 : 
        interval = 0
        drv.close()
        drv = webdriver.Firefox()
    print(url)
    drv.get(url)
    return drv.page_source

def gmarket_extract(doc):
    soup = bs(doc, 'lxml')
    title = soup.find('h1', {'class':'itemtit'})
    seller = soup.find('dl', {'class':'exchange_data seller_data'})
    if title is None or seller is None: return ''
    return str(title) + '\n' + str(seller)

def street_extract(doc):
    soup = bs(doc, 'lxml')
    title = soup.find('h1', {'class': 'title'})
    for caption in soup.find_all('caption'):
        if caption.get_text() == '판매자정보 테이블':
            seller = caption.find_parent('table')
    return str(title) + '\n' + str(seller)
                
def extract_link(doc):
    soup = bs(doc, 'lxml')
    return [x.get('href') for x in soup.find_all('a')]

def crawl(url, depth, extract, file):
    if depth == 0: return
    doc = get_url(url)
    if doc == '' or doc is None: return
    result = extract(doc)
    if result is None: return
    print(result)
    f = open(file, 'a')
    f.write(result)
    f.close()
    
    for link in extract_link(doc):
        if link is not None and len(link) > 4 and link[:4] == 'http' and link.find('dealermall') == -1:
            crawl(link, depth - 1, extract, file)
    
        


# In[58]:


crawl('https://www.gmarket.co.kr', 2, gmarket_extract, 'gmarket.txt')


# In[46]:


doc = get_url('http://item.gmarket.co.kr/Item?goodsCode=1859437894')


# In[47]:


gmarket_extract(doc)


# In[7]:


s = bs(doc,'lxml')


# In[8]:


s.find_all('h1')


# In[17]:


title = s.find('h1', {'class':'itemtit'})
seller = s.find('dl', {'class':'exchange_data seller_data'})


# In[40]:


for i in seller: print(i)


# In[41]:


str(seller)

