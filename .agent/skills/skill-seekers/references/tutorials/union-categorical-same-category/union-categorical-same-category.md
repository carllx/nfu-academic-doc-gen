# How To: Union Categorical Same Category

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union categorical same category

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.concat`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign c1 = Categorical(...)

```python
c1 = Categorical([1, 2, 3, 4], categories=[1, 2, 3, 4])
```

### Step 2: Assign c2 = Categorical(...)

```python
c2 = Categorical([3, 2, 1, np.nan], categories=[1, 2, 3, 4])
```

### Step 3: Assign res = union_categoricals(...)

```python
res = union_categoricals([c1, c2])
```

### Step 4: Assign exp = Categorical(...)

```python
exp = Categorical([1, 2, 3, 4, 3, 2, 1, np.nan], categories=[1, 2, 3, 4])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```


## Complete Example

```python
# Workflow
c1 = Categorical([1, 2, 3, 4], categories=[1, 2, 3, 4])
c2 = Categorical([3, 2, 1, np.nan], categories=[1, 2, 3, 4])
res = union_categoricals([c1, c2])
exp = Categorical([1, 2, 3, 4, 3, 2, 1, np.nan], categories=[1, 2, 3, 4])
tm.assert_categorical_equal(res, exp)
```

## Next Steps


---

*Source: test_union_categoricals.py:138 | Complexity: Intermediate | Last updated: 2026-06-02*