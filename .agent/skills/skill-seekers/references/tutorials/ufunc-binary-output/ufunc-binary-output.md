# How To: Ufunc Binary Output

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ufunc binary output

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([1, 2, np.nan])
```

**Verification:**
```python
assert isinstance(result, tuple)
```

### Step 2: Assign result = np.modf(...)

```python
result = np.modf(a)
```

**Verification:**
```python
assert len(result) == 2
```

### Step 3: Assign expected = np.modf(...)

```python
expected = np.modf(a.to_numpy(na_value=np.nan, dtype='float'))
```

### Step 4: Assign expected = value

```python
expected = (pd.array(expected[0]), pd.array(expected[1]))
```

**Verification:**
```python
assert isinstance(result, tuple)
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(x, y)
```


## Complete Example

```python
# Workflow
a = pd.array([1, 2, np.nan])
result = np.modf(a)
expected = np.modf(a.to_numpy(na_value=np.nan, dtype='float'))
expected = (pd.array(expected[0]), pd.array(expected[1]))
assert isinstance(result, tuple)
assert len(result) == 2
for x, y in zip(result, expected):
    tm.assert_extension_array_equal(x, y)
```

## Next Steps


---

*Source: test_function.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*