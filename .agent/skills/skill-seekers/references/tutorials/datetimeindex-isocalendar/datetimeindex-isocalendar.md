# How To: Datetimeindex Isocalendar

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetimeindex isocalendar

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
dt = date_range('2019-12-31', periods=3, freq='D')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dt)
```

### Step 3: Assign df = DatetimeIndex.isocalendar(...)

```python
df = DatetimeIndex(ser).isocalendar()
```

### Step 4: Assign expected = df.index.copy(...)

```python
expected = df.index.copy(deep=True)
```

### Step 5: Assign unknown = Timestamp(...)

```python
ser.iloc[0] = Timestamp('2020-12-31')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
dt = date_range('2019-12-31', periods=3, freq='D')
ser = Series(dt)
df = DatetimeIndex(ser).isocalendar()
expected = df.index.copy(deep=True)
ser.iloc[0] = Timestamp('2020-12-31')
if using_copy_on_write:
    tm.assert_index_equal(df.index, expected)
```

## Next Steps


---

*Source: test_datetimeindex.py:53 | Complexity: Intermediate | Last updated: 2026-06-02*