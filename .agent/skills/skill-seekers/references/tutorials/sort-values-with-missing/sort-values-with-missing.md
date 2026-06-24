# How To: Sort Values With Missing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sort values with missing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_with_missing, na_position, request
```

## Step-by-Step Guide

### Step 1: Assign missing_count = np.sum(...)

```python
missing_count = np.sum(index_with_missing.isna())
```

### Step 2: Assign not_na_vals = value

```python
not_na_vals = index_with_missing[index_with_missing.notna()].values
```

### Step 3: Assign sorted_values = np.sort(...)

```python
sorted_values = np.sort(not_na_vals)
```

### Step 4: Assign expected = type(...)

```python
expected = type(index_with_missing)(sorted_values, dtype=index_with_missing.dtype)
```

### Step 5: Assign result = index_with_missing.sort_values(...)

```python
result = index_with_missing.sort_values(na_position=na_position)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='missing value sorting order not well-defined', strict=False))
```

### Step 8: Assign sorted_values = np.concatenate(...)

```python
sorted_values = np.concatenate([[None] * missing_count, sorted_values])
```

### Step 9: Assign sorted_values = np.concatenate(...)

```python
sorted_values = np.concatenate([sorted_values, [None] * missing_count])
```


## Complete Example

```python
# Setup
# Fixtures: index_with_missing, na_position, request

# Workflow
if isinstance(index_with_missing, CategoricalIndex):
    request.applymarker(pytest.mark.xfail(reason='missing value sorting order not well-defined', strict=False))
missing_count = np.sum(index_with_missing.isna())
not_na_vals = index_with_missing[index_with_missing.notna()].values
sorted_values = np.sort(not_na_vals)
if na_position == 'first':
    sorted_values = np.concatenate([[None] * missing_count, sorted_values])
else:
    sorted_values = np.concatenate([sorted_values, [None] * missing_count])
expected = type(index_with_missing)(sorted_values, dtype=index_with_missing.dtype)
result = index_with_missing.sort_values(na_position=na_position)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_common.py:459 | Complexity: Advanced | Last updated: 2026-06-02*