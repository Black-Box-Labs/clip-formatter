import datetime

import numpy as np
import pandas as pd
import pytest

from formatter.base import BaseFormatter


@pytest.fixture
def formatter():
    return BaseFormatter()


def test_date_standard_format(formatter):
    raw_dates = pd.Series(["2024-03-22", "01/01/2020", "15-08-2019"])
    expected = pd.Series(["22-03-2024", "01-01-2020", "15-08-2019"])
    result = formatter.date(raw_dates)
    pd.testing.assert_series_equal(result, expected)


def test_date_custom_format(formatter):
    raw_dates = pd.Series(["2024-03-22", "01/01/2020", "15-08-2019"])
    expected = pd.Series(["2024/03/22", "2020/01/01", "2019/08/15"])
    result = formatter.date(raw_dates, output_format="%Y/%m/%d")
    pd.testing.assert_series_equal(result, expected)


def test_date_invalid_values(formatter):
    raw_dates = pd.Series(["not_a_date", "32/01/2020", None, ""])
    expected = pd.Series(["not_a_date", "32/01/2020", np.nan, ""])
    result = formatter.date(raw_dates)
    pd.testing.assert_series_equal(result, expected)


def test_date_mixed_lenguages(formatter):
    raw_dates = pd.Series(["2024-03-22", "22 de Marzo de 2024", "22 de jun 2023", "March 14, 2022"])
    expected = pd.Series(["22-03-2024", "22-03-2024", "22-06-2023", "14-03-2022"])
    dates_kwargs = {
        'languages': ['es', 'en'],
    }
    result = formatter.date(raw_dates, **dates_kwargs)
    pd.testing.assert_series_equal(result, expected)


def test_date_mixed_formats(formatter):
    raw_dates = pd.Series(
        ["2024-03-22", "March 22, 2024", "22nd Mar 2024", "2024/03/22"]
    )
    expected = pd.Series(["22-03-2024", "22-03-2024", "22-03-2024", "22-03-2024"])
    result = formatter.date(raw_dates)
    pd.testing.assert_series_equal(result, expected)
