# How To: Array Ufuncs For Many Arguments

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array ufuncs for many arguments

## Prerequisites

**Required Modules:**
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign ufunc = np.frompyfunc(...)

```python
ufunc = np.frompyfunc(add3, 3, 1)
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame([[1, 2], [3, 4]])
```

### Step 3: Assign result = ufunc(...)

```python
result = ufunc(df, df, 1)
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([[3, 5], [7, 9]], dtype=object)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign ser = pd.Series(...)

```python
ser = pd.Series([1, 2])
```

### Step 7: Assign msg = "Cannot apply ufunc <ufunc 'add3 (vectorized)'> to mixed DataFrame and Series inputs."

```python
msg = "Cannot apply ufunc <ufunc 'add3 (vectorized)'> to mixed DataFrame and Series inputs."
```

### Step 8: Call ufunc()

```python
ufunc(df, df, ser)
```


## Complete Example

```python
# Workflow
def add3(x, y, z):
    return x + y + z
ufunc = np.frompyfunc(add3, 3, 1)
df = pd.DataFrame([[1, 2], [3, 4]])
result = ufunc(df, df, 1)
expected = pd.DataFrame([[3, 5], [7, 9]], dtype=object)
tm.assert_frame_equal(result, expected)
ser = pd.Series([1, 2])
msg = "Cannot apply ufunc <ufunc 'add3 (vectorized)'> to mixed DataFrame and Series inputs."
with pytest.raises(NotImplementedError, match=re.escape(msg)):
    ufunc(df, df, ser)
```

## Next Steps


---

*Source: test_ufunc.py:293 | Complexity: Advanced | Last updated: 2026-06-02*