# How To: Cat Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: cat series

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

### Step 2: Assign input2 = np.array(...)

```python
input2 = np.array([1, 2, 3, 5, 3, 2, 4], dtype=np.dtype(dtype))
```

### Step 3: Assign cat = Categorical(...)

```python
cat = Categorical(input2, categories=cat_array, ordered=ordered)
```

### Step 4: Assign tc2 = Series(...)

```python
tc2 = Series(cat)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, ordered

# Workflow
cat_array = np.array([1, 2, 3, 4, 5], dtype=np.dtype(dtype))
input2 = np.array([1, 2, 3, 5, 3, 2, 4], dtype=np.dtype(dtype))
cat = Categorical(input2, categories=cat_array, ordered=ordered)
tc2 = Series(cat)
return tc2
```

## Next Steps


---

*Source: test_drop_duplicates.py:143 | Complexity: Intermediate | Last updated: 2026-06-02*