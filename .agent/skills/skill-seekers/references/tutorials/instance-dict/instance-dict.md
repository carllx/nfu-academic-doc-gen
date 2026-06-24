# How To: Instance Dict

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test instance dict

## Prerequisites

**Required Modules:**
- `gc`
- `sys`
- `time`
- `threading`
- `unittest`
- `abc`
- `abc`
- `greenlet`
- `greenlet`
- `leakcheck`
- `io`
- `copy`
- `greenlet`
- `greenlet`
- `threading`
- `threading`
- `greenlet`
- `functools`


## Step-by-Step Guide

### Step 1: Assign g = RawGreenlet(...)

```python
g = RawGreenlet(f)
```

### Step 2: Call self.assertEqual()

```python
self.assertEqual(g.__dict__, {})
```

### Step 3: Call g.switch()

```python
g.switch()
```

### Step 4: Call self.assertEqual()

```python
self.assertEqual(g.test, 42)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(g.__dict__, {'test': 42})
```

### Step 6: Assign g.__dict__ = value

```python
g.__dict__ = g.__dict__
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(g.__dict__, {'test': 42})
```

### Step 8: Call self.assertRaises()

```python
self.assertRaises(TypeError, deldict, g)
```

### Step 9: Call self.assertRaises()

```python
self.assertRaises(TypeError, setdict, g, 42)
```

### Step 10: Assign greenlet.getcurrent.test = 42

```python
greenlet.getcurrent().test = 42
```

### Step 11: Assign g.__dict__ = value

```python
g.__dict__ = value
```


## Complete Example

```python
# Workflow
def f():
    greenlet.getcurrent().test = 42

def deldict(g):
    del g.__dict__

def setdict(g, value):
    g.__dict__ = value
g = RawGreenlet(f)
self.assertEqual(g.__dict__, {})
g.switch()
self.assertEqual(g.test, 42)
self.assertEqual(g.__dict__, {'test': 42})
g.__dict__ = g.__dict__
self.assertEqual(g.__dict__, {'test': 42})
self.assertRaises(TypeError, deldict, g)
self.assertRaises(TypeError, setdict, g, 42)
```

## Next Steps


---

*Source: test_greenlet.py:367 | Complexity: Advanced | Last updated: 2026-06-02*