# How To: Std

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test std

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: add
```

## Step-by-Step Guide

### Step 1: Assign tdi = value

```python
tdi = pd.TimedeltaIndex(['0h', '4h', 'NaT', '4h', '0h', '2h']) + add
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 2: Assign arr = value

```python
arr = tdi.array
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = arr.std(...)

```python
result = arr.std(skipna=True)
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 4: Assign expected = Timedelta(...)

```python
expected = Timedelta(hours=2)
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = tdi.std(...)

```python
result = tdi.std(skipna=True)
```

**Verification:**
```python
assert isinstance(result, np.timedelta64)
```

### Step 6: Assign result = arr.std(...)

```python
result = arr.std(skipna=False)
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign result = tdi.std(...)

```python
result = tdi.std(skipna=False)
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 8: Assign result = nanops.nanstd(...)

```python
result = nanops.nanstd(np.asarray(arr), skipna=True)
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 9: Assign result = nanops.nanstd(...)

```python
result = nanops.nanstd(np.asarray(arr), skipna=False)
```

**Verification:**
```python
assert isinstance(result, np.timedelta64)
```


## Complete Example

```python
# Setup
# Fixtures: add

# Workflow
tdi = pd.TimedeltaIndex(['0h', '4h', 'NaT', '4h', '0h', '2h']) + add
arr = tdi.array
result = arr.std(skipna=True)
expected = Timedelta(hours=2)
assert isinstance(result, Timedelta)
assert result == expected
result = tdi.std(skipna=True)
assert isinstance(result, Timedelta)
assert result == expected
if getattr(arr, 'tz', None) is None:
    result = nanops.nanstd(np.asarray(arr), skipna=True)
    assert isinstance(result, np.timedelta64)
    assert result == expected
result = arr.std(skipna=False)
assert result is pd.NaT
result = tdi.std(skipna=False)
assert result is pd.NaT
if getattr(arr, 'tz', None) is None:
    result = nanops.nanstd(np.asarray(arr), skipna=False)
    assert isinstance(result, np.timedelta64)
    assert np.isnat(result)
```

## Next Steps


---

*Source: test_reductions.py:138 | Complexity: Advanced | Last updated: 2026-06-02*