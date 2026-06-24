# How To: Numpy Array Equal Copy Flag

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numpy array equal copy flag

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: other_type, check_same
```

## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3])
```

### Step 2: Assign msg = None

```python
msg = None
```

### Step 3: Assign other = a.view(...)

```python
other = a.view()
```

### Step 4: Assign other = a.copy(...)

```python
other = a.copy()
```

### Step 5: Assign msg = value

```python
msg = 'array\\(\\[1, 2, 3\\]\\) is not array\\(\\[1, 2, 3\\]\\)' if check_same == 'same' else 'array\\(\\[1, 2, 3\\]\\) is array\\(\\[1, 2, 3\\]\\)'
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(a, other, check_same=check_same)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(a, other, check_same=check_same)
```


## Complete Example

```python
# Setup
# Fixtures: other_type, check_same

# Workflow
a = np.array([1, 2, 3])
msg = None
if other_type == 'same':
    other = a.view()
else:
    other = a.copy()
if check_same != other_type:
    msg = 'array\\(\\[1, 2, 3\\]\\) is not array\\(\\[1, 2, 3\\]\\)' if check_same == 'same' else 'array\\(\\[1, 2, 3\\]\\) is array\\(\\[1, 2, 3\\]\\)'
if msg is not None:
    with pytest.raises(AssertionError, match=msg):
        tm.assert_numpy_array_equal(a, other, check_same=check_same)
else:
    tm.assert_numpy_array_equal(a, other, check_same=check_same)
```

## Next Steps


---

*Source: test_assert_numpy_array_equal.py:160 | Complexity: Intermediate | Last updated: 2026-06-02*