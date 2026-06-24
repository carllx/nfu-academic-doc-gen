# How To: To Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to series

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


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

### Step 4: Assign result = idx.to_series(...)

```python
result = idx.to_series(index=[0, 1])
```

**Verification:**
```python
assert expected.dtype == idx.dtype
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
result = idx.to_series(index=[0, 1])
assert expected.dtype == idx.dtype
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_to_series.py:11 | Complexity: Intermediate | Last updated: 2026-06-02*