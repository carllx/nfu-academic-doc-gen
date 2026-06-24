# How To: Na Flags Int Categories

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test na flags int categories

## Prerequisites

**Required Modules:**
- `collections`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign categories = list(...)

```python
categories = list(range(10))
```

### Step 2: Assign labels = np.random.default_rng.integers(...)

```python
labels = np.random.default_rng(2).integers(0, 10, 20)
```

### Step 3: Assign unknown = value

```python
labels[::5] = -1
```

### Step 4: Assign cat = Categorical(...)

```python
cat = Categorical(labels, categories)
```

### Step 5: Call repr()

```python
repr(cat)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(isna(cat), labels == -1)
```


## Complete Example

```python
# Workflow
categories = list(range(10))
labels = np.random.default_rng(2).integers(0, 10, 20)
labels[::5] = -1
cat = Categorical(labels, categories)
repr(cat)
tm.assert_numpy_array_equal(isna(cat), labels == -1)
```

## Next Steps


---

*Source: test_missing.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*