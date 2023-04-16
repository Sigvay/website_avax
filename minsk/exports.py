import xlsxwriter as xlsx
import lxml.etree as ET
from lxml import etree as etr
from django.http import FileResponse


from website_avax import settings
from .support import *


def export_price(name: str):
    print(name)
    if name == 'Drom':
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
            worksheet.write(f'P{i}', (result.price + 100) * 88)
            worksheet.write(f'Q{i}', 'В наличии')
            worksheet.write(f'S{i}', result.photo)
        workbook.close()
        return FileResponse(open(settings.EXCEL_BASE_EXPORT, 'rb'))
    elif name == "Bamper":
        results = requests.get(f'https://avax.by/api/all_zap/DueMQ88!Sm43')
        workbook = xlsx.Workbook(settings.EXCEL_BASE_EXPORT)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        worksheet.write('A1', 'АРТИКУЛ', bold)
        worksheet.write('B1', 'МАРКА', bold)
        worksheet.write('C1', 'МОДЕЛЬ', bold)
        worksheet.write('D1', 'ВЕРСИЯ', bold)
        worksheet.write('E1', 'ГОД', bold)
        worksheet.write('F1', 'ТОПЛИВО', bold)
        worksheet.write('G1', 'ОБЪЕМ', bold)
        worksheet.write('H1', 'ТИП ДВИГАТЕЛЯ', bold)
        worksheet.write('I1', 'КОРОБКА', bold)
        worksheet.write('J1', 'ТИП КУЗОВА', bold)
        worksheet.write('K1', 'ЗАПЧАСТЬ', bold)
        worksheet.write('L1', 'ОПИСАНИЕ', bold)
        worksheet.write('M1', 'НОМЕР', bold)
        worksheet.write('N1', 'ПОД ЗАКАЗ', bold)
        worksheet.write('O1', 'НОВАЯ', bold)
        worksheet.write('P1', 'R ДИАМЕТР', bold)
        worksheet.write('Q1', 'J ШИРИНА', bold)
        worksheet.write('R1', 'КОЛ ОТВЕРСТИЙ', bold)
        worksheet.write('S1', 'ET ВЫЛЕТ', bold)
        worksheet.write('T1', 'DIA', bold)
        worksheet.write('U1', 'PCD', bold)
        worksheet.write('V1', 'СКЛАДСКАЯ ИНФОРМАЦИЯ', bold)
        worksheet.write('W1', 'ЦЕНА', bold)
        worksheet.write('X1', 'ВАЛЮТА', bold)
        worksheet.write('Y1', 'СКИДКА', bold)
        worksheet.write('Z1', 'ФОТО', bold)
        for i, (result) in enumerate(results.json(), start=2):
            worksheet.write(f'A{i}', result["ID_EXT"])
            worksheet.write(f'B{i}', result["МАРКА"])
            worksheet.write(f'C{i}', result["МОДЕЛЬ"])
            worksheet.write(f'E{i}', result["ГОД"])
            worksheet.write(f'F{i}', result["ТОПЛИВО"])
            worksheet.write(f'G{i}', result["ОБЪЕМ"])
            worksheet.write(f'H{i}', result["ТИП ДВИГАТЕЛЯ"])
            worksheet.write(f'I{i}', result["КОРОБКА"])
            worksheet.write(f'J{i}', result["ТИП КУЗОВА"])
            worksheet.write(f'K{i}', result["ЗАПЧАСТЬ"])
            worksheet.write(f'L{i}', "Цена за ДВС в комплектации как на фото, навесное с ДВС и КПП по отдельности не продаем. Видео работы ДВС перед снятием.")
            worksheet.write(f'M{i}', result["МАРКИРОВКА ДВИГАТЕЛЯ"])
            worksheet.write(f'N{i}', "0")
            worksheet.write(f'O{i}', "0")
            worksheet.write(f'W{i}', result["ЦЕНА"]+50)
            worksheet.write(f'X{i}', result["ВАЛЮТА"])
            worksheet.write(f'Z{i}', result["ФОТО"])
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


