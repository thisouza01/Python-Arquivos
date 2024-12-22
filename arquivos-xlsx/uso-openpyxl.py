import openpyxl
from openpyxl.utils.exceptions import InvalidFileException

path = "Book.xlsx"

try:
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    colunas = [cell.value for cell in sheet[1]]
    print("Nomes das colunas:", colunas)
except FileNotFoundError:
    print(f"O arquivo {path} não foi encontrado.")
except InvalidFileException:
    print(f"O arquivo {path} não é um arquivo Excel válido.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
