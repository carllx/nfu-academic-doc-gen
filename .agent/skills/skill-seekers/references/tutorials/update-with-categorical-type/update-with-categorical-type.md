# How To: Update With Categorical Type

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test update with categorical type

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(['a', 'b', 'c', 'd'])
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(['a', 'b', 'c'], index=[1, 2, 3], dtype=dtype)
```

### Step 3: Assign s2 = Series(...)

```python
s2 = Series(['b', 'a'], index=[1, 2], dtype=dtype)
```

### Step 4: Call s1.update()

```python
s1.update(s2)
```

### Step 5: Assign result = s1

```python
result = s1
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(['b', 'a', 'c'], index=[1, 2, 3], dtype=dtype)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
dtype = CategoricalDtype(['a', 'b', 'c', 'd'])
s1 = Series(['a', 'b', 'c'], index=[1, 2, 3], dtype=dtype)
s2 = Series(['b', 'a'], index=[1, 2], dtype=dtype)
s1.update(s2)
result = s1
expected = Series(['b', 'a', 'c'], index=[1, 2, 3], dtype=dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_update.py:135 | Complexity: Intermediate | Last updated: 2026-06-02*