# How To: Join Utc Convert

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join utc convert

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
# Fixtures: join_type
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2011', periods=100, freq='h', tz='utc')
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 2: Assign left = rng.tz_convert(...)

```python
left = rng.tz_convert('US/Eastern')
```

**Verification:**
```python
assert result.tz == left.tz
```

### Step 3: Assign right = rng.tz_convert(...)

```python
right = rng.tz_convert('Europe/Berlin')
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 4: Assign result = left.join(...)

```python
result = left.join(left[:-5], how=join_type)
```

**Verification:**
```python
assert result.tz is timezone.utc
```

### Step 5: Assign result = left.join(...)

```python
result = left.join(right[:-5], how=join_type)
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```


## Complete Example

```python
# Setup
# Fixtures: join_type

# Workflow
rng = date_range('1/1/2011', periods=100, freq='h', tz='utc')
left = rng.tz_convert('US/Eastern')
right = rng.tz_convert('Europe/Berlin')
result = left.join(left[:-5], how=join_type)
assert isinstance(result, DatetimeIndex)
assert result.tz == left.tz
result = left.join(right[:-5], how=join_type)
assert isinstance(result, DatetimeIndex)
assert result.tz is timezone.utc
```

## Next Steps


---

*Source: test_join.py:59 | Complexity: Intermediate | Last updated: 2026-06-02*