# How To: Tdi Division

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tdi division

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_or_series
```

## Step-by-Step Guide

### Step 1: Assign scalar = Timedelta(...)

```python
scalar = Timedelta(days=31)
```

### Step 2: Assign td = index_or_series(...)

```python
td = index_or_series([scalar, scalar, scalar + Timedelta(minutes=5, seconds=3), NaT], dtype='m8[ns]')
```

### Step 3: Assign result = value

```python
result = td / np.timedelta64(1, 'D')
```

### Step 4: Assign expected = index_or_series(...)

```python
expected = index_or_series([31, 31, (31 * 86400 + 5 * 60 + 3) / 86400.0, np.nan])
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = td / np.timedelta64(1, 's')
```

### Step 7: Assign expected = index_or_series(...)

```python
expected = index_or_series([31 * 86400, 31 * 86400, 31 * 86400 + 5 * 60 + 3, np.nan])
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series

# Workflow
scalar = Timedelta(days=31)
td = index_or_series([scalar, scalar, scalar + Timedelta(minutes=5, seconds=3), NaT], dtype='m8[ns]')
result = td / np.timedelta64(1, 'D')
expected = index_or_series([31, 31, (31 * 86400 + 5 * 60 + 3) / 86400.0, np.nan])
tm.assert_equal(result, expected)
result = td / np.timedelta64(1, 's')
expected = index_or_series([31 * 86400, 31 * 86400, 31 * 86400 + 5 * 60 + 3, np.nan])
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:32 | Complexity: Advanced | Last updated: 2026-06-02*