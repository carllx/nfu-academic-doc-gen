# How To: Constructor From 2D Datetimearray

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor from 2d datetimearray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `array`
- `collections`
- `collections.abc`
- `dataclasses`
- `datetime`
- `functools`
- `re`
- `numpy`
- `numpy`
- `numpy.ma`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `numpy.dtypes`

**Setup Required:**
```python
# Fixtures: using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=6, tz='US/Pacific')
```

**Verification:**
```python
assert len(df._mgr.blocks) == 1
```

### Step 2: Assign dta = dti._data.reshape(...)

```python
dta = dti._data.reshape(3, 2)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(dta)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: dta[:, 0], 1: dta[:, 1]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

**Verification:**
```python
assert len(df._mgr.blocks) == 1
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager

# Workflow
dti = date_range('2016-01-01', periods=6, tz='US/Pacific')
dta = dti._data.reshape(3, 2)
df = DataFrame(dta)
expected = DataFrame({0: dta[:, 0], 1: dta[:, 1]})
tm.assert_frame_equal(df, expected)
if not using_array_manager:
    assert len(df._mgr.blocks) == 1
```

## Next Steps


---

*Source: test_constructors.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*