# How To: Kill

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test kill

## Prerequisites

**Required Modules:**
- `sys`
- `greenlet`


## Step-by-Step Guide

### Step 1: Assign g = greenlet(...)

```python
g = greenlet(f)
```

### Step 2: Assign res = g.switch(...)

```python
res = g.switch()
```

### Step 3: Call self.assertEqual()

```python
self.assertEqual(res, 'ok')
```

### Step 4: Assign res = g.throw(...)

```python
res = g.throw()
```

### Step 5: Call self.assertTrue()

```python
self.assertTrue(isinstance(res, greenlet.GreenletExit))
```

### Step 6: Call self.assertTrue()

```python
self.assertTrue(g.dead)
```

### Step 7: Assign res = g.throw(...)

```python
res = g.throw()
```

### Step 8: Call self.assertTrue()

```python
self.assertTrue(isinstance(res, greenlet.GreenletExit))
```

### Step 9: Call switch()

```python
switch('ok')
```

### Step 10: Call switch()

```python
switch('fail')
```


## Complete Example

```python
# Workflow
def f():
    switch('ok')
    switch('fail')
g = greenlet(f)
res = g.switch()
self.assertEqual(res, 'ok')
res = g.throw()
self.assertTrue(isinstance(res, greenlet.GreenletExit))
self.assertTrue(g.dead)
res = g.throw()
self.assertTrue(isinstance(res, greenlet.GreenletExit))
```

## Next Steps


---

*Source: test_throw.py:49 | Complexity: Advanced | Last updated: 2026-06-02*