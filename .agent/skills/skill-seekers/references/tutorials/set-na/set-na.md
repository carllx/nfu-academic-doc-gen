# How To: Set Na

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: left_right_dtypes
```

## Step-by-Step Guide

### Step 1: Assign unknown = left_right_dtypes

```python
left, right = left_right_dtypes
```

### Step 2: Assign left = left.copy(...)

```python
left = left.copy(deep=True)
```

### Step 3: Assign right = right.copy(...)

```python
right = right.copy(deep=True)
```

### Step 4: Assign result = IntervalArray.from_arrays(...)

```python
result = IntervalArray.from_arrays(left, right)
```

### Step 5: Assign unknown = value

```python
result[0] = np.nan
```

### Step 6: Assign expected_left = Index(...)

```python
expected_left = Index([left._na_value] + list(left[1:]))
```

### Step 7: Assign expected_right = Index(...)

```python
expected_right = Index([right._na_value] + list(right[1:]))
```

### Step 8: Assign expected = IntervalArray.from_arrays(...)

```python
expected = IntervalArray.from_arrays(expected_left, expected_right)
```

### Step 9: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 10: Assign msg = "'value' should be an interval type, got <.*NaTType'> instead."

```python
msg = "'value' should be an interval type, got <.*NaTType'> instead."
```

### Step 11: Assign msg = 'Cannot set float NaN to integer-backed IntervalArray'

```python
msg = 'Cannot set float NaN to integer-backed IntervalArray'
```

### Step 12: Assign unknown = value

```python
result[0] = pd.NaT
```

### Step 13: Assign unknown = value

```python
result[0] = np.nan
```


## Complete Example

```python
# Setup
# Fixtures: left_right_dtypes

# Workflow
left, right = left_right_dtypes
left = left.copy(deep=True)
right = right.copy(deep=True)
result = IntervalArray.from_arrays(left, right)
if result.dtype.subtype.kind not in ['m', 'M']:
    msg = "'value' should be an interval type, got <.*NaTType'> instead."
    with pytest.raises(TypeError, match=msg):
        result[0] = pd.NaT
if result.dtype.subtype.kind in ['i', 'u']:
    msg = 'Cannot set float NaN to integer-backed IntervalArray'
    with pytest.raises(TypeError, match=msg):
        result[0] = np.nan
    return
result[0] = np.nan
expected_left = Index([left._na_value] + list(left[1:]))
expected_right = Index([right._na_value] + list(right[1:]))
expected = IntervalArray.from_arrays(expected_left, expected_right)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_interval.py:117 | Complexity: Advanced | Last updated: 2026-06-02*