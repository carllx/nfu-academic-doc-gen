# How To: Union Same Value Duplicated In Both

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union same value duplicated in both

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
a = Index([0, 0, 1])
```

### Step 2: Assign b = Index(...)

```python
b = Index([0, 0, 1, 2])
```

### Step 3: Assign result = a.union(...)

```python
result = a.union(b)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([0, 0, 1, 2])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = Index([0, 0, 1])
b = Index([0, 0, 1, 2])
result = a.union(b)
expected = Index([0, 0, 1, 2])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:617 | Complexity: Intermediate | Last updated: 2026-06-02*