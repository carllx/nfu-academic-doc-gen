# How To: Truediv Timedeltalike

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test truediv timedeltalike

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
assert td / td == 1
```

### Step 2: Assign msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow."

```python
msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow."
```

**Verification:**
```python
assert 2.5 * td / td == 2.5
```

### Step 3: Assign res = value

```python
res = other.to_pytimedelta() / td
```

**Verification:**
```python
assert res == expected
```

### Step 4: Assign expected = value

```python
expected = other.to_pytimedelta() / td.to_pytimedelta()
```

**Verification:**
```python
assert result == 0.001
```

### Step 5: Assign left = Timedelta._from_value_and_reso(...)

```python
left = Timedelta._from_value_and_reso(50, NpyDatetimeUnit.NPY_FR_us.value)
```

**Verification:**
```python
assert result == 1000
```

### Step 6: Assign right = Timedelta._from_value_and_reso(...)

```python
right = Timedelta._from_value_and_reso(50, NpyDatetimeUnit.NPY_FR_ms.value)
```

### Step 7: Assign result = value

```python
result = left / right
```

**Verification:**
```python
assert result == 0.001
```

### Step 8: Assign result = value

```python
result = right / left
```

**Verification:**
```python
assert result == 1000
```

### Step 9: td / other

```python
td / other
```


## Complete Example

```python
# Setup
# Fixtures: td

# Workflow
assert td / td == 1
assert 2.5 * td / td == 2.5
other = Timedelta(td._value)
msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow."
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td / other
res = other.to_pytimedelta() / td
expected = other.to_pytimedelta() / td.to_pytimedelta()
assert res == expected
left = Timedelta._from_value_and_reso(50, NpyDatetimeUnit.NPY_FR_us.value)
right = Timedelta._from_value_and_reso(50, NpyDatetimeUnit.NPY_FR_ms.value)
result = left / right
assert result == 0.001
result = right / left
assert result == 1000
```

## Next Steps


---

*Source: test_timedelta.py:104 | Complexity: Advanced | Last updated: 2026-06-02*