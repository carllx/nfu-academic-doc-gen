# How To: Align Dt64Tzindex Mismatched Tzs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test align dt64tzindex mismatched tzs

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = date_range(...)

```python
idx1 = date_range('2001', periods=5, freq='h', tz='US/Eastern')
```

**Verification:**
```python
assert new1.index.tz is timezone.utc
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(np.random.default_rng(2).standard_normal(len(idx1)), index=idx1)
```

**Verification:**
```python
assert new2.index.tz is timezone.utc
```

### Step 3: Assign ser_central = ser.tz_convert(...)

```python
ser_central = ser.tz_convert('US/Central')
```

### Step 4: Assign unknown = ser.align(...)

```python
new1, new2 = ser.align(ser_central)
```

**Verification:**
```python
assert new1.index.tz is timezone.utc
```


## Complete Example

```python
# Workflow
idx1 = date_range('2001', periods=5, freq='h', tz='US/Eastern')
ser = Series(np.random.default_rng(2).standard_normal(len(idx1)), index=idx1)
ser_central = ser.tz_convert('US/Central')
new1, new2 = ser.align(ser_central)
assert new1.index.tz is timezone.utc
assert new2.index.tz is timezone.utc
```

## Next Steps


---

*Source: test_align.py:195 | Complexity: Intermediate | Last updated: 2026-06-02*