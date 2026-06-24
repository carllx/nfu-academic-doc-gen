# How To: Update Dtype

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test update dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: ordered, new_categories, new_ordered
```

## Step-by-Step Guide

### Step 1: Assign original_categories = list(...)

```python
original_categories = list('abc')
```

**Verification:**
```python
assert result.ordered is expected_ordered
```

### Step 2: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(original_categories, ordered)
```

### Step 3: Assign new_dtype = CategoricalDtype(...)

```python
new_dtype = CategoricalDtype(new_categories, new_ordered)
```

### Step 4: Assign result = dtype.update_dtype(...)

```python
result = dtype.update_dtype(new_dtype)
```

### Step 5: Assign expected_categories = pd.Index(...)

```python
expected_categories = pd.Index(new_categories or original_categories)
```

### Step 6: Assign expected_ordered = value

```python
expected_ordered = new_ordered if new_ordered is not None else dtype.ordered
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.categories, expected_categories)
```

**Verification:**
```python
assert result.ordered is expected_ordered
```


## Complete Example

```python
# Setup
# Fixtures: ordered, new_categories, new_ordered

# Workflow
original_categories = list('abc')
dtype = CategoricalDtype(original_categories, ordered)
new_dtype = CategoricalDtype(new_categories, new_ordered)
result = dtype.update_dtype(new_dtype)
expected_categories = pd.Index(new_categories or original_categories)
expected_ordered = new_ordered if new_ordered is not None else dtype.ordered
tm.assert_index_equal(result.categories, expected_categories)
assert result.ordered is expected_ordered
```

## Next Steps


---

*Source: test_dtypes.py:1080 | Complexity: Intermediate | Last updated: 2026-06-02*