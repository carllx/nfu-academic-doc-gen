# How To: Drop Tz Aware Timestamp Across Dst

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop tz aware timestamp across dst

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign start = Timestamp(...)

```python
start = Timestamp('2017-10-29', tz='Europe/Berlin')
```

### Step 2: Assign end = Timestamp(...)

```python
end = Timestamp('2017-10-29 04:00:00', tz='Europe/Berlin')
```

### Step 3: Assign index = pd.date_range(...)

```python
index = pd.date_range(start, end, freq='15min')
```

### Step 4: Assign data = frame_or_series(...)

```python
data = frame_or_series(data=[1] * len(index), index=index)
```

### Step 5: Assign result = data.drop(...)

```python
result = data.drop(start)
```

### Step 6: Assign expected_start = Timestamp(...)

```python
expected_start = Timestamp('2017-10-29 00:15:00', tz='Europe/Berlin')
```

### Step 7: Assign expected_idx = pd.date_range(...)

```python
expected_idx = pd.date_range(expected_start, end, freq='15min')
```

### Step 8: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(data=[1] * len(expected_idx), index=expected_idx)
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
start = Timestamp('2017-10-29', tz='Europe/Berlin')
end = Timestamp('2017-10-29 04:00:00', tz='Europe/Berlin')
index = pd.date_range(start, end, freq='15min')
data = frame_or_series(data=[1] * len(index), index=index)
result = data.drop(start)
expected_start = Timestamp('2017-10-29 00:15:00', tz='Europe/Berlin')
expected_idx = pd.date_range(expected_start, end, freq='15min')
expected = frame_or_series(data=[1] * len(expected_idx), index=expected_idx)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_drop.py:423 | Complexity: Advanced | Last updated: 2026-06-02*