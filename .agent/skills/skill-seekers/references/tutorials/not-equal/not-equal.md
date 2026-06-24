# How To: Not Equal

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test not equal

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numbers`
- `pytest`
- `numpy`
- `numpy.exceptions`
- `numpy.polynomial`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: Poly
```

## Step-by-Step Guide

### Step 1: Assign p1 = Poly(...)

```python
p1 = Poly([1, 2, 3], domain=[0, 1], window=[2, 3])
```

**Verification:**
```python
assert_(not p1 != p1)
```

### Step 2: Assign p2 = Poly(...)

```python
p2 = Poly([1, 1, 1], domain=[0, 1], window=[2, 3])
```

**Verification:**
```python
assert_(p1 != p2)
```

### Step 3: Assign p3 = Poly(...)

```python
p3 = Poly([1, 2, 3], domain=[1, 2], window=[2, 3])
```

**Verification:**
```python
assert_(p1 != p3)
```

### Step 4: Assign p4 = Poly(...)

```python
p4 = Poly([1, 2, 3], domain=[0, 1], window=[1, 2])
```

**Verification:**
```python
assert_(p1 != p4)
```

### Step 5: Call assert_()

```python
assert_(not p1 != p1)
```

### Step 6: Call assert_()

```python
assert_(p1 != p2)
```

### Step 7: Call assert_()

```python
assert_(p1 != p3)
```

### Step 8: Call assert_()

```python
assert_(p1 != p4)
```


## Complete Example

```python
# Setup
# Fixtures: Poly

# Workflow
p1 = Poly([1, 2, 3], domain=[0, 1], window=[2, 3])
p2 = Poly([1, 1, 1], domain=[0, 1], window=[2, 3])
p3 = Poly([1, 2, 3], domain=[1, 2], window=[2, 3])
p4 = Poly([1, 2, 3], domain=[0, 1], window=[1, 2])
assert_(not p1 != p1)
assert_(p1 != p2)
assert_(p1 != p3)
assert_(p1 != p4)
```

## Next Steps


---

*Source: test_classes.py:205 | Complexity: Advanced | Last updated: 2026-06-02*