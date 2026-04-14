import pytest
from main import main

@pytest.mark.timeout(5)
def test_main():
    assert main() == 8