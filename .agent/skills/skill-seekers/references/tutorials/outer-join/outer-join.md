# How To: Outer Join

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test outer join

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
start, end = (datetime(2009, 1, 1), datetime(2010, 1, 1))
```

**Verification:**
```python
assert isinstance(the_join, DatetimeIndex)
```

### Step 2: Assign rng = date_range(...)

```python
rng = date_range(start=start, end=end, freq=freq)
```

**Verification:**
```python
assert isinstance(the_join, DatetimeIndex)
```

### Step 3: Assign left = value

```python
left = rng[:10]
```

**Verification:**
```python
assert the_join.freq is None
```

### Step 4: Assign right = value

```python
right = rng[5:10]
```

**Verification:**
```python
assert isinstance(the_join, DatetimeIndex)
```

### Step 5: Assign the_join = left.join(...)

```python
the_join = left.join(right, how='outer')
```

**Verification:**
```python
assert isinstance(the_join, DatetimeIndex)
```

### Step 6: Assign left = value

```python
left = rng[:5]
```

**Verification:**
```python
assert the_join.freq is None
```

### Step 7: Assign right = value

```python
right = rng[10:]
```

### Step 8: Assign the_join = left.join(...)

```python
the_join = left.join(right, how='outer')
```

**Verification:**
```python
assert isinstance(the_join, DatetimeIndex)
```

### Step 9: Assign left = value

```python
left = rng[:5]
```

### Step 10: Assign right = value

```python
right = rng[5:10]
```

### Step 11: Assign the_join = left.join(...)

```python
the_join = left.join(right, how='outer')
```

**Verification:**
```python
assert isinstance(the_join, DatetimeIndex)
```

### Step 12: Assign other = date_range(...)

```python
other = date_range(start, end, freq=BMonthEnd())
```

### Step 13: Assign the_join = rng.join(...)

```python
the_join = rng.join(other, how='outer')
```

**Verification:**
```python
assert isinstance(the_join, DatetimeIndex)
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
start, end = (datetime(2009, 1, 1), datetime(2010, 1, 1))
rng = date_range(start=start, end=end, freq=freq)
left = rng[:10]
right = rng[5:10]
the_join = left.join(right, how='outer')
assert isinstance(the_join, DatetimeIndex)
left = rng[:5]
right = rng[10:]
the_join = left.join(right, how='outer')
assert isinstance(the_join, DatetimeIndex)
assert the_join.freq is None
left = rng[:5]
right = rng[5:10]
the_join = left.join(right, how='outer')
assert isinstance(the_join, DatetimeIndex)
other = date_range(start, end, freq=BMonthEnd())
the_join = rng.join(other, how='outer')
assert isinstance(the_join, DatetimeIndex)
assert the_join.freq is None
```

## Next Steps


---

*Source: test_join.py:96 | Complexity: Advanced | Last updated: 2026-06-02*