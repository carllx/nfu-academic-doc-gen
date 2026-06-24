# How To: Dti Shift Across Dst

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti shift across dst

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2013-11-03', tz='America/Chicago', periods=7, freq='h', unit=unit)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(index=idx[:-1], dtype=object)
```

### Step 3: Assign result = ser.shift(...)

```python
result = ser.shift(freq='h')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(index=idx[1:], dtype=object)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
idx = date_range('2013-11-03', tz='America/Chicago', periods=7, freq='h', unit=unit)
ser = Series(index=idx[:-1], dtype=object)
result = ser.shift(freq='h')
expected = Series(index=idx[1:], dtype=object)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_shift.py:105 | Complexity: Intermediate | Last updated: 2026-06-02*