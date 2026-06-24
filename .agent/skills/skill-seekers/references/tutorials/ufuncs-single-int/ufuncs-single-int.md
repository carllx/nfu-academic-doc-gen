# How To: Ufuncs Single Int

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufuncs single int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: ufunc
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([1, 2, -3, np.nan])
```

### Step 2: Assign result = ufunc(...)

```python
result = ufunc(a)
```

### Step 3: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a.astype(float)), dtype='Int64')
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 5: Assign s = pd.Series(...)

```python
s = pd.Series(a)
```

### Step 6: Assign result = ufunc(...)

```python
result = ufunc(s)
```

### Step 7: Assign expected = pd.Series(...)

```python
expected = pd.Series(pd.array(ufunc(a.astype(float)), dtype='Int64'))
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ufunc

# Workflow
a = pd.array([1, 2, -3, np.nan])
result = ufunc(a)
expected = pd.array(ufunc(a.astype(float)), dtype='Int64')
tm.assert_extension_array_equal(result, expected)
s = pd.Series(a)
result = ufunc(s)
expected = pd.Series(pd.array(ufunc(a.astype(float)), dtype='Int64'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_function.py:12 | Complexity: Advanced | Last updated: 2026-06-02*