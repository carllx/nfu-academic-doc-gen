# How To: Numpy Array Equal Identical Na

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy array equal identical na

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
# Fixtures: nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([nulls_fixture], dtype=object)
```

### Step 2: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(a, a)
```

### Step 3: Assign b = np.array(...)

```python
b = np.array([other], dtype=object)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(a, b)
```

### Step 5: Assign other = nulls_fixture.copy(...)

```python
other = nulls_fixture.copy()
```

### Step 6: Assign other = copy.copy(...)

```python
other = copy.copy(nulls_fixture)
```


## Complete Example

```python
# Setup
# Fixtures: nulls_fixture

# Workflow
a = np.array([nulls_fixture], dtype=object)
tm.assert_numpy_array_equal(a, a)
if hasattr(nulls_fixture, 'copy'):
    other = nulls_fixture.copy()
else:
    other = copy.copy(nulls_fixture)
b = np.array([other], dtype=object)
tm.assert_numpy_array_equal(a, b)
```

## Next Steps


---

*Source: test_assert_numpy_array_equal.py:198 | Complexity: Intermediate | Last updated: 2026-06-02*