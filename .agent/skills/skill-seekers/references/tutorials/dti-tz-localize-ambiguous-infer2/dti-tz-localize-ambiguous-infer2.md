# How To: Dti Tz Localize Ambiguous Infer2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti tz localize ambiguous infer2

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
# Fixtures: tz, unit
```

## Step-by-Step Guide

### Step 1: Assign dr = date_range(...)

```python
dr = date_range(datetime(2011, 11, 6, 0), periods=5, freq=offsets.Hour(), tz=tz, unit=unit)
```

### Step 2: Assign times = value

```python
times = ['11/06/2011 00:00', '11/06/2011 01:00', '11/06/2011 01:00', '11/06/2011 02:00', '11/06/2011 03:00']
```

### Step 3: Assign di = DatetimeIndex.as_unit(...)

```python
di = DatetimeIndex(times).as_unit(unit)
```

### Step 4: Assign result = di.tz_localize(...)

```python
result = di.tz_localize(tz, ambiguous='infer')
```

### Step 5: Assign expected = dr._with_freq(...)

```python
expected = dr._with_freq(None)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign result2 = DatetimeIndex.as_unit(...)

```python
result2 = DatetimeIndex(times, tz=tz, ambiguous='infer').as_unit(unit)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz, unit

# Workflow
dr = date_range(datetime(2011, 11, 6, 0), periods=5, freq=offsets.Hour(), tz=tz, unit=unit)
times = ['11/06/2011 00:00', '11/06/2011 01:00', '11/06/2011 01:00', '11/06/2011 02:00', '11/06/2011 03:00']
di = DatetimeIndex(times).as_unit(unit)
result = di.tz_localize(tz, ambiguous='infer')
expected = dr._with_freq(None)
tm.assert_index_equal(result, expected)
result2 = DatetimeIndex(times, tz=tz, ambiguous='infer').as_unit(unit)
tm.assert_index_equal(result2, expected)
```

## Next Steps


---

*Source: test_tz_localize.py:100 | Complexity: Advanced | Last updated: 2026-06-02*