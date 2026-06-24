# How To: Round Dst Border Ambiguous

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test round dst border ambiguous

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.period`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, unit
```

## Step-by-Step Guide

### Step 1: Assign ts = Timestamp.tz_convert(...)

```python
ts = Timestamp('2017-10-29 00:00:00', tz='UTC').tz_convert('Europe/Madrid')
```

**Verification:**
```python
assert result == ts
```

### Step 2: Assign ts = ts.as_unit(...)

```python
ts = ts.as_unit(unit)
```

**Verification:**
```python
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(ts, method)('h', ambiguous=True)
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(ts, method)('h', ambiguous=False)
```

**Verification:**
```python
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
```

### Step 5: Assign expected = Timestamp.tz_convert(...)

```python
expected = Timestamp('2017-10-29 01:00:00', tz='UTC').tz_convert('Europe/Madrid')
```

**Verification:**
```python
assert result is NaT
```

### Step 6: Assign result = getattr(...)

```python
result = getattr(ts, method)('h', ambiguous='NaT')
```

**Verification:**
```python
assert result is NaT
```

### Step 7: Assign msg = 'Cannot infer dst time'

```python
msg = 'Cannot infer dst time'
```

### Step 8: Call getattr()

```python
getattr(ts, method)('h', ambiguous='raise')
```


## Complete Example

```python
# Setup
# Fixtures: method, unit

# Workflow
ts = Timestamp('2017-10-29 00:00:00', tz='UTC').tz_convert('Europe/Madrid')
ts = ts.as_unit(unit)
result = getattr(ts, method)('h', ambiguous=True)
assert result == ts
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
result = getattr(ts, method)('h', ambiguous=False)
expected = Timestamp('2017-10-29 01:00:00', tz='UTC').tz_convert('Europe/Madrid')
assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f'NPY_FR_{unit}').value
result = getattr(ts, method)('h', ambiguous='NaT')
assert result is NaT
msg = 'Cannot infer dst time'
with pytest.raises(pytz.AmbiguousTimeError, match=msg):
    getattr(ts, method)('h', ambiguous='raise')
```

## Next Steps


---

*Source: test_round.py:171 | Complexity: Advanced | Last updated: 2026-06-02*