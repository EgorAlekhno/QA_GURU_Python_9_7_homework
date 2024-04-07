import shutil
from zipfile import ZipFile
import zipfile
import os
import pytest


# with ZipFile("tmp\\hello.zip") as zip_file:
#     print(zip_file.namelist())
#     text = zip_file.read('Hello.txt')
#     print(text)
#
#     zip_file.extract('Hello.txt', path='tmp')

@pytest.fixture(autouse=True)
def archive():
    # Имя архива, который вы хотите создать
    zip_file_name = "tmp\\example.zip"

    # Создание нового архива
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        # Добавление файлов в архив
        zipf.write("tmp\\python_testing.pdf", arcname="python_testing.pdf")
        # Можно также добавить файлы с изменением их имени в архиве:
        zipf.write("tmp\\example.csv", arcname="example_test.csv")
        zipf.write("tmp\\import_company_xlsx.xlsx", arcname="import_company_xlsx_test.xlsx")

    # Создание папки и перемещение в resources
    new_folder_path = "resources"
    os.makedirs(new_folder_path, exist_ok=True)
    shutil.move("tmp\\example.zip", "resources\\example.zip")
    yield
    shutil.rmtree("resources")