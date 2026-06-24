# How To: Diff Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diff tz

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Series(...)

```python
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10), name='ts')
```

### Step 2: Call ts.diff()

```python
ts.diff()
```

### Step 3: Assign result = ts.diff(...)

```python
result = ts.diff(-1)
```

### Step 4: Assign expected = value

```python
expected = ts - ts.shift(-1)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = ts.diff(...)

```python
result = ts.diff(0)
```

### Step 7: Assign expected = value

```python
expected = ts - ts
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10), name='ts')
ts.diff()
result = ts.diff(-1)
expected = ts - ts.shift(-1)
tm.assert_series_equal(result, expected)
result = ts.diff(0)
expected = ts - ts
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_diff.py:32 | Complexity: Advanced | Last updated: 2026-06-02*