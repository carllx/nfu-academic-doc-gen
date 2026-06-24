# How To: Constructor From Categorical With Unknown Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor from categorical with unknown dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(None, ordered=True)
```

### Step 2: Assign values = Categorical(...)

```python
values = Categorical(['a', 'b', 'd'])
```

### Step 3: Assign result = Categorical(...)

```python
result = Categorical(values, dtype=dtype)
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(['a', 'b', 'd'], categories=['a', 'b', 'd'], ordered=True)
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
dtype = CategoricalDtype(None, ordered=True)
values = Categorical(['a', 'b', 'd'])
result = Categorical(values, dtype=dtype)
expected = Categorical(['a', 'b', 'd'], categories=['a', 'b', 'd'], ordered=True)
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:472 | Complexity: Intermediate | Last updated: 2026-06-02*