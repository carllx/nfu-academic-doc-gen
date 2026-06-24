# How To: With Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test with tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign start = datetime(...)

```python
start = datetime(2011, 3, 12, tzinfo=pytz.utc)
```

**Verification:**
```python
assert dr.tz is pytz.utc
```

### Step 2: Assign dr = bdate_range(...)

```python
dr = bdate_range(start, periods=50, freq=pd.offsets.Hour())
```

**Verification:**
```python
assert central.tz is tz
```

### Step 3: Assign dr = bdate_range(...)

```python
dr = bdate_range('1/1/2005', '1/1/2009', tz=pytz.utc)
```

**Verification:**
```python
assert central[0].tz is comp
```

### Step 4: Assign dr = bdate_range(...)

```python
dr = bdate_range('1/1/2005', '1/1/2009', tz=tz)
```

**Verification:**
```python
assert central[0].tz is comp
```

### Step 5: Assign central = dr.tz_convert(...)

```python
central = dr.tz_convert(tz)
```

**Verification:**
```python
assert central.tz is tz
```

### Step 6: Assign naive = unknown.to_pydatetime.replace(...)

```python
naive = central[0].to_pydatetime().replace(tzinfo=None)
```

### Step 7: Assign comp = value

```python
comp = conversion.localize_pydatetime(naive, tz).tzinfo
```

**Verification:**
```python
assert central[0].tz is comp
```

### Step 8: Assign naive = unknown.to_pydatetime.replace(...)

```python
naive = dr[0].to_pydatetime().replace(tzinfo=None)
```

### Step 9: Assign comp = value

```python
comp = conversion.localize_pydatetime(naive, tz).tzinfo
```

**Verification:**
```python
assert central[0].tz is comp
```

### Step 10: Assign dr = bdate_range(...)

```python
dr = bdate_range(datetime(2005, 1, 1, tzinfo=pytz.utc), datetime(2009, 1, 1, tzinfo=pytz.utc))
```

### Step 11: Assign msg = 'Start and end cannot both be tz-aware with different timezones'

```python
msg = 'Start and end cannot both be tz-aware with different timezones'
```

### Step 12: Call bdate_range()

```python
bdate_range(datetime(2005, 1, 1, tzinfo=pytz.utc), '1/1/2009', tz=tz)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
start = datetime(2011, 3, 12, tzinfo=pytz.utc)
dr = bdate_range(start, periods=50, freq=pd.offsets.Hour())
assert dr.tz is pytz.utc
dr = bdate_range('1/1/2005', '1/1/2009', tz=pytz.utc)
dr = bdate_range('1/1/2005', '1/1/2009', tz=tz)
central = dr.tz_convert(tz)
assert central.tz is tz
naive = central[0].to_pydatetime().replace(tzinfo=None)
comp = conversion.localize_pydatetime(naive, tz).tzinfo
assert central[0].tz is comp
naive = dr[0].to_pydatetime().replace(tzinfo=None)
comp = conversion.localize_pydatetime(naive, tz).tzinfo
assert central[0].tz is comp
dr = bdate_range(datetime(2005, 1, 1, tzinfo=pytz.utc), datetime(2009, 1, 1, tzinfo=pytz.utc))
msg = 'Start and end cannot both be tz-aware with different timezones'
with pytest.raises(Exception, match=msg):
    bdate_range(datetime(2005, 1, 1, tzinfo=pytz.utc), '1/1/2009', tz=tz)
```

## Next Steps


---

*Source: test_timezones.py:209 | Complexity: Advanced | Last updated: 2026-06-02*