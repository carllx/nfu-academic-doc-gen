# How To: Reductions Empty

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reductions empty

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
# Fixtures: name, skipna
```

## Step-by-Step Guide

### Step 1: Assign tdi = pd.TimedeltaIndex(...)

```python
tdi = pd.TimedeltaIndex([])
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 2: Assign arr = value

```python
arr = tdi.array
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(tdi, name)(skipna=skipna)
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(arr, name)(skipna=skipna)
```

**Verification:**
```python
assert result is pd.NaT
```


## Complete Example

```python
# Setup
# Fixtures: name, skipna

# Workflow
tdi = pd.TimedeltaIndex([])
arr = tdi.array
result = getattr(tdi, name)(skipna=skipna)
assert result is pd.NaT
result = getattr(arr, name)(skipna=skipna)
assert result is pd.NaT
```

## Next Steps


---

*Source: test_reductions.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*