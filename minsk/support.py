import datetime
import os.path

import pandas
import random
import requests
import string

from minsk.models import WarehouseMinsk, ExportPrice
from website_avax import settings

UTC = datetime.timezone(datetime.timedelta(hours=3))


def download_ex():
    down = requests.request('get', settings.URL_AVAX)
    output = open(settings.EXCEL_BASE_IMPORT, 'wb')
    output.write(down.content)
    output.close()


def read_ex():
    download_ex()
    read = pandas.read_excel(settings.EXCEL_BASE_IMPORT)
    result = read[settings.LI].values
    return result


def generate(quantity):
    return ''.join(random.choice(string.ascii_letters) for x in range(quantity))


def _convert(list_convert):
    return [itm[0] for itm in list_convert]


def get_position_minsk(art):
    result = WarehouseMinsk.objects.get(article=art)
    return result


def count_down_price(name: str):
    count = ExportPrice.objects.get(name=name)
    count.date_last = datetime.datetime.now(UTC)
    count.count += 1
    count.save()


def update_minsksklad():
    export = read_ex()
    import_art = [item[0] for item in export]
    minsk_art = _convert(WarehouseMinsk.objects.all().values_list('article'))
    try:
        for art in minsk_art:
            if art not in import_art:
                position = WarehouseMinsk.objects.get(article=art)
                position.delete()
        for art in export:
            if art[0] not in minsk_art:
                record = WarehouseMinsk(article=art[0], mark_auto=art[1], model_auto=art[2], submodel_auto=art[3],
                                        year=art[4], spare=art[5], fuel=art[6], volume=art[7], type_engine=art[8],
                                        transmission=art[9],
                                        original_number=art[10], description=art[11], price=art[12] + 50,
                                        currency=art[13],
                                        id_photo=generate(6),
                                        photo=art[14], input_article='s' + str(art[15]), vin=art[16],
                                        id_video=generate(8),
                                        video=art[17])
                record.save()
            elif get_position_minsk(art[0]).photo != art[14]:
                update = WarehouseMinsk.objects.get(article=art[0])
                update.photo = art[14]
                update.save()
            elif get_position_minsk(art[0]).video != art[17]:
                update = WarehouseMinsk.objects.get(article=art[0])
                update.video = art[17]
                update.save()
            elif get_position_minsk(art[0]).price != art[12]+50:
                update = WarehouseMinsk.objects.get(article=art[0])
                update.price = art[12]+50
                update.save()
    except Exception as error:
        print(f'При обновлении возникла ошибка - {error}')


drom_description = """
VIN - {}
Цена за ДВС с КПП в сборе, навесное с ДВС и КПП по отдельности не продаем. Видео работы ДВС перед снятием.

Уточняйте наличие товара на складе
"""

drom_name = "{} {} {}{}"

drom_body = "{}{}"
drom_year = "{}г."


avito_name = '{} {} {}{} {}г.'
avito_decription = """
Артикул товара - {}

{}
"""