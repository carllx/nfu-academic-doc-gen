# How To: Constructor With Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor with dtype

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: ordered
```

## Step-by-Step Guide

### Step 1: Assign categories = value

```python
categories = ['b', 'a', 'c']
```

**Verification:**
```python
assert result.ordered is ordered
```

### Step 2: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(categories, ordered=ordered)
```

### Step 3: Assign result = Categorical(...)

```python
result = Categorical(['a', 'b', 'a', 'c'], dtype=dtype)
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(['a', 'b', 'a', 'c'], categories=categories, ordered=ordered)
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```

**Verification:**
```python
assert result.ordered is ordered
```


## Complete Example

```python
# Setup
# Fixtures: ordered

# Workflow
categories = ['b', 'a', 'c']
dtype = CategoricalDtype(categories, ordered=ordered)
result = Categorical(['a', 'b', 'a', 'c'], dtype=dtype)
expected = Categorical(['a', 'b', 'a', 'c'], categories=categories, ordered=ordered)
tm.assert_categorical_equal(result, expected)
assert result.ordered is ordered
```

## Next Steps


---

*Source: test_constructors.py:419 | Complexity: Intermediate | Last updated: 2026-06-02*