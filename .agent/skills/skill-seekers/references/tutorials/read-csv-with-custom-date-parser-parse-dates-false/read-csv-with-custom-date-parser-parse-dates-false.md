# How To: Read Csv With Custom Date Parser Parse Dates False

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv with custom date parser parse dates false

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `dateutil.parser`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.tools.datetimes`
- `pandas.io.parsers`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign testdata = StringIO(...)

```python
testdata = StringIO('time e\n        41047.00 -93.77\n        41048.00 -95.79\n        41049.00 -98.73\n        41050.00 -93.99\n        41051.00 -97.72\n        ')
```

### Step 2: Assign result = all_parsers.read_csv_check_warnings(...)

```python
result = all_parsers.read_csv_check_warnings(FutureWarning, "Please use 'date_format' instead", testdata, delim_whitespace=True, parse_dates=False, date_parser=__custom_date_parser, index_col='time')
```

### Step 3: Assign time = Series(...)

```python
time = Series([41047.0, 41048.0, 41049.0, 41050.0, 41051.0], name='time')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'e': [-93.77, -95.79, -98.73, -93.99, -97.72]}, index=time)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign time = time.astype(...)

```python
time = time.astype(np.float64)
```

### Step 7: Assign time = time.astype(...)

```python
time = time.astype(int)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
def __custom_date_parser(time):
    time = time.astype(np.float64)
    time = time.astype(int)
    return pd.to_timedelta(time, unit='s')
testdata = StringIO('time e\n        41047.00 -93.77\n        41048.00 -95.79\n        41049.00 -98.73\n        41050.00 -93.99\n        41051.00 -97.72\n        ')
result = all_parsers.read_csv_check_warnings(FutureWarning, "Please use 'date_format' instead", testdata, delim_whitespace=True, parse_dates=False, date_parser=__custom_date_parser, index_col='time')
time = Series([41047.0, 41048.0, 41049.0, 41050.0, 41051.0], name='time')
expected = DataFrame({'e': [-93.77, -95.79, -98.73, -93.99, -97.72]}, index=time)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*