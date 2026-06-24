# How To: Datetimeindex Tz Convert

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetimeindex tz convert

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign dt = date_range(...)

```python
dt = date_range('2019-12-31', periods=3, freq='D', tz='Europe/Berlin')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dt)
```

### Step 3: Assign idx = DatetimeIndex.tz_convert(...)

```python
idx = DatetimeIndex(ser).tz_convert('US/Eastern')
```

### Step 4: Assign expected = idx.copy(...)

```python
expected = idx.copy(deep=True)
```

### Step 5: Assign unknown = Timestamp(...)

```python
ser.iloc[0] = Timestamp('2020-12-31', tz='Europe/Berlin')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
dt = date_range('2019-12-31', periods=3, freq='D', tz='Europe/Berlin')
ser = Series(dt)
idx = DatetimeIndex(ser).tz_convert('US/Eastern')
expected = idx.copy(deep=True)
ser.iloc[0] = Timestamp('2020-12-31', tz='Europe/Berlin')
if using_copy_on_write:
    tm.assert_index_equal(idx, expected)
```

## Next Steps


---

*Source: test_datetimeindex.py:33 | Complexity: Intermediate | Last updated: 2026-06-02*