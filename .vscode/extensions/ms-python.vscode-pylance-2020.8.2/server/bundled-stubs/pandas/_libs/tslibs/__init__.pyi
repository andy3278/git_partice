from __future__ import annotations
from .nattype import is_null_datetimelike as is_null_datetimelike, nat_strings as nat_strings
from .dtypes import Resolution as Resolution
from .vectorized import (
    get_resolution as get_resolution,
    ints_to_pydatetime as ints_to_pydatetime,
    dt64arr_to_periodarr as dt64arr_to_periodarr,
    is_date_array_normalized as is_date_array_normalized,
    normalize_i8_timestamps as normalize_i8_timestamps)
from .tzconversion import tz_convert_from_utc_single as tz_convert_from_utc_single
from .offsets import to_offset as to_offset, SingleConstructorOffset
from .conversion import localize_pydatetime as localize_pydatetime, OutOfBoundsTimedelta as OutOfBoundsTimedelta
from .np_datetime import OutOfBoundsDatetime as OutOfBoundsDatetime
from .period import IncompatibleFrequency as IncompatibleFrequency
from .timedeltas import delta_to_nanoseconds as delta_to_nanoseconds, ints_to_pytimedelta as ints_to_pytimedelta

import datetime
import numpy as _np
from typing import Any, Mapping, Optional, Tuple, Union

_Scalar = Union[str, bytes, datetime.date, datetime.datetime, datetime.timedelta, bool, int, float, complex]

#class OutOfBoundsDatetime(OutOfBoundsDatetime): ...
class NullFrequencyError: ...
class BaseOffset: ...
class NaT: ...
NaTType = type(NaT)
iNaT: int = ...

