import json
from pyexpat import model
from . import models, ocr
import dramatiq
import jsonpickle
from celery import shared_task
import pathlib


def process_by_id(pk):
    process_image.delay(pk=pk)

def get_clearn_text(result):
    clean_text = ''
    for item_result in result:
        clean_text += item_result[1] + ' '
    return clean_text

def to_array_dict(result):
    array_result = list()
    for item_result in result:
        array_result.append({
            'coordinate' : item_result[0],
            'text' : item_result[1],
            'confident_level' : item_result[2]
        })
    return array_result

# @dramatiq.actor
@shared_task(serializer='json')
def process_image(pk):

    image: models.Image = models.Image.objects.get(pk=pk)
    result = ocr.extract_data(str(image.file))
    image.text = jsonpickle.encode(to_array_dict(result))
    image.status = 1
    image.result = get_clearn_text(result=result)
    image.title = str(image.file).replace("images/", "")
    image.save()
    print("finish process image")


if __name__ == '__main__':
    process_by_id(10)