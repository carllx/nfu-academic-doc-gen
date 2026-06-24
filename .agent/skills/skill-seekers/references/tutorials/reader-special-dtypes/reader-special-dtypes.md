# How To: Reader Special Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reader special dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `io`
- `os`
- `pathlib`
- `platform`
- `re`
- `urllib.error`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `s3fs`
- `py.path`
- `pyarrow`
- `pandas.arrays`
- `xlrd`
- `xlrd`
- `python_calamine`
- `python_calamine`

**Setup Required:**
```python
# Fixtures: request, engine, read_ext
```

## Step-by-Step Guide

### Step 1: Call xfail_datetimes_with_pyxlsb()

```python
xfail_datetimes_with_pyxlsb(engine, request)
```

### Step 2: Assign unit = get_exp_unit(...)

```python
unit = get_exp_unit(read_ext, engine)
```

### Step 3: Assign expected = DataFrame.from_dict(...)

```python
expected = DataFrame.from_dict({'IntCol': [1, 2, -3, 4, 0], 'FloatCol': [1.25, 2.25, 1.83, 1.92, 5e-10], 'BoolCol': [True, False, True, True, False], 'StrCol': [1, 2, 3, 4, 5], 'Str2Col': ['a', 3, 'c', 'd', 'e'], 'DateCol': Index([datetime(2013, 10, 30), datetime(2013, 10, 31), datetime(1905, 1, 1), datetime(2013, 12, 14), datetime(2015, 3, 14)], dtype=f'M8[{unit}]')})
```

### Step 4: Assign basename = 'test_types'

```python
basename = 'test_types'
```

### Step 5: Assign actual = pd.read_excel(...)

```python
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```

### Step 7: Assign float_expected = expected.copy(...)

```python
float_expected = expected.copy()
```

### Step 8: Assign unknown = 3.0

```python
float_expected.loc[float_expected.index[1], 'Str2Col'] = 3.0
```

### Step 9: Assign actual = pd.read_excel(...)

```python
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, float_expected)
```

### Step 11: Assign unknown = unknown.apply(...)

```python
expected['StrCol'] = expected['StrCol'].apply(str)
```

### Step 12: Assign actual = pd.read_excel(...)

```python
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1', converters={'StrCol': str})
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, expected)
```

### Step 14: Assign actual = pd.read_excel(...)

```python
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1', index_col=icol)
```

### Step 15: Assign exp = expected.set_index(...)

```python
exp = expected.set_index(name)
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(actual, exp)
```


## Complete Example

```python
# Setup
# Fixtures: request, engine, read_ext

# Workflow
xfail_datetimes_with_pyxlsb(engine, request)
unit = get_exp_unit(read_ext, engine)
expected = DataFrame.from_dict({'IntCol': [1, 2, -3, 4, 0], 'FloatCol': [1.25, 2.25, 1.83, 1.92, 5e-10], 'BoolCol': [True, False, True, True, False], 'StrCol': [1, 2, 3, 4, 5], 'Str2Col': ['a', 3, 'c', 'd', 'e'], 'DateCol': Index([datetime(2013, 10, 30), datetime(2013, 10, 31), datetime(1905, 1, 1), datetime(2013, 12, 14), datetime(2015, 3, 14)], dtype=f'M8[{unit}]')})
basename = 'test_types'
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1')
tm.assert_frame_equal(actual, expected)
float_expected = expected.copy()
float_expected.loc[float_expected.index[1], 'Str2Col'] = 3.0
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1')
tm.assert_frame_equal(actual, float_expected)
for icol, name in enumerate(expected.columns):
    actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1', index_col=icol)
    exp = expected.set_index(name)
    tm.assert_frame_equal(actual, exp)
expected['StrCol'] = expected['StrCol'].apply(str)
actual = pd.read_excel(basename + read_ext, sheet_name='Sheet1', converters={'StrCol': str})
tm.assert_frame_equal(actual, expected)
```

## Next Steps


---

*Source: test_readers.py:453 | Complexity: Advanced | Last updated: 2026-06-02*