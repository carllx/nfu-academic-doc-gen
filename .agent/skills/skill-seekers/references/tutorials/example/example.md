# How To: Example

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test example

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array(b'123\x00\x00')
```

**Verification:**
```python
assert a.tobytes() == b'123\x00\x00'
```

### Step 2: Assign b = np.array(...)

```python
b = np.array(b'123\x00\x00')
```

**Verification:**
```python
assert b.tobytes() == b'B23\x00\x00'
```

### Step 3: Assign c = np.array(...)

```python
c = np.array(b'123')
```

**Verification:**
```python
assert c.tobytes() == b'123'
```

### Step 4: Assign d = np.array(...)

```python
d = np.array(b'123')
```

**Verification:**
```python
assert d.tobytes() == b'D23'
```

### Step 5: Call self.module.foo()

```python
self.module.foo(a, b, c, d)
```

**Verification:**
```python
assert a.tobytes() == b'123\x00\x00'
```


## Complete Example

```python
# Workflow
a = np.array(b'123\x00\x00')
b = np.array(b'123\x00\x00')
c = np.array(b'123')
d = np.array(b'123')
self.module.foo(a, b, c, d)
assert a.tobytes() == b'123\x00\x00'
assert b.tobytes() == b'B23\x00\x00'
assert c.tobytes() == b'123'
assert d.tobytes() == b'D23'
```

## Next Steps


---

*Source: test_string.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*