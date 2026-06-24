# How To: Shift Bday

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test shift bday

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: freq, unit
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range(START, END, freq=freq, unit=unit)
```

**Verification:**
```python
assert shifted[0] == rng[5]
```

### Step 2: Assign shifted = rng.shift(...)

```python
shifted = rng.shift(5)
```

**Verification:**
```python
assert shifted.freq == rng.freq
```

### Step 3: Assign shifted = rng.shift(...)

```python
shifted = rng.shift(-5)
```

**Verification:**
```python
assert shifted[5] == rng[0]
```

### Step 4: Assign shifted = rng.shift(...)

```python
shifted = rng.shift(0)
```

**Verification:**
```python
assert shifted.freq == rng.freq
```


## Complete Example

```python
# Setup
# Fixtures: freq, unit

# Workflow
rng = date_range(START, END, freq=freq, unit=unit)
shifted = rng.shift(5)
assert shifted[0] == rng[5]
assert shifted.freq == rng.freq
shifted = rng.shift(-5)
assert shifted[5] == rng[0]
assert shifted.freq == rng.freq
shifted = rng.shift(0)
assert shifted[0] == rng[0]
assert shifted.freq == rng.freq
```

## Next Steps


---

*Source: test_shift.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*