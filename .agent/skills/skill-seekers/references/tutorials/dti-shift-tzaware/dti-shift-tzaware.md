# How To: Dti Shift Tzaware

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti shift tzaware

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
# Fixtures: tz_naive_fixture, unit
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

### Step 2: Assign idx = DatetimeIndex.as_unit(...)

```python
idx = DatetimeIndex([], name='xxx', tz=tz).as_unit(unit)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(0, freq='h'), idx)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(3, freq='h'), idx)
```

### Step 5: Assign idx = DatetimeIndex.as_unit(...)

```python
idx = DatetimeIndex(['2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00'], name='xxx', tz=tz, freq='h').as_unit(unit)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(0, freq='h'), idx)
```

### Step 7: Assign exp = DatetimeIndex.as_unit(...)

```python
exp = DatetimeIndex(['2011-01-01 13:00', '2011-01-01 14:00', '2011-01-01 15:00'], name='xxx', tz=tz, freq='h').as_unit(unit)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(3, freq='h'), exp)
```

### Step 9: Assign exp = DatetimeIndex.as_unit(...)

```python
exp = DatetimeIndex(['2011-01-01 07:00', '2011-01-01 08:00', '2011-01-01 09:00'], name='xxx', tz=tz, freq='h').as_unit(unit)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.shift(-3, freq='h'), exp)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture, unit

# Workflow
tz = tz_naive_fixture
idx = DatetimeIndex([], name='xxx', tz=tz).as_unit(unit)
tm.assert_index_equal(idx.shift(0, freq='h'), idx)
tm.assert_index_equal(idx.shift(3, freq='h'), idx)
idx = DatetimeIndex(['2011-01-01 10:00', '2011-01-01 11:00', '2011-01-01 12:00'], name='xxx', tz=tz, freq='h').as_unit(unit)
tm.assert_index_equal(idx.shift(0, freq='h'), idx)
exp = DatetimeIndex(['2011-01-01 13:00', '2011-01-01 14:00', '2011-01-01 15:00'], name='xxx', tz=tz, freq='h').as_unit(unit)
tm.assert_index_equal(idx.shift(3, freq='h'), exp)
exp = DatetimeIndex(['2011-01-01 07:00', '2011-01-01 08:00', '2011-01-01 09:00'], name='xxx', tz=tz, freq='h').as_unit(unit)
tm.assert_index_equal(idx.shift(-3, freq='h'), exp)
```

## Next Steps


---

*Source: test_shift.py:23 | Complexity: Advanced | Last updated: 2026-06-02*