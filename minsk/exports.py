import xlsxwriter as xlsx
import csv
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
            worksheet.write(f'P{i}', (result.price + 250) * 100)
            worksheet.write(f'Q{i}', 'В наличии')
            worksheet.write(f'S{i}', result.photo)
        workbook.close()
        return FileResponse(open(settings.EXCEL_BASE_EXPORT, 'rb'))
    elif name == "Bamper":
        results = requests.get(f'https://avax.by/api/all_zap/DueMQ88!Sm43')
        with open(settings.CSV_BASE_EXPORT, "w", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                (
                    "ID_EXT",
                    "МАРКА",
                    "МОДЕЛЬ",
                    "ГОД",
                    "ЗАПЧАСТЬ",
                    "ВЕРСИЯ",
                    "ТОПЛИВО",
                    "ОБЪЕМ",
                    "ТИП ДВИГАТЕЛЯ",
                    "КОРОБКА",
                    "ТИП КУЗОВА",
                    "R ДИАМЕТР",
                    "J ШИРИНА",
                    "КОЛ ОТВЕРСТИЙ",
                    "ET ВЫЛЕТ",
                    "DIA",
                    "PCD",
                    "НОМЕР",
                    "ОПИСАНИЕ",
                    "НОВАЯ",
                    "ПОД ЗАКАЗ",
                    "СКЛАДСКАЯ ИНФОРМАЦИЯ",
                    "ЦЕНА",
                    "ВАЛЮТА",
                    "СКИДКА",
                    "АДРЕС",
                    "ТЕЛЕФОНЫ",
                    "EMAIL",
                    "ИМЯ",
                    "ФОТО",
                )
            )
        for result in results.json():
            with open(settings.CSV_BASE_EXPORT, "a", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(
                    (
                        result['ID_EXT'],
                        result['МАРКА'],
                        result['МОДЕЛЬ'],
                        result['ГОД'],
                        result['ЗАПЧАСТЬ'],
                        "",
                        result['ТОПЛИВО'],
                        result['ОБЪЕМ'],
                        result['ТИП ДВИГАТЕЛЯ'],
                        result['КОРОБКА'],
                        result['ТИП КУЗОВА'],
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        result['МАРКИРОВКА ДВИГАТЕЛЯ'],
                        "Цена за ДВС с навесным оборудованием и КПП, навесное с ДВС и КПП по отдельности не продаем. Видео работы ДВС перед снятием.",
                        0,
                        0,
                        "",
                        result['ЦЕНА'] + 50,
                        result['ВАЛЮТА'],
                        "",
                        "",
                        "",
                        "",
                        "",
                        result['ФОТО']
                    )
                )
        return FileResponse(open(settings.CSV_BASE_EXPORT, 'rb'))
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
            f"Марка: {result['МАРКА']}<br />" +
            f"Модель: {result['МОДЕЛЬ']}<br />" +
            f"Год: {result['ГОД']}<br />" +
            f"Трансмиссия: {result['КОРОБКА']}<br /><br />" +
            f"{result['ЗАПЧАСТЬ']}: {result['ОБЪЕМ']}{result['ТИП ДВИГАТЕЛЯ']}  {result['МАРКИРОВКА ДВИГАТЕЛЯ']} Б/У.<br /><br />" +
            f"<strong>Цена указана за {result['ЗАПЧАСТЬ']} в сборе, в комплектации как на фото!</strong><br />"+
            "Проверочный срок на ДВС 14 дней. На навесное, КПП гарантии нет<br /><br />"+
            f"У нас в наличии контрактный {result['ЗАПЧАСТЬ']} {result['МАРКА']} {result['МОДЕЛЬ']} {result['ОБЪЕМ']}{result['ТИП ДВИГАТЕЛЯ']}  {result['МАРКИРОВКА ДВИГАТЕЛЯ']}, произведенный в {result['ГОД']} году. "+
            f"Данный {result['ЗАПЧАСТЬ']} в отличном состоянии и готов к установке. Он был снят с рабочего машинокомплекта и имеет небольшой пробег. {result['ЗАПЧАСТЬ']} не имеет пробега по СНГ. <br />"+
            "Мы предлагаем качественные б/у двигатели по низким ценам, так как являемся прямым импортером. Компания AVAX Motors гарантирует высокое качество товара и отличное обслуживание. <br /><br />"+
            "Адрес складов: <br />"+
            "Беларусь, Минская область, Узденский район, Озерский сельсовет, агрогородок Озеро, Институтский переулок, 2/2 <br />"+
            "Россия, Московская область, Ленинский городской округ, г.Видное, северная промзона, владение 8<br /><br />"
            f"<strong>Данный {result['ЗАПЧАСТЬ']} находится на складе в Республике Беларусь</strong><br /><br />"+
            "<strong>Если вы находитесь в Москве, срок поставки на наш склад займет всего 1-3 дня! Мы также предлагаем услуги доставки с помощью транспортных компаний.</strong><br /><br />"+
            "У нас есть видео работы данного двигателя в Англии перед разбором автомобиля, чтобы вы могли оценить его работу и состояние. Двигатель был привезен из Англии и находится в хорошем состоянии. " +
            f"Не упустите возможность приобрести отличный двигатель для своего {result['МАРКА']} {result['МОДЕЛЬ']}! Свяжитесь с нами прямо сейчас и мы с радостью ответим на все ваши вопросы и организуем доставку."
        ))
        ET.SubElement(ad, "Price").text = str((int(result["ЦЕНА"]) + 150) * data.exchange)
        ET.SubElement(ad, "Availability").text = data.avalibale
        ET.SubElement(ad, "Condition").text = data.condition
        ET.SubElement(ad, "Brand").text = result["МАРКА"]
        ET.SubElement(ad, "Make").text = result["МАРКА"]
        images = ET.SubElement(ad, "Images")
        for i in str(result["ФОТО"]).split(','):
            ET.SubElement(images, "Image").set("url", i)

    tree = ET.tostring(ads, encoding='utf8')
    with open(f"{settings.XML_DIR}/{data.slug}.xml", 'wb') as my_file:
        my_file.write(tree)
    return FileResponse(open(f"{settings.XML_DIR}/{data.slug}.xml", 'rb'))
