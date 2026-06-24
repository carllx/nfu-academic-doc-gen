# How To: Tz Localize Ambiguous

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz localize ambiguous

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pytz.exceptions`
- `pandas._libs.tslibs.dtypes`
- `pandas.errors`
- `pandas`
- `zoneinfo`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2014-11-02 01:00')
```

**Verification:**
```python
assert ts_no_dst._value - ts_dst._value == 3600
```

### Step 2: Assign ts_dst = ts.tz_localize(...)

```python
ts_dst = ts.tz_localize('US/Eastern', ambiguous=True)
```

### Step 3: Assign ts_no_dst = ts.tz_localize(...)

```python
ts_no_dst = ts.tz_localize('US/Eastern', ambiguous=False)
```

**Verification:**
```python
assert ts_no_dst._value - ts_dst._value == 3600
```

### Step 4: Assign msg = re.escape(...)

```python
msg = re.escape("'ambiguous' parameter must be one of: True, False, 'NaT', 'raise' (default)")
```

### Step 5: Assign msg = 'Cannot localize tz-aware Timestamp, use tz_convert for conversions'

```python
msg = 'Cannot localize tz-aware Timestamp, use tz_convert for conversions'
```

### Step 6: Assign msg = 'Cannot convert tz-naive Timestamp, use tz_localize to localize'

```python
msg = 'Cannot convert tz-naive Timestamp, use tz_localize to localize'
```

### Step 7: Call ts.tz_localize()

```python
ts.tz_localize('US/Eastern', ambiguous='infer')
```

### Step 8: Call Timestamp.tz_localize()

```python
Timestamp('2011-01-01', tz='US/Eastern').tz_localize('Asia/Tokyo')
```

### Step 9: Call Timestamp.tz_convert()

```python
Timestamp('2011-01-01').tz_convert('Asia/Tokyo')
```


## Complete Example

```python
# Workflow
ts = Timestamp('2014-11-02 01:00')
ts_dst = ts.tz_localize('US/Eastern', ambiguous=True)
ts_no_dst = ts.tz_localize('US/Eastern', ambiguous=False)
assert ts_no_dst._value - ts_dst._value == 3600
msg = re.escape("'ambiguous' parameter must be one of: True, False, 'NaT', 'raise' (default)")
with pytest.raises(ValueError, match=msg):
    ts.tz_localize('US/Eastern', ambiguous='infer')
msg = 'Cannot localize tz-aware Timestamp, use tz_convert for conversions'
with pytest.raises(TypeError, match=msg):
    Timestamp('2011-01-01', tz='US/Eastern').tz_localize('Asia/Tokyo')
msg = 'Cannot convert tz-naive Timestamp, use tz_localize to localize'
with pytest.raises(TypeError, match=msg):
    Timestamp('2011-01-01').tz_convert('Asia/Tokyo')
```

## Next Steps


---

*Source: test_tz_localize.py:86 | Complexity: Advanced | Last updated: 2026-06-02*