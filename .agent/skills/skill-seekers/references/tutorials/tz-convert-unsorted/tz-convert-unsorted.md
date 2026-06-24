# How To: Tz Convert Unsorted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tz convert unsorted

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tzstr
```

## Step-by-Step Guide

### Step 1: Assign dr = date_range(...)

```python
dr = date_range('2012-03-09', freq='h', periods=100, tz='utc')
```

### Step 2: Assign dr = dr.tz_convert(...)

```python
dr = dr.tz_convert(tzstr)
```

### Step 3: Assign result = value

```python
result = dr[::-1].hour
```

### Step 4: Assign exp = value

```python
exp = dr.hour[::-1]
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, exp)
```


## Complete Example

```python
# Setup
# Fixtures: tzstr

# Workflow
dr = date_range('2012-03-09', freq='h', periods=100, tz='utc')
dr = dr.tz_convert(tzstr)
result = dr[::-1].hour
exp = dr.hour[::-1]
tm.assert_almost_equal(result, exp)
```

## Next Steps


---

*Source: test_tz_convert.py:277 | Complexity: Intermediate | Last updated: 2026-06-02*