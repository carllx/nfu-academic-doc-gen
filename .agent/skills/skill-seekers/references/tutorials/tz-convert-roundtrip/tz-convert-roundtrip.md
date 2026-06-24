# How To: Tz Convert Roundtrip

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tz convert roundtrip

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `dateutil`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`

**Setup Required:**
```python
# Fixtures: stamp, tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

**Verification:**
```python
assert reset == Timestamp(stamp)
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(stamp, tz='UTC')
```

**Verification:**
```python
assert reset.tzinfo is None
```

### Step 3: Assign converted = ts.tz_convert(...)

```python
converted = ts.tz_convert(tz)
```

**Verification:**
```python
assert reset == converted.tz_convert('UTC').tz_localize(None)
```

### Step 4: Assign reset = converted.tz_convert(...)

```python
reset = converted.tz_convert(None)
```

**Verification:**
```python
assert reset == Timestamp(stamp)
```


## Complete Example

```python
# Setup
# Fixtures: stamp, tz_aware_fixture

# Workflow
tz = tz_aware_fixture
ts = Timestamp(stamp, tz='UTC')
converted = ts.tz_convert(tz)
reset = converted.tz_convert(None)
assert reset == Timestamp(stamp)
assert reset.tzinfo is None
assert reset == converted.tz_convert('UTC').tz_localize(None)
```

## Next Steps


---

*Source: test_tz_convert.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*