# How To: Dti Tz Convert Trans Pos Plus 1  Bug

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti tz convert trans pos plus 1  bug

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: freq, n
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range(datetime(2011, 3, 26, 23), datetime(2011, 3, 27, 1), freq=freq)
```

### Step 2: Assign idx = idx.tz_localize(...)

```python
idx = idx.tz_localize('UTC')
```

### Step 3: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('Europe/Moscow')
```

### Step 4: Assign expected = np.repeat(...)

```python
expected = np.repeat(np.array([3, 4, 5]), np.array([n, n, 1]))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
```


## Complete Example

```python
# Setup
# Fixtures: freq, n

# Workflow
idx = date_range(datetime(2011, 3, 26, 23), datetime(2011, 3, 27, 1), freq=freq)
idx = idx.tz_localize('UTC')
idx = idx.tz_convert('Europe/Moscow')
expected = np.repeat(np.array([3, 4, 5]), np.array([n, n, 1]))
tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
```

## Next Steps


---

*Source: test_tz_convert.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*