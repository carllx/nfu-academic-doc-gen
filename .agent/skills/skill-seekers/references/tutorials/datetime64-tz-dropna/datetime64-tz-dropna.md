# How To: Datetime64 Tz Dropna

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime64 tz dropna

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([Timestamp('2011-01-01 10:00'), NaT, Timestamp('2011-01-03 10:00'), NaT], dtype=f'M8[{unit}]')
```

**Verification:**
```python
assert ser.dtype == f'datetime64[{unit}, Asia/Tokyo]'
```

### Step 2: Assign result = ser.dropna(...)

```python
result = ser.dropna()
```

**Verification:**
```python
assert result.dtype == f'datetime64[{unit}, Asia/Tokyo]'
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-03 10:00')], index=[0, 2], dtype=f'M8[{unit}]')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign idx = DatetimeIndex.as_unit(...)

```python
idx = DatetimeIndex(['2011-01-01 10:00', NaT, '2011-01-03 10:00', NaT], tz='Asia/Tokyo').as_unit(unit)
```

### Step 6: Assign ser = Series(...)

```python
ser = Series(idx)
```

**Verification:**
```python
assert ser.dtype == f'datetime64[{unit}, Asia/Tokyo]'
```

### Step 7: Assign result = ser.dropna(...)

```python
result = ser.dropna()
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-03 10:00', tz='Asia/Tokyo')], index=[0, 2], dtype=f'datetime64[{unit}, Asia/Tokyo]')
```

**Verification:**
```python
assert result.dtype == f'datetime64[{unit}, Asia/Tokyo]'
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
ser = Series([Timestamp('2011-01-01 10:00'), NaT, Timestamp('2011-01-03 10:00'), NaT], dtype=f'M8[{unit}]')
result = ser.dropna()
expected = Series([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-03 10:00')], index=[0, 2], dtype=f'M8[{unit}]')
tm.assert_series_equal(result, expected)
idx = DatetimeIndex(['2011-01-01 10:00', NaT, '2011-01-03 10:00', NaT], tz='Asia/Tokyo').as_unit(unit)
ser = Series(idx)
assert ser.dtype == f'datetime64[{unit}, Asia/Tokyo]'
result = ser.dropna()
expected = Series([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-03 10:00', tz='Asia/Tokyo')], index=[0, 2], dtype=f'datetime64[{unit}, Asia/Tokyo]')
assert result.dtype == f'datetime64[{unit}, Asia/Tokyo]'
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_dropna.py:71 | Complexity: Advanced | Last updated: 2026-06-02*