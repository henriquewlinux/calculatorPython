from calculator import *

def test_somar():
    x = 5
    y = 2
    expected = 7
    actual = somar(x,y)
    assert actual == expected

def test_somar_valor_negativo():
    x = 5
    y = -9
    expectd = -4
    actual = somar(x,y)
    assert actual == expectd
    

def test_subtrair():
    x = 2
    y = 1
    expectd = 1
    actual = subtrair(x,y)
    assert actual == expectd

def test_subtrair_valor_negativo():
    x = 2
    y = -5
    expectd = 7
    actual = subtrair(x,y)
    assert actual == expectd

def test_dividir():
    x = 2
    y = 10
    expected = 0.2
    actual = dividir(x,y)
    assert actual == expected

def test_dividir_zero():
    x = 10
    y = 0
    expected = "Erro: Divisao por zero"
    actual = dividir(x,y)
    assert actual == expected

def test_multiplicar():
    x = 5
    y = 3
    expected = 15
    actual = multiplicar(x,y)
    assert actual == expected