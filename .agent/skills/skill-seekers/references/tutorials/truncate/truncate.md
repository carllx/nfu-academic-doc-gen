# How To: Truncate

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test truncate

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_frame, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = datetime_frame[::3]
```

**Verification:**
```python
assert len(truncated) == 0
```

### Step 2: Assign ts = tm.get_obj(...)

```python
ts = tm.get_obj(ts, frame_or_series)
```

**Verification:**
```python
assert len(truncated) == 0
```

### Step 3: Assign unknown = value

```python
start, end = (datetime_frame.index[3], datetime_frame.index[6])
```

### Step 4: Assign start_missing = value

```python
start_missing = datetime_frame.index[2]
```

### Step 5: Assign end_missing = value

```python
end_missing = datetime_frame.index[7]
```

### Step 6: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate()
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(truncated, ts)
```

### Step 8: Assign expected = value

```python
expected = ts[1:3]
```

### Step 9: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate(start, end)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(truncated, expected)
```

### Step 11: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate(start_missing, end_missing)
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(truncated, expected)
```

### Step 13: Assign expected = value

```python
expected = ts[1:]
```

### Step 14: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate(before=start)
```

### Step 15: Call tm.assert_equal()

```python
tm.assert_equal(truncated, expected)
```

### Step 16: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate(before=start_missing)
```

### Step 17: Call tm.assert_equal()

```python
tm.assert_equal(truncated, expected)
```

### Step 18: Assign expected = value

```python
expected = ts[:3]
```

### Step 19: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate(after=end)
```

### Step 20: Call tm.assert_equal()

```python
tm.assert_equal(truncated, expected)
```

### Step 21: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate(after=end_missing)
```

### Step 22: Call tm.assert_equal()

```python
tm.assert_equal(truncated, expected)
```

### Step 23: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate(after=ts.index[0] - ts.index.freq)
```

**Verification:**
```python
assert len(truncated) == 0
```

### Step 24: Assign truncated = ts.truncate(...)

```python
truncated = ts.truncate(before=ts.index[-1] + ts.index.freq)
```

**Verification:**
```python
assert len(truncated) == 0
```

### Step 25: Assign msg = 'Truncate: 2000-01-06 00:00:00 must be after 2000-05-16 00:00:00'

```python
msg = 'Truncate: 2000-01-06 00:00:00 must be after 2000-05-16 00:00:00'
```

### Step 26: Call ts.truncate()

```python
ts.truncate(before=ts.index[-1] - ts.index.freq, after=ts.index[0] + ts.index.freq)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame, frame_or_series

# Workflow
ts = datetime_frame[::3]
ts = tm.get_obj(ts, frame_or_series)
start, end = (datetime_frame.index[3], datetime_frame.index[6])
start_missing = datetime_frame.index[2]
end_missing = datetime_frame.index[7]
truncated = ts.truncate()
tm.assert_equal(truncated, ts)
expected = ts[1:3]
truncated = ts.truncate(start, end)
tm.assert_equal(truncated, expected)
truncated = ts.truncate(start_missing, end_missing)
tm.assert_equal(truncated, expected)
expected = ts[1:]
truncated = ts.truncate(before=start)
tm.assert_equal(truncated, expected)
truncated = ts.truncate(before=start_missing)
tm.assert_equal(truncated, expected)
expected = ts[:3]
truncated = ts.truncate(after=end)
tm.assert_equal(truncated, expected)
truncated = ts.truncate(after=end_missing)
tm.assert_equal(truncated, expected)
truncated = ts.truncate(after=ts.index[0] - ts.index.freq)
assert len(truncated) == 0
truncated = ts.truncate(before=ts.index[-1] + ts.index.freq)
assert len(truncated) == 0
msg = 'Truncate: 2000-01-06 00:00:00 must be after 2000-05-16 00:00:00'
with pytest.raises(ValueError, match=msg):
    ts.truncate(before=ts.index[-1] - ts.index.freq, after=ts.index[0] + ts.index.freq)
```

## Next Steps


---

*Source: test_truncate.py:16 | Complexity: Advanced | Last updated: 2026-06-02*