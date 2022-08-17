import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import schedule
import time

ua = UserAgent()
url = 'https://nic.kz'
headers ={
    'user-agent': ua.random
    }
def get_data():
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    trs = soup.find_all('td', class_='white-text')[-1].find_all('tr')
    with open('data.txt', 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        for tr in trs:
            data = tr.find_all('td')[0].text
            domen = tr.find_all('td')[1].text + '\n'
            if domen in lines:
                print("Есть")
            else:
                print('Добавлено')
                f.write(domen)
    

def main():
    schedule.every(10).minutes.do(get_data) 
    while True:
        schedule.run_pending()
if __name__ == '__main__':
    main()