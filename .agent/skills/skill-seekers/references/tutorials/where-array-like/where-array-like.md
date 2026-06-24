# How To: Where Array Like

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test where array like

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: klass
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 2, 3])
```

### Step 2: Assign cond = value

```python
cond = [False, True, True]
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([np.nan, 2, 3])
```

### Step 4: Assign result = s.where(...)

```python
result = s.where(klass(cond))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: klass

# Workflow
s = Series([1, 2, 3])
cond = [False, True, True]
expected = Series([np.nan, 2, 3])
result = s.where(klass(cond))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_where.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*