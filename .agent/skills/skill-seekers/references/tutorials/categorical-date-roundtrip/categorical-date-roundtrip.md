# How To: Categorical Date Roundtrip

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical date roundtrip

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: box
```

## Step-by-Step Guide

### Step 1: Assign v = date.today(...)

```python
v = date.today()
```

**Verification:**
```python
assert obj.dtype == object
```

### Step 2: Assign obj = Index(...)

```python
obj = Index([v, v])
```

**Verification:**
```python
assert rtrip.dtype == object
```

### Step 3: Assign cat = obj.astype(...)

```python
cat = obj.astype('category')
```

**Verification:**
```python
assert type(rtrip[0]) is date
```

### Step 4: Assign rtrip = cat.astype(...)

```python
rtrip = cat.astype(object)
```

**Verification:**
```python
assert rtrip.dtype == object
```

### Step 5: Assign obj = value

```python
obj = obj.array
```


## Complete Example

```python
# Setup
# Fixtures: box

# Workflow
v = date.today()
obj = Index([v, v])
assert obj.dtype == object
if box:
    obj = obj.array
cat = obj.astype('category')
rtrip = cat.astype(object)
assert rtrip.dtype == object
assert type(rtrip[0]) is date
```

## Next Steps


---

*Source: test_astype.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*