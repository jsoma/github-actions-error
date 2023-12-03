import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://www.npr.org/")
doc = BeautifulSoup(response.text, features='html.parser')

stories = doc.find_all("article")

all_data = []
for story in stories:
    data = {}
    try:
        data['title'] = story.find(class_="title").text.strip()
        data['url'] = story.find("a")['href']
        all_data.append(data)
    except:
        pass

df = pd.DataFrame(all_data)
df.to_csv("headlines.csv", index=False)
print("Done! 🎉")