# How To: Constructor Start End With Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor start end with tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `operator`
- `dateutil`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign start = Timestamp(...)

```python
start = Timestamp('2013-01-01 06:00:00', tz='America/Los_Angeles')
```

**Verification:**
```python
assert pytz.timezone('America/Los_Angeles') is result.tz
```

### Step 2: Assign end = Timestamp(...)

```python
end = Timestamp('2013-01-02 06:00:00', tz='America/Los_Angeles')
```

### Step 3: Assign result = date_range(...)

```python
result = date_range(freq='D', start=start, end=end, tz=tz)
```

### Step 4: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2013-01-01 06:00:00', '2013-01-02 06:00:00'], dtype='M8[ns, America/Los_Angeles]', freq='D')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

**Verification:**
```python
assert pytz.timezone('America/Los_Angeles') is result.tz
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
start = Timestamp('2013-01-01 06:00:00', tz='America/Los_Angeles')
end = Timestamp('2013-01-02 06:00:00', tz='America/Los_Angeles')
result = date_range(freq='D', start=start, end=end, tz=tz)
expected = DatetimeIndex(['2013-01-01 06:00:00', '2013-01-02 06:00:00'], dtype='M8[ns, America/Los_Angeles]', freq='D')
tm.assert_index_equal(result, expected)
assert pytz.timezone('America/Los_Angeles') is result.tz
```

## Next Steps


---

*Source: test_constructors.py:771 | Complexity: Intermediate | Last updated: 2026-06-02*