# How To: Construction Index With Mixed Timezones With Nat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction index with mixed timezones with NaT

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

### Step 1: Assign result = Index(...)

```python
result = Index([pd.NaT, Timestamp('2011-01-01'), pd.NaT, Timestamp('2011-01-02')], name='idx')
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 2: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([pd.NaT, Timestamp('2011-01-01'), pd.NaT, Timestamp('2011-01-02')], name='idx')
```

**Verification:**
```python
assert result.tz is None
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 4: Assign result = Index(...)

```python
result = Index([pd.NaT, Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), pd.NaT, Timestamp('2011-01-02 10:00', tz='Asia/Tokyo')], name='idx')
```

**Verification:**
```python
assert result.tz is not None
```

### Step 5: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([pd.NaT, Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-01-02 10:00')], tz='Asia/Tokyo', name='idx')
```

**Verification:**
```python
assert result.tz == exp.tz
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 7: Assign result = Index(...)

```python
result = Index([Timestamp('2011-01-01 10:00', tz='US/Eastern'), pd.NaT, Timestamp('2011-08-01 10:00', tz='US/Eastern')], name='idx')
```

**Verification:**
```python
assert result.tz is not None
```

### Step 8: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-08-01 10:00')], tz='US/Eastern', name='idx')
```

**Verification:**
```python
assert result.tz == exp.tz
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert not isinstance(result, DatetimeIndex)
```

### Step 10: Assign result = Index(...)

```python
result = Index([pd.NaT, Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
```

**Verification:**
```python
assert not isinstance(result, DatetimeIndex)
```

### Step 11: Assign exp = Index(...)

```python
exp = Index([pd.NaT, Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], dtype='object', name='idx')
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert result.tz is None
```

### Step 13: Assign result = Index(...)

```python
result = Index([pd.NaT, Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
```

### Step 14: Assign exp = Index(...)

```python
exp = Index([pd.NaT, Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], dtype='object', name='idx')
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert not isinstance(result, DatetimeIndex)
```

### Step 16: Assign result = Index(...)

```python
result = Index([pd.NaT, pd.NaT], name='idx')
```

### Step 17: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([pd.NaT, pd.NaT], name='idx')
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp, exact=True)
```

**Verification:**
```python
assert isinstance(result, DatetimeIndex)
```


## Complete Example

```python
# Workflow
result = Index([pd.NaT, Timestamp('2011-01-01'), pd.NaT, Timestamp('2011-01-02')], name='idx')
exp = DatetimeIndex([pd.NaT, Timestamp('2011-01-01'), pd.NaT, Timestamp('2011-01-02')], name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
assert result.tz is None
result = Index([pd.NaT, Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), pd.NaT, Timestamp('2011-01-02 10:00', tz='Asia/Tokyo')], name='idx')
exp = DatetimeIndex([pd.NaT, Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-01-02 10:00')], tz='Asia/Tokyo', name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
assert result.tz is not None
assert result.tz == exp.tz
result = Index([Timestamp('2011-01-01 10:00', tz='US/Eastern'), pd.NaT, Timestamp('2011-08-01 10:00', tz='US/Eastern')], name='idx')
exp = DatetimeIndex([Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-08-01 10:00')], tz='US/Eastern', name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
assert result.tz is not None
assert result.tz == exp.tz
result = Index([pd.NaT, Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
exp = Index([pd.NaT, Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], dtype='object', name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert not isinstance(result, DatetimeIndex)
result = Index([pd.NaT, Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], name='idx')
exp = Index([pd.NaT, Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), pd.NaT, Timestamp('2011-01-02 10:00', tz='US/Eastern')], dtype='object', name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert not isinstance(result, DatetimeIndex)
result = Index([pd.NaT, pd.NaT], name='idx')
exp = DatetimeIndex([pd.NaT, pd.NaT], name='idx')
tm.assert_index_equal(result, exp, exact=True)
assert isinstance(result, DatetimeIndex)
assert result.tz is None
```

## Next Steps


---

*Source: test_constructors.py:322 | Complexity: Advanced | Last updated: 2026-06-02*