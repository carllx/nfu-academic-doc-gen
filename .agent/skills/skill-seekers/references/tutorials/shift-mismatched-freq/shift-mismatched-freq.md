# How To: Shift Mismatched Freq

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift mismatched freq

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign ts = frame_or_series(...)

```python
ts = frame_or_series(np.random.default_rng(2).standard_normal(5), index=date_range('1/1/2000', periods=5, freq='h'))
```

### Step 2: Assign result = ts.shift(...)

```python
result = ts.shift(1, freq='5min')
```

### Step 3: Assign exp_index = ts.index.shift(...)

```python
exp_index = ts.index.shift(1, freq='5min')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, exp_index)
```

### Step 5: Assign result = ts.shift(...)

```python
result = ts.shift(1, freq='4h')
```

### Step 6: Assign exp_index = value

```python
exp_index = ts.index + offsets.Hour(4)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, exp_index)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
ts = frame_or_series(np.random.default_rng(2).standard_normal(5), index=date_range('1/1/2000', periods=5, freq='h'))
result = ts.shift(1, freq='5min')
exp_index = ts.index.shift(1, freq='5min')
tm.assert_index_equal(result.index, exp_index)
result = ts.shift(1, freq='4h')
exp_index = ts.index + offsets.Hour(4)
tm.assert_index_equal(result.index, exp_index)
```

## Next Steps


---

*Source: test_shift.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*