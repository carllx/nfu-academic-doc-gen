# How To: Insert Empty Preserves Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert empty preserves freq

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

**Verification:**
```python
assert result.freq == dti.freq
```

### Step 2: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([], tz=tz, freq='D')
```

**Verification:**
```python
assert result.freq is None
```

### Step 3: Assign item = Timestamp.tz_localize(...)

```python
item = Timestamp('2017-04-05').tz_localize(tz)
```

### Step 4: Assign result = dti.insert(...)

```python
result = dti.insert(0, item)
```

**Verification:**
```python
assert result.freq == dti.freq
```

### Step 5: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([], tz=tz, freq='W-THU')
```

### Step 6: Assign result = dti.insert(...)

```python
result = dti.insert(0, item)
```

**Verification:**
```python
assert result.freq is None
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = tz_naive_fixture
dti = DatetimeIndex([], tz=tz, freq='D')
item = Timestamp('2017-04-05').tz_localize(tz)
result = dti.insert(0, item)
assert result.freq == dti.freq
dti = DatetimeIndex([], tz=tz, freq='W-THU')
result = dti.insert(0, item)
assert result.freq is None
```

## Next Steps


---

*Source: test_insert.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*