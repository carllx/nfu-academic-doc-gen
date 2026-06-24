# How To: Alignment

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test alignment

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign x = Series(...)

```python
x = Series(data=[1, 2, 3], index=MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 3)]))
```

### Step 2: Assign y = Series(...)

```python
y = Series(data=[4, 5, 6], index=MultiIndex.from_tuples([('Z', 1), ('Z', 2), ('B', 3)]))
```

### Step 3: Assign res = value

```python
res = x - y
```

### Step 4: Assign exp_index = x.index.union(...)

```python
exp_index = x.index.union(y.index)
```

### Step 5: Assign exp = value

```python
exp = x.reindex(exp_index) - y.reindex(exp_index)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 7: Assign res = value

```python
res = x[::-1] - y[::-1]
```

### Step 8: Assign exp_index = x.index.union(...)

```python
exp_index = x.index.union(y.index)
```

### Step 9: Assign exp = value

```python
exp = x.reindex(exp_index) - y.reindex(exp_index)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
x = Series(data=[1, 2, 3], index=MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 3)]))
y = Series(data=[4, 5, 6], index=MultiIndex.from_tuples([('Z', 1), ('Z', 2), ('B', 3)]))
res = x - y
exp_index = x.index.union(y.index)
exp = x.reindex(exp_index) - y.reindex(exp_index)
tm.assert_series_equal(res, exp)
res = x[::-1] - y[::-1]
exp_index = x.index.union(y.index)
exp = x.reindex(exp_index) - y.reindex(exp_index)
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_multilevel.py:131 | Complexity: Advanced | Last updated: 2026-06-02*