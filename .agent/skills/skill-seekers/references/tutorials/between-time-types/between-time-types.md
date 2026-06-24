# How To: Between Time Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between time types

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

### Step 2: Assign obj = DataFrame(...)

```python
obj = DataFrame({'A': 0}, index=rng)
```

### Step 3: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(obj, frame_or_series)
```

### Step 4: Assign msg = 'Cannot convert arg \\[datetime\\.datetime\\(2010, 1, 2, 1, 0\\)\\] to a time'

```python
msg = 'Cannot convert arg \\[datetime\\.datetime\\(2010, 1, 2, 1, 0\\)\\] to a time'
```

### Step 5: Call obj.between_time()

```python
obj.between_time(datetime(2010, 1, 2, 1), datetime(2010, 1, 2, 5))
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
obj = DataFrame({'A': 0}, index=rng)
obj = tm.get_obj(obj, frame_or_series)
msg = 'Cannot convert arg \\[datetime\\.datetime\\(2010, 1, 2, 1, 0\\)\\] to a time'
with pytest.raises(ValueError, match=msg):
    obj.between_time(datetime(2010, 1, 2, 1), datetime(2010, 1, 2, 5))
```

## Next Steps


---

*Source: test_between_time.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*