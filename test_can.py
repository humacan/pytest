import pytest
from shopping import shopping

def test_can_add_item():
    cart=shopping(5)
    cart.add('apple')
    assert cart.size()==1

def test_when_item_added():
    cart=shopping(5)
    cart.add('apple')
    assert 'apple' in cart.get_items()

def test_when_Add_more_than_max():
    cart=shopping(5)
    for _ in range(5):
        cart.add('apple')
    
    with pytest.raises(OverflowError):
        cart.add('apple')    

def test_can_get_total_price():
    print("Testing can get price")
    # python -m pytest test_can.py::test_can_get_total_price
    # run specific 
    # python -m pytest test_can.py::test_can_get_total_price -s
    cart=shopping(5)
    cart.add('orange')
    cart.add('apple')

    price_map ={"apple": 1.0,"orange": 2.0}
    assert cart.get_total_price(price_map)==3.0      