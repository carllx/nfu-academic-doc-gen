# How To: Asfreq Ts

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq ts

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign index = period_range(...)

```python
index = period_range(freq='Y', start='1/1/2001', end='12/31/2010')
```

**Verification:**
```python
assert len(result) == len(obj)
```

### Step 2: Assign obj = DataFrame(...)

```python
obj = DataFrame(np.random.default_rng(2).standard_normal((len(index), 3)), index=index)
```

**Verification:**
```python
assert len(result) == len(obj)
```

### Step 3: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 4: Assign result = obj.asfreq(...)

```python
result = obj.asfreq('D', how='end')
```

### Step 5: Assign exp_index = index.asfreq(...)

```python
exp_index = index.asfreq('D', how='end')
```

**Verification:**
```python
assert len(result) == len(obj)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, exp_index)
```

### Step 7: Assign result = obj.asfreq(...)

```python
result = obj.asfreq('D', how='start')
```

### Step 8: Assign exp_index = index.asfreq(...)

```python
exp_index = index.asfreq('D', how='start')
```

**Verification:**
```python
assert len(result) == len(obj)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, exp_index)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
index = period_range(freq='Y', start='1/1/2001', end='12/31/2010')
obj = DataFrame(np.random.default_rng(2).standard_normal((len(index), 3)), index=index)
obj = tm.get_obj(obj, frame_or_series)
result = obj.asfreq('D', how='end')
exp_index = index.asfreq('D', how='end')
assert len(result) == len(obj)
tm.assert_index_equal(result.index, exp_index)
result = obj.asfreq('D', how='start')
exp_index = index.asfreq('D', how='start')
assert len(result) == len(obj)
tm.assert_index_equal(result.index, exp_index)
```

## Next Steps


---

*Source: test_asfreq.py:107 | Complexity: Advanced | Last updated: 2026-06-02*