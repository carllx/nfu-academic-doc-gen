# How To: Dti Tdi Numeric Ops

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti tdi numeric ops

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`


## Step-by-Step Guide

### Step 1: Assign tdi = TimedeltaIndex(...)

```python
tdi = TimedeltaIndex(['1 days', NaT, '2 days'], name='foo')
```

### Step 2: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('20130101', periods=3, name='bar')
```

### Step 3: Assign result = value

```python
result = tdi - tdi
```

### Step 4: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['0 days', NaT, '0 days'], name='foo')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = tdi + tdi
```

### Step 7: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['2 days', NaT, '4 days'], name='foo')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = dti - tdi
```

### Step 10: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['20121231', NaT, '20130101'], dtype='M8[ns]')
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
tdi = TimedeltaIndex(['1 days', NaT, '2 days'], name='foo')
dti = pd.date_range('20130101', periods=3, name='bar')
result = tdi - tdi
expected = TimedeltaIndex(['0 days', NaT, '0 days'], name='foo')
tm.assert_index_equal(result, expected)
result = tdi + tdi
expected = TimedeltaIndex(['2 days', NaT, '4 days'], name='foo')
tm.assert_index_equal(result, expected)
result = dti - tdi
expected = DatetimeIndex(['20121231', NaT, '20130101'], dtype='M8[ns]')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta64.py:443 | Complexity: Advanced | Last updated: 2026-06-02*