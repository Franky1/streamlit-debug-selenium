import bs4 as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import streamlit as st
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Helper():

    global browser
    
    def init(self):
        self.API_TOKEN = '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'
        self.headers = {"Authorization": f"Bearer {self.API_TOKEN}"}
        self.API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        s = Service('C:/Users/.../chromedriver.exe')
        browser = webdriver.Chrome(service = s,chrome_options=chrome_options)

    def spell_check(self,input_term):
        self.suggestion = input_term

    def get_snippet(self):
        self.query = self.suggestion.replace(" ","+")
        self.url = "https://www.google.com/search?q=" + self.query
        browser.get(self.url)
        html_source = browser.page_source
        browser.close()
        soup = bs.BeautifulSoup(html_source, "html")
        text = soup.find('span',class_='hgKElc').text
        return text
    
def get_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    s = Service('C:/Users/.../chromedriver.exe')
    browser = webdriver.Chrome(service = s,chrome_options=chrome_options)
    return browser


st.header( 'Question' )

input_term = st.text_area('','What is the impact of Globalization ?')

if st.button('Ask'):
    browser = get_browser()
    helper = Helper()
    helper.spell_check(input_term)
    snippet = helper.get_snippet()
else:
    snippet = ''

st.header( 'Answer' )

st.markdown( snippet )
