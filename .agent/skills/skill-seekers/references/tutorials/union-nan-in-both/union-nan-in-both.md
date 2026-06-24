# How To: Union Nan In Both

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union nan in both

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: dup
```

## Step-by-Step Guide

### Step 1: Assign a = Index(...)

```python
a = Index([np.nan, 1, 2, 2])
```

### Step 2: Assign b = Index(...)

```python
b = Index([np.nan, dup, 1, 2])
```

### Step 3: Assign result = a.union(...)

```python
result = a.union(b, sort=False)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([np.nan, dup, 1.0, 2.0, 2.0])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dup

# Workflow
a = Index([np.nan, 1, 2, 2])
b = Index([np.nan, dup, 1, 2])
result = a.union(b, sort=False)
expected = Index([np.nan, dup, 1.0, 2.0, 2.0])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:627 | Complexity: Intermediate | Last updated: 2026-06-02*