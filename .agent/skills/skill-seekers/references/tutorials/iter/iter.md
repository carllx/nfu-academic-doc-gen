# How To: Iter

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iter

## Prerequisites

**Required Modules:**
- `pickle`
- `copy`
- `pytest`
- `networkx`
- `networkx.classes`
- `networkx.classes.reportviews`
- `pickle`
- `pickle`
- `pickle`
- `pickle`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign nv = value

```python
nv = self.nv
```

**Verification:**
```python
assert i == n
```

### Step 2: Assign inv = iter(...)

```python
inv = iter(nv)
```

**Verification:**
```python
assert next(inv) == 0
```

### Step 3: Assign inv2 = iter(...)

```python
inv2 = iter(nv)
```

**Verification:**
```python
assert iter(nv) != nv
```

### Step 4: Call next()

```python
next(inv2)
```

**Verification:**
```python
assert iter(inv) == inv
```

### Step 5: Assign nnv = nv(...)

```python
nnv = nv(data=False)
```

**Verification:**
```python
assert list(inv) == list(inv2)
```


## Complete Example

```python
# Workflow
nv = self.nv
for i, n in enumerate(nv):
    assert i == n
inv = iter(nv)
assert next(inv) == 0
assert iter(nv) != nv
assert iter(inv) == inv
inv2 = iter(nv)
next(inv2)
assert list(inv) == list(inv2)
nnv = nv(data=False)
for i, n in enumerate(nnv):
    assert i == n
```

## Next Steps


---

*Source: test_reportviews.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*