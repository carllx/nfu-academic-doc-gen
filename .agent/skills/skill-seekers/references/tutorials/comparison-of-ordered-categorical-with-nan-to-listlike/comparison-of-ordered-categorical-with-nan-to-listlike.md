# How To: Comparison Of Ordered Categorical With Nan To Listlike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comparison of ordered categorical with nan to listlike

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
# Fixtures: compare_operators_no_eq_ne
```

## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical([1, 2, 3, None], categories=[1, 2, 3], ordered=True)
```

### Step 2: Assign other = Categorical(...)

```python
other = Categorical([2, 2, 2, 2], categories=[1, 2, 3], ordered=True)
```

### Step 3: Assign expected = getattr(...)

```python
expected = getattr(np.array(cat), compare_operators_no_eq_ne)(2)
```

### Step 4: Assign actual = getattr(...)

```python
actual = getattr(cat, compare_operators_no_eq_ne)(other)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: compare_operators_no_eq_ne

# Workflow
cat = Categorical([1, 2, 3, None], categories=[1, 2, 3], ordered=True)
other = Categorical([2, 2, 2, 2], categories=[1, 2, 3], ordered=True)
expected = getattr(np.array(cat), compare_operators_no_eq_ne)(2)
actual = getattr(cat, compare_operators_no_eq_ne)(other)
tm.assert_numpy_array_equal(actual, expected)
```

## Next Steps


---

*Source: test_operators.py:228 | Complexity: Intermediate | Last updated: 2026-06-02*