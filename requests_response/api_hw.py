import requests

authors = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors')
print(authors.status_code)
print(authors.text)

authors_2 = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Authors/5')
print(authors_2.status_code)
print(authors_2.text)


data = {
  "id": 100,
  "title": "Изучаем Python",
  "description": "Краткий курсо по Python",
  "pageCount": 320,
  "excerpt": "API",
  "publishDate": "2022-07-14"
}
add_author = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Books', json=data)
print(add_author.status_code)
print(add_author.text)

user = {
  "id": 125,
  "userName": "Egor",
  "password": "egor"
}
add_user = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Users', json=user)
print(add_user.status_code)
print(add_user.text)

update_book = {
  "id": 10,
  "title": "Просто книга",
  "description": "Просто текст",
  "pageCount": 500,
  "excerpt": "Просто пример из книги",
  "publishDate": "2022-07-14T12:13:46.292Z"
}
update = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=update_book)
print(update.status_code)
print(update.text)

old_user = 125
delete_user = requests.delete(f'https://fakerestapi.azurewebsites.net/api/v1/Users/{old_user}', timeout=2.5)
print(delete_user.status_code)
print(f"Пользователь с ID={old_user} удален")
