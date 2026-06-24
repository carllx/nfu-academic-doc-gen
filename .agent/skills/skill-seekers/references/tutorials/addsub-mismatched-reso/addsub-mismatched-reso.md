# How To: Addsub Mismatched Reso

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test addsub mismatched reso

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

### Step 1: Assign other = Timedelta.as_unit(...)

```python
other = Timedelta(days=1).as_unit('us')
```

**Verification:**
```python
assert result._creso == other._creso
```

### Step 2: Assign result = value

```python
result = td + other
```

**Verification:**
```python
assert result.days == td.days + 1
```

### Step 3: Assign result = value

```python
result = other + td
```

**Verification:**
```python
assert result._creso == other._creso
```

### Step 4: Assign result = value

```python
result = td - other
```

**Verification:**
```python
assert result.days == td.days + 1
```

### Step 5: Assign result = value

```python
result = other - td
```

**Verification:**
```python
assert result._creso == other._creso
```

### Step 6: Assign other2 = Timedelta(...)

```python
other2 = Timedelta(500)
```

**Verification:**
```python
assert result.days == td.days - 1
```

### Step 7: Assign msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"

```python
msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"
```

**Verification:**
```python
assert result._creso == other._creso
```

### Step 8: td + other2

```python
td + other2
```

**Verification:**
```python
assert result.days == 1 - td.days
```

### Step 9: other2 + td

```python
other2 + td
```

### Step 10: td - other2

```python
td - other2
```

### Step 11: other2 - td

```python
other2 - td
```


## Complete Example

```python
# Setup
# Fixtures: td

# Workflow
other = Timedelta(days=1).as_unit('us')
result = td + other
assert result._creso == other._creso
assert result.days == td.days + 1
result = other + td
assert result._creso == other._creso
assert result.days == td.days + 1
result = td - other
assert result._creso == other._creso
assert result.days == td.days - 1
result = other - td
assert result._creso == other._creso
assert result.days == 1 - td.days
other2 = Timedelta(500)
msg = "Cannot cast 106752 days 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td + other2
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    other2 + td
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    td - other2
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    other2 - td
```

## Next Steps


---

*Source: test_timedelta.py:184 | Complexity: Advanced | Last updated: 2026-06-02*