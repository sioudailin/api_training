# 從 Dad jokes 網站爬取笑話，並可以讓使用者指定『關鍵字』，將相關資料收集下來，儲存到一個 txt 檔中。
# 將笑話總數印出，若超過一筆，隨機取一筆 show 給使用者看。

# Packages
import requests
import json
import random

url = "https://icanhazdadjoke.com/search"
term = input("Please enter what you want to search? ").lower()
# version 1
# response = requests.get(url, headers={"Accept": "application/json"}, params={"term": f"{term}"}).json()

# version 2
response = requests.get(url, headers={"Accept": "application/json"}, params={"term": f"{term}"})

response = json.loads(response.text)
results = response["results"]
if results:
    result = random.choice(results)["joke"]
    total_jokes = response["total_jokes"]
    print(f"I found {total_jokes}. And here's one for you! \n {result}")
else:
    print("I found nothing!!!")

