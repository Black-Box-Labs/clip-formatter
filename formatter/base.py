import datetime
from collections.abc import Callable

import dateparser
import numpy as np
import pandas as pd


class BaseFormatter:
    def __init__(self) -> None:
        pass

    def _apply_not_nan(
        self, series: pd.Series, function: Callable, **kwargs: dict
    ) -> pd.Series:
        return series.apply(
            lambda series_value: function(series_value, **kwargs)
            if (not pd.isnull(series_value))
            else np.nan
        )

    def date(
        self,
        raw_date: pd.Series,
        output_format: str = "%d-%m-%Y",
        return_original: bool = False,
        **kwargs: dict,
    ) -> pd.Series:
        # Converting to timestamp
        date = self._apply_not_nan(raw_date, dateparser.parse, **kwargs)
        parsed_date = self._apply_not_nan(
            date, datetime.datetime.strftime, format=output_format
        )
        if return_original:
            return pd.DataFrame({"date": parsed_date, "org_date": date})
        return parsed_date.fillna(raw_date)
