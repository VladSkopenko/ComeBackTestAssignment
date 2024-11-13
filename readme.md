# Інструмент автоматизованого форматування наукових статей

## Опис
Цей проект є веб-сервісом для автоматизованого форматування наукових статей у стилі APA (Journal of Applied Psychology). Користувачі можуть завантажувати свої документи у форматі Word, обирати журнал для публікації, а система автоматично надає пропозиції щодо виправлення форматування відповідно до вимог цього журналу.

## Мета
Забезпечити автоматичне форматування наукових статей для економії часу та зменшення помилок форматування.

---

## Опис рішення

### Підхід до розробки вебсервісу
Вебсервіс розробляється на основі FastAPI для обробки запитів, управління завантаженням і форматуванням документів. Основні етапи роботи сервісу:

1. **Завантаження документів**: 
   - Користувач завантажує документ Word через інтерфейс сервісу.
   - Завантажені документи зберігаються у Dropbox для подальшої обробки.
   - Python-бібліотека `python-docx` використовується для роботи з вмістом Word-документів.

2. **Визначення цитувань**:
   - Для виявлення та перевірки цитувань, що відповідають вимогам APA, використовується бібліотека `regex`.
   - Цитати, що слідують формату (Автор, Рік), ідентифікуються та перевіряються на відповідність вимогам журналу.

3. **Аналіз та пропозиції з форматування**:
   - Аналізуються елементи документа (шрифти, відступи, заголовки, список літератури) для відповідності стилю APA.
   - Сервіс надає пропозиції з виправлення таких елементів, як:
     - Шрифти
     - Відступи
     - Заголовки
     - Список літератури

4. **Експорт виправленого документа**:
   - Після внесення користувачем затверджених змін генерується кінцевий документ з форматуванням APA.
   - Експортований документ доступний користувачу для завантаження.

### Використані бібліотеки та інструменти
- **FastAPI** — для реалізації API.
- **PostgreSQL** — для зберігання даних про документи, статус перевірки і пропозиції змін.
- **Docker і Docker Compose** — для контейнеризації і налаштування середовища.
- **Dropbox** — для зберігання та завантаження документів користувачів.
- **Alembic** — для керування міграціями бази даних.
- **Pydantic** — для валідації даних.
- **python-docx** — для обробки та аналізу Word-документів.
- **Regex** — для виявлення цитувань і перевірки відповідності правил стилю APA.
- **HTML** — для структурування контенту веб-сторінки.
- **CSS** — для стилізації елементів інтерфейсу, включаючи використання фреймворку **Bootstrap** для адаптивного дизайну.
- **JavaScript** — для інтерактивності на клієнтській стороні, обробки кліків та асинхронних запитів.
    - **Fetch API** — для здійснення асинхронних запитів і взаємодії з сервером.
    - **Event Listeners** — для обробки кліків на кнопках і ініціації завантаження файлів.
### Додаткові бібліотеки

- **annotated-types** — для забезпечення гнучкішої типізації в Python, корисно при роботі з Pydantic для строгішої валідації.
- **anyio** — для асинхронного вводу/виводу, часто використовується з FastAPI для обробки асинхронних запитів.
- **asyncpg** — асинхронна бібліотека для роботи з PostgreSQL, що забезпечує швидку обробку запитів.
- **black** — для автоматичного форматування коду Python за загальноприйнятими стандартами.
- **certifi** — для забезпечення актуальних сертифікатів SSL, необхідних для безпечного з'єднання.
- **charset-normalizer** — для нормалізації та обробки тексту в різних кодуваннях.
- **click** — інструмент для створення командних інтерфейсів у Python, корисний для розробки скриптів управління додатком.
- **colorama** — для додавання кольорів у текстові інтерфейси, що покращує читабельність логів.
- **greenlet** — забезпечує ефективне управління асинхронними завданнями.
- **httpcore** і **httpx** — для асинхронних HTTP-запитів, корисні для інтеграції з зовнішніми сервісами.
- **idna** — для підтримки інтернаціоналізованих доменних імен у запитах.
- **iniconfig** — для конфігурації в ini-файлах, застосовується у налаштуванні тестів.
- **Jinja2** — шаблонізатор, що використовується для створення HTML-сторінок, інтегрується з FastAPI.
- **lxml** — для роботи з XML і HTML документами, включає розширену підтримку роботи з текстом.
- **Mako** — альтернативний шаблонізатор для Python.
- **MarkupSafe** — захист від ін'єкцій HTML, використовується в Jinja2.
- **mypy-extensions** — розширення для статичної типізації, що корисно при написанні строго типізованого коду.
- **packaging** — для аналізу та управління версіями, корисно при розробці та розгортанні додатків.
- **pathspec** — для визначення шаблонів ігнорування файлів, корисно з Black і Git.
- **pip** — менеджер пакетів Python, використовується для встановлення та управління бібліотеками.
- **pypandoc** — для конвертації документів між форматами, корисно для перетворення текстових документів у різні формати.
- **pytest** — фреймворк для тестування, що дозволяє створювати автоматизовані тести для перевірки правильності роботи додатку.
- **requests** — для здійснення HTTP-запитів, використовується в інтеграції з зовнішніми API.
- **six** — бібліотека для підтримки сумісності коду між Python 2 та Python 3.
- **sniffio** — інструмент для виявлення типу середовища виконання (асинхронний або синхронний).
- **SQLAlchemy** — ORM для роботи з базами даних, що спрощує взаємодію з PostgreSQL.
- **starlette** — фреймворк для створення асинхронних веб-додатків, основа для FastAPI.
- **stone** — використовується для роботи з API Dropbox, допомагає у створенні специфікацій та обробці запитів.
- **typing_extensions** — розширення типів, які додають нові можливості для Python типізації.
- **urllib3** — для керування HTTP-запитами з додатковими можливостями.
- **uvicorn** — ASGI сервер для запуску FastAPI додатку, забезпечує швидке і асинхронне оброблення запитів.

