# How To: Read Csv With Custom Date Parser

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv with custom date parser

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
testdata = StringIO('time e n h\n        41047.00 -98573.7297 871458.0640 389.0089\n        41048.00 -98573.7299 871458.0640 389.0089\n        41049.00 -98573.7300 871458.0642 389.0088\n        41050.00 -98573.7299 871458.0643 389.0088\n        41051.00 -98573.7302 871458.0640 389.0086\n        ')
```

### Step 2: Assign result = all_parsers.read_csv_check_warnings(...)

```python
result = all_parsers.read_csv_check_warnings(FutureWarning, "Please use 'date_format' instead", testdata, delim_whitespace=True, parse_dates=True, date_parser=__custom_date_parser, index_col='time')
```

### Step 3: Assign time = value

```python
time = [41047, 41048, 41049, 41050, 41051]
```

### Step 4: Assign time = pd.TimedeltaIndex(...)

```python
time = pd.TimedeltaIndex([pd.to_timedelta(i, unit='s') for i in time], name='time')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'e': [-98573.7297, -98573.7299, -98573.73, -98573.7299, -98573.7302], 'n': [871458.064, 871458.064, 871458.0642, 871458.0643, 871458.064], 'h': [389.0089, 389.0089, 389.0088, 389.0088, 389.0086]}, index=time)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign time = time.astype(...)

```python
time = time.astype(np.float64)
```

### Step 8: Assign time = time.astype(...)

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
testdata = StringIO('time e n h\n        41047.00 -98573.7297 871458.0640 389.0089\n        41048.00 -98573.7299 871458.0640 389.0089\n        41049.00 -98573.7300 871458.0642 389.0088\n        41050.00 -98573.7299 871458.0643 389.0088\n        41051.00 -98573.7302 871458.0640 389.0086\n        ')
result = all_parsers.read_csv_check_warnings(FutureWarning, "Please use 'date_format' instead", testdata, delim_whitespace=True, parse_dates=True, date_parser=__custom_date_parser, index_col='time')
time = [41047, 41048, 41049, 41050, 41051]
time = pd.TimedeltaIndex([pd.to_timedelta(i, unit='s') for i in time], name='time')
expected = DataFrame({'e': [-98573.7297, -98573.7299, -98573.73, -98573.7299, -98573.7302], 'n': [871458.064, 871458.064, 871458.0642, 871458.0643, 871458.064], 'h': [389.0089, 389.0089, 389.0088, 389.0088, 389.0086]}, index=time)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:45 | Complexity: Advanced | Last updated: 2026-06-02*