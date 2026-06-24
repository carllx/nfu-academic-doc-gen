# How To: Union Categorical Same Category Str

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union categorical same category str

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
c1 = Categorical(['z', 'z', 'z'], categories=['x', 'y', 'z'])
```

### Step 2: Assign c2 = Categorical(...)

```python
c2 = Categorical(['x', 'x', 'x'], categories=['x', 'y', 'z'])
```

### Step 3: Assign res = union_categoricals(...)

```python
res = union_categoricals([c1, c2])
```

### Step 4: Assign exp = Categorical(...)

```python
exp = Categorical(['z', 'z', 'z', 'x', 'x', 'x'], categories=['x', 'y', 'z'])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(res, exp)
```


## Complete Example

```python
# Workflow
c1 = Categorical(['z', 'z', 'z'], categories=['x', 'y', 'z'])
c2 = Categorical(['x', 'x', 'x'], categories=['x', 'y', 'z'])
res = union_categoricals([c1, c2])
exp = Categorical(['z', 'z', 'z', 'x', 'x', 'x'], categories=['x', 'y', 'z'])
tm.assert_categorical_equal(res, exp)
```

## Next Steps


---

*Source: test_union_categoricals.py:146 | Complexity: Intermediate | Last updated: 2026-06-02*