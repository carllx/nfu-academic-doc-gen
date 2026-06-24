# How To: Min Max Empty

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test min max empty

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: skipna, tz
```

## Step-by-Step Guide

### Step 1: Assign dtype = value

```python
dtype = DatetimeTZDtype(tz=tz) if tz is not None else np.dtype('M8[ns]')
```

**Verification:**
```python
assert result is NaT
```

### Step 2: Assign arr = DatetimeArray._from_sequence(...)

```python
arr = DatetimeArray._from_sequence([], dtype=dtype)
```

**Verification:**
```python
assert result is NaT
```

### Step 3: Assign result = arr.min(...)

```python
result = arr.min(skipna=skipna)
```

**Verification:**
```python
assert result is NaT
```

### Step 4: Assign result = arr.max(...)

```python
result = arr.max(skipna=skipna)
```

**Verification:**
```python
assert result is NaT
```


## Complete Example

```python
# Setup
# Fixtures: skipna, tz

# Workflow
dtype = DatetimeTZDtype(tz=tz) if tz is not None else np.dtype('M8[ns]')
arr = DatetimeArray._from_sequence([], dtype=dtype)
result = arr.min(skipna=skipna)
assert result is NaT
result = arr.max(skipna=skipna)
assert result is NaT
```

## Next Steps


---

*Source: test_reductions.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*