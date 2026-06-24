# How To: Cast 1D Array Like From Scalar Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cast 1d array like from scalar categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cats = value

```python
cats = ['a', 'b', 'c']
```

### Step 2: Assign cat_type = CategoricalDtype(...)

```python
cat_type = CategoricalDtype(categories=cats, ordered=False)
```

### Step 3: Assign expected = Categorical(...)

```python
expected = Categorical(['a', 'a'], categories=cats)
```

### Step 4: Assign result = construct_1d_arraylike_from_scalar(...)

```python
result = construct_1d_arraylike_from_scalar('a', len(expected), cat_type)
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
cats = ['a', 'b', 'c']
cat_type = CategoricalDtype(categories=cats, ordered=False)
expected = Categorical(['a', 'a'], categories=cats)
result = construct_1d_arraylike_from_scalar('a', len(expected), cat_type)
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_construct_from_scalar.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*