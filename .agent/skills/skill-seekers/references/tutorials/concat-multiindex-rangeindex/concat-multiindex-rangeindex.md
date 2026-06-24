# How To: Concat Multiindex Rangeindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat multiindex rangeindex

## Prerequisites

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((9, 2)))
```

### Step 2: Assign df.index = MultiIndex(...)

```python
df.index = MultiIndex(levels=[pd.RangeIndex(3), pd.RangeIndex(3)], codes=[np.repeat(np.arange(3), 3), np.tile(np.arange(3), 3)])
```

### Step 3: Assign res = concat(...)

```python
res = concat([df.iloc[[2, 3, 4], :], df.iloc[[5], :]])
```

### Step 4: Assign exp = value

```python
exp = df.iloc[[2, 3, 4, 5], :]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((9, 2)))
df.index = MultiIndex(levels=[pd.RangeIndex(3), pd.RangeIndex(3)], codes=[np.repeat(np.arange(3), 3), np.tile(np.arange(3), 3)])
res = concat([df.iloc[[2, 3, 4], :], df.iloc[[5], :]])
exp = df.iloc[[2, 3, 4, 5], :]
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_index.py:242 | Complexity: Intermediate | Last updated: 2026-06-02*