# How To: Get Indexer Datetime

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer datetime

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ii = IntervalIndex.from_breaks(...)

```python
ii = IntervalIndex.from_breaks(date_range('2018-01-01', periods=4))
```

### Step 2: Assign target = DatetimeIndex(...)

```python
target = DatetimeIndex(['2018-01-02'], dtype='M8[ns]')
```

### Step 3: Assign result = ii.get_indexer(...)

```python
result = ii.get_indexer(target)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = ii.get_indexer(...)

```python
result = ii.get_indexer(target.astype(str))
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign result = ii.get_indexer(...)

```python
result = ii.get_indexer(target.asi8)
```

### Step 9: Assign expected = np.array(...)

```python
expected = np.array([-1], dtype=np.intp)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
ii = IntervalIndex.from_breaks(date_range('2018-01-01', periods=4))
target = DatetimeIndex(['2018-01-02'], dtype='M8[ns]')
result = ii.get_indexer(target)
expected = np.array([0], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
result = ii.get_indexer(target.astype(str))
tm.assert_numpy_array_equal(result, expected)
result = ii.get_indexer(target.asi8)
expected = np.array([-1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:367 | Complexity: Advanced | Last updated: 2026-06-02*