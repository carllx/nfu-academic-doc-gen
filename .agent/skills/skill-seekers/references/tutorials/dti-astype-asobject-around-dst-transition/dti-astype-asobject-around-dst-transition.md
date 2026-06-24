# How To: Dti Astype Asobject Around Dst Transition

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti astype asobject around dst transition

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tzstr
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('2/13/2010', '5/6/2010', tz=tzstr)
```

**Verification:**
```python
assert x == exval
```

### Step 2: Assign objs = rng.astype(...)

```python
objs = rng.astype(object)
```

**Verification:**
```python
assert x.tzinfo == exval.tzinfo
```

### Step 3: Assign objs = rng.astype(...)

```python
objs = rng.astype(object)
```

**Verification:**
```python
assert x == exval
```

### Step 4: Assign exval = value

```python
exval = rng[i]
```

**Verification:**
```python
assert x.tzinfo == exval.tzinfo
```

### Step 5: Assign exval = value

```python
exval = rng[i]
```

**Verification:**
```python
assert x == exval
```


## Complete Example

```python
# Setup
# Fixtures: tzstr

# Workflow
rng = date_range('2/13/2010', '5/6/2010', tz=tzstr)
objs = rng.astype(object)
for i, x in enumerate(objs):
    exval = rng[i]
    assert x == exval
    assert x.tzinfo == exval.tzinfo
objs = rng.astype(object)
for i, x in enumerate(objs):
    exval = rng[i]
    assert x == exval
    assert x.tzinfo == exval.tzinfo
```

## Next Steps


---

*Source: test_astype.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*