## Виклики та рішення

1. **Неправильний формат файлів**:
   - Виклик: Користувач може завантажити файли з неправильним форматом.
   - Рішення: Застосування перевірки та обмежень до файлів які обробляються програмою.

2. **Обмеження розміру файлу**:
   - **Виклик**: Користувачі можуть намагатись завантажити файли, що перевищують встановлені обмеження.
   - **Рішення**: Встановлення обмежень на максимальний розмір файлу та перевірка цього перед завантаженням. Якщо файл   занадто великий, користувачу буде виведено відповідне повідомлення.

3. **Файли з однаковими назвами**:
   - **Виклик**: Файли з однаковими назвами можуть викликати конфлікти при завантаженні.
   - **Рішення**: Генерація унікальних імен для файлів, що вже існують в системі, шляхом додавання числових індексів до   назв файлів або створення нових шляхів для завантаження.

4. **Прив'язка файлів до користувачів**:
   - **Виклик**: Потрібно відслідковувати, які файли належать конкретному користувачу.
   - **Рішення**: Збереження метаданих про файли в базі даних, де кожен файл буде прив'язаний до конкретного користувача   через унікальний ідентифікатор.Таблиця один до багатьох в базі даних

5. **Зберігання файлів**:
   - **Виклик**: Зберігання файлів на сервері призводить до швидкого заповнення дискового простору, ускладнює   масштабування, резервне копіювання та балансування навантаження.
   - **Рішення**: Використання хмарних сервісів для зберігання файлів, таких як Dropbox або Amazon S3.   Це дозволяє зберігати файли у віддаленому сховищі, залишаючи сервер для обробки запитів. Хмарне сховище забезпечує легке масштабування, ефективне управління файлами та зменшує навантаження на сервер.

6. **Можливість користувача змінювати свої документи**:
   - **Виклик**: Користувач має можливість змінювати свої документи, затверджувати або відхиляти зміни.
   - **Рішення**: Фомартувати документ цілком , зміни додавати в список , при натисканні на кнопку "форматування" переводити на сторінку з пітдвердженням, тим самим "обирати" зі списка виправлення   
   після завершення користувачем форматувати документ та  та повернути його на скачування.

7. **Визначення цитувань**:
    - **Виклик**: Виявлення цитувань у тексті може бути складним через варіації у форматах цитувань або невідповідності
      стилю APA.
    - **Рішення**: Використання регулярних виразів для визначення цитувань у тексті (наприклад, цитат у дужках у форматі
      APA). Але насправді, не бачу жодної причини не використати якусь nlp модель для цього.
8. **Перевірка на відповідність стилю APA**:
    - **Виклик**: Деякі елементи документа можуть мати специфічні вимоги до форматування, наприклад, шрифт, міжрядковий
      інтервал, заголовки, які не відповідають APA.
    - **Рішення**: Впровадження правил форматування для кожного елементу (наприклад, заголовки, абзаци, списки) та
      застосування їх до документа з використанням бібліотеки `python-docx`. Система надаватиме рекомендації щодо змін
      та автоматично оновлюватиме формат за необхідності.

9. **Виявлення та виправлення некоректних бібліографічних посилань**:
    - **Виклик**: Список літератури може містити неправильно оформлені посилання, що не відповідають вимогам APA.
    - **Рішення**: Аналіз списку літератури з використанням бібліотеки `bibtexparser` для виявлення некоректних форматів
      та надання рекомендацій щодо їх виправлення відповідно до стандарту APA.

10. **Тестування точності форматування**:
    - **Виклик**: Перевірка на точність форматування документа, щоб переконатися, що всі елементи відповідають APA.
    - **Рішення**: Автоматичне тестування форматування документа за допомогою спеціально розроблених тестових сценаріїв. Ці тести перевіряють правильність шрифтів, інтервалів, цитат та списку літератури відповідно до вимог APA.Простий приклад в test/test_formatted_apa.py
---

## Тестування та перевірка

Для перевірки точності форматування проводиться автоматизоване тестування:
- Використання тестових документів для перевірки коректності аналізу цитувань і форматування.
- Тестування основних функцій сервісу з використанням unit-тестів для контролю якості обробки тексту.

---

## Загальний план роботи

1. Розробка основних функцій для завантаження документів.
2. Реалізація механізму визначення цитувань і перевірки на відповідність стилю APA.
3. Додавання функцій для виявлення та виправлення невідповідностей форматування.
4. Впровадження експорту документів із внесеними виправленнями.
5. Створення автоматизованих тестів для перевірки точності роботи сервісу.
