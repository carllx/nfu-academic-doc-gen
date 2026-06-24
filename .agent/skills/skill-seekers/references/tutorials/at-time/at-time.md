# How To: At Time

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test at time

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
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
```

**Verification:**
```python
assert (rs.index.hour == rng[1].hour).all()
```

### Step 2: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 2)), index=rng)
```

**Verification:**
```python
assert (rs.index.minute == rng[1].minute).all()
```

### Step 3: Assign ts = tm.get_obj(...)

```python
ts = tm.get_obj(ts, frame_or_series)
```

**Verification:**
```python
assert (rs.index.second == rng[1].second).all()
```

### Step 4: Assign rs = ts.at_time(...)

```python
rs = ts.at_time(rng[1])
```

**Verification:**
```python
assert (rs.index.hour == rng[1].hour).all()
```

### Step 5: Assign result = ts.at_time(...)

```python
result = ts.at_time('9:30')
```

### Step 6: Assign expected = ts.at_time(...)

```python
expected = ts.at_time(time(9, 30))
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), 2)), index=rng)
ts = tm.get_obj(ts, frame_or_series)
rs = ts.at_time(rng[1])
assert (rs.index.hour == rng[1].hour).all()
assert (rs.index.minute == rng[1].minute).all()
assert (rs.index.second == rng[1].second).all()
result = ts.at_time('9:30')
expected = ts.at_time(time(9, 30))
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_at_time.py:33 | Complexity: Intermediate | Last updated: 2026-06-02*