# How To: Binary Ufunc Other Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test binary ufunc other types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `re`
- `string`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: type_
```

## Step-by-Step Guide

### Step 1: Assign a = pd.Series(...)

```python
a = pd.Series([1, 2, 3], name='name')
```

### Step 2: Assign b = type_(...)

```python
b = type_([3, 4, 5])
```

### Step 3: Assign result = np.add(...)

```python
result = np.add(a, b)
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series(np.add(a.to_numpy(), b), name='name')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: type_

# Workflow
a = pd.Series([1, 2, 3], name='name')
b = type_([3, 4, 5])
result = np.add(a, b)
expected = pd.Series(np.add(a.to_numpy(), b), name='name')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:384 | Complexity: Intermediate | Last updated: 2026-06-02*