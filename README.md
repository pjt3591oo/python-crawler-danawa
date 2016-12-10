# crawler
해당 프로그램은 selenium을 사용하여 다나와 페이지에서 제품 정보를 수집하는 크롤러 입니다.

## install OR excute

```python
$ git clone https://github.com/pjt3591oo/python-crawler-danawa

$ pip install -r requirements.txt  # python 2.x version
$ pip3 install -r requirements.txt  # python 3.x version

$ python app.py    # python 2.x version
$ python3 app.py    # python 3.x version
```

윈도우7-64bit 환경에서는 즉시 실행이 가능.

윈도우7-64bit 이외의 환경에서는 웹 드라이버를 따로 설치를 하여 경로를 잡아주어야 합니다.
(해당 디렉토리에 있는 chromedriver.exe를 지우셔도 됩니다.)


`Danawa.py`

```python
browser = webdriver.Chrome('chromedriver.exe')
```

parameter로 넘겨주는 값이 해당 드라이버 경로입니다.

