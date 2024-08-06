import pytest
from praktikum.database import Database

@pytest.fixture
def db():
    """Фикстура для базы данных."""
    return Database()

