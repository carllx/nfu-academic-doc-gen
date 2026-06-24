# How To: Map Same Length Inference Bug

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map same length inference bug

## Prerequisites

**Required Modules:**
- `collections`
- `decimal`
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 2])
```

### Step 2: Assign s = Series(...)

```python
s = Series([1, 2, 3])
```

### Step 3: Assign result = s.map(...)

```python
result = s.map(f)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([(1, 2), (2, 3), (3, 4)])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign s = Series(...)

```python
s = Series(['foo,bar'])
```

### Step 7: Assign result = s.map(...)

```python
result = s.map(lambda x: x.split(','))
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([('foo', 'bar')])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series([1, 2])

def f(x):
    return (x, x + 1)
s = Series([1, 2, 3])
result = s.map(f)
expected = Series([(1, 2), (2, 3), (3, 4)])
tm.assert_series_equal(result, expected)
s = Series(['foo,bar'])
result = s.map(lambda x: x.split(','))
expected = Series([('foo', 'bar')])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_map.py:59 | Complexity: Advanced | Last updated: 2026-06-02*