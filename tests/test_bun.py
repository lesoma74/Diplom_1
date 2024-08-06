import pytest
from tests.test_data import BUN_TEST_DATA

def test_available_buns(db):
    buns = db.available_buns()
    # Проверка на количество булочек
    assert len(buns) == len(BUN_TEST_DATA)

@pytest.mark.parametrize("name, price", BUN_TEST_DATA)
def test_bun_properties(db, name, price):
    buns = db.available_buns()
    # Поиск булочки по имени
    bun = next((b for b in buns if b.get_name() == name), None)
    assert bun is not None
    # Проверка имени и цены булочки
    assert bun.get_name() == name
    assert bun.get_price() == price
