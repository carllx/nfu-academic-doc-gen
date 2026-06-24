# How To: Series Xs Droplevel False

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series xs droplevel false

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([('a', 'x'), ('a', 'y'), ('b', 'x')], names=['level1', 'level2'])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 1, 1], index=mi)
```

### Step 3: Assign result = ser.xs(...)

```python
result = ser.xs('a', axis=0, drop_level=False)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, 1], index=MultiIndex.from_tuples([('a', 'x'), ('a', 'y')], names=['level1', 'level2']))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([('a', 'x'), ('a', 'y'), ('b', 'x')], names=['level1', 'level2'])
ser = Series([1, 1, 1], index=mi)
result = ser.xs('a', axis=0, drop_level=False)
expected = Series([1, 1], index=MultiIndex.from_tuples([('a', 'x'), ('a', 'y')], names=['level1', 'level2']))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:59 | Complexity: Intermediate | Last updated: 2026-06-02*