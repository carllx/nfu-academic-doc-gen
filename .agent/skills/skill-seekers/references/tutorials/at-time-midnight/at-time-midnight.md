# How To: At Time Midnight

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at time midnight

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', '1/31/2000')
```

### Step 2: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 3)), index=rng)
```

### Step 3: Assign ts = tm.get_obj(...)

```python
ts = tm.get_obj(ts, frame_or_series)
```

### Step 4: Assign result = ts.at_time(...)

```python
result = ts.at_time(time(0, 0))
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, ts)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2000', '1/31/2000')
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 3)), index=rng)
ts = tm.get_obj(ts, frame_or_series)
result = ts.at_time(time(0, 0))
tm.assert_equal(result, ts)
```

## Next Steps


---

*Source: test_at_time.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*