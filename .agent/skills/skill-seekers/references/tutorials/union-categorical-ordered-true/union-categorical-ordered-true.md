# How To: Union Categorical Ordered True

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union categorical ordered true

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
s = Categorical([0, 1.2, 2], ordered=True)
```

### Step 2: Assign s2 = Categorical(...)

```python
s2 = Categorical([0, 1.2, 2], ordered=True)
```

### Step 3: Assign result = union_categoricals(...)

```python
result = union_categoricals([s, s2])
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical([0, 1.2, 2, 0, 1.2, 2], ordered=True)
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Categorical([0, 1.2, 2], ordered=True)
s2 = Categorical([0, 1.2, 2], ordered=True)
result = union_categoricals([s, s2])
expected = Categorical([0, 1.2, 2, 0, 1.2, 2], ordered=True)
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_union_categoricals.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*