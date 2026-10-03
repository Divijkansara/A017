from calculator import calculate_total, calculate_average, get_result

def test_calculate_total():
    assert calculate_total([40, 50, 60]) == 150

def test_calculate_average():
    assert calculate_average([40, 50, 60]) == 50

def test_get_result_pass():
    assert get_result([40, 50, 60]) == "PASS"

def test_get_result_fail():
    assert get_result([10, 20, 30]) == "FAIL"
