# How To: Multiple Output Binary Ufuncs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multiple output binary ufuncs

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
# Fixtures: ufunc, sparse, shuffle, arrays_for_binary_ufunc
```

## Step-by-Step Guide

### Step 1: Assign unknown = arrays_for_binary_ufunc

```python
a1, a2 = arrays_for_binary_ufunc
```

**Verification:**
```python
assert isinstance(expected, tuple)
```

### Step 2: Assign unknown = 1

```python
a1[a1 == 0] = 1
```

**Verification:**
```python
assert isinstance(result, tuple)
```

### Step 3: Assign unknown = 1

```python
a2[a2 == 0] = 1
```

### Step 4: Assign s1 = pd.Series(...)

```python
s1 = pd.Series(a1)
```

### Step 5: Assign s2 = pd.Series(...)

```python
s2 = pd.Series(a2)
```

### Step 6: Assign expected = ufunc(...)

```python
expected = ufunc(a1, a2)
```

**Verification:**
```python
assert isinstance(expected, tuple)
```

### Step 7: Assign result = ufunc(...)

```python
result = ufunc(s1, s2)
```

**Verification:**
```python
assert isinstance(result, tuple)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[0], pd.Series(expected[0]))
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[1], pd.Series(expected[1]))
```

### Step 10: Assign a1 = SparseArray(...)

```python
a1 = SparseArray(a1, dtype=pd.SparseDtype('int64', 0))
```

### Step 11: Assign a2 = SparseArray(...)

```python
a2 = SparseArray(a2, dtype=pd.SparseDtype('int64', 0))
```

### Step 12: Assign s2 = s2.sample(...)

```python
s2 = s2.sample(frac=1)
```


## Complete Example

```python
# Setup
# Fixtures: ufunc, sparse, shuffle, arrays_for_binary_ufunc

# Workflow
a1, a2 = arrays_for_binary_ufunc
a1[a1 == 0] = 1
a2[a2 == 0] = 1
if sparse:
    a1 = SparseArray(a1, dtype=pd.SparseDtype('int64', 0))
    a2 = SparseArray(a2, dtype=pd.SparseDtype('int64', 0))
s1 = pd.Series(a1)
s2 = pd.Series(a2)
if shuffle:
    s2 = s2.sample(frac=1)
expected = ufunc(a1, a2)
assert isinstance(expected, tuple)
result = ufunc(s1, s2)
assert isinstance(result, tuple)
tm.assert_series_equal(result[0], pd.Series(expected[0]))
tm.assert_series_equal(result[1], pd.Series(expected[1]))
```

## Next Steps


---

*Source: test_ufunc.py:176 | Complexity: Advanced | Last updated: 2026-06-02*