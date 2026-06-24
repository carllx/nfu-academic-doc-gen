# How To: Union Duplicate Index Different Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union duplicate index different dtypes

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign a = Index(...)

```python
a = Index([1, 2, 2, 3])
```

### Step 2: Assign b = Index(...)

```python
b = Index(['1', '0', '0'])
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([1, 2, 2, 3, '1', '0', '0'])
```

### Step 4: Assign result = a.union(...)

```python
result = a.union(b, sort=False)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = Index([1, 2, 2, 3])
b = Index(['1', '0', '0'])
expected = Index([1, 2, 2, 3, '1', '0', '0'])
result = a.union(b, sort=False)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:608 | Complexity: Intermediate | Last updated: 2026-06-02*