# How To: Range Slice Day

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test range slice day

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
idx = make_range(start='2013/01/01', freq='D', periods=400)
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
tm.assert_series_equal(s['2013/01/02':], s[1:])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s['2013/01/02':'2013/01/05'], s[1:5])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s['2013/02':], s[31:])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s['2014':], s[365:])
```

### Step 9: Assign invalid = value

```python
invalid = ['2013/02/01 9H', '2013/02/01 09:00']
```

### Step 10: idx[v:]

```python
idx[v:]
```

### Step 11: idx[v:]

```python
idx[v:]
```


## Complete Example

```python
# Setup
# Fixtures: make_range

# Workflow
idx = make_range(start='2013/01/01', freq='D', periods=400)
msg = 'slice indices must be integers or None or have an __index__ method'
values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9H', '2013/02/01 09:00']
for v in values:
    with pytest.raises(TypeError, match=msg):
        idx[v:]
s = Series(np.random.default_rng(2).random(len(idx)), index=idx)
tm.assert_series_equal(s['2013/01/02':], s[1:])
tm.assert_series_equal(s['2013/01/02':'2013/01/05'], s[1:5])
tm.assert_series_equal(s['2013/02':], s[31:])
tm.assert_series_equal(s['2014':], s[365:])
invalid = ['2013/02/01 9H', '2013/02/01 09:00']
for v in invalid:
    with pytest.raises(TypeError, match=msg):
        idx[v:]
```

## Next Steps


---

*Source: test_partial_slicing.py:58 | Complexity: Advanced | Last updated: 2026-06-02*