class Period(object):
    def __init__(
        self,
        value: Any = ...,
        freqstr: Any = ...,
        ordinal: Any = ...,
        year: Any = ...,
        month: int = ...,
        quarter: Any = ...,
        day: int = ...,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
    ) -> None: ...
    @property
    def day(self) -> int: ...
    @property
    def dayofweek(self) -> int: ...
    @property
    def dayofyear(self) -> int: ...
    @property
    def days_in_month(self) -> int: ...
    @property
    def end_time(self) -> Timestamp: ...
    @property
    def freq(self) -> Any: ...
    @property
    def freqstr(self) -> str: ...
    @property
    def hour(self) -> int: ...
    @property
    def is_leap_year(self) -> bool: ...
    @property
    def minute(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def ordinal(self) -> int: ...
    @property
    def quarter(self) -> int: ...
    @property
    def qyear(self) -> int: ...
    @property
    def second(self) -> int: ...
    @property
    def start_time(self) -> Timestamp: ...
    @property
    def week(self) -> int: ...
    @property
    def weekday(self) -> int: ...
    @property
    def weekofyear(self) -> int: ...
    @property
    def year(self) -> int: ...
    # Static methods
    @staticmethod
    def now() -> Period: ...
    # Methods
    def asfreq(self, freq: str, how: str = ...) -> Period: ...
    def strftime(self, fmt: str) -> str: ...
    def to_timestamp(self, freq: str, how: str = ...) -> Timestamp: ...


class Interval(object):
    def __init__(self, left: _Scalar, right: _Scalar, closed: str = ...): ...
    @property
    def closed(self) -> bool: ...
    @property
    def closed_left(self) -> bool: ...
    @property
    def closed_right(self) -> bool: ...
    @property
    def is_empty(self) -> bool: ...
    @property
    def left(self) -> _Scalar: ...
    @property
    def length(self) -> _Scalar: ...
    @property
    def mid(self) -> _Scalar: ...
    @property
    def open_left(self) -> bool: ...
    @property
    def open_right(self) -> bool: ...
    @property
    def right(self) -> _Scalar: ...
    # Methods
    def overlaps(self, other: Interval) -> bool: ...


class Timedelta(object):
    def __init__(self, value: Any, unit: str = ..., **kwargs) -> None: ...
    @property
    def asm8(self) -> int: ...
    @property
    def components(self) -> int: ...
    @property
    def days(self) -> int: ...
    @property
    def delta(self) -> int: ...
    @property
    def microseconds(self) -> int: ...
    @property
    def nanoseconds(self) -> int: ...
    @property
    def resolution_string(self) -> str: ...
    @property
    def seconds(self) -> int: ...
    max: Timedelta = ...
    min: Timedelta = ...
    resolution: 'Timedelta' = ...
    def ceil(self, freq, **kwargs) -> Timedelta: ...
    def floor(self, freq, **kwargs) -> Timedelta: ...
    def isoformat(self) -> str: ...
    def round(self, freq) -> Timedelta: ...
    def to_numpy(self) -> _np.timedelta64: ...
    def to_pytimedelta(self) -> datetime.timedelta: ...
    def to_timedelta64(self) -> _np.timedelta64: ...
    def total_seconds(self) -> int: ...

class Timestamp(object):
    def __init__(
        self,
        ts_input: Any,
        freq: Any,
        tz: Any,
        unit: str,
        year: int,
        month: int,
        day: int,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        microsecond: int = ...,
        nanosecond: int = ...,
        tzinfo: Any = ...,
    ): ...
    # Still need to do parameter types
    @property
    def asm8(self) -> int: ...
    @property
    def dayofweek(self) -> int: ...
    @property
    def dayofyear(self) -> int: ...
    @property
    def daysinmonth(self) -> int: ...
    @property
    def days_in_month(self) -> int: ...
    @property
    def freqstr(self) -> int: ...
    @property
    def is_leap_year(self) -> bool: ...
    @property
    def is_month_end(self) -> bool: ...
    @property
    def is_month_start(self) -> bool: ...
    @property
    def is_quarter_end(self) -> bool: ...
    @property
    def is_quarter_start(self) -> bool: ...
    @property
    def is_year_end(self) -> bool: ...
    @property
    def is_year_start(self) -> int: ...
    @property
    def quarter(self) -> int: ...
    @property
    def tz(self) -> Any: ...
    @property
    def week(self) -> int: ...
    @property
    def weekofyear(self) -> int: ...
    # Class methods
    @staticmethod
    def combine(date, time) -> Timestamp: ...
    @staticmethod
    def fromordinal(ordinal: int, freq: Any = ..., tz: Any = ...) -> Timestamp: ...
    @staticmethod
    def fromtimestamp(ts) -> Timestamp: ...
    @staticmethod
    def now(tz: Any) -> Timestamp: ...
    @staticmethod
    def today(tz: Any) -> Timestamp: ...
    @staticmethod
    def utcfromtimestamp(ts) -> Timestamp: ...
    @staticmethod
    def utcnow() -> Timestamp: ...
    # Methods
    def astimezone(self, tz: Any) -> Timestamp: ...
    def ceil(self, freq: str, ambiguous: str = ..., nonexistent: str = ...) -> Timestamp: ...
    def ctime(self) -> str: ...
    def date(self) -> Any: ...
    def day_name(self, local: Optional[str] = ...) -> str: ...
    def dst(self) -> Timestamp: ...
    def floor(self, freq: str, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def fromisoformat(self) -> Any: ...
    def isocalendar(self) -> Tuple[int, int, int]: ...
    def isoweekday(self) -> int: ...
    def monthname(self, local: Any) -> str: ...
    def normalize(self) -> None: ...
    def replace(
        self,
        year: Optional[int] = ...,
        month: Optional[int] = ...,
        day: Optional[int] = ...,
        hour: Optional[int] = ...,
        minute: Optional[int] = ...,
        second: Optional[int] = ...,
        microsecond: Optional[int] = ...,
        nanosecond: Optional[int] = ...,
        tzinfo: Any = ...,
        fold: int = ...,
    ) -> Timestamp: ...
    def round(self, freq: str, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def strftime(self) -> str: ...
    def time(self) -> Timestamp: ...
    def timestamp(self) -> float: ...
    def timetuple(self) -> Tuple: ...
    def timetz(self) -> Timestamp: ...
    def to_datetime64(self) -> _np.datetime64: ...
    def to_julian_date(self) -> Any: ...
    def to_numpy(self) -> _np.datetime64: ...
    def to_period(self, freq: Optional[str] = ...) -> Any: ...
    def to_pydatetime(self) -> datetime.datetime: ...
    def toordinal(self) -> Any: ...
    def tz_convert(self, tz: Any) -> Timestamp: ...
    def tz_localize(self, tz: Any, ambiguous: Any = ..., nonexistent: Any = ...) -> Timestamp: ...
    def tzname(self) -> str: ...
    def utcoffset(self) -> Any: ...
    def utctimetuple(self) -> Any: ...
    def weekday(self) -> int: ...

class Tick(SingleConstructorOffset):
    __array_priority__: int
    def __init__(self, n: int = ..., normalize: bool = ...) -> None: ...
    @property
    def delta(self) -> int: ...
    @property
    def nanos(self) -> int: ...
    def is_on_offset(self, dt: datetime.datetime) -> bool: ...
    def is_anchored(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __mul__(self, other) -> Tick: ...
    def __truediv__(self, other) -> Tick: ...
    def __add__(self, other) -> Tick: ...
    def apply(self, other) -> Any: ...
    def __setstate__(self, state: Mapping) -> None: ...

class Day(Tick): ...
class Hour(Tick): ...
class Minute(Tick): ...
class Second(Tick): ...
class Milli(Tick): ...
class Micro(Tick): ...
class Nano(Tick): ...

def delta_to_tick(delta: datetime.timedelta) -> Tick: ...

