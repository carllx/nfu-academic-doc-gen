# How To: Series Equal Categorical Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series equal categorical mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: check_categorical, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign msg = value

```python
msg = f"""Attributes of Series are different\n\nAttribute "dtype" are different\n\\[left\\]:  CategoricalDtype\\(categories=\\['a', 'b'\\], ordered=False, categories_dtype={dtype}\\)\n\\[right\\]: CategoricalDtype\\(categories=\\['a', 'b', 'c'\\], ordered=False, categories_dtype={dtype}\\)"""
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(Categorical(['a', 'b']))
```

### Step 3: Assign s2 = Series(...)

```python
s2 = Series(Categorical(['a', 'b'], categories=list('abc')))
```

### Step 4: Assign dtype = 'str'

```python
dtype = 'str'
```

### Step 5: Assign dtype = 'object'

```python
dtype = 'object'
```

### Step 6: Call _assert_series_equal_both()

```python
_assert_series_equal_both(s1, s2, check_categorical=check_categorical)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1, s2, check_categorical=check_categorical)
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
msg = f"""Attributes of Series are different\n\nAttribute "dtype" are different\n\\[left\\]:  CategoricalDtype\\(categories=\\['a', 'b'\\], ordered=False, categories_dtype={dtype}\\)\n\\[right\\]: CategoricalDtype\\(categories=\\['a', 'b', 'c'\\], ordered=False, categories_dtype={dtype}\\)"""
s1 = Series(Categorical(['a', 'b']))
s2 = Series(Categorical(['a', 'b'], categories=list('abc')))
if check_categorical:
    with pytest.raises(AssertionError, match=msg):
        tm.assert_series_equal(s1, s2, check_categorical=check_categorical)
else:
    _assert_series_equal_both(s1, s2, check_categorical=check_categorical)
```

## Next Steps


---

*Source: test_assert_series_equal.py:250 | Complexity: Intermediate | Last updated: 2026-06-02*