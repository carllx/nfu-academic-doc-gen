# How To: Full Format Converters

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test full format converters

## Prerequisites

**Required Modules:**
- `datetime`
- `sys`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign d1 = np.timedelta64(...)

```python
d1 = np.timedelta64(1, 'D')
```

**Verification:**
```python
assert Timedelta('1days') == conv(d1)
```

### Step 2: Assign msg = 'have leftover units'

```python
msg = 'have leftover units'
```

**Verification:**
```python
assert Timedelta('1days,') == conv(d1)
```

### Step 3: Call Timedelta()

```python
Timedelta('- 1days, 00')
```

**Verification:**
```python
assert Timedelta('- 1days,') == -conv(d1)
```


## Complete Example

```python
# Workflow
def conv(v):
    return v.astype('m8[ns]')
d1 = np.timedelta64(1, 'D')
assert Timedelta('1days') == conv(d1)
assert Timedelta('1days,') == conv(d1)
assert Timedelta('- 1days,') == -conv(d1)
assert Timedelta('00:00:01') == conv(np.timedelta64(1, 's'))
assert Timedelta('06:00:01') == conv(np.timedelta64(6 * 3600 + 1, 's'))
assert Timedelta('06:00:01.0') == conv(np.timedelta64(6 * 3600 + 1, 's'))
assert Timedelta('06:00:01.01') == conv(np.timedelta64(1000 * (6 * 3600 + 1) + 10, 'ms'))
assert Timedelta('- 1days, 00:00:01') == conv(-d1 + np.timedelta64(1, 's'))
assert Timedelta('1days, 06:00:01') == conv(d1 + np.timedelta64(6 * 3600 + 1, 's'))
assert Timedelta('1days, 06:00:01.01') == conv(d1 + np.timedelta64(1000 * (6 * 3600 + 1) + 10, 'ms'))
msg = 'have leftover units'
with pytest.raises(ValueError, match=msg):
    Timedelta('- 1days, 00')
```

## Next Steps


---

*Source: test_timedelta.py:503 | Complexity: Beginner | Last updated: 2026-06-02*