# How To: Where Inplace

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where inplace

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(5))
```

### Step 2: Assign cond = value

```python
cond = s > 0
```

### Step 3: Assign rs = s.copy(...)

```python
rs = s.copy()
```

### Step 4: Call rs.where()

```python
rs.where(cond, inplace=True)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs.dropna(), s[cond])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, s.where(cond))
```

### Step 7: Assign rs = s.copy(...)

```python
rs = s.copy()
```

### Step 8: Call rs.where()

```python
rs.where(cond, -s, inplace=True)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, s.where(cond, -s))
```


## Complete Example

```python
# Workflow
s = Series(np.random.default_rng(2).standard_normal(5))
cond = s > 0
rs = s.copy()
rs.where(cond, inplace=True)
tm.assert_series_equal(rs.dropna(), s[cond])
tm.assert_series_equal(rs, s.where(cond))
rs = s.copy()
rs.where(cond, -s, inplace=True)
tm.assert_series_equal(rs, s.where(cond, -s))
```

## Next Steps


---

*Source: test_where.py:328 | Complexity: Advanced | Last updated: 2026-06-02*