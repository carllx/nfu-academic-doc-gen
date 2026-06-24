# How To: Setitem Same But Unordered

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test setitem same but unordered

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: other
```

## Step-by-Step Guide

### Step 1: Assign target = Categorical(...)

```python
target = Categorical(['a', 'b'], categories=['a', 'b'])
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([True, False])
```

### Step 3: Assign unknown = value

```python
target[mask] = other[mask]
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(['b', 'b'], categories=['a', 'b'])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(target, expected)
```


## Complete Example

```python
# Setup
# Fixtures: other

# Workflow
target = Categorical(['a', 'b'], categories=['a', 'b'])
mask = np.array([True, False])
target[mask] = other[mask]
expected = Categorical(['b', 'b'], categories=['a', 'b'])
tm.assert_categorical_equal(target, expected)
```

## Next Steps


---

*Source: test_indexing.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*