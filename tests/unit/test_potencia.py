import pytest
from src.operations.potencia import potencia


def test_potencia_n_cero():
    assert potencia(0, 0) == 1.0


def test_potencia_n_fraccion():
    assert potencia(16, 0.25) == 2.0


def test_potencia_n_entera():
    assert potencia(10, -2.0) == 0.01
