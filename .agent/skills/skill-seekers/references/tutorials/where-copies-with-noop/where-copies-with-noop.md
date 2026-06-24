# How To: Where Copies With Noop

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where copies with noop

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign result = frame_or_series(...)

```python
result = frame_or_series([1, 2, 3, 4])
```

### Step 2: Assign expected = result.copy(...)

```python
expected = result.copy()
```

### Step 3: Assign col = value

```python
col = result[0] if frame_or_series is DataFrame else result
```

### Step 4: Assign where_res = result.where(...)

```python
where_res = result.where(col < 5)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign where_res = result.where(...)

```python
where_res = result.where(col > 5, [1, 2, 3, 4])
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
result = frame_or_series([1, 2, 3, 4])
expected = result.copy()
col = result[0] if frame_or_series is DataFrame else result
where_res = result.where(col < 5)
where_res *= 2
tm.assert_equal(result, expected)
where_res = result.where(col > 5, [1, 2, 3, 4])
where_res *= 2
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_where.py:828 | Complexity: Intermediate | Last updated: 2026-06-02*