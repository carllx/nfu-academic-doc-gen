# How To: Multiple Date Col Timestamp Parse

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple date col timestamp parse

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

### Step 2: Assign data = '05/31/2012,15:30:00.029,1306.25,1,E,0,,1306.25\n05/31/2012,15:30:00.029,1306.25,8,E,0,,1306.25'

```python
data = '05/31/2012,15:30:00.029,1306.25,1,E,0,,1306.25\n05/31/2012,15:30:00.029,1306.25,8,E,0,,1306.25'
```

### Step 3: Assign result = parser.read_csv_check_warnings(...)

```python
result = parser.read_csv_check_warnings(FutureWarning, "use 'date_format' instead", StringIO(data), parse_dates=[[0, 1]], header=None, date_parser=Timestamp, raise_on_extra_warnings=False)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[Timestamp('05/31/2012, 15:30:00.029'), 1306.25, 1, 'E', 0, np.nan, 1306.25], [Timestamp('05/31/2012, 15:30:00.029'), 1306.25, 8, 'E', 0, np.nan, 1306.25]], columns=['0_1', 2, 3, 4, 5, 6, 7])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '05/31/2012,15:30:00.029,1306.25,1,E,0,,1306.25\n05/31/2012,15:30:00.029,1306.25,8,E,0,,1306.25'
result = parser.read_csv_check_warnings(FutureWarning, "use 'date_format' instead", StringIO(data), parse_dates=[[0, 1]], header=None, date_parser=Timestamp, raise_on_extra_warnings=False)
expected = DataFrame([[Timestamp('05/31/2012, 15:30:00.029'), 1306.25, 1, 'E', 0, np.nan, 1306.25], [Timestamp('05/31/2012, 15:30:00.029'), 1306.25, 8, 'E', 0, np.nan, 1306.25]], columns=['0_1', 2, 3, 4, 5, 6, 7])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_parse_dates.py:562 | Complexity: Intermediate | Last updated: 2026-06-02*