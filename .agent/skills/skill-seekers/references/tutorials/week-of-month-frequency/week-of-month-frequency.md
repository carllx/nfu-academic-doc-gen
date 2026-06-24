# How To: Week Of Month Frequency

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test week of month frequency

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign d1 = date(...)

```python
d1 = date(2002, 9, 1)
```

### Step 2: Assign d2 = date(...)

```python
d2 = date(2013, 10, 27)
```

### Step 3: Assign d3 = date(...)

```python
d3 = date(2012, 9, 30)
```

### Step 4: Assign idx1 = DatetimeIndex(...)

```python
idx1 = DatetimeIndex([d1, d2])
```

### Step 5: Assign idx2 = DatetimeIndex(...)

```python
idx2 = DatetimeIndex([d3])
```

### Step 6: Assign result_append = idx1.append(...)

```python
result_append = idx1.append(idx2)
```

### Step 7: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([d1, d2, d3])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result_append, expected)
```

### Step 9: Assign result_union = idx1.union(...)

```python
result_union = idx1.union(idx2)
```

### Step 10: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([d1, d3, d2])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result_union, expected)
```


## Complete Example

```python
# Workflow
d1 = date(2002, 9, 1)
d2 = date(2013, 10, 27)
d3 = date(2012, 9, 30)
idx1 = DatetimeIndex([d1, d2])
idx2 = DatetimeIndex([d3])
result_append = idx1.append(idx2)
expected = DatetimeIndex([d1, d2, d3])
tm.assert_index_equal(result_append, expected)
result_union = idx1.union(idx2)
expected = DatetimeIndex([d1, d3, d2])
tm.assert_index_equal(result_union, expected)
```

## Next Steps


---

*Source: test_datetime.py:47 | Complexity: Advanced | Last updated: 2026-06-02*