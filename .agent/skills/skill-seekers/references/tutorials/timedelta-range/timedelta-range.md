# How To: Timedelta Range

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timedelta range

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign expected = to_timedelta(...)

```python
expected = to_timedelta(np.arange(5), unit='D')
```

### Step 2: Assign result = timedelta_range(...)

```python
result = timedelta_range('0 days', periods=5, freq='D')
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign expected = to_timedelta(...)

```python
expected = to_timedelta(np.arange(11), unit='D')
```

### Step 5: Assign result = timedelta_range(...)

```python
result = timedelta_range('0 days', '10 days', freq='D')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign expected = value

```python
expected = to_timedelta(np.arange(5), unit='D') + Second(2) + Day()
```

### Step 8: Assign result = timedelta_range(...)

```python
result = timedelta_range('1 days, 00:00:02', '5 days, 00:00:02', freq='D')
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign expected = value

```python
expected = to_timedelta([1, 3, 5, 7, 9], unit='D') + Second(2)
```

### Step 11: Assign result = timedelta_range(...)

```python
result = timedelta_range('1 days, 00:00:02', periods=5, freq='2D')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 13: Assign expected = value

```python
expected = to_timedelta(np.arange(50), unit='min') * 30
```

### Step 14: Assign result = timedelta_range(...)

```python
result = timedelta_range('0 days', freq='30min', periods=50)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = to_timedelta(np.arange(5), unit='D')
result = timedelta_range('0 days', periods=5, freq='D')
tm.assert_index_equal(result, expected)
expected = to_timedelta(np.arange(11), unit='D')
result = timedelta_range('0 days', '10 days', freq='D')
tm.assert_index_equal(result, expected)
expected = to_timedelta(np.arange(5), unit='D') + Second(2) + Day()
result = timedelta_range('1 days, 00:00:02', '5 days, 00:00:02', freq='D')
tm.assert_index_equal(result, expected)
expected = to_timedelta([1, 3, 5, 7, 9], unit='D') + Second(2)
result = timedelta_range('1 days, 00:00:02', periods=5, freq='2D')
tm.assert_index_equal(result, expected)
expected = to_timedelta(np.arange(50), unit='min') * 30
result = timedelta_range('0 days', freq='30min', periods=50)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta_range.py:25 | Complexity: Advanced | Last updated: 2026-06-02*