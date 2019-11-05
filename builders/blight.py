import os
import json
import requests as req
import ui
from pyfiglet import Figlet

BLIGHT_URL_CLONE = 'https://gitlab.com/aisahana-misc/aisastack-blight-vue.git'
BLIGHT_DIR_APP = 'blight'
# Initialize
SRC = 'src'
APPLICATION = 'Application'
SRC_APPLICATION = f'{SRC}/{APPLICATION}'
APP = 'Apps'
COMPONENTS = 'Components'


def blight_clone(git):
    git('clone', f'{BLIGHT_URL_CLONE}')

def blight_build(package):
    package = package.get('aisastack')
    url_service = package.get('service')
    url_component_detail = package.get('detail')
    url_component_filter = package.get('filter')
    url_component_list = package.get('list')
    url_component_popup = package.get('popup')
    url_component_info = package.get('info')
    progress_length = 6

    _Model = input("CamelCase\t\t: ")
    _model = input("camelCase\t\t: ")
    _Models = input("CamelCase(s)\t\t: ")
    _models = input("camelCase(s)\t\t: ")

    os.makedirs(f'{SRC_APPLICATION}/{_Models}/{APP}')
    os.makedirs(f'{SRC_APPLICATION}/{_Models}/{COMPONENTS}')

    text = req.get(url_service).text
    with open(f'{SRC_APPLICATION}/{_Models}/{_Model}Service.js', 'w+') as data:
        text = text.replace('Pr0ducts', _Models)
        text = text.replace('Pr0duct', _Model)
        text = text.replace('pr0ducts', _models)
        text = text.replace('pr0duct', _model)
        data.write(text)
        ui.info_progress(f'[done] {_Model}Service.js',  1, progress_length)

    text = req.get(url_component_detail).text
    with open(f'{SRC_APPLICATION}/{_Models}/{COMPONENTS}/{_Model}Detail.vue', 'w+') as data:
        text = text.replace('Pr0ducts', _Models)
        text = text.replace('Pr0duct', _Model)
        text = text.replace('pr0ducts', _models)
        text = text.replace('pr0duct', _model)
        data.write(text)
        ui.info_progress(f'[done] {_Model}Detail.vue',  2, progress_length)

    text = req.get(url_component_filter).text
    with open(f'{SRC_APPLICATION}/{_Models}/{COMPONENTS}/{_Model}Filter.vue', 'w+') as data:
        text = text.replace('Pr0ducts', _Models)
        text = text.replace('Pr0duct', _Model)
        text = text.replace('pr0ducts', _models)
        text = text.replace('pr0duct', _model)
        data.write(text)
        ui.info_progress(f'[done] {_Model}Filter.vue',  3, progress_length)

    text = req.get(url_component_list).text
    with open(f'{SRC_APPLICATION}/{_Models}/{COMPONENTS}/{_Model}List.vue', 'w+') as data:
        text = text.replace('Pr0ducts', _Models)
        text = text.replace('Pr0duct', _Model)
        text = text.replace('pr0ducts', _models)
        text = text.replace('pr0duct', _model)
        data.write(text)
        ui.info_progress(f'[done] {_Model}List.vue',  4, progress_length)

    text = req.get(url_component_popup).text
    with open(f'{SRC_APPLICATION}/{_Models}/{COMPONENTS}/{_Model}PopupSingle.vue', 'w+') as data:
        text = text.replace('Pr0ducts', _Models)
        text = text.replace('Pr0duct', _Model)
        text = text.replace('pr0ducts', _models)
        text = text.replace('pr0duct', _model)
        data.write(text)
        ui.info_progress(f'[done] {_Model}PopupSingle.vue',  5, progress_length)

    text = req.get(url_component_info).text
    with open(f'{SRC_APPLICATION}/{_Models}/{COMPONENTS}/{_Model}Info.vue', 'w+') as data:
        text = text.replace('Pr0ducts', _Models)
        text = text.replace('Pr0duct', _Model)
        text = text.replace('pr0ducts', _models)
        text = text.replace('pr0duct', _model)
        data.write(text)
        ui.info_progress(f'[done] {_Model}Info.vue',  6, progress_length)

