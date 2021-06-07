# Selenium-crewler

# 이 레포지토리의 목록  
- 셀레니움으로 다음 맞춤법 검사기로 자동 검사하기.
- 셀레니움으로 인스타 불법 토토충 신고 먹이기


## 한국어 문법은 어렵다.

그래서 그런지 공식적인 자리에서 한글 맞춤법 검사기는 필수이다. OCR을 프로젝트를 진행하던 도중, 낮은 인식률을 보여주고 있었기에, 이를 맞춤법 검사기를 한 번 거치게 된다면 좋겠다는 생각을 했다.

- 한글 OCR 정확도가 상당히 떨어짐.
- 문법이나, 어미 정도만 고칠 수 있어도 상당히 자연스러운 문장이 되지 않을까 생각해봄.

### 셀레니움을 활용하여 지원하지 않는 API를 온라인으로 굴려보자.

물론 공식적으로 지원되는 API를 사용하는 것이 가장 좋지만, 맞춤법 검사기의 경우 표절시비로 카카오에서 지원을 중단한 것으로 알고 있다. 우리는, 서버가 부하되지 않는 선에서, 검사기를 적당히 사용하여야 한다. 

### 셀레니움 활용

```python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
```
우리는 셀레니움패키지를 활용하여, 맞춤법을 검사할 것이다.

```python
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
```
텍스트를 한 줄 씩 읽어서, 저장할 것이다.

```python
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

```

함수는 간단하다. 크롬드라이버를 열고, 인터넷에서 누르고자 하는 버튼을 F11을 눌러 검사를 한다. 
![](https://images.velog.io/images/juncode/post/706e1f42-8eeb-4877-940c-c42465cb160b/image.png)
그러면 크롬 오른편에 이런식으로 코드가 주르륵 뜬다.

이 때 누르고자 했던 버튼의 id나 name을 찾아, element_by_XX에 (XX: id, xpath등)함수에 넣으면 된다.

### 결과



```text
맞춤법틀린건 오타다< 라는주제로 싸우고있어서요 알려주시면 감사하겠습니다 맞춤법을틀렸는데 그게 오타가 될 수 있나요? 오타는 단순히 타자를 치다가 실수가 난거아닌가요?```

```text
맞춤법 틀린 건 오타다 <라는 주제로 싸우고 있어서요 알려주시면 감사하겠습니다 맞춤법을 틀렸는데 그게 오타가 될 수 있나요? 오타는 단순히 타자를 치다가 실수가 난 거 아닌가요?

```

오타도 수정 되지만 생각보다 띄어쓰기가 잘고쳐진다. 

여러 자소서를 첨삭할 때 편하지 않을까..
