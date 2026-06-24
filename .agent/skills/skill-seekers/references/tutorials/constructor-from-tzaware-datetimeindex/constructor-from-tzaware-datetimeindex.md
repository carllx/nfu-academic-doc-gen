# How To: Constructor From Tzaware Datetimeindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor from tzaware datetimeindex

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign naive = DatetimeIndex(...)

```python
naive = DatetimeIndex(['2013-1-1 13:00', '2013-1-2 14:00'], name='B')
```

**Verification:**
```python
assert expected.dtype == idx.dtype
```

### Step 2: Assign idx = naive.tz_localize(...)

```python
idx = naive.tz_localize('US/Pacific')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(np.array(idx.tolist(), dtype='object'), name='B')
```

**Verification:**
```python
assert expected.dtype == idx.dtype
```

### Step 4: Assign result = Series(...)

```python
result = Series(idx)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
naive = DatetimeIndex(['2013-1-1 13:00', '2013-1-2 14:00'], name='B')
idx = naive.tz_localize('US/Pacific')
expected = Series(np.array(idx.tolist(), dtype='object'), name='B')
assert expected.dtype == idx.dtype
result = Series(idx)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:126 | Complexity: Intermediate | Last updated: 2026-06-02*