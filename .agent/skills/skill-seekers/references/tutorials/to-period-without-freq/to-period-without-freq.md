# How To: To Period Without Freq

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to period without freq

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

### Step 1: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'])
```

### Step 2: Assign exp_idx = PeriodIndex(...)

```python
exp_idx = PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'], freq='D')
```

### Step 3: Assign obj = DataFrame(...)

```python
obj = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=idx, columns=idx)
```

### Step 4: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 5: Assign expected = obj.copy(...)

```python
expected = obj.copy()
```

### Step 6: Assign expected.index = exp_idx

```python
expected.index = exp_idx
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(obj.to_period(), expected)
```

### Step 8: Assign expected = obj.copy(...)

```python
expected = obj.copy()
```

### Step 9: Assign expected.columns = exp_idx

```python
expected.columns = exp_idx
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(obj.to_period(axis=1), expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
idx = DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'])
exp_idx = PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'], freq='D')
obj = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), index=idx, columns=idx)
obj = tm.get_obj(obj, frame_or_series)
expected = obj.copy()
expected.index = exp_idx
tm.assert_equal(obj.to_period(), expected)
if frame_or_series is DataFrame:
    expected = obj.copy()
    expected.columns = exp_idx
    tm.assert_frame_equal(obj.to_period(axis=1), expected)
```

## Next Steps


---

*Source: test_to_period.py:37 | Complexity: Advanced | Last updated: 2026-06-02*