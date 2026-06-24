# How To: Reindex Nearest

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex nearest

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.arange(10, dtype='int64'))
```

### Step 2: Assign target = value

```python
target = [0.1, 0.9, 1.5, 2.0]
```

### Step 3: Assign result = s.reindex(...)

```python
result = s.reindex(target, method='nearest')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(np.around(target).astype('int64'), target)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 6: Assign result = s.reindex(...)

```python
result = s.reindex(target, method='nearest', tolerance=0.2)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([0, 1, np.nan, 2], target)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 9: Assign result = s.reindex(...)

```python
result = s.reindex(target, method='nearest', tolerance=[0.3, 0.01, 0.4, 3])
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([0, np.nan, np.nan, 2], target)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```


## Complete Example

```python
# Workflow
s = Series(np.arange(10, dtype='int64'))
target = [0.1, 0.9, 1.5, 2.0]
result = s.reindex(target, method='nearest')
expected = Series(np.around(target).astype('int64'), target)
tm.assert_series_equal(expected, result)
result = s.reindex(target, method='nearest', tolerance=0.2)
expected = Series([0, 1, np.nan, 2], target)
tm.assert_series_equal(expected, result)
result = s.reindex(target, method='nearest', tolerance=[0.3, 0.01, 0.4, 3])
expected = Series([0, np.nan, np.nan, 2], target)
tm.assert_series_equal(expected, result)
```

## Next Steps


---

*Source: test_reindex.py:172 | Complexity: Advanced | Last updated: 2026-06-02*