def export_avito(data):
    results = requests.get(f'https://avax.by/api/all_zap/DueMQ88!Sm43')
    ads = ET.Element("Ads")
    ads.set("formatVersion", "3")
    ads.set("target", "Avito.ru")
    for result in results.json():
        ad = ET.SubElement(ads, "Ad")
        ET.SubElement(ad, "Id").text = str(result["id"])
        ET.SubElement(ad, "AdType").text = data.type_category
        ET.SubElement(ad, "Category").text = data.category
        ET.SubElement(ad, "Address").text = data.adress
        ET.SubElement(ad, "ManagerName").text = data.manager_name
        ET.SubElement(ad, "ContactPhone").text = data.contact
        ET.SubElement(ad, "TypeId").text = data.type_id
        ET.SubElement(ad, "Title").text = f"{result['ЗАПЧАСТЬ']} {result['МАРКА']} " \
                                          f"{result['МОДЕЛЬ']} {result['ОБЪЕМ']}{result['ТИП ДВИГАТЕЛЯ']} " \
                                          f"{result['МАРКИРОВКА ДВИГАТЕЛЯ']}"
        ET.SubElement(ad, "Description").text = etr.CDATA(str(
            f"<p><strong>Артикул товара {result['ID_EXT']}</strong><br /><br />" +
            f"{result['ЗАПЧАСТЬ']} {result['МАРКА']} {result['МОДЕЛЬ']} {result['ОБЪЕМ']}{result['ТИП ДВИГАТЕЛЯ']}  {result['МАРКИРОВКА ДВИГАТЕЛЯ']} {result['ГОД']}г. (б/у)<br /><br />" +
            f"Марка: {result['МАРКА']}<br />" +
            f"Модель: {result['МОДЕЛЬ']}<br />" +
            f"Год: {result['ГОД']}<br /><br />" +
            f"Двигатель: {result['ОБЪЕМ']}{result['ТИП ДВИГАТЕЛЯ']}  {result['МАРКИРОВКА ДВИГАТЕЛЯ']}<br /><br />" +
            f"ЦЕНА УКАЗАНА ЗА ДВИГАТЕЛЬ В СБОРЕ В КОМПЛЕКТАЦИИ КАК НА ФОТО!<br />"+
            f"ДАННЫЙ ДВИГАТЕЛЬ НА ХОДИТСЯ НА УДАЛЕННОМ СКЛАДЕ.<br />"+
            f"срок поставки на центральный склад займет 1-2 дня!<br /><br />"+
            f"ЕСТЬ ВИДЕО РАБОТЫ ДВИГАТЕЛЯ в Англии перед разбором автомобиля.<br />" +
            f"Привезен из Англии, хорошее состояние, без пробега по СНГ.<br /><br />" +
            f"Производитель: {result['МАРКА']}<br />" +
            f"Маркировка: {result['МАРКИРОВКА ДВИГАТЕЛЯ']}<br /><br />" +
            f"Контpaктный {result['ЗАПЧАСТЬ']} {result['ОБЪЕМ']}{result['ТИП ДВИГАТЕЛЯ']} {result['МАРКИРОВКА ДВИГАТЕЛЯ']}, {result['ГОД']} годa, для {result['МАРКА']} {result['МОДЕЛЬ']} Снят с рабочего машинокомплекта. Небольшой пробег, без пробега по СНГ. Отличное состояние.<br />" +
            f"Отправка транспортными компаниями<br /><br /><br />"
        ))
        ET.SubElement(ad, "Price").text = str((int(result["ЦЕНА"]) + 50) * data.exchange)
        ET.SubElement(ad, "Availability").text = data.avalibale
        ET.SubElement(ad, "Condition").text = data.condition
        ET.SubElement(ad, "Brand").text = result["МАРКА"]
        images = ET.SubElement(ad, "Images")
        for i in str(result["ФОТО"]).split(','):
            ET.SubElement(images, "Image").set("url", i)

    tree = ET.tostring(ads, encoding='utf8')
    with open(f"{settings.XML_DIR}/{data.slug}.xml", 'wb') as my_file:
        my_file.write(tree)
    return FileResponse(open(f"{settings.XML_DIR}/{data.slug}.xml", 'rb'))
