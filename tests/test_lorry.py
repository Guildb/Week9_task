import pytest
from Lorry import Lorry


def test_create_lorry():
    vehicle = Lorry("abc", 7000)
    assert vehicle.weight == 7000
    assert vehicle.registration == "abc"
    assert vehicle.calculatefee() == 10


def test_lorry_free_over_weigh():
    vehicle = Lorry("abc", 9000)
    assert vehicle.calculatefee() == 15
