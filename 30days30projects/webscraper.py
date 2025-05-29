import requests
from bs4 import BeautifulSoup
URL = 'https://www.bbc.com/news'
response = requests.get(URL)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    print("Latest BBC News Headlines:\n")

    headlines = soup.find_all('h2')

    for i, headline in enumerate(headlines[:10], start=1):
        text = headline.get_text(strip=True)
        if text:
            print(f"{i}. {text}")
else:
    print("Failed")
