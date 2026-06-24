# How To: Tz Localize Pushes Out Of Bounds

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tz localize pushes out of bounds

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

### Step 1: Assign msg = value

```python
msg = f"Converting {Timestamp.min.strftime('%Y-%m-%d %H:%M:%S')} underflows past {Timestamp.min}"
```

**Verification:**
```python
assert pac._value > Timestamp.min._value
```

### Step 2: Assign pac = Timestamp.min.tz_localize(...)

```python
pac = Timestamp.min.tz_localize('US/Pacific')
```

**Verification:**
```python
assert tokyo._value < Timestamp.max._value
```

### Step 3: Call pac.tz_convert()

```python
pac.tz_convert('Asia/Tokyo')
```

### Step 4: Assign msg = value

```python
msg = f"Converting {Timestamp.max.strftime('%Y-%m-%d %H:%M:%S')} overflows past {Timestamp.max}"
```

### Step 5: Assign tokyo = Timestamp.max.tz_localize(...)

```python
tokyo = Timestamp.max.tz_localize('Asia/Tokyo')
```

**Verification:**
```python
assert tokyo._value < Timestamp.max._value
```

### Step 6: Call tokyo.tz_convert()

```python
tokyo.tz_convert('US/Pacific')
```

### Step 7: Call Timestamp.min.tz_localize()

```python
Timestamp.min.tz_localize('Asia/Tokyo')
```

### Step 8: Call Timestamp.max.tz_localize()

```python
Timestamp.max.tz_localize('US/Pacific')
```


## Complete Example

```python
# Workflow
msg = f"Converting {Timestamp.min.strftime('%Y-%m-%d %H:%M:%S')} underflows past {Timestamp.min}"
pac = Timestamp.min.tz_localize('US/Pacific')
assert pac._value > Timestamp.min._value
pac.tz_convert('Asia/Tokyo')
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp.min.tz_localize('Asia/Tokyo')
msg = f"Converting {Timestamp.max.strftime('%Y-%m-%d %H:%M:%S')} overflows past {Timestamp.max}"
tokyo = Timestamp.max.tz_localize('Asia/Tokyo')
assert tokyo._value < Timestamp.max._value
tokyo.tz_convert('US/Pacific')
with pytest.raises(OutOfBoundsDatetime, match=msg):
    Timestamp.max.tz_localize('US/Pacific')
```

## Next Steps


---

*Source: test_tz_localize.py:29 | Complexity: Advanced | Last updated: 2026-06-02*