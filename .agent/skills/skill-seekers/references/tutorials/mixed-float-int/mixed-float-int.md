# How To: Mixed Float Int

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: mixed int/float left/right results in float for both sides

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: 'mixed int/float left/right results in float for both sides'

```python
'mixed int/float left/right results in float for both sides'
```

**Verification:**
```python
assert result.dtype.subtype == expected_subtype
```

### Step 2: Assign left = np.arange(...)

```python
left = np.arange(9, dtype=left_subtype)
```

### Step 3: Assign right = np.arange(...)

```python
right = np.arange(1, 10, dtype=right_subtype)
```

### Step 4: Assign result = IntervalIndex.from_arrays(...)

```python
result = IntervalIndex.from_arrays(left, right)
```

### Step 5: Assign expected_left = Index(...)

```python
expected_left = Index(left, dtype=np.float64)
```

### Step 6: Assign expected_right = Index(...)

```python
expected_right = Index(right, dtype=np.float64)
```

### Step 7: Assign expected_subtype = value

```python
expected_subtype = np.float64
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.left, expected_left)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.right, expected_right)
```

**Verification:**
```python
assert result.dtype.subtype == expected_subtype
```


## Complete Example

```python
# Workflow
'mixed int/float left/right results in float for both sides'
left = np.arange(9, dtype=left_subtype)
right = np.arange(1, 10, dtype=right_subtype)
result = IntervalIndex.from_arrays(left, right)
expected_left = Index(left, dtype=np.float64)
expected_right = Index(right, dtype=np.float64)
expected_subtype = np.float64
tm.assert_index_equal(result.left, expected_left)
tm.assert_index_equal(result.right, expected_right)
assert result.dtype.subtype == expected_subtype
```

## Next Steps


---

*Source: test_constructors.py:248 | Complexity: Advanced | Last updated: 2026-06-02*