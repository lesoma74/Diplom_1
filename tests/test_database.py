import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_available_buns(db):
    buns = db.available_buns()
    assert len(buns) == 3
    # Проверяем атрибуты первой и последней булочки
    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100
    assert buns[-1].get_name() == "red bun"
    assert buns[-1].get_price() == 300

def test_available_ingredients(db):
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    # Проверяем атрибуты первого и последнего ингредиента
    assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[0].get_price() == 100
    assert ingredients[-1].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[-1].get_name() == "sausage"
    assert ingredients[-1].get_price() == 300


