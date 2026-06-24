# How To: Tz Localize Invalidates Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz localize invalidates freq

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `zoneinfo`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2014-03-08 23:00', '2014-03-09 09:00', freq='h')
```

**Verification:**
```python
assert dti.freq == 'h'
```

### Step 2: Assign result = dti.tz_localize(...)

```python
result = dti.tz_localize(None)
```

**Verification:**
```python
assert result.freq == 'h'
```

### Step 3: Assign result = dti.tz_localize(...)

```python
result = dti.tz_localize('UTC')
```

**Verification:**
```python
assert result.freq == 'h'
```

### Step 4: Assign result = dti.tz_localize(...)

```python
result = dti.tz_localize('US/Eastern', nonexistent='shift_forward')
```

**Verification:**
```python
assert result.freq is None
```

### Step 5: Assign dti2 = value

```python
dti2 = dti[:1]
```

**Verification:**
```python
assert result.inferred_freq is None
```

### Step 6: Assign result = dti2.tz_localize(...)

```python
result = dti2.tz_localize('US/Eastern')
```

**Verification:**
```python
assert result.freq == 'h'
```


## Complete Example

```python
# Workflow
dti = date_range('2014-03-08 23:00', '2014-03-09 09:00', freq='h')
assert dti.freq == 'h'
result = dti.tz_localize(None)
assert result.freq == 'h'
result = dti.tz_localize('UTC')
assert result.freq == 'h'
result = dti.tz_localize('US/Eastern', nonexistent='shift_forward')
assert result.freq is None
assert result.inferred_freq is None
dti2 = dti[:1]
result = dti2.tz_localize('US/Eastern')
assert result.freq == 'h'
```

## Next Steps


---

*Source: test_tz_localize.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*