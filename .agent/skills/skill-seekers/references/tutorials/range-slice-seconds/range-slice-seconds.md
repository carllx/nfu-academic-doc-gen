# How To: Range Slice Seconds

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test range slice seconds

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: make_range
```

## Step-by-Step Guide

### Step 1: Assign idx = make_range(...)

```python
idx = make_range(start='2013/01/01 09:00:00', freq='s', periods=4000)
```

### Step 2: Assign msg = 'slice indices must be integers or None or have an __index__ method'

```python
msg = 'slice indices must be integers or None or have an __index__ method'
```

### Step 3: Assign values = value

```python
values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9H', '2013/02/01 09:00']
```

### Step 4: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).random(len(idx)), index=idx)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s['2013/01/01 09:05':'2013/01/01 09:10'], s[300:660])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s['2013/01/01 10:00':'2013/01/01 10:05'], s[3600:3960])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s['2013/01/01 10H':], s[3600:])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s[:'2013/01/01 09:30'], s[:1860])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s[d:], s)
```

### Step 10: idx[v:]

```python
idx[v:]
```


## Complete Example

```python
# Setup
# Fixtures: make_range

# Workflow
idx = make_range(start='2013/01/01 09:00:00', freq='s', periods=4000)
msg = 'slice indices must be integers or None or have an __index__ method'
values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9H', '2013/02/01 09:00']
for v in values:
    with pytest.raises(TypeError, match=msg):
        idx[v:]
s = Series(np.random.default_rng(2).random(len(idx)), index=idx)
tm.assert_series_equal(s['2013/01/01 09:05':'2013/01/01 09:10'], s[300:660])
tm.assert_series_equal(s['2013/01/01 10:00':'2013/01/01 10:05'], s[3600:3960])
tm.assert_series_equal(s['2013/01/01 10H':], s[3600:])
tm.assert_series_equal(s[:'2013/01/01 09:30'], s[:1860])
for d in ['2013/01/01', '2013/01', '2013']:
    tm.assert_series_equal(s[d:], s)
```

## Next Steps


---

*Source: test_partial_slicing.py:88 | Complexity: Advanced | Last updated: 2026-06-02*