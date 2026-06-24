# How To: Tz Localize Roundtrip

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tz localize roundtrip

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pytz.exceptions`
- `pandas._libs.tslibs.dtypes`
- `pandas.errors`
- `pandas`
- `zoneinfo`

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
assert localized == Timestamp(stamp, tz=tz)
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp(stamp)
```

**Verification:**
```python
assert reset == ts
```

### Step 3: Assign localized = ts.tz_localize(...)

```python
localized = ts.tz_localize(tz)
```

**Verification:**
```python
assert reset.tzinfo is None
```

### Step 4: Assign msg = 'Cannot localize tz-aware Timestamp'

```python
msg = 'Cannot localize tz-aware Timestamp'
```

### Step 5: Assign reset = localized.tz_localize(...)

```python
reset = localized.tz_localize(None)
```

**Verification:**
```python
assert reset == ts
```

### Step 6: Call localized.tz_localize()

```python
localized.tz_localize(tz)
```


## Complete Example

```python
# Setup
# Fixtures: stamp, tz_aware_fixture

# Workflow
tz = tz_aware_fixture
ts = Timestamp(stamp)
localized = ts.tz_localize(tz)
assert localized == Timestamp(stamp, tz=tz)
msg = 'Cannot localize tz-aware Timestamp'
with pytest.raises(TypeError, match=msg):
    localized.tz_localize(tz)
reset = localized.tz_localize(None)
assert reset == ts
assert reset.tzinfo is None
```

## Next Steps


---

*Source: test_tz_localize.py:192 | Complexity: Intermediate | Last updated: 2026-06-02*