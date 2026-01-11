import pytest

@pytest.fixture(scope="module", autouse=True) 
#module runs once per module, were function runs once per function, module and class run once per class 
#autouse makes it run without being called
#session would run once per test execution
def test_inicialcheck():
    print("Inicial check complete.")
    return True

def test_example_1(test_inicialcheck):
    print("Running test example 1.")
    assert test_inicialcheck is True