# How To: Get Loc Masked Na

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc masked na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_and_arrow_dtype
```

## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([1, 2, NA], dtype=any_numeric_ea_and_arrow_dtype)
```

**Verification:**
```python
assert result == 2
```

### Step 2: Assign result = idx.get_loc(...)

```python
result = idx.get_loc(NA)
```

**Verification:**
```python
assert result == 2
```

### Step 3: Assign idx = Index(...)

```python
idx = Index([1, 2, NA, NA], dtype=any_numeric_ea_and_arrow_dtype)
```

### Step 4: Assign result = idx.get_loc(...)

```python
result = idx.get_loc(NA)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, np.array([False, False, True, True]))
```

### Step 6: Assign idx = Index(...)

```python
idx = Index([1, 2, 3], dtype=any_numeric_ea_and_arrow_dtype)
```

### Step 7: Call idx.get_loc()

```python
idx.get_loc(NA)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_ea_and_arrow_dtype

# Workflow
idx = Index([1, 2, NA], dtype=any_numeric_ea_and_arrow_dtype)
result = idx.get_loc(NA)
assert result == 2
idx = Index([1, 2, NA, NA], dtype=any_numeric_ea_and_arrow_dtype)
result = idx.get_loc(NA)
tm.assert_numpy_array_equal(result, np.array([False, False, True, True]))
idx = Index([1, 2, 3], dtype=any_numeric_ea_and_arrow_dtype)
with pytest.raises(KeyError, match='NA'):
    idx.get_loc(NA)
```

## Next Steps


---

*Source: test_indexing.py:332 | Complexity: Intermediate | Last updated: 2026-06-02*