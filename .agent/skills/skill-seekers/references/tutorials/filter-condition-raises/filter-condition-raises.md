# How To: Filter Condition Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filter condition raises

## Prerequisites

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([-1, 0, 1, 2])
```

### Step 2: Assign grouper = s.apply(...)

```python
grouper = s.apply(lambda x: x % 2)
```

### Step 3: Assign grouped = s.groupby(...)

```python
grouped = s.groupby(grouper)
```

### Step 4: Assign msg = 'the filter must return a boolean result'

```python
msg = 'the filter must return a boolean result'
```

### Step 5: Call grouped.filter()

```python
grouped.filter(raise_if_sum_is_zero)
```


## Complete Example

```python
# Workflow
def raise_if_sum_is_zero(x):
    if x.sum() == 0:
        raise ValueError
    return x.sum() > 0
s = Series([-1, 0, 1, 2])
grouper = s.apply(lambda x: x % 2)
grouped = s.groupby(grouper)
msg = 'the filter must return a boolean result'
with pytest.raises(TypeError, match=msg):
    grouped.filter(raise_if_sum_is_zero)
```

## Next Steps


---

*Source: test_filters.py:110 | Complexity: Intermediate | Last updated: 2026-06-02*