# Пример 1.31.PP4E\Prevuew\cgi-bin\cgi101.py

#!/usr/bin/python
import cgi
form = cgi.FieldStorage()               # парсинг данных формы
print('Content-type: text/html\n')      # http-заголовок плюс пустая строка
print('<title>Reply Page</title>')      # html-разметка ответа
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print(f'<h1>Hello <i>{cqi.escape(form["user"].value)}</i>!</h1>')