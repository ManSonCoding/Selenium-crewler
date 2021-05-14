from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip

# default setting
filepath = './test.txt'
correct = []
lines = []

f = open(filepath, 'r', encoding='euc-kr')
while True:
    line = f.readline()
    lines.append(line)
    if not line: break
f.close()


# corrcting function
def wrong_to_correct(sentences):
    # 셀레니움 설정
    options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
    options.add_argument("headless")


    for sentence in sentences:
        try:
            driver = webdriver.Chrome('./chromedriver',options=options)

            driver.get('https://dic.daum.net/grammar_checker.do')

            elem = driver.find_element_by_name("sentence")
            elem.send_keys(sentence)
            elem.send_keys(Keys.RETURN)

            # 검사
            elem = driver.find_element_by_id("btnCheck")
            elem.click()


            # 복사
            elem = driver.find_element_by_id("btnCopy")
            elem.click()


            text = pyperclip.paste()
            correct.append(text)

        except Exception as e:
            correct.append(text)

        driver.quit()

    for i in correct:
        print(i)

wrong_to_correct(lines)