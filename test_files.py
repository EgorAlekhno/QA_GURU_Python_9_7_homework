import zipfile
import csv
from pypdf import PdfReader
from io import BytesIO, TextIOWrapper
from openpyxl import load_workbook


# проверка pdf файла
def test_read_pdf():
    with zipfile.ZipFile('resources/example.zip', 'r') as file_zip:
        with file_zip.open('python_testing.pdf') as text_pdf:
            pdf_data = BytesIO(text_pdf.read())
            pdf_file = PdfReader(pdf_data)
            number_of_pages = len(pdf_file.pages)
            page = pdf_file.pages[3]
            pdf_text = page.extract_text()
            assert number_of_pages == 256, "Количество страниц в PDF-file не 256!"
            # assert "БР = браузерные расширения" in pdf_text
