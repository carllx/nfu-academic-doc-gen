# How To: Getitem Slice

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem slice

## Prerequisites

**Required Modules:**
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'd', 'a', 'b', 'c'])
```

**Verification:**
```python
assert sliced == 'd'
```

### Step 2: Assign sliced = value

```python
sliced = cat[3]
```

**Verification:**
```python
assert sliced == 'd'
```

### Step 3: Assign sliced = value

```python
sliced = cat[3:5]
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(['d', 'a'], categories=['a', 'b', 'c', 'd'])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(sliced, expected)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c', 'd', 'a', 'b', 'c'])
sliced = cat[3]
assert sliced == 'd'
sliced = cat[3:5]
expected = Categorical(['d', 'a'], categories=['a', 'b', 'c', 'd'])
tm.assert_categorical_equal(sliced, expected)
```

## Next Steps


---

*Source: test_indexing.py:124 | Complexity: Intermediate | Last updated: 2026-06-02*