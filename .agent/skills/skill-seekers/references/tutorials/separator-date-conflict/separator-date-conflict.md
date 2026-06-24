# How To: Separator Date Conflict

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test separator date conflict

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

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = '06-02-2013;13:00;1-000.215'

```python
data = '06-02-2013;13:00;1-000.215'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[datetime(2013, 6, 2, 13, 0, 0), 1000.215]], columns=['Date', 2])
```

### Step 4: Assign depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"

```python
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 6: Assign df = parser.read_csv(...)

```python
df = parser.read_csv(StringIO(data), sep=';', thousands='-', parse_dates={'Date': [0, 1]}, header=None)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '06-02-2013;13:00;1-000.215'
expected = DataFrame([[datetime(2013, 6, 2, 13, 0, 0), 1000.215]], columns=['Date', 2])
depr_msg = "Support for nested sequences for 'parse_dates' in pd.read_csv is deprecated"
with tm.assert_produces_warning(FutureWarning, match=depr_msg, check_stacklevel=False):
    df = parser.read_csv(StringIO(data), sep=';', thousands='-', parse_dates={'Date': [0, 1]}, header=None)
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*