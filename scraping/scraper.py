from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
from selenium.webdriver.common.keys import Keys
import time
list1=[]
def gift_shop():
	browser=webdriver.Chrome('/home/shivansh/Documents/driver/chromedriver')
	browser.get('https://www.justdial.com/Delhi/Gift-Stores/nct-10231352/page-1')
	elm=browser.find_element_by_tag_name('html')
	elm.send_keys(Keys.END)
	time.sleep(7)
	elm.send_keys(Keys.HOME)
	response = browser.execute_script('return document.documentElement.outerHTML')
	soup=BeautifulSoup(response,'html.parser')
	div=soup.find('ul',class_='rsl col-md-12 padding0')
	div2=div.find_all('li',class_='cntanr')
	a=1
	for i in div2:
		Dict={}
		name=i.find('span',class_='lng_cont_name').text
		rateing=i.find('span',class_='green-box').text
		address=i.find('p',class_='address-info tme_adrssec').a.text.split()
		address.remove('more..')
		main_Address=''
		for j in address:
			main_Address+=(j+" ")
		img=i.find('a',class_='nlogo lazy srtbyPic').img['src']
		try:
			contact_span=i.find("p",class_="contact-info ").a.find_all('span')
			contact_no=""
			dic_contact={'icon-dc':'+','icon-fe':'(','icon-hg':')','icon-ba':'-','icon-acb':'0','icon-yz':'1','icon-wx':'2','icon-vu':'3','icon-ts':'4','icon-rq':'5','icon-po':'6','icon-nm':'7','icon-lk':'8','icon-ji':'9'}
			for j in contact_span:
				b=dic_contact[(j)['class'][1]]
				contact_no+=b
		except AttributeError:
			contact_no=""
			pass
		dic["contact"]=contact_no
		Dict['Shop name ']=name
		Dict['Address']=main_Address
		Dict['rateing']=rateing
		Dict['img-link']=img
		list1.append(Dict)
		a+=1
	return(list1)
pprint(gift_shop())
