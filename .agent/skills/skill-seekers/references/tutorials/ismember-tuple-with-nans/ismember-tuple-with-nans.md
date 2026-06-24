# How To: Ismember Tuple With Nans

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ismember tuple with nans

## Prerequisites

**Required Modules:**
- `collections.abc`
- `contextlib`
- `re`
- `struct`
- `tracemalloc`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = [('a', float('nan')), ('b', 1)]
```

### Step 2: Assign comps = value

```python
comps = [('a', float('nan'))]
```

### Step 3: Assign msg = 'isin with argument that is not not a Series'

```python
msg = 'isin with argument that is not not a Series'
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([True, False], dtype=np.bool_)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = isin(...)

```python
result = isin(values, comps)
```


## Complete Example

```python
# Workflow
values = [('a', float('nan')), ('b', 1)]
comps = [('a', float('nan'))]
msg = 'isin with argument that is not not a Series'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = isin(values, comps)
expected = np.array([True, False], dtype=np.bool_)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_hashtable.py:731 | Complexity: Intermediate | Last updated: 2026-06-02*