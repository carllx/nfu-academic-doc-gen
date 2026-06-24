# How To: Constructor Dtype Tz Mismatch Raises

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor dtype tz mismatch raises

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

### Step 1: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(['2013-01-01', '2013-01-02'], dtype='datetime64[ns, US/Eastern]')
```

### Step 2: Assign msg = 'cannot supply both a tz and a timezone-naive dtype \\(i\\.e\\. datetime64\\[ns\\]\\)'

```python
msg = 'cannot supply both a tz and a timezone-naive dtype \\(i\\.e\\. datetime64\\[ns\\]\\)'
```

### Step 3: Assign msg = 'data is already tz-aware US/Eastern, unable to set specified tz: CET'

```python
msg = 'data is already tz-aware US/Eastern, unable to set specified tz: CET'
```

### Step 4: Assign msg = 'cannot supply both a tz and a dtype with a tz'

```python
msg = 'cannot supply both a tz and a dtype with a tz'
```

### Step 5: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex(idx, dtype='datetime64[ns, US/Eastern]')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, result)
```

### Step 7: Call DatetimeIndex()

```python
DatetimeIndex(idx, dtype='datetime64[ns]')
```

### Step 8: Call DatetimeIndex()

```python
DatetimeIndex(idx, dtype='datetime64[ns, CET]')
```

### Step 9: Call DatetimeIndex()

```python
DatetimeIndex(idx, tz='CET', dtype='datetime64[ns, US/Eastern]')
```


## Complete Example

```python
# Workflow
idx = DatetimeIndex(['2013-01-01', '2013-01-02'], dtype='datetime64[ns, US/Eastern]')
msg = 'cannot supply both a tz and a timezone-naive dtype \\(i\\.e\\. datetime64\\[ns\\]\\)'
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(idx, dtype='datetime64[ns]')
msg = 'data is already tz-aware US/Eastern, unable to set specified tz: CET'
with pytest.raises(TypeError, match=msg):
    DatetimeIndex(idx, dtype='datetime64[ns, CET]')
msg = 'cannot supply both a tz and a dtype with a tz'
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(idx, tz='CET', dtype='datetime64[ns, US/Eastern]')
result = DatetimeIndex(idx, dtype='datetime64[ns, US/Eastern]')
tm.assert_index_equal(idx, result)
```

## Next Steps


---

*Source: test_constructors.py:717 | Complexity: Advanced | Last updated: 2026-06-02*