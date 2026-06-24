# How To: Drop Index Ea Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop index ea dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = Series(...)

```python
df = Series(100, index=Index([1, 2, 2], dtype=any_numeric_ea_dtype))
```

### Step 2: Assign idx = Index(...)

```python
idx = Index([df.index[1]])
```

### Step 3: Assign result = df.drop(...)

```python
result = df.drop(idx)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(100, index=Index([1], dtype=any_numeric_ea_dtype))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_ea_dtype

# Workflow
df = Series(100, index=Index([1, 2, 2], dtype=any_numeric_ea_dtype))
idx = Index([df.index[1]])
result = df.drop(idx)
expected = Series(100, index=Index([1], dtype=any_numeric_ea_dtype))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_drop.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*