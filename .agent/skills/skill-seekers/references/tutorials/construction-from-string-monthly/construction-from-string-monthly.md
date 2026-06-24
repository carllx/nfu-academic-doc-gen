# How To: Construction From String Monthly

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction from string monthly

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = date_range.to_period(...)

```python
expected = date_range(start='2017-01-01', periods=5, freq='ME', name='foo').to_period()
```

### Step 2: Assign unknown = value

```python
start, end = (str(expected[0]), str(expected[-1]))
```

### Step 3: Assign result = period_range(...)

```python
result = period_range(start=start, end=end, freq='M', name='foo')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = period_range(...)

```python
result = period_range(start=start, periods=5, freq='M', name='foo')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign result = period_range(...)

```python
result = period_range(end=end, periods=5, freq='M', name='foo')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex([], freq='M', name='foo')
```

### Step 10: Assign result = period_range(...)

```python
result = period_range(start=start, periods=0, freq='M', name='foo')
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Assign result = period_range(...)

```python
result = period_range(end=end, periods=0, freq='M', name='foo')
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 14: Assign result = period_range(...)

```python
result = period_range(start=end, end=start, freq='M', name='foo')
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = date_range(start='2017-01-01', periods=5, freq='ME', name='foo').to_period()
start, end = (str(expected[0]), str(expected[-1]))
result = period_range(start=start, end=end, freq='M', name='foo')
tm.assert_index_equal(result, expected)
result = period_range(start=start, periods=5, freq='M', name='foo')
tm.assert_index_equal(result, expected)
result = period_range(end=end, periods=5, freq='M', name='foo')
tm.assert_index_equal(result, expected)
expected = PeriodIndex([], freq='M', name='foo')
result = period_range(start=start, periods=0, freq='M', name='foo')
tm.assert_index_equal(result, expected)
result = period_range(end=end, periods=0, freq='M', name='foo')
tm.assert_index_equal(result, expected)
result = period_range(start=end, end=start, freq='M', name='foo')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_period_range.py:116 | Complexity: Advanced | Last updated: 2026-06-02*