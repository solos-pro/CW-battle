from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from game.equipment import EquipmentData
from game.personages import personage_classes
from game.utils import load_equipment
import os

BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
TEMPLATES: str = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, template_folder=TEMPLATES)
app.url_map.strict_slashes = False

EQUIPMENT: EquipmentData = load_equipment()
eq = load_equipment()
result = {
    "header": 'Выберите героя',  # для названия страниц
    "classes": ['Воин', 'Вор'],  # для названия классов
    "weapons": eq.weapon_names,  # для названия оружия
    "armors": eq.armor_names  # для названия брони
}

# def render_choose_personage_template(**kwargs) -> str:
#     return render_template(
#         'hero_choosing.html',
#         result=result
#     )

@app.route('/')
def index():
    return render_template('index.html')  # /game/templates/


@app.route('/choose-hero', methods=['GET', 'POST'])
def choose_hero():
    if request.method == 'GET':
        return render_template(
            'hero_choosing.html',
            result=result
        )
    return redirect(url_for('choose_enemy'))

@app.route('/choose-enemy', methods=['GET', 'POST'])
def choose_enemy():
    if request.method == 'GET':
        return render_template(
            'hero_choosing.html',
            result=result
        )
    return '<h2>Not implemented</h2>'

# result = {
# "header": 'Выберите героя', # для названия страниц
# "classes": ['Воин', 'Вор'], # для названия классов
# "weapons": eq.get_weapon_names, # для названия оружия
# "armors": eq.get_armor_names # для названия брони
# }
