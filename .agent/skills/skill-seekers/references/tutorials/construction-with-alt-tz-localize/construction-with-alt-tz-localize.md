# How To: Construction With Alt Tz Localize

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test construction with alt tz localize

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: kwargs, tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

### Step 2: Assign i = date_range(...)

```python
i = date_range('20130101', periods=5, freq='h', tz=tz)
```

### Step 3: Assign i = i._with_freq(...)

```python
i = i._with_freq(None)
```

### Step 4: Assign kwargs = value

```python
kwargs = {key: attrgetter(val)(i) for key, val in kwargs.items()}
```

### Step 5: Assign i2 = DatetimeIndex(...)

```python
i2 = DatetimeIndex(i.tz_localize(None).asi8, tz='UTC')
```

### Step 6: Assign expected = i.tz_localize.tz_localize(...)

```python
expected = i.tz_localize(None).tz_localize('UTC')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(i2, expected)
```

### Step 8: Assign msg = 'cannot supply both a tz and a dtype with a tz'

```python
msg = 'cannot supply both a tz and a dtype with a tz'
```

### Step 9: Assign result = DatetimeIndex.tz_convert(...)

```python
result = DatetimeIndex(i.asi8, tz='UTC').tz_convert(kwargs['tz'])
```

### Step 10: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(i, **kwargs)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Call DatetimeIndex()

```python
DatetimeIndex(i.tz_localize(None).asi8, dtype=i.dtype, tz='US/Pacific')
```


## Complete Example

```python
# Setup
# Fixtures: kwargs, tz_aware_fixture

# Workflow
tz = tz_aware_fixture
i = date_range('20130101', periods=5, freq='h', tz=tz)
i = i._with_freq(None)
kwargs = {key: attrgetter(val)(i) for key, val in kwargs.items()}
if 'tz' in kwargs:
    result = DatetimeIndex(i.asi8, tz='UTC').tz_convert(kwargs['tz'])
    expected = DatetimeIndex(i, **kwargs)
    tm.assert_index_equal(result, expected)
i2 = DatetimeIndex(i.tz_localize(None).asi8, tz='UTC')
expected = i.tz_localize(None).tz_localize('UTC')
tm.assert_index_equal(i2, expected)
msg = 'cannot supply both a tz and a dtype with a tz'
with pytest.raises(ValueError, match=msg):
    DatetimeIndex(i.tz_localize(None).asi8, dtype=i.dtype, tz='US/Pacific')
```

## Next Steps


---

*Source: test_constructors.py:194 | Complexity: Advanced | Last updated: 2026-06-02*