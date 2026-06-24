# How To: Dti Tz Localize Roundtrip

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti tz localize roundtrip

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `zoneinfo`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range(start='2014-06-01', end='2014-08-30', freq='15min')
```

**Verification:**
```python
assert reset.tzinfo is None
```

### Step 2: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

### Step 3: Assign localized = idx.tz_localize(...)

```python
localized = idx.tz_localize(tz)
```

### Step 4: Assign reset = localized.tz_localize(...)

```python
reset = localized.tz_localize(None)
```

**Verification:**
```python
assert reset.tzinfo is None
```

### Step 5: Assign expected = idx._with_freq(...)

```python
expected = idx._with_freq(None)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(reset, expected)
```

### Step 7: Call localized.tz_localize()

```python
localized.tz_localize(tz)
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture

# Workflow
idx = date_range(start='2014-06-01', end='2014-08-30', freq='15min')
tz = tz_aware_fixture
localized = idx.tz_localize(tz)
with pytest.raises(TypeError, match='Already tz-aware, use tz_convert to convert'):
    localized.tz_localize(tz)
reset = localized.tz_localize(None)
assert reset.tzinfo is None
expected = idx._with_freq(None)
tm.assert_index_equal(reset, expected)
```

## Next Steps


---

*Source: test_tz_localize.py:210 | Complexity: Intermediate | Last updated: 2026-06-02*