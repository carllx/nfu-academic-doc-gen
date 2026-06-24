# How To: Overflow On Construction

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test overflow on construction

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

### Step 1: Assign value = value

```python
value = Timedelta('1day')._value * 20169940
```

**Verification:**
```python
assert td._creso == NpyDatetimeUnit.NPY_FR_us.value
```

### Step 2: Assign msg = "Cannot cast 1742682816000000000000 from ns to 'ns' without overflow"

```python
msg = "Cannot cast 1742682816000000000000 from ns to 'ns' without overflow"
```

**Verification:**
```python
assert td.days == 13 * 19999
```

### Step 3: Assign msg = "Cannot cast 139993 from D to 'ns' without overflow"

```python
msg = "Cannot cast 139993 from D to 'ns' without overflow"
```

### Step 4: Assign td = Timedelta(...)

```python
td = Timedelta(timedelta(days=13 * 19999))
```

**Verification:**
```python
assert td._creso == NpyDatetimeUnit.NPY_FR_us.value
```

### Step 5: Call Timedelta()

```python
Timedelta(value)
```

### Step 6: Call Timedelta()

```python
Timedelta(7 * 19999, unit='D')
```


## Complete Example

```python
# Workflow
value = Timedelta('1day')._value * 20169940
msg = "Cannot cast 1742682816000000000000 from ns to 'ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    Timedelta(value)
msg = "Cannot cast 139993 from D to 'ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    Timedelta(7 * 19999, unit='D')
td = Timedelta(timedelta(days=13 * 19999))
assert td._creso == NpyDatetimeUnit.NPY_FR_us.value
assert td.days == 13 * 19999
```

## Next Steps


---

*Source: test_constructors.py:437 | Complexity: Intermediate | Last updated: 2026-06-02*