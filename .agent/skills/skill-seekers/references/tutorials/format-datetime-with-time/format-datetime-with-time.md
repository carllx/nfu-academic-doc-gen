# How To: Format Datetime With Time

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test format datetime with time

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([datetime(2012, 2, 7), datetime(2012, 2, 7, 23)])
```

**Verification:**
```python
assert len(result) == 2
```

### Step 2: Assign msg = 'DatetimeIndex.format is deprecated'

```python
msg = 'DatetimeIndex.format is deprecated'
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign expected = value

```python
expected = ['2012-02-07 00:00:00', '2012-02-07 23:00:00']
```

**Verification:**
```python
assert len(result) == 2
```

### Step 4: Assign result = dti.format(...)

```python
result = dti.format()
```


## Complete Example

```python
# Workflow
dti = DatetimeIndex([datetime(2012, 2, 7), datetime(2012, 2, 7, 23)])
msg = 'DatetimeIndex.format is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = dti.format()
expected = ['2012-02-07 00:00:00', '2012-02-07 23:00:00']
assert len(result) == 2
assert result == expected
```

## Next Steps


---

*Source: test_formats.py:314 | Complexity: Intermediate | Last updated: 2026-06-02*