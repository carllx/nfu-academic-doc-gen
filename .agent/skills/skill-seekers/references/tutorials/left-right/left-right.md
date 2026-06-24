# How To: Left Right

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: left right

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.common`
- `pandas.core.sorting`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
low, high, n = (-1 << 10, 1 << 10, 1 << 20)
```

### Step 2: Assign left = DataFrame(...)

```python
left = DataFrame(np.random.default_rng(2).integers(low, high, (n, 7)), columns=list('ABCDEFG'))
```

### Step 3: Assign unknown = left.sum(...)

```python
left['left'] = left.sum(axis=1)
```

### Step 4: Assign i = np.random.default_rng.permutation(...)

```python
i = np.random.default_rng(2).permutation(len(left))
```

### Step 5: Assign right = unknown.copy(...)

```python
right = left.iloc[i].copy()
```

### Step 6: Assign right.columns = value

```python
right.columns = right.columns[:-1].tolist() + ['right']
```

### Step 7: Assign right.index = np.arange(...)

```python
right.index = np.arange(len(right))
```


## Complete Example

```python
# Workflow
low, high, n = (-1 << 10, 1 << 10, 1 << 20)
left = DataFrame(np.random.default_rng(2).integers(low, high, (n, 7)), columns=list('ABCDEFG'))
left['left'] = left.sum(axis=1)
i = np.random.default_rng(2).permutation(len(left))
right = left.iloc[i].copy()
right.columns = right.columns[:-1].tolist() + ['right']
right.index = np.arange(len(right))
right['right'] *= -1
return (left, right)
```

## Next Steps


---

*Source: test_sorting.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*