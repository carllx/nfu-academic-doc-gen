# How To: Cat Series Unused Category

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: cat series unused category

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
# Fixtures: dtype, ordered
```

## Step-by-Step Guide

### Step 1: Assign cat_array = np.array(...)

```python
cat_array = np.array([1, 2, 3, 4, 5], dtype=np.dtype(dtype))
```

### Step 2: Assign input1 = np.array(...)

```python
input1 = np.array([1, 2, 3, 3], dtype=np.dtype(dtype))
```

### Step 3: Assign cat = Categorical(...)

```python
cat = Categorical(input1, categories=cat_array, ordered=ordered)
```

### Step 4: Assign tc1 = Series(...)

```python
tc1 = Series(cat)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, ordered

# Workflow
cat_array = np.array([1, 2, 3, 4, 5], dtype=np.dtype(dtype))
input1 = np.array([1, 2, 3, 3], dtype=np.dtype(dtype))
cat = Categorical(input1, categories=cat_array, ordered=ordered)
tc1 = Series(cat)
return tc1
```

## Next Steps


---

*Source: test_drop_duplicates.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*