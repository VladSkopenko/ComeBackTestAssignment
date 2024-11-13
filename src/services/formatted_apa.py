from io import BytesIO

from docx import Document
from docx.shared import Pt

from src.core.exceptions import NotFound
from src.core.messages import Messages


class FormatterApa:
    """
    Клас для автоматичного форматування документа у стилі APA.
    Виконує налаштування шрифта, полів та міжстрокового інтервалу для документа.
    """

    def __init__(self, file_content):
        """
        Ініціалізація класу та завантаження документа з переданого вмісту.

        :param file_content: Вміст документа у байтовому форматі (наприклад, файл .docx).
        """
        self.doc = Document(BytesIO(file_content))

    def formatted_font(self):
        """
        Метод для налаштування шрифта та міжстрокового інтервалу в документі.

        Встановлює шрифт 'Times New Roman' розміром 12 та міжстроковий інтервал 2 для всіх текстових елементів.
        """
        style = self.doc.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(12)

        style.paragraph_format.line_spacing = 2

    def formatted_margins(self):
        """
        Метод для налаштування полів документа (1 дюйм з усіх боків).

        Встановлює поля на 1 дюйм для всіх сторін документа.
        Поля налаштовуються для всіх секцій документа.
        """
        for section in self.doc.sections:
            section.left_margin = Pt(72)
            section.right_margin = Pt(72)
            section.top_margin = Pt(72)
            section.bottom_margin = Pt(72)

    def get_formatted_stream(self) -> BytesIO:
        """
        Метод для отримання відформатованого документа у вигляді потоку байтів.

        Зберігає відформатований документ в об'єкт BytesIO, який можна передати або зберегти.

        :return: Потік байтів з відформатованим документом.
        :raises ValueError: Якщо документ не був відформатований.
        """
        if not self.doc:
            raise NotFound(Messages.NOT_FOUND)

        docx_stream = BytesIO()
        self.doc.save(docx_stream)
        docx_stream.seek(0)
        return docx_stream
