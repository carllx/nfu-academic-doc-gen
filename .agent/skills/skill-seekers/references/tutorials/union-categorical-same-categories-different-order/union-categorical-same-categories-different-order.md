# How To: Union Categorical Same Categories Different Order

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union categorical same categories different order

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
c1 = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c'])
```

### Step 2: Assign c2 = Categorical(...)

```python
c2 = Categorical(['a', 'b', 'c'], categories=['b', 'a', 'c'])
```

### Step 3: Assign result = union_categoricals(...)

```python
result = union_categoricals([c1, c2])
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(['a', 'b', 'c', 'a', 'b', 'c'], categories=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
c1 = Categorical(['a', 'b', 'c'], categories=['a', 'b', 'c'])
c2 = Categorical(['a', 'b', 'c'], categories=['b', 'a', 'c'])
result = union_categoricals([c1, c2])
expected = Categorical(['a', 'b', 'c', 'a', 'b', 'c'], categories=['a', 'b', 'c'])
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_union_categoricals.py:153 | Complexity: Intermediate | Last updated: 2026-06-02*