import time, openpyxl
from selenium import webdriver
from datetime import date

driver = webdriver.Chrome()  
wb = openpyxl.load_workbook('prices.xlsx')
sheet = wb['Sheet1']
today = date.today()

driver.get('https://www2.hm.com/en_gb/productpage.0963056001.html')

try:
    product = driver.find_element_by_css_selector('#main-content > div.product.parbase > div.layout.pdp-wrapper.product-detail.sticky-footer-wrapper.js-reviews > div.module.product-description.sticky-wrapper > div.sub-content.product-detail-info.product-detail-meta.inner.sticky-on-scroll.semi-sticky > div > section > h1')
    price = driver.find_element_by_css_selector('#product-price > div > span')
    todaydate = today.strftime('%d/%m/%Y')
    producttext = '%s'%(product.text)
    pricetext = '%s'%(price.text)
    row = (todaydate, producttext, pricetext)
    sheet.append(row)
except:
    row2 = (todaydate, 'N/A', 'N/A')
    sheet.append(row2)
    
driver.quit()
sheet.column_dimensions['A'].width = 11
sheet.column_dimensions['B'].width = 30
wb.save('prices.xlsx')
