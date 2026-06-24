# How To: Difference Sort Incomparable

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test difference sort incomparable

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([[1, pd.Timestamp('2000'), 2], ['a', 'b']])
```

### Step 2: Assign other = MultiIndex.from_product(...)

```python
other = MultiIndex.from_product([[3, pd.Timestamp('2000'), 4], ['c', 'd']])
```

### Step 3: Assign msg = 'sort order is undefined for incomparable objects'

```python
msg = 'sort order is undefined for incomparable objects'
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

### Step 5: Assign result = idx.difference(...)

```python
result = idx.difference(other, sort=False)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, idx)
```

### Step 7: Assign result = idx.difference(...)

```python
result = idx.difference(other)
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_product([[1, pd.Timestamp('2000'), 2], ['a', 'b']])
other = MultiIndex.from_product([[3, pd.Timestamp('2000'), 4], ['c', 'd']])
msg = 'sort order is undefined for incomparable objects'
with tm.assert_produces_warning(RuntimeWarning, match=msg):
    result = idx.difference(other)
tm.assert_index_equal(result, idx)
result = idx.difference(other, sort=False)
tm.assert_index_equal(result, idx)
```

## Next Steps


---

*Source: test_setops.py:213 | Complexity: Intermediate | Last updated: 2026-06-02*