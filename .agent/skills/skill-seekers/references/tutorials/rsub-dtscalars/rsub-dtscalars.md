# How To: Rsub Dtscalars

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rsub dtscalars

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign td = Timedelta(...)

```python
td = Timedelta(1235345642000)
```

**Verification:**
```python
assert other - ts == td
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp('2021-01-01', tz=tz_naive_fixture)
```

**Verification:**
```python
assert other.to_pydatetime() - ts == td
```

### Step 3: Assign other = value

```python
other = ts + td
```

**Verification:**
```python
assert other.to_datetime64() - ts == td
```

### Step 4: Assign msg = 'Cannot subtract tz-naive and tz-aware datetime-like objects'

```python
msg = 'Cannot subtract tz-naive and tz-aware datetime-like objects'
```

### Step 5: other.to_datetime64() - ts

```python
other.to_datetime64() - ts
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
td = Timedelta(1235345642000)
ts = Timestamp('2021-01-01', tz=tz_naive_fixture)
other = ts + td
assert other - ts == td
assert other.to_pydatetime() - ts == td
if tz_naive_fixture is None:
    assert other.to_datetime64() - ts == td
else:
    msg = 'Cannot subtract tz-naive and tz-aware datetime-like objects'
    with pytest.raises(TypeError, match=msg):
        other.to_datetime64() - ts
```

## Next Steps


---

*Source: test_arithmetic.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*