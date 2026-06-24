# How To: Concat Categoricalindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat categoricalindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign categories = value

```python
categories = [9, 0, 1, 2, 3]
```

### Step 2: Assign a = Series(...)

```python
a = Series(1, index=pd.CategoricalIndex([9, 0], categories=categories))
```

### Step 3: Assign b = Series(...)

```python
b = Series(2, index=pd.CategoricalIndex([0, 1], categories=categories))
```

### Step 4: Assign c = Series(...)

```python
c = Series(3, index=pd.CategoricalIndex([1, 2], categories=categories))
```

### Step 5: Assign result = pd.concat(...)

```python
result = pd.concat([a, b, c], axis=1)
```

### Step 6: Assign exp_idx = pd.CategoricalIndex(...)

```python
exp_idx = pd.CategoricalIndex([9, 0, 1, 2], categories=categories)
```

### Step 7: Assign exp = DataFrame(...)

```python
exp = DataFrame({0: [1, 1, np.nan, np.nan], 1: [np.nan, 2, 2, np.nan], 2: [np.nan, np.nan, 3, 3]}, columns=[0, 1, 2], index=exp_idx)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```


## Complete Example

```python
# Workflow
categories = [9, 0, 1, 2, 3]
a = Series(1, index=pd.CategoricalIndex([9, 0], categories=categories))
b = Series(2, index=pd.CategoricalIndex([0, 1], categories=categories))
c = Series(3, index=pd.CategoricalIndex([1, 2], categories=categories))
result = pd.concat([a, b, c], axis=1)
exp_idx = pd.CategoricalIndex([9, 0, 1, 2], categories=categories)
exp = DataFrame({0: [1, 1, np.nan, np.nan], 1: [np.nan, 2, 2, np.nan], 2: [np.nan, np.nan, 3, 3]}, columns=[0, 1, 2], index=exp_idx)
tm.assert_frame_equal(result, exp)
```

## Next Steps


---

*Source: test_categorical.py:74 | Complexity: Advanced | Last updated: 2026-06-02*