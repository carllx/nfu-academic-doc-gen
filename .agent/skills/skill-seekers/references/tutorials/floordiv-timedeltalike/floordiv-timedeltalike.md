# How To: Floordiv Timedeltalike

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test floordiv timedeltalike

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: td
```

## Step-by-Step Guide

### Step 1: Assign other = Timedelta(...)

```python
other = Timedelta(td._value)
```

**Verification:**
```python
assert td // td == 1
```

### Step 2: Assign msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"

```python
msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"
```

**Verification:**
```python
assert 2.5 * td // td == 2
```

### Step 3: Assign res = value

```python
res = other.to_pytimedelta() // td
```

**Verification:**
```python
assert res == 0
```

### Step 4: Assign left = Timedelta._from_value_and_reso(...)

```python
left = Timedelta._from_value_and_reso(50050, NpyDatetimeUnit.NPY_FR_us.value)
```

**Verification:**
```python
assert result == 1
```

### Step 5: Assign right = Timedelta._from_value_and_reso(...)

```python
right = Timedelta._from_value_and_reso(50, NpyDatetimeUnit.NPY_FR_ms.value)
```

**Verification:**
```python
assert result == 0
```

### Step 6: Assign result = value

```python
result = left // right
```

**Verification:**
```python
assert result == 1
```

### Step 7: Assign result = value

```python
result = right // left
```

**Verification:**
```python
assert result == 0
```

### Step 8: td // other

```python
td // other
```


## Complete Example

```python
# Setup
# Fixtures: td

# Workflow
assert td // td == 1
assert 2.5 * td // td == 2
other = Timedelta(td._value)
msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td // other
res = other.to_pytimedelta() // td
assert res == 0
left = Timedelta._from_value_and_reso(50050, NpyDatetimeUnit.NPY_FR_us.value)
right = Timedelta._from_value_and_reso(50, NpyDatetimeUnit.NPY_FR_ms.value)
result = left // right
assert result == 1
result = right // left
assert result == 0
```

## Next Steps


---

*Source: test_timedelta.py:140 | Complexity: Advanced | Last updated: 2026-06-02*