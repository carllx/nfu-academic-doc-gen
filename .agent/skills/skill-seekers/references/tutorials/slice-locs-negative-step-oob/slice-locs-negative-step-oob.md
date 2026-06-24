# How To: Slice Locs Negative Step Oob

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slice locs negative step oob

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(list('bcdxy'), dtype=any_string_dtype)
```

### Step 2: Assign result = value

```python
result = index[-10:5:1]
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, index)
```

### Step 4: Assign result = value

```python
result = index[4:-10:-1]
```

### Step 5: Assign expected = Index(...)

```python
expected = Index(list('yxdcb'), dtype=any_string_dtype)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
index = Index(list('bcdxy'), dtype=any_string_dtype)
result = index[-10:5:1]
tm.assert_index_equal(result, index)
result = index[4:-10:-1]
expected = Index(list('yxdcb'), dtype=any_string_dtype)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*