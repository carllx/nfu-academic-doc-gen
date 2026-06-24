# How To: Union Categorical Ordered Appearance

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union categorical ordered appearance

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.concat`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Categorical(...)

```python
s = Categorical(['x', 'y', 'z'])
```

### Step 2: Assign s2 = Categorical(...)

```python
s2 = Categorical(['a', 'b', 'c'])
```

### Step 3: Assign result = union_categoricals(...)

```python
result = union_categoricals([s, s2])
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(['x', 'y', 'z', 'a', 'b', 'c'], categories=['x', 'y', 'z', 'a', 'b', 'c'])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Categorical(['x', 'y', 'z'])
s2 = Categorical(['a', 'b', 'c'])
result = union_categoricals([s, s2])
expected = Categorical(['x', 'y', 'z', 'a', 'b', 'c'], categories=['x', 'y', 'z', 'a', 'b', 'c'])
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_union_categoricals.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*