# How To: Equals Matching Nas

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equals matching nas

## Prerequisites

**Required Modules:**
- `contextlib`
- `copy`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = Series(...)

```python
left = Series([np.datetime64('NaT')], dtype=object)
```

**Verification:**
```python
assert left.equals(right)
```

### Step 2: Assign right = Series(...)

```python
right = Series([np.datetime64('NaT')], dtype=object)
```

**Verification:**
```python
assert Index(left).equals(Index(right))
```

### Step 3: Assign left = Series(...)

```python
left = Series([np.timedelta64('NaT')], dtype=object)
```

**Verification:**
```python
assert left.array.equals(right.array)
```

### Step 4: Assign right = Series(...)

```python
right = Series([np.timedelta64('NaT')], dtype=object)
```

**Verification:**
```python
assert left.equals(right)
```

### Step 5: Assign left = Series(...)

```python
left = Series([np.float64('NaN')], dtype=object)
```

**Verification:**
```python
assert Index(left).equals(Index(right))
```

### Step 6: Assign right = Series(...)

```python
right = Series([np.float64('NaN')], dtype=object)
```

**Verification:**
```python
assert left.array.equals(right.array)
```


## Complete Example

```python
# Workflow
left = Series([np.datetime64('NaT')], dtype=object)
right = Series([np.datetime64('NaT')], dtype=object)
assert left.equals(right)
with tm.assert_produces_warning(FutureWarning, match='Dtype inference'):
    assert Index(left).equals(Index(right))
assert left.array.equals(right.array)
left = Series([np.timedelta64('NaT')], dtype=object)
right = Series([np.timedelta64('NaT')], dtype=object)
assert left.equals(right)
with tm.assert_produces_warning(FutureWarning, match='Dtype inference'):
    assert Index(left).equals(Index(right))
assert left.array.equals(right.array)
left = Series([np.float64('NaN')], dtype=object)
right = Series([np.float64('NaN')], dtype=object)
assert left.equals(right)
assert Index(left, dtype=left.dtype).equals(Index(right, dtype=right.dtype))
assert left.array.equals(right.array)
```

## Next Steps


---

*Source: test_equals.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*