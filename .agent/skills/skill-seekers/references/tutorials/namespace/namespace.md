# How To: Namespace

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test namespace

## Prerequisites

**Required Modules:**
- `pandas._libs`


## Step-by-Step Guide

### Step 1: Assign submodules = value

```python
submodules = ['base', 'ccalendar', 'conversion', 'dtypes', 'fields', 'nattype', 'np_datetime', 'offsets', 'parsing', 'period', 'strptime', 'vectorized', 'timedeltas', 'timestamps', 'timezones', 'tzconversion']
```

**Verification:**
```python
assert set(names) == expected
```

### Step 2: Assign api = value

```python
api = ['BaseOffset', 'NaT', 'NaTType', 'iNaT', 'nat_strings', 'OutOfBoundsDatetime', 'OutOfBoundsTimedelta', 'Period', 'IncompatibleFrequency', 'Resolution', 'Tick', 'Timedelta', 'dt64arr_to_periodarr', 'Timestamp', 'is_date_array_normalized', 'ints_to_pydatetime', 'normalize_i8_timestamps', 'get_resolution', 'delta_to_nanoseconds', 'ints_to_pytimedelta', 'localize_pydatetime', 'tz_convert_from_utc', 'tz_convert_from_utc_single', 'to_offset', 'tz_compare', 'is_unitless', 'astype_overflowsafe', 'get_unit_from_dtype', 'periods_per_day', 'periods_per_second', 'guess_datetime_format', 'add_overflowsafe', 'get_supported_dtype', 'is_supported_dtype']
```

### Step 3: Assign expected = set(...)

```python
expected = set(submodules + api)
```

### Step 4: Assign names = value

```python
names = [x for x in dir(tslibs) if not x.startswith('__')]
```

**Verification:**
```python
assert set(names) == expected
```


## Complete Example

```python
# Workflow
submodules = ['base', 'ccalendar', 'conversion', 'dtypes', 'fields', 'nattype', 'np_datetime', 'offsets', 'parsing', 'period', 'strptime', 'vectorized', 'timedeltas', 'timestamps', 'timezones', 'tzconversion']
api = ['BaseOffset', 'NaT', 'NaTType', 'iNaT', 'nat_strings', 'OutOfBoundsDatetime', 'OutOfBoundsTimedelta', 'Period', 'IncompatibleFrequency', 'Resolution', 'Tick', 'Timedelta', 'dt64arr_to_periodarr', 'Timestamp', 'is_date_array_normalized', 'ints_to_pydatetime', 'normalize_i8_timestamps', 'get_resolution', 'delta_to_nanoseconds', 'ints_to_pytimedelta', 'localize_pydatetime', 'tz_convert_from_utc', 'tz_convert_from_utc_single', 'to_offset', 'tz_compare', 'is_unitless', 'astype_overflowsafe', 'get_unit_from_dtype', 'periods_per_day', 'periods_per_second', 'guess_datetime_format', 'add_overflowsafe', 'get_supported_dtype', 'is_supported_dtype']
expected = set(submodules + api)
names = [x for x in dir(tslibs) if not x.startswith('__')]
assert set(names) == expected
```

## Next Steps


---

*Source: test_api.py:6 | Complexity: Intermediate | Last updated: 2026-06-02*