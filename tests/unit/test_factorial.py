import pytest
from src.operations.factorial import factorial


def test_factorial_x_positivo():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_x_negativo():
    with pytest.raises(ValueError) as excinfo:
        factorial(-3)
    assert str(excinfo.value) == "Factorial no definido para números negativos"
