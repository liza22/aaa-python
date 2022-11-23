import io
import urllib.request
from unittest.mock import patch

import pytest

from what_is_year_now import what_is_year_now


def test_year_at_start():
    resp_stringio = io.StringIO("{\"currentDateTime\" : \"2022-11-16\"}")
    with patch.object(urllib.request, 'urlopen', return_value=resp_stringio):
        assert what_is_year_now() == 2022


def test_year_at_end():
    resp_stringio = io.StringIO("{\"currentDateTime\" : \"16.11.2022\"}")
    with patch.object(urllib.request, 'urlopen', return_value=resp_stringio):
        assert what_is_year_now() == 2022


def test_invalid():
    resp_stringio = io.StringIO("{\"currentDateTime\" : \"2022.11.16\"}")
    with patch.object(urllib.request, 'urlopen', return_value=resp_stringio):
        with pytest.raises(ValueError):
            what_is_year_now()
