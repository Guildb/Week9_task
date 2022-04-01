import pytest
from Car import Car


def test_create_car():
    vehicle = Car("abc", 1500)
    assert vehicle.weight == 1500
    assert vehicle.registration == "abc"
    assert vehicle.calculatefee() == 5


def test_car_fee():
    vehicle = Car("abc", 2000)
    assert vehicle.calculatefee() == 5.4


