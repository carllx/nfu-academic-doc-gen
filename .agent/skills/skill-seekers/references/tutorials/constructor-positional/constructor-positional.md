# How To: Constructor Positional

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor positional

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `zoneinfo`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas.compat`
- `pandas.errors`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign msg = value

```python
msg = "'NoneType' object cannot be interpreted as an integer" if PY310 else 'an integer is required'
```

**Verification:**
```python
assert repr(Timestamp(2015, 11, 12)) == repr(Timestamp('20151112'))
```

### Step 2: Assign msg = 'month must be in 1..12'

```python
msg = 'month must be in 1..12'
```

**Verification:**
```python
assert repr(Timestamp(2015, 11, 12, 1, 2, 3, 999999)) == repr(Timestamp('2015-11-12 01:02:03.999999'))
```

### Step 3: Call Timestamp()

```python
Timestamp(2000, 1)
```

### Step 4: Call Timestamp()

```python
Timestamp(2000, 0, 1)
```

### Step 5: Call Timestamp()

```python
Timestamp(2000, 13, 1)
```

### Step 6: Assign msg = 'must be in range 1..31 for month 1 in year 2000'

```python
msg = 'must be in range 1..31 for month 1 in year 2000'
```

### Step 7: Assign msg = 'day is out of range for month'

```python
msg = 'day is out of range for month'
```

### Step 8: Call Timestamp()

```python
Timestamp(2000, 1, 0)
```

### Step 9: Call Timestamp()

```python
Timestamp(2000, 1, 32)
```


## Complete Example

```python
# Workflow
msg = "'NoneType' object cannot be interpreted as an integer" if PY310 else 'an integer is required'
with pytest.raises(TypeError, match=msg):
    Timestamp(2000, 1)
msg = 'month must be in 1..12'
with pytest.raises(ValueError, match=msg):
    Timestamp(2000, 0, 1)
with pytest.raises(ValueError, match=msg):
    Timestamp(2000, 13, 1)
if PY314:
    msg = 'must be in range 1..31 for month 1 in year 2000'
else:
    msg = 'day is out of range for month'
with pytest.raises(ValueError, match=msg):
    Timestamp(2000, 1, 0)
with pytest.raises(ValueError, match=msg):
    Timestamp(2000, 1, 32)
assert repr(Timestamp(2015, 11, 12)) == repr(Timestamp('20151112'))
assert repr(Timestamp(2015, 11, 12, 1, 2, 3, 999999)) == repr(Timestamp('2015-11-12 01:02:03.999999'))
```

## Next Steps


---

*Source: test_constructors.py:215 | Complexity: Advanced | Last updated: 2026-06-02*