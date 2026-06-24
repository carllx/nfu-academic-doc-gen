# How To: Dti Shift Freqs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti shift freqs

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

### Step 1: Assign drange = date_range(...)

```python
drange = date_range('20130101', periods=5, unit=unit)
```

### Step 2: Assign result = drange.shift(...)

```python
result = drange.shift(1)
```

### Step 3: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05', '2013-01-06'], dtype=f'M8[{unit}]', freq='D')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = drange.shift(...)

```python
result = drange.shift(-1)
```

### Step 6: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2012-12-31', '2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04'], dtype=f'M8[{unit}]', freq='D')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign result = drange.shift(...)

```python
result = drange.shift(3, freq='2D')
```

### Step 9: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2013-01-07', '2013-01-08', '2013-01-09', '2013-01-10', '2013-01-11'], dtype=f'M8[{unit}]', freq='D')
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
drange = date_range('20130101', periods=5, unit=unit)
result = drange.shift(1)
expected = DatetimeIndex(['2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05', '2013-01-06'], dtype=f'M8[{unit}]', freq='D')
tm.assert_index_equal(result, expected)
result = drange.shift(-1)
expected = DatetimeIndex(['2012-12-31', '2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04'], dtype=f'M8[{unit}]', freq='D')
tm.assert_index_equal(result, expected)
result = drange.shift(3, freq='2D')
expected = DatetimeIndex(['2013-01-07', '2013-01-08', '2013-01-09', '2013-01-10', '2013-01-11'], dtype=f'M8[{unit}]', freq='D')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_shift.py:52 | Complexity: Advanced | Last updated: 2026-06-02*