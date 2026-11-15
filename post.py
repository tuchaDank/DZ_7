import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, timeout=10)
response.raise_for_status()

posts = response.json()

for post in posts[:5]:
    title = post["title"]
    body = post["body"]
    
    print(f"Заголовок: {title}")
    print(f"Текст: {body}")
    print("-" * 45)
