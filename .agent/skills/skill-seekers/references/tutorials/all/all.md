# How To: All

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test all

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign r = self.module.foo(...)

```python
r = self.module.foo([[]])
```

**Verification:**
```python
assert r == [0]
```

### Step 2: Assign r = self.module.foo(...)

```python
r = self.module.foo([[1, 2]])
```

**Verification:**
```python
assert r == [3]
```

### Step 3: Assign r = self.module.foo(...)

```python
r = self.module.foo([[1, 2], [3, 4]])
```

**Verification:**
```python
assert np.allclose(r, [3, 7])
```

### Step 4: Assign r = self.module.foo(...)

```python
r = self.module.foo([[1, 2], [3, 4], [5, 6]])
```

**Verification:**
```python
assert np.allclose(r, [3, 7, 11])
```


## Complete Example

```python
# Workflow
r = self.module.foo([[]])
assert r == [0]
r = self.module.foo([[1, 2]])
assert r == [3]
r = self.module.foo([[1, 2], [3, 4]])
assert np.allclose(r, [3, 7])
r = self.module.foo([[1, 2], [3, 4], [5, 6]])
assert np.allclose(r, [3, 7, 11])
```

## Next Steps


---

*Source: test_size.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*