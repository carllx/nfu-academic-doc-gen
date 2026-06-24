# How To: Index Equal Category Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index equal category mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: check_categorical, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign msg = value

```python
msg = f"""Index are different\n\nAttribute "dtype" are different\n\\[left\\]:  CategoricalDtype\\(categories=\\['a', 'b'\\], ordered=False, categories_dtype={dtype}\\)\n\\[right\\]: CategoricalDtype\\(categories=\\['a', 'b', 'c'\\], ordered=False, categories_dtype={dtype}\\)"""
```

### Step 2: Assign idx1 = Index(...)

```python
idx1 = Index(Categorical(['a', 'b']))
```

### Step 3: Assign idx2 = Index(...)

```python
idx2 = Index(Categorical(['a', 'b'], categories=['a', 'b', 'c']))
```

### Step 4: Assign dtype = 'str'

```python
dtype = 'str'
```

### Step 5: Assign dtype = 'object'

```python
dtype = 'object'
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx1, idx2, check_categorical=check_categorical)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx1, idx2, check_categorical=check_categorical)
```


## Complete Example

```python
# Setup
# Fixtures: check_categorical, using_infer_string

# Workflow
if using_infer_string:
    dtype = 'str'
else:
    dtype = 'object'
msg = f"""Index are different\n\nAttribute "dtype" are different\n\\[left\\]:  CategoricalDtype\\(categories=\\['a', 'b'\\], ordered=False, categories_dtype={dtype}\\)\n\\[right\\]: CategoricalDtype\\(categories=\\['a', 'b', 'c'\\], ordered=False, categories_dtype={dtype}\\)"""
idx1 = Index(Categorical(['a', 'b']))
idx2 = Index(Categorical(['a', 'b'], categories=['a', 'b', 'c']))
if check_categorical:
    with pytest.raises(AssertionError, match=msg):
        tm.assert_index_equal(idx1, idx2, check_categorical=check_categorical)
else:
    tm.assert_index_equal(idx1, idx2, check_categorical=check_categorical)
```

## Next Steps


---

*Source: test_assert_index_equal.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*