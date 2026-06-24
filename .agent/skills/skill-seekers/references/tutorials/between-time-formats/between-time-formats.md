# How To: Between Time Formats

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between time formats

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
```

**Verification:**
```python
assert len(ts.between_time(*time_string)) == expected_length
```

### Step 2: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 2)), index=rng)
```

### Step 3: Assign ts = tm.get_obj(...)

```python
ts = tm.get_obj(ts, frame_or_series)
```

### Step 4: Assign strings = value

```python
strings = [('2:00', '2:30'), ('0200', '0230'), ('2:00am', '2:30am'), ('0200am', '0230am'), ('2:00:00', '2:30:00'), ('020000', '023000'), ('2:00:00am', '2:30:00am'), ('020000am', '023000am')]
```

### Step 5: Assign expected_length = 28

```python
expected_length = 28
```

**Verification:**
```python
assert len(ts.between_time(*time_string)) == expected_length
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 2)), index=rng)
ts = tm.get_obj(ts, frame_or_series)
strings = [('2:00', '2:30'), ('0200', '0230'), ('2:00am', '2:30am'), ('0200am', '0230am'), ('2:00:00', '2:30:00'), ('020000', '023000'), ('2:00:00am', '2:30:00am'), ('020000am', '023000am')]
expected_length = 28
for time_string in strings:
    assert len(ts.between_time(*time_string)) == expected_length
```

## Next Steps


---

*Source: test_between_time.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*