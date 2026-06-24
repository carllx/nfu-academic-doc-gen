# How To: To Timestamp Hourly

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to timestamp hourly

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign index = period_range(...)

```python
index = period_range(freq='h', start='1/1/2001', end='1/2/2001')
```

**Verification:**
```python
assert result.name == 'foo'
```

### Step 2: Assign obj = Series(...)

```python
obj = Series(1, index=index, name='foo')
```

### Step 3: Assign exp_index = date_range(...)

```python
exp_index = date_range('1/1/2001 00:59:59', end='1/2/2001 00:59:59', freq='h')
```

### Step 4: Assign result = obj.to_timestamp(...)

```python
result = obj.to_timestamp(how='end')
```

### Step 5: Assign exp_index = value

```python
exp_index = exp_index + Timedelta(1, 's') - Timedelta(1, 'ns')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, exp_index)
```

### Step 7: Assign obj = obj.to_frame(...)

```python
obj = obj.to_frame()
```

**Verification:**
```python
assert result.name == 'foo'
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
index = period_range(freq='h', start='1/1/2001', end='1/2/2001')
obj = Series(1, index=index, name='foo')
if frame_or_series is not Series:
    obj = obj.to_frame()
exp_index = date_range('1/1/2001 00:59:59', end='1/2/2001 00:59:59', freq='h')
result = obj.to_timestamp(how='end')
exp_index = exp_index + Timedelta(1, 's') - Timedelta(1, 'ns')
tm.assert_index_equal(result.index, exp_index)
if frame_or_series is Series:
    assert result.name == 'foo'
```

## Next Steps


---

*Source: test_to_timestamp.py:134 | Complexity: Intermediate | Last updated: 2026-06-02*