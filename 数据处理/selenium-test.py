from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://book.qidian.com/info/3578389'
browser.get(url)
input1 = browser.find_elements_by_id('score1')
print(input1.text)