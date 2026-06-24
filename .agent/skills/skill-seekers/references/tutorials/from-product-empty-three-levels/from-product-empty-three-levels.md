# How To: From Product Empty Three Levels

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from product empty three levels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: N
```

## Step-by-Step Guide

### Step 1: Assign names = value

```python
names = ['A', 'B', 'C']
```

### Step 2: Assign lvl2 = list(...)

```python
lvl2 = list(range(N))
```

### Step 3: Assign result = MultiIndex.from_product(...)

```python
result = MultiIndex.from_product([[], lvl2, []], names=names)
```

### Step 4: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[[], lvl2, []], codes=[[], [], []], names=names)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: N

# Workflow
names = ['A', 'B', 'C']
lvl2 = list(range(N))
result = MultiIndex.from_product([[], lvl2, []], names=names)
expected = MultiIndex(levels=[[], lvl2, []], codes=[[], [], []], names=names)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:442 | Complexity: Intermediate | Last updated: 2026-06-02*