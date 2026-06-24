# How To: Round Int64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test round int64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.period`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: timestamp, freq
```

## Step-by-Step Guide

### Step 1: Assign dt = Timestamp.as_unit(...)

```python
dt = Timestamp(timestamp).as_unit('ns')
```

**Verification:**
```python
assert result._value % unit == 0, f'floor not a {freq} multiple'
```

### Step 2: Assign unit = value

```python
unit = to_offset(freq).nanos
```

**Verification:**
```python
assert 0 <= dt._value - result._value < unit, 'floor error'
```

### Step 3: Assign result = dt.floor(...)

```python
result = dt.floor(freq)
```

**Verification:**
```python
assert result._value % unit == 0, f'ceil not a {freq} multiple'
```

### Step 4: Assign result = dt.ceil(...)

```python
result = dt.ceil(freq)
```

**Verification:**
```python
assert 0 <= result._value - dt._value < unit, 'ceil error'
```

### Step 5: Assign result = dt.round(...)

```python
result = dt.round(freq)
```

**Verification:**
```python
assert result._value % unit == 0, f'round not a {freq} multiple'
```


## Complete Example

```python
# Setup
# Fixtures: timestamp, freq

# Workflow
dt = Timestamp(timestamp).as_unit('ns')
unit = to_offset(freq).nanos
result = dt.floor(freq)
assert result._value % unit == 0, f'floor not a {freq} multiple'
assert 0 <= dt._value - result._value < unit, 'floor error'
result = dt.ceil(freq)
assert result._value % unit == 0, f'ceil not a {freq} multiple'
assert 0 <= result._value - dt._value < unit, 'ceil error'
result = dt.round(freq)
assert result._value % unit == 0, f'round not a {freq} multiple'
assert abs(result._value - dt._value) <= unit // 2, 'round error'
if unit % 2 == 0 and abs(result._value - dt._value) == unit // 2:
    assert result._value // unit % 2 == 0, 'round half to even error'
```

## Next Steps


---

*Source: test_round.py:255 | Complexity: Intermediate | Last updated: 2026-06-02*