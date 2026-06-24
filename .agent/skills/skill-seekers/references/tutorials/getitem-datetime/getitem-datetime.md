# How To: Getitem Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem datetime

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = period_range(...)

```python
rng = period_range(start='2012-01-01', periods=10, freq='W-MON')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(range(len(rng)), index=rng)
```

### Step 3: Assign dt1 = datetime(...)

```python
dt1 = datetime(2011, 10, 2)
```

### Step 4: Assign dt4 = datetime(...)

```python
dt4 = datetime(2012, 4, 20)
```

### Step 5: Assign rs = value

```python
rs = ts[dt1:dt4]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, ts)
```


## Complete Example

```python
# Workflow
rng = period_range(start='2012-01-01', periods=10, freq='W-MON')
ts = Series(range(len(rng)), index=rng)
dt1 = datetime(2011, 10, 2)
dt4 = datetime(2012, 4, 20)
rs = ts[dt1:dt4]
tm.assert_series_equal(rs, ts)
```

## Next Steps


---

*Source: test_indexing.py:145 | Complexity: Intermediate | Last updated: 2026-06-02*