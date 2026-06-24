# How To: Mask

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mask

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
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

### Step 3: Assign rs = s.where(...)

```python
rs = s.where(~cond, np.nan)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, s.mask(cond))
```

### Step 5: Assign rs = s.where(...)

```python
rs = s.where(~cond)
```

### Step 6: Assign rs2 = s.mask(...)

```python
rs2 = s.mask(cond)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, rs2)
```

### Step 8: Assign rs = s.where(...)

```python
rs = s.where(~cond, -s)
```

### Step 9: Assign rs2 = s.mask(...)

```python
rs2 = s.mask(cond, -s)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, rs2)
```

### Step 11: Assign cond = Series(...)

```python
cond = Series([True, False, False, True, False], index=s.index)
```

### Step 12: Assign s2 = value

```python
s2 = -s.abs()
```

### Step 13: Assign rs = s2.where(...)

```python
rs = s2.where(~cond[:3])
```

### Step 14: Assign rs2 = s2.mask(...)

```python
rs2 = s2.mask(cond[:3])
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, rs2)
```

### Step 16: Assign rs = s2.where(...)

```python
rs = s2.where(~cond[:3], -s2)
```

### Step 17: Assign rs2 = s2.mask(...)

```python
rs2 = s2.mask(cond[:3], -s2)
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, rs2)
```

### Step 19: Assign msg = 'Array conditional must be same shape as self'

```python
msg = 'Array conditional must be same shape as self'
```

### Step 20: Call s.mask()

```python
s.mask(1)
```

### Step 21: Call s.mask()

```python
s.mask(cond[:3].values, -s)
```


## Complete Example

```python
# Workflow
s = Series(np.random.default_rng(2).standard_normal(5))
cond = s > 0
rs = s.where(~cond, np.nan)
tm.assert_series_equal(rs, s.mask(cond))
rs = s.where(~cond)
rs2 = s.mask(cond)
tm.assert_series_equal(rs, rs2)
rs = s.where(~cond, -s)
rs2 = s.mask(cond, -s)
tm.assert_series_equal(rs, rs2)
cond = Series([True, False, False, True, False], index=s.index)
s2 = -s.abs()
rs = s2.where(~cond[:3])
rs2 = s2.mask(cond[:3])
tm.assert_series_equal(rs, rs2)
rs = s2.where(~cond[:3], -s2)
rs2 = s2.mask(cond[:3], -s2)
tm.assert_series_equal(rs, rs2)
msg = 'Array conditional must be same shape as self'
with pytest.raises(ValueError, match=msg):
    s.mask(1)
with pytest.raises(ValueError, match=msg):
    s.mask(cond[:3].values, -s)
```

## Next Steps


---

*Source: test_mask.py:8 | Complexity: Advanced | Last updated: 2026-06-02*