# How To: Setitem Listlike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem listlike

## Prerequisites

**Required Modules:**
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical.add_categories(...)

```python
cat = Categorical(np.random.default_rng(2).integers(0, 5, size=150000).astype(np.int8)).add_categories([-1000])
```

### Step 2: Assign indexer = np.array.astype(...)

```python
indexer = np.array([100000]).astype(np.int64)
```

### Step 3: Assign unknown = value

```python
cat[indexer] = -1000
```

### Step 4: Assign result = value

```python
result = cat.codes[np.array([100000]).astype(np.int64)]
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, np.array([5], dtype='int8'))
```


## Complete Example

```python
# Workflow
cat = Categorical(np.random.default_rng(2).integers(0, 5, size=150000).astype(np.int8)).add_categories([-1000])
indexer = np.array([100000]).astype(np.int64)
cat[indexer] = -1000
result = cat.codes[np.array([100000]).astype(np.int64)]
tm.assert_numpy_array_equal(result, np.array([5], dtype='int8'))
```

## Next Steps


---

*Source: test_indexing.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*