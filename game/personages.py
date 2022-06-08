from abc import ABC

from game.skills import Skill, ferocious_kick, powerful_thrust


class Personage(ABC):
    name: str = NotImplemented
    max_health: float = NotImplemented
    max_staming: float = NotImplemented
    stamina: float = NotImplemented
    attack: float = NotImplemented
    armor: float = NotImplemented
    skill: Skill = NotImplemented


class Warrior(Personage):
    name = 'Воин'
    max_health: float = 60.0
    max_staming: float = 30.0
    stamina: float = 0.8
    attack: float = 0.9
    armor: float = 1.2
    skill: Skill = ferocious_kick


class Thief(Personage):
    name = 'Вор'
    max_health: float = 50.0
    max_staming: float = 25.0
    stamina: float = 1.5
    attack: float = 1.2
    armor: float = 1.0
    skill: Skill = powerful_thrust
# Имя: "Воин"
# Очки здоровья: 60.0
# Очки выносливости: 30.0
# Модификатор атаки: 0.8
# Модификатор выносливости: 0.9
# Модификатор брони: 1.2
# Умение: Свирепый пинок

# Имя: "Вор"
# Очки здоровья: 50.0
# Очки выносливости: 25.0
# Модификатор атаки: 1.5
# Модификатор выносливости: 1.2
# Модификатор брони: 1.0
# Умение: Мощный укол