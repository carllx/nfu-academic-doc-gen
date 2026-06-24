# How To: Multiple Date Cols Int Cast

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple date cols int cast

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

### Step 1: Assign data = 'KORD,19990127, 19:00:00, 18:56:00, 0.8100\nKORD,19990127, 20:00:00, 19:56:00, 0.0100\nKORD,19990127, 21:00:00, 20:56:00, -0.5900\nKORD,19990127, 21:00:00, 21:18:00, -0.9900\nKORD,19990127, 22:00:00, 21:56:00, -0.5900\nKORD,19990127, 23:00:00, 22:56:00, -0.5900'

```python
data = 'KORD,19990127, 19:00:00, 18:56:00, 0.8100\nKORD,19990127, 20:00:00, 19:56:00, 0.0100\nKORD,19990127, 21:00:00, 20:56:00, -0.5900\nKORD,19990127, 21:00:00, 21:18:00, -0.9900\nKORD,19990127, 22:00:00, 21:56:00, -0.5900\nKORD,19990127, 23:00:00, 22:56:00, -0.5900'
```

### Step 2: Assign parse_dates = value

```python
parse_dates = {'actual': [1, 2], 'nominal': [1, 3]}
```

### Step 3: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 4: Assign kwds = value

```python
kwds = {'header': None, 'parse_dates': parse_dates, 'date_parser': pd.to_datetime}
```

### Step 5: Assign result = parser.read_csv_check_warnings(...)

```python
result = parser.read_csv_check_warnings(FutureWarning, "use 'date_format' instead", StringIO(data), **kwds, raise_on_extra_warnings=False)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[datetime(1999, 1, 27, 19, 0), datetime(1999, 1, 27, 18, 56), 'KORD', 0.81], [datetime(1999, 1, 27, 20, 0), datetime(1999, 1, 27, 19, 56), 'KORD', 0.01], [datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 20, 56), 'KORD', -0.59], [datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 21, 18), 'KORD', -0.99], [datetime(1999, 1, 27, 22, 0), datetime(1999, 1, 27, 21, 56), 'KORD', -0.59], [datetime(1999, 1, 27, 23, 0), datetime(1999, 1, 27, 22, 56), 'KORD', -0.59]], columns=['actual', 'nominal', 0, 4])
```

### Step 7: Assign result = value

```python
result = result[expected.columns]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
data = 'KORD,19990127, 19:00:00, 18:56:00, 0.8100\nKORD,19990127, 20:00:00, 19:56:00, 0.0100\nKORD,19990127, 21:00:00, 20:56:00, -0.5900\nKORD,19990127, 21:00:00, 21:18:00, -0.9900\nKORD,19990127, 22:00:00, 21:56:00, -0.5900\nKORD,19990127, 23:00:00, 22:56:00, -0.5900'
parse_dates = {'actual': [1, 2], 'nominal': [1, 3]}
parser = all_parsers
kwds = {'header': None, 'parse_dates': parse_dates, 'date_parser': pd.to_datetime}
result = parser.read_csv_check_warnings(FutureWarning, "use 'date_format' instead", StringIO(data), **kwds, raise_on_extra_warnings=False)
expected = DataFrame([[datetime(1999, 1, 27, 19, 0), datetime(1999, 1, 27, 18, 56), 'KORD', 0.81], [datetime(1999, 1, 27, 20, 0), datetime(1999, 1, 27, 19, 56), 'KORD', 0.01], [datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 20, 56), 'KORD', -0.59], [datetime(1999, 1, 27, 21, 0), datetime(1999, 1, 27, 21, 18), 'KORD', -0.99], [datetime(1999, 1, 27, 22, 0), datetime(1999, 1, 27, 21, 56), 'KORD', -0.59], [datetime(1999, 1, 27, 23, 0), datetime(1999, 1, 27, 22, 56), 'KORD', -0.59]], columns=['actual', 'nominal', 0, 4])
result = result[expected.columns]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:498 | Complexity: Advanced | Last updated: 2026-06-02*