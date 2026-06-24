# How To: Union Sort Other Incomparable

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union sort other incomparable

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([1, pd.Timestamp('2000')])
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

### Step 4: Assign result = idx.union(...)

```python
result = idx.union(idx[:1], sort=False)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

### Step 6: Assign result = idx.union(...)

```python
result = idx.union(idx[:1])
```

### Step 7: Assign result = idx.union(...)

```python
result = idx.union(idx[:1], sort=None)
```


## Complete Example

```python
# Workflow
idx = Index([1, pd.Timestamp('2000')])
with tm.assert_produces_warning(RuntimeWarning):
    result = idx.union(idx[:1])
tm.assert_index_equal(result, idx)
with tm.assert_produces_warning(RuntimeWarning):
    result = idx.union(idx[:1], sort=None)
tm.assert_index_equal(result, idx)
result = idx.union(idx[:1], sort=False)
tm.assert_index_equal(result, idx)
```

## Next Steps


---

*Source: test_setops.py:83 | Complexity: Intermediate | Last updated: 2026-06-02*