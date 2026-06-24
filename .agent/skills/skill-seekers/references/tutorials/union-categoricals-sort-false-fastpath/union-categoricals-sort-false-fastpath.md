# How To: Union Categoricals Sort False Fastpath

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union categoricals sort false fastpath

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
c1 = Categorical(['a', 'b'], categories=['b', 'a', 'c'])
```

### Step 2: Assign c2 = Categorical(...)

```python
c2 = Categorical(['b', 'c'], categories=['b', 'a', 'c'])
```

### Step 3: Assign result = union_categoricals(...)

```python
result = union_categoricals([c1, c2], sort_categories=False)
```

### Step 4: Assign expected = Categorical(...)

```python
expected = Categorical(['a', 'b', 'b', 'c'], categories=['b', 'a', 'c'])
```

### Step 5: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, expected)
```


## Complete Example

```python
# Workflow
c1 = Categorical(['a', 'b'], categories=['b', 'a', 'c'])
c2 = Categorical(['b', 'c'], categories=['b', 'a', 'c'])
result = union_categoricals([c1, c2], sort_categories=False)
expected = Categorical(['a', 'b', 'b', 'c'], categories=['b', 'a', 'c'])
tm.assert_categorical_equal(result, expected)
```

## Next Steps


---

*Source: test_union_categoricals.py:305 | Complexity: Intermediate | Last updated: 2026-06-02*