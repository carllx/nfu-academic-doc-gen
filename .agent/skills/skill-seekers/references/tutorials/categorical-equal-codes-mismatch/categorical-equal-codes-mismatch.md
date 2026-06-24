# How To: Categorical Equal Codes Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical equal codes mismatch

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign categories = value

```python
categories = [1, 2, 3, 4]
```

### Step 2: Assign msg = 'Categorical\\.codes are different\n\nCategorical\\.codes values are different \\(50\\.0 %\\)\n\\[left\\]:  \\[0, 1, 3, 2\\]\n\\[right\\]: \\[0, 1, 2, 3\\]'

```python
msg = 'Categorical\\.codes are different\n\nCategorical\\.codes values are different \\(50\\.0 %\\)\n\\[left\\]:  \\[0, 1, 3, 2\\]\n\\[right\\]: \\[0, 1, 2, 3\\]'
```

### Step 3: Assign c1 = Categorical(...)

```python
c1 = Categorical([1, 2, 4, 3], categories=categories)
```

### Step 4: Assign c2 = Categorical(...)

```python
c2 = Categorical([1, 2, 3, 4], categories=categories)
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(c1, c2)
```


## Complete Example

```python
# Workflow
categories = [1, 2, 3, 4]
msg = 'Categorical\\.codes are different\n\nCategorical\\.codes values are different \\(50\\.0 %\\)\n\\[left\\]:  \\[0, 1, 3, 2\\]\n\\[right\\]: \\[0, 1, 2, 3\\]'
c1 = Categorical([1, 2, 4, 3], categories=categories)
c2 = Categorical([1, 2, 3, 4], categories=categories)
with pytest.raises(AssertionError, match=msg):
    tm.assert_categorical_equal(c1, c2)
```

## Next Steps


---

*Source: test_assert_categorical_equal.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*