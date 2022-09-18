from selenium.webdriver.common.keys import Keys
import pyperclip #클립보드를 이용하여 

from selenium import webdriver

from selenium.webdriver.common.by import By


import time
    #페이지 로딩을 기다리는데에 사용할 모듈

chrome_path = 'C:\\Users\\Administrator\\Desktop\\chromedriver_win32\\chromedriver.exe'
    # 유니코드 에러 경로 \ -> \\하면 해결됩니다!!
url = 'https://www.naver.com/'
browser = webdriver.Chrome(chrome_path)
    #
browser.get(url)
    #크롬 드라이버에 url 주소 넣고 실행

time.sleep(3)
    # 페이지가 완전히 로딩될 때 까지 기다리기
    
# browser.find_element_by_xpath('//*[@id="react-page"]/div[1]/a[2]').click()    
    
browser.find_element(By.XPATH, '//*[@id="account"]/a/i').click()
    # 자동으로 클릭하도록 합니다!!
    
time.sleep(2)

pyperclip.copy('tjdfody133')
browser.find_element(By.XPATH, '//*[@id="id"]').send_keys(Keys.CONTROL,'v')

pyperclip.copy('wptjf0985!')
browser.find_element(By.XPATH, '//*[@id="pw"]').send_keys(Keys.CONTROL,'v')
    
browser.find_element(By.XPATH, '//*[@id="log.login"]').click()
    # 자동으로 클릭하도록 합니다!!
    
time.sleep(3)

browser.switch_to.window(browser.window_handles[-1])
    # -1    >>  최신팝업창으로 이동
browser.switch_to.window(browser.window_handles[0])
    # 0     >>  원래 창으로 이동 

browser.close() #크롬 창 닫기

# .click()
# .send_keys('')
# .clear() -> 글자지우기

# browser.find_element(By.XPATH, '//*[@id="sessionUserAvatar"]').click()
# browser.find_element(By.XPATH, '//*[@id="logout"]').click()
    # 코드펜에서 로그아웃하기

