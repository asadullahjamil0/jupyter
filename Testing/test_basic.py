from basicmath import div

def test_div():
    assert div(4, 2) == 2 

def test_div_2():
    assert div(15, 3) == 5

def test_div_3():
    assert div(1, 2) == 0.5

from basicmath import sortlist

def test_list():
    l = [12, 45, 77, 9, 8, 2, 1]
    sortetd_list = [1, 2, 8, 9, 12, 45, 77]

    assert sortlist(l) == sortetd_list