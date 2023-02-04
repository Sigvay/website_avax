import xlsxwriter as xlsx
from django.http import FileResponse

from website_avax import settings
from .support import *


def export_price(name: str):
    if name == 'Avito':
        results = WarehouseMinsk.objects.all()
        workbook = xlsx.Workbook(settings.EXCEL_BASE_EXPORT)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', 'Id', bold)  # обязательный
        worksheet.write('B1', 'ManagerName', bold)  # не обязательный "имя менеджера"
        worksheet.write('C1', 'ContactPhone', bold)  # не обязательный "конт. телефон"
        worksheet.write('D1', 'Address', bold)  # обязательный "адресс"
        worksheet.write('E1', 'ContactMethod', bold)  # не обязательный способ связи "По телефону и в сообщениях"
        worksheet.write('F1', 'Category', bold)  # обязательный "Запчасти и аксессуары"
        worksheet.write('G1', 'Title', bold)  # обязательный "Дверь правая передняя Skoda Rapid"
        worksheet.write('H1', 'Description', bold)  # обязательный "Описание смотреть документацию"
        worksheet.write('I1', 'Price', bold)  # не обязательный "цена в рублях"
        worksheet.write('J1', 'ImageUrls', bold)  # не обязательный "url photo"
        worksheet.write('K1', 'GoodsType', bold)  # обязательный "Запчасти"
        worksheet.write('L1', 'AdType', bold)  # обязательный "Товар приобретен на продажу"
        worksheet.write('M1', 'ProductType', bold)  # обязательный "Для автомобилей"
        worksheet.write('N1', 'SparePartType', bold)  # обязательный "Двигатель"
        worksheet.write('O1', 'EngineSparePartType', bold)  # обязательный "Двигатель в сборе"
        worksheet.write('P1', 'Condition', bold)  # обязательный "Б/у"
        worksheet.write('Q1', 'Originality', bold)  # не обязательный "Оригинал"
        worksheet.write('R1', 'Availability', bold)  # не обязательный "В наличии"
        worksheet.write('S1', 'OEM', bold)  # не обязательный "Маркировку наверное вписать лучше"
        for i, (result) in enumerate(results, start=2):
            worksheet.write(f'A{i}', result.article)
            worksheet.write(f'B{i}', 'Александр')
            worksheet.write(f'C{i}', '79165147176')
            worksheet.write(f'D{i}', 'Москва, улица Промышленная, 11, стр.3')
            worksheet.write(f'E{i}', 'По телефону и в сообщениях')
            worksheet.write(f'F{i}', 'Запчасти и аксессуары')
            worksheet.write(f'G{i}', avito_name.format(result.spare, result.original_number, result.volume,
                                                       result.type_engine, result.year))
            worksheet.write(f'H{i}', avito_decription.format(result.input_article, result.description))
            worksheet.write(f'I{i}', (result.price + 100) * 80)
            worksheet.write(f'J{i}', result.photo)
            worksheet.write(f'K{i}', "Запчасти")
            worksheet.write(f'L{i}', "Товар приобретен на продажу")
            worksheet.write(f'M{i}', "Для автомобилей")
            worksheet.write(f'N{i}', "Двигатель")
            worksheet.write(f'O{i}', "Двигатель в сборе")
            worksheet.write(f'P{i}', "Б/у")
            worksheet.write(f'Q{i}', "Оригинал")
            worksheet.write(f'R{i}', "В наличии")
            worksheet.write(f'S{i}', result.original_number)
        workbook.close()
        return FileResponse(open(settings.EXCEL_BASE_EXPORT, 'rb'))
    elif name == 'Drom':
        results = WarehouseMinsk.objects.all()
        workbook = xlsx.Workbook(settings.EXCEL_BASE_EXPORT)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', 'Артикул', bold)
        worksheet.write('B1', 'Наименование товара', bold)
        worksheet.write('C1', 'Новый/б.у.', bold)
        worksheet.write('D1', 'Марка', bold)
        worksheet.write('E1', 'Модель', bold)
        worksheet.write('F1', 'Кузов', bold)
        worksheet.write('G1', 'Номер', bold)
        worksheet.write('H1', 'Двигатель', bold)
        worksheet.write('I1', 'Год', bold)
        worksheet.write('J1', 'L-R', bold)
        worksheet.write('K1', 'F-R', bold)
        worksheet.write('L1', 'U-D', bold)
        worksheet.write('M1', 'Цвет', bold)
        worksheet.write('N1', 'Примечание', bold)
        worksheet.write('O1', 'Количество', bold)
        worksheet.write('P1', 'Цена', bold)
        worksheet.write('Q1', 'Наличие', bold)
        worksheet.write('R1', 'Сроки доставки', bold)
        worksheet.write('S1', 'Фотография', bold)

        for i, (result) in enumerate(results, start=2):
            worksheet.write(f'A{i}', result.input_article)
            worksheet.write(f'B{i}', drom_name.format(result.spare, result.original_number, result.volume,
                                                      result.type_engine))
            worksheet.write(f'C{i}', 'б.у.')
            worksheet.write(f'D{i}', result.mark_auto)
            worksheet.write(f'E{i}', result.model_auto)
            worksheet.write(f'G{i}', result.original_number)
            worksheet.write(f'H{i}', drom_body.format(result.volume, result.type_engine))
            worksheet.write(f'I{i}', drom_year.format(result.year))
            worksheet.write(f'N{i}', drom_description.format(result.vin))
            worksheet.write(f'O{i}', 1)
            worksheet.write(f'P{i}', (result.price + 100) * 80)
            worksheet.write(f'Q{i}', 'В наличии')
            worksheet.write(f'S{i}', result.photo)
        workbook.close()
        return FileResponse(open(settings.EXCEL_BASE_EXPORT, 'rb'))
    else:
        results = WarehouseMinsk.objects.all()
        workbook = xlsx.Workbook(settings.EXCEL_BASE_EXPORT)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', 'Артикул', bold)
        worksheet.write('B1', 'Наименование', bold)
        worksheet.write('C1', 'Марка', bold)
        worksheet.write('D1', 'Модель', bold)
        worksheet.write('E1', 'Год', bold)
        worksheet.write('F1', 'Топливо', bold)
        worksheet.write('G1', 'Объем', bold)
        worksheet.write('H1', 'Тип двигателя', bold)
        worksheet.write('I1', 'Трансмиссия', bold)
        worksheet.write('J1', 'Маркировка', bold)
        worksheet.write('K1', 'Цена', bold)
        worksheet.write('L1', 'Валюта', bold)
        worksheet.write('M1', 'Разборочный', bold)
        worksheet.write('N1', 'ВИН', bold)
        worksheet.write('O1', 'Фото', bold)
        worksheet.set_column('J:J', 25)
        for i, (result) in enumerate(results, start=2):
            worksheet.write(f'A{i}', result.article)
            worksheet.write(f'B{i}', result.spare)
            worksheet.write(f'C{i}', result.mark_auto)
            worksheet.write(f'D{i}', result.model_auto)
            worksheet.write(f'E{i}', result.year)
            worksheet.write(f'F{i}', result.fuel)
            worksheet.write(f'G{i}', str(result.volume))
            worksheet.write(f'H{i}', result.type_engine)
            worksheet.write(f'I{i}', result.transmission)
            worksheet.write(f'J{i}', result.original_number)
            worksheet.write(f'K{i}', result.price)
            worksheet.write(f'L{i}', result.currency)
            worksheet.write(f'M{i}', result.input_article)
            worksheet.write(f'N{i}', result.vin)
            worksheet.write(f'O{i}', result.photo)
        workbook.close()
        return FileResponse(open(settings.EXCEL_BASE_EXPORT, 'rb'))
