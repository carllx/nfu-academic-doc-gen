# How To: To Period

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to period

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign K = 5

```python
K = 5
```

### Step 2: Assign dr = date_range(...)

```python
dr = date_range('1/1/2000', '1/1/2001', freq='D')
```

### Step 3: Assign obj = DataFrame(...)

```python
obj = DataFrame(np.random.default_rng(2).standard_normal((len(dr), K)), index=dr, columns=['A', 'B', 'C', 'D', 'E'])
```

### Step 4: Assign unknown = 'a'

```python
obj['mix'] = 'a'
```

### Step 5: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 6: Assign pts = obj.to_period(...)

```python
pts = obj.to_period()
```

### Step 7: Assign exp = obj.copy(...)

```python
exp = obj.copy()
```

### Step 8: Assign exp.index = period_range(...)

```python
exp.index = period_range('1/1/2000', '1/1/2001')
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(pts, exp)
```

### Step 10: Assign pts = obj.to_period(...)

```python
pts = obj.to_period('M')
```

### Step 11: Assign exp.index = exp.index.asfreq(...)

```python
exp.index = exp.index.asfreq('M')
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(pts, exp)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
K = 5
dr = date_range('1/1/2000', '1/1/2001', freq='D')
obj = DataFrame(np.random.default_rng(2).standard_normal((len(dr), K)), index=dr, columns=['A', 'B', 'C', 'D', 'E'])
obj['mix'] = 'a'
obj = tm.get_obj(obj, frame_or_series)
pts = obj.to_period()
exp = obj.copy()
exp.index = period_range('1/1/2000', '1/1/2001')
tm.assert_equal(pts, exp)
pts = obj.to_period('M')
exp.index = exp.index.asfreq('M')
tm.assert_equal(pts, exp)
```

## Next Steps


---

*Source: test_to_period.py:16 | Complexity: Advanced | Last updated: 2026-06-02*