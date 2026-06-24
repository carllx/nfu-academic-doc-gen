# How To: Repr Range Categories

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr range categories

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign rng = pd.Index(...)

```python
rng = pd.Index(range(3))
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(categories=rng, ordered=False)
```

### Step 3: Assign result = repr(...)

```python
result = repr(dtype)
```

### Step 4: Assign expected = 'CategoricalDtype(categories=range(0, 3), ordered=False, categories_dtype=int64)'

```python
expected = 'CategoricalDtype(categories=range(0, 3), ordered=False, categories_dtype=int64)'
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
rng = pd.Index(range(3))
dtype = CategoricalDtype(categories=rng, ordered=False)
result = repr(dtype)
expected = 'CategoricalDtype(categories=range(0, 3), ordered=False, categories_dtype=int64)'
assert result == expected
```

## Next Steps


---

*Source: test_dtypes.py:211 | Complexity: Intermediate | Last updated: 2026-06-02*