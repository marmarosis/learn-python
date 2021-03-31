import time, openpyxl
from selenium import webdriver
from datetime import date

driver = webdriver.Chrome()  
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
today = date.today()

driver.get('https://www.bbc.co.uk/weather/2643743')

try:
    temp = driver.find_element_by_css_selector('#daylink-0 > div.wr-day__body > div.wr-day__details-container > div > div.wr-day__temperature > div > div.wr-day-temperature__high > span.wr-day-temperature__high-value > span > span.wr-value--temperature--c')
    print('Today\'s temperature is %sC'%(temp.text))
    todaydate = today.strftime('%d/%m/%Y')
    temptext = '%sC'%(temp.text)
    row = (todaydate, temptext)
    sheet.append(row)
except:
    print('No temperature found!')
    row2 = (todaydate, 'N/A')
    sheet.append(row2)
    
driver.quit()
sheet.column_dimensions['A'].width = 11
wb.save('example.xlsx')
