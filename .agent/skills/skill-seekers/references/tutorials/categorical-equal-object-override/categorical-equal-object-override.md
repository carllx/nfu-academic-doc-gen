# How To: Categorical Equal Object Override

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical equal object override

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: obj
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [1, 2, 3, 4]
```

### Step 2: Assign msg = value

```python
msg = f'{obj} are different\n\nAttribute "ordered" are different\n\\[left\\]:  False\n\\[right\\]: True'
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
tm.assert_categorical_equal(c1, c2, obj=obj)
```


## Complete Example

```python
# Setup
# Fixtures: obj

# Workflow
data = [1, 2, 3, 4]
msg = f'{obj} are different\n\nAttribute "ordered" are different\n\\[left\\]:  False\n\\[right\\]: True'
c1 = Categorical(data, ordered=False)
c2 = Categorical(data, ordered=True)
with pytest.raises(AssertionError, match=msg):
    tm.assert_categorical_equal(c1, c2, obj=obj)
```

## Next Steps


---

*Source: test_assert_categorical_equal.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*