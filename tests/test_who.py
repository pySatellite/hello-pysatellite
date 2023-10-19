from hello_pysatellite.who import my_name, lotto

def test_my_name():
    my_name()

def test_lotto():
    numbers = lotto()
    assert len(numbers) == 6

