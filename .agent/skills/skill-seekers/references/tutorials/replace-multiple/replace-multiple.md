# How To: Replace Multiple

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace multiple

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas.util._test_decorators`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-01-01 09:00:00.000000123', tz=tz)
```

### Step 3: Assign result = ts.replace(...)

```python
result = ts.replace(year=2015, month=2, day=2, hour=0, minute=5, second=5, microsecond=5, nanosecond=5)
```

### Step 4: Assign expected = Timestamp(...)

```python
expected = Timestamp('2015-02-02 00:05:05.000005005', tz=tz)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture

# Workflow
tz = tz_aware_fixture
ts = Timestamp('2016-01-01 09:00:00.000000123', tz=tz)
result = ts.replace(year=2015, month=2, day=2, hour=0, minute=5, second=5, microsecond=5, nanosecond=5)
expected = Timestamp('2015-02-02 00:05:05.000005005', tz=tz)
assert result == expected
```

## Next Steps


---

*Source: test_replace.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*