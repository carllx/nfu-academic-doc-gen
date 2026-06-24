# How To: From Tick Reso

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from tick reso

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tick = offsets.Nano(...)

```python
tick = offsets.Nano()
```

**Verification:**
```python
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_ns.value
```

### Step 2: Assign tick = offsets.Micro(...)

```python
tick = offsets.Micro()
```

**Verification:**
```python
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_us.value
```

### Step 3: Assign tick = offsets.Milli(...)

```python
tick = offsets.Milli()
```

**Verification:**
```python
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_ms.value
```

### Step 4: Assign tick = offsets.Second(...)

```python
tick = offsets.Second()
```

**Verification:**
```python
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
```

### Step 5: Assign tick = offsets.Minute(...)

```python
tick = offsets.Minute()
```

**Verification:**
```python
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
```

### Step 6: Assign tick = offsets.Hour(...)

```python
tick = offsets.Hour()
```

**Verification:**
```python
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
```

### Step 7: Assign tick = offsets.Day(...)

```python
tick = offsets.Day()
```

**Verification:**
```python
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
```


## Complete Example

```python
# Workflow
tick = offsets.Nano()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_ns.value
tick = offsets.Micro()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_us.value
tick = offsets.Milli()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_ms.value
tick = offsets.Second()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
tick = offsets.Minute()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
tick = offsets.Hour()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
tick = offsets.Day()
assert Timedelta(tick)._creso == NpyDatetimeUnit.NPY_FR_s.value
```

## Next Steps


---

*Source: test_constructors.py:238 | Complexity: Intermediate | Last updated: 2026-06-02*