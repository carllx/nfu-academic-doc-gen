# How To: Switch To Dead Greenlet Reparent

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test switch to dead greenlet reparent

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

### Step 2: Assign parent_never_started = RawGreenlet(...)

```python
parent_never_started = RawGreenlet(lambda: seen.append(24))
```

### Step 3: Assign child = RawGreenlet(...)

```python
child = RawGreenlet(lambda: seen.append(42))
```

### Step 4: Call child.switch()

```python
child.switch()
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(seen, [42])
```

### Step 6: Assign child.parent = parent_never_started

```python
child.parent = parent_never_started
```

### Step 7: Assign result = child.switch(...)

```python
result = child.switch()
```

### Step 8: Call self.assertIsNone()

```python
self.assertIsNone(result)
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(seen, [42, 24])
```


## Complete Example

```python
# Workflow
seen = []
parent_never_started = RawGreenlet(lambda: seen.append(24))
child = RawGreenlet(lambda: seen.append(42))
child.switch()
self.assertEqual(seen, [42])
child.parent = parent_never_started
result = child.switch()
self.assertIsNone(result)
self.assertEqual(seen, [42, 24])
```

## Next Steps


---

*Source: test_greenlet.py:875 | Complexity: Advanced | Last updated: 2026-06-02*