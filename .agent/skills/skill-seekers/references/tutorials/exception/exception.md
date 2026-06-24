# How To: Exception

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test exception

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

### Step 1: Assign seen = value

```python
seen = []
```

### Step 2: Assign g1 = RawGreenlet(...)

```python
g1 = RawGreenlet(fmain)
```

### Step 3: Assign g2 = RawGreenlet(...)

```python
g2 = RawGreenlet(fmain)
```

### Step 4: Call g1.switch()

```python
g1.switch(seen)
```

### Step 5: Call g2.switch()

```python
g2.switch(seen)
```

### Step 6: Assign g2.parent = g1

```python
g2.parent = g1
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(seen, [])
```

### Step 8: Call self.assertRaises()

```python
self.assertRaises(SomeError, g2.switch)
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(seen, [SomeError])
```

### Step 10: Assign value = g2.switch(...)

```python
value = g2.switch()
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(value, ())
```

### Step 12: Call self.assertEqual()

```python
self.assertEqual(seen, [SomeError])
```

### Step 13: Assign value = g2.switch(...)

```python
value = g2.switch(25)
```

### Step 14: Call self.assertEqual()

```python
self.assertEqual(value, 25)
```

### Step 15: Call self.assertEqual()

```python
self.assertEqual(seen, [SomeError])
```


## Complete Example

```python
# Workflow
seen = []
g1 = RawGreenlet(fmain)
g2 = RawGreenlet(fmain)
g1.switch(seen)
g2.switch(seen)
g2.parent = g1
self.assertEqual(seen, [])
self.assertRaises(SomeError, g2.switch)
self.assertEqual(seen, [SomeError])
value = g2.switch()
self.assertEqual(value, ())
self.assertEqual(seen, [SomeError])
value = g2.switch(25)
self.assertEqual(value, 25)
self.assertEqual(seen, [SomeError])
```

## Next Steps


---

*Source: test_greenlet.py:151 | Complexity: Advanced | Last updated: 2026-06-02*