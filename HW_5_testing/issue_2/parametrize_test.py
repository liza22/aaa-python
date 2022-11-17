import pytest
from morse import decode


@pytest.mark.parametrize(
    "message, result",
    [
        ("... --- ...", "SOS"),
        ("-..-. - .- ... -.- ..--- ..--..", "/TASK2?"),
        ("-.--. .---- --..-- ..--- --..-- ...-- -.--.-", "(1, 2, 3)"),
    ],
)
def test_decode(message, result):
    assert decode(message) == result
