from functools import wraps
from typing import Dict, Type

from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

from controller import Game
from game.equipment import EquipmentData
from game.hero import Player, Hero, Enemy
from game.personages import personage_classes, Personage
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
heroes: Dict[str, Type[Hero]] = dict()

game = Game()


def game_processing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if game.game_processing:
            return func(*args, **kwargs)
        if game.game_results:
            return render_template('fight.html', heroes=heroes, result=game.game_results)
        return redirect(url_for('index'))
    return wrapper


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose-hero', methods=['GET', 'POST'])
def choose_hero():
    if request.method == 'GET':
        return render_template(
            'hero_choosing.html',
            result=result
        )
    heroes['player'] = Player(
        class_=personage_classes[request.form['unit_class']],
        weapon=EQUIPMENT.get_weapon(request.form['weapon']),
        armor=EQUIPMENT.get_armor(request.form['armor']),
        name=request.form['name']
    )

    return redirect(url_for('choose_enemy'))

@app.route('/choose-enemy', methods=['GET', 'POST'])
def choose_enemy():
    if request.method == 'GET':
        return render_template(
            'hero_choosing.html',
            result=result
        )
    heroes['enemy'] = Enemy(
        class_=personage_classes[request.form['unit_class']],
        weapon=EQUIPMENT.get_weapon(request.form['weapon']),
        armor=EQUIPMENT.get_armor(request.form['armor']),
        name=request.form['name']
    )
    return redirect(url_for('start_fight'))


@app.route('/fight')
def start_fight():
    if 'player' in heroes and 'enemy' in heroes:
        game.run(**heroes)
        return render_template('fight.html', heroes=heroes, result='Fight')
    return redirect(url_for('index'))

@app.route('/fight/hit')
@game_processing
def hit():
    return render_template('fight.html', heroes=heroes, result=game.player_hit())


@app.route('/fight/use-skill')
@game_processing
def user_skill():
    return render_template('fight.html', heroes=heroes, result=game.player_use_skill())

@app.route('/fight/pass-turn')
@game_processing
def pass_turn():
    return render_template('fight.html', heroes=heroes, result=game.next_turn())

@app.route('/fight/end-fight')
def end_figth():
    return redirect(url_for('index'))

