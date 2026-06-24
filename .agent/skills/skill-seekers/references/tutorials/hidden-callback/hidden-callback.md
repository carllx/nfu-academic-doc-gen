# How To: Hidden Callback

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hidden callback

## Prerequisites

**Required Modules:**
- `math`
- `platform`
- `sys`
- `textwrap`
- `threading`
- `time`
- `traceback`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign self.module.global_f = value

```python
self.module.global_f = lambda x: x + 1
```

**Verification:**
```python
assert str(msg).startswith('Callback global_f not defined')
```

### Step 2: Assign r = self.module.hidden_callback(...)

```python
r = self.module.hidden_callback(2)
```

**Verification:**
```python
assert str(msg).startswith('cb: Callback global_f not defined')
```

### Step 3: Assign self.module.global_f = value

```python
self.module.global_f = lambda x: x + 2
```

**Verification:**
```python
assert r == 3
```

### Step 4: Assign r = self.module.hidden_callback(...)

```python
r = self.module.hidden_callback(2)
```

**Verification:**
```python
assert r == 4
```

### Step 5: Assign self.module.global_f = value

```python
self.module.global_f = lambda x=0: x + 3
```

**Verification:**
```python
assert str(msg).startswith('Callback global_f not defined')
```

### Step 6: Assign r = self.module.hidden_callback(...)

```python
r = self.module.hidden_callback(2)
```

**Verification:**
```python
assert r == 5
```

### Step 7: Assign r = self.module.hidden_callback2(...)

```python
r = self.module.hidden_callback2(2)
```

**Verification:**
```python
assert r == 3
```

### Step 8: Call self.module.hidden_callback()

```python
self.module.hidden_callback(2)
```

### Step 9: Call self.module.hidden_callback2()

```python
self.module.hidden_callback2(2)
```

### Step 10: Call self.module.hidden_callback()

```python
self.module.hidden_callback(2)
```

**Verification:**
```python
assert str(msg).startswith('Callback global_f not defined')
```


## Complete Example

```python
# Workflow
try:
    self.module.hidden_callback(2)
except Exception as msg:
    assert str(msg).startswith('Callback global_f not defined')
try:
    self.module.hidden_callback2(2)
except Exception as msg:
    assert str(msg).startswith('cb: Callback global_f not defined')
self.module.global_f = lambda x: x + 1
r = self.module.hidden_callback(2)
assert r == 3
self.module.global_f = lambda x: x + 2
r = self.module.hidden_callback(2)
assert r == 4
del self.module.global_f
try:
    self.module.hidden_callback(2)
except Exception as msg:
    assert str(msg).startswith('Callback global_f not defined')
self.module.global_f = lambda x=0: x + 3
r = self.module.hidden_callback(2)
assert r == 5
r = self.module.hidden_callback2(2)
assert r == 3
```

## Next Steps


---

*Source: test_callback.py:166 | Complexity: Advanced | Last updated: 2026-06-02*