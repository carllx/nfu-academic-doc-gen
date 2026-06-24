# How To: Constructor From Categorical String

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor from categorical string

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

### Step 1: Assign values = Categorical(...)

```python
values = Categorical(['a', 'b', 'd'])
```

### Step 2: Assign result = Categorical(...)

```python
result = Categorical(values, categories=['a', 'b', 'c'], ordered=True, dtype='category')
```

### Step 3: Assign expected = Categorical(...)

```python
expected = Categorical(['a', 'b', 'd'], categories=['a', 'b', 'c'], ordered=True)
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

### Step 5: Assign result = Categorical(...)

```python
result = Categorical(values, categories=['a', 'b', 'c'], ordered=True)
```

### Step 6: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
values = Categorical(['a', 'b', 'd'])
result = Categorical(values, categories=['a', 'b', 'c'], ordered=True, dtype='category')
expected = Categorical(['a', 'b', 'd'], categories=['a', 'b', 'c'], ordered=True)
tm.assert_categorical_equal(result, expected)
result = Categorical(values, categories=['a', 'b', 'c'], ordered=True)
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:482 | Complexity: Intermediate | Last updated: 2026-06-02*