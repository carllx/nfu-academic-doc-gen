# How To: At Time Nonexistent

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at time nonexistent

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
rng = date_range('1/1/2012', freq='23Min', periods=384)
```

**Verification:**
```python
assert len(rs) == 0
```

### Step 2: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal(len(rng)), rng)
```

### Step 3: Assign ts = tm.get_obj(...)

```python
ts = tm.get_obj(ts, frame_or_series)
```

### Step 4: Assign rs = ts.at_time(...)

```python
rs = ts.at_time('16:00')
```

**Verification:**
```python
assert len(rs) == 0
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2012', freq='23Min', periods=384)
ts = DataFrame(np.random.default_rng(2).standard_normal(len(rng)), rng)
ts = tm.get_obj(ts, frame_or_series)
rs = ts.at_time('16:00')
assert len(rs) == 0
```

## Next Steps


---

*Source: test_at_time.py:59 | Complexity: Intermediate | Last updated: 2026-06-02*