from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Отправляем запрос к публичному API для получения случайной цитаты
    response = requests.get('https://api.quotable.io/random', verify=False)

    # Проверяем, что запрос успешен
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data['content']
        author = quote_data['author']
    else:
        quote = "Не удалось загрузить цитату. Попробуйте обновить страницу."
        author = ""

    return render_template('index.html', quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)
