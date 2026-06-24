# How To: Construction Dti With Mixed Timezones

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction dti with mixed timezones

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `operator`
- `dateutil`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex([Timestamp('2011-01-01'), Timestamp('2011-01-02')], name='idx')
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 2: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([Timestamp('2011-01-01'), Timestamp('2011-01-02')], name='idx')
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 4: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='Asia/Tokyo')], name='idx')
```

### Step 5: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00')], tz='Asia/Tokyo', name='idx')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 7: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='US/Eastern'), Timestamp('2011-08-01 10:00', tz='US/Eastern')], name='idx')
```

### Step 8: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-08-01 10:00')], tz='US/Eastern', name='idx')
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 10: Assign msg = 'cannot be converted to datetime64'

```python
msg = 'cannot be converted to datetime64'
```

### Step 11: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='Asia/Tokyo', name='idx')
```

### Step 12: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern').tz_convert('Asia/Tokyo')], tz='Asia/Tokyo', name='idx')
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(dti, expected)
```

### Step 14: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='US/Eastern', name='idx')
```

### Step 15: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo').tz_convert('US/Eastern'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='US/Eastern', name='idx')
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(dti, expected)
```

### Step 17: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], dtype='M8[ns, US/Eastern]', name='idx')
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(dti, expected)
```

### Step 19: Call DatetimeIndex()

```python
DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
```


## Complete Example

```python
# Workflow
result = DatetimeIndex([Timestamp('2011-01-01'), Timestamp('2011-01-02')], name='idx')
exp = DatetimeIndex([Timestamp('2011-01-01'), Timestamp('2011-01-02')], name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
result = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='Asia/Tokyo')], name='idx')
exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00')], tz='Asia/Tokyo', name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
result = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='US/Eastern'), Timestamp('2011-08-01 10:00', tz='US/Eastern')], name='idx')
exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-08-01 10:00')], tz='US/Eastern', name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
msg = 'cannot be converted to datetime64'
with pytest.raises(ValueError, match=msg):
    DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
dti = DatetimeIndex([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='Asia/Tokyo', name='idx')
expected = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern').tz_convert('Asia/Tokyo')], tz='Asia/Tokyo', name='idx')
tm.assert_index_equal(dti, expected)
dti = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='US/Eastern', name='idx')
expected = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo').tz_convert('US/Eastern'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], tz='US/Eastern', name='idx')
tm.assert_index_equal(dti, expected)
dti = DatetimeIndex([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-02 10:00', tz='US/Eastern')], dtype='M8[ns, US/Eastern]', name='idx')
tm.assert_index_equal(dti, expected)
```

## Next Steps


---

*Source: test_constructors.py:432 | Complexity: Advanced | Last updated: 2026-06-02*