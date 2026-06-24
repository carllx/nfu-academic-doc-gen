# How To: Pindex Slice Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pindex slice index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pi = period_range(...)

```python
pi = period_range(start='1/1/10', end='12/31/12', freq='M')
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).random(len(pi)), index=pi)
```

### Step 3: Assign res = value

```python
res = s['2010']
```

### Step 4: Assign exp = value

```python
exp = s[0:12]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 6: Assign res = value

```python
res = s['2011']
```

### Step 7: Assign exp = value

```python
exp = s[12:24]
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
pi = period_range(start='1/1/10', end='12/31/12', freq='M')
s = Series(np.random.default_rng(2).random(len(pi)), index=pi)
res = s['2010']
exp = s[0:12]
tm.assert_series_equal(res, exp)
res = s['2011']
exp = s[12:24]
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_partial_slicing.py:47 | Complexity: Advanced | Last updated: 2026-06-02*