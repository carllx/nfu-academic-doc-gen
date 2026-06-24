# How To: Multiindex Compare

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex compare

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_product(...)

```python
midx = MultiIndex.from_product([[0, 1]])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([True, True])
```

### Step 3: Assign result = Series(...)

```python
result = Series(midx == midx)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([False, False])
```

### Step 6: Assign result = Series(...)

```python
result = Series(midx > midx)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
midx = MultiIndex.from_product([[0, 1]])
expected = Series([True, True])
result = Series(midx == midx)
tm.assert_series_equal(result, expected)
expected = Series([False, False])
result = Series(midx > midx)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_equivalence.py:261 | Complexity: Intermediate | Last updated: 2026-06-02*