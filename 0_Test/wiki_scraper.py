import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://sv.wikipedia.org/wiki/Bobby_Fischer'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

content_div = soup.find('div', {'id': 'bodyContent'})
text = content_div.get_text(separator='\n', strip=True)

lines = text.split('\n')
first_10_lines = lines[:10]

now = datetime.now()
timestamp = now.strftime("Sparad ---------------------------------- %Y-%m-%d kl %H:%M:%S")

with open('wikipedia_text.txt', 'a', encoding='utf-8') as f:
    f.write('\n\n' + timestamp + '\n')  
    for line in first_10_lines:
        f.write(line + '\n')