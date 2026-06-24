# How To: Categorical Equal Ordered Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical equal ordered mismatch

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [1, 2, 3, 4]
```

### Step 2: Assign msg = 'Categorical are different\n\nAttribute "ordered" are different\n\\[left\\]:  False\n\\[right\\]: True'

```python
msg = 'Categorical are different\n\nAttribute "ordered" are different\n\\[left\\]:  False\n\\[right\\]: True'
```

### Step 3: Assign c1 = Categorical(...)

```python
c1 = Categorical(data, ordered=False)
```

### Step 4: Assign c2 = Categorical(...)

```python
c2 = Categorical(data, ordered=True)
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(c1, c2)
```


## Complete Example

```python
# Workflow
data = [1, 2, 3, 4]
msg = 'Categorical are different\n\nAttribute "ordered" are different\n\\[left\\]:  False\n\\[right\\]: True'
c1 = Categorical(data, ordered=False)
c2 = Categorical(data, ordered=True)
with pytest.raises(AssertionError, match=msg):
    tm.assert_categorical_equal(c1, c2)
```

## Next Steps


---

*Source: test_assert_categorical_equal.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*