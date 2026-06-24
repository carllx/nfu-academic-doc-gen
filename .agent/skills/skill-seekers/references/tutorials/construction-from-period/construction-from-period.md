# How To: Construction From Period

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction from period

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
start, end = (Period('2017Q1', freq='Q'), Period('2018Q1', freq='Q'))
```

### Step 2: Assign expected = date_range.to_period(...)

```python
expected = date_range(start='2017-03-31', end='2018-03-31', freq='ME', name='foo').to_period()
```

### Step 3: Assign result = period_range(...)

```python
result = period_range(start=start, end=end, freq='M', name='foo')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign start = Period(...)

```python
start = Period('2017-1', freq='M')
```

### Step 6: Assign end = Period(...)

```python
end = Period('2019-12', freq='M')
```

### Step 7: Assign expected = date_range.to_period(...)

```python
expected = date_range(start='2017-01-31', end='2019-12-31', freq='QE', name='foo').to_period()
```

### Step 8: Assign result = period_range(...)

```python
result = period_range(start=start, end=end, freq='Q', name='foo')
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign start = Period(...)

```python
start = Period('2017Q1', freq='Q')
```

### Step 11: Assign end = Period(...)

```python
end = Period('2018Q1', freq='Q')
```

### Step 12: Assign idx = period_range(...)

```python
idx = period_range(start=start, end=end, freq='Q', name='foo')
```

### Step 13: Assign result = value

```python
result = idx == idx.values
```

### Step 14: Assign expected = np.array(...)

```python
expected = np.array([True, True, True, True, True])
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 16: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex([], freq='W', name='foo')
```

### Step 17: Assign result = period_range(...)

```python
result = period_range(start=start, periods=0, freq='W', name='foo')
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 19: Assign result = period_range(...)

```python
result = period_range(end=end, periods=0, freq='W', name='foo')
```

### Step 20: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 21: Assign result = period_range(...)

```python
result = period_range(start=end, end=start, freq='W', name='foo')
```

### Step 22: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
start, end = (Period('2017Q1', freq='Q'), Period('2018Q1', freq='Q'))
expected = date_range(start='2017-03-31', end='2018-03-31', freq='ME', name='foo').to_period()
result = period_range(start=start, end=end, freq='M', name='foo')
tm.assert_index_equal(result, expected)
start = Period('2017-1', freq='M')
end = Period('2019-12', freq='M')
expected = date_range(start='2017-01-31', end='2019-12-31', freq='QE', name='foo').to_period()
result = period_range(start=start, end=end, freq='Q', name='foo')
tm.assert_index_equal(result, expected)
start = Period('2017Q1', freq='Q')
end = Period('2018Q1', freq='Q')
idx = period_range(start=start, end=end, freq='Q', name='foo')
result = idx == idx.values
expected = np.array([True, True, True, True, True])
tm.assert_numpy_array_equal(result, expected)
expected = PeriodIndex([], freq='W', name='foo')
result = period_range(start=start, periods=0, freq='W', name='foo')
tm.assert_index_equal(result, expected)
result = period_range(end=end, periods=0, freq='W', name='foo')
tm.assert_index_equal(result, expected)
result = period_range(start=end, end=start, freq='W', name='foo')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_period_range.py:144 | Complexity: Advanced | Last updated: 2026-06-02*