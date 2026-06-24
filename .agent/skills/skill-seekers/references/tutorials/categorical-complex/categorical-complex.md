# How To: Categorical Complex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical complex

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

### Step 1: Assign result = Categorical(...)

```python
result = Categorical([1, 2 + 2j])
```

### Step 2: Assign expected = Categorical(...)

```python
expected = Categorical([1.0 + 0j, 2.0 + 2j])
```

### Step 3: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 4: Assign result = Categorical(...)

```python
result = Categorical([1, 2, 2 + 2j])
```

### Step 5: Assign expected = Categorical(...)

```python
expected = Categorical([1.0 + 0j, 2.0 + 0j, 2.0 + 2j])
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
result = Categorical([1, 2 + 2j])
expected = Categorical([1.0 + 0j, 2.0 + 2j])
tm.assert_categorical_equal(result, expected)
result = Categorical([1, 2, 2 + 2j])
expected = Categorical([1.0 + 0j, 2.0 + 0j, 2.0 + 2j])
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_dtypes.py:1216 | Complexity: Intermediate | Last updated: 2026-06-02*