# How To: Construction Out Of Bounds Td64Ns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test construction out of bounds td64ns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: val, unit
```

## Step-by-Step Guide

### Step 1: Assign td64 = np.timedelta64(...)

```python
td64 = np.timedelta64(val, unit)
```

**Verification:**
```python
assert td64.astype('m8[ns]').view('i8') < 0
```

### Step 2: Assign td = Timedelta(...)

```python
td = Timedelta(td64)
```

**Verification:**
```python
assert td.asm8 == td64
```

### Step 3: Assign msg = "Cannot cast 1067\\d\\d days .* to unit='ns' without overflow"

```python
msg = "Cannot cast 1067\\d\\d days .* to unit='ns' without overflow"
```

**Verification:**
```python
assert td.asm8.dtype == 'm8[s]'
```

### Step 4: Assign td2 = Timedelta(...)

```python
td2 = Timedelta(td64)
```

**Verification:**
```python
assert Timedelta(td64 - 1) == td64 - 1
```

### Step 5: Assign msg = "Cannot cast -1067\\d\\d days .* to unit='ns' without overflow"

```python
msg = "Cannot cast -1067\\d\\d days .* to unit='ns' without overflow"
```

**Verification:**
```python
assert td64.astype('m8[ns]').view('i8') > 0
```

### Step 6: Call td.as_unit()

```python
td.as_unit('ns')
```

**Verification:**
```python
assert Timedelta(td64 + 1) == td64 + 1
```

### Step 7: Call td2.as_unit()

```python
td2.as_unit('ns')
```


## Complete Example

```python
# Setup
# Fixtures: val, unit

# Workflow
td64 = np.timedelta64(val, unit)
assert td64.astype('m8[ns]').view('i8') < 0
td = Timedelta(td64)
if unit != 'M':
    assert td.asm8 == td64
assert td.asm8.dtype == 'm8[s]'
msg = "Cannot cast 1067\\d\\d days .* to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td.as_unit('ns')
assert Timedelta(td64 - 1) == td64 - 1
td64 *= -1
assert td64.astype('m8[ns]').view('i8') > 0
td2 = Timedelta(td64)
msg = "Cannot cast -1067\\d\\d days .* to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td2.as_unit('ns')
assert Timedelta(td64 + 1) == td64 + 1
```

## Next Steps


---

*Source: test_constructors.py:465 | Complexity: Intermediate | Last updated: 2026-06-02*