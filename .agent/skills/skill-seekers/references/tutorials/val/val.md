# How To: Val

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test val

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
res = g.throw(RuntimeError('ciao'))
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(res, 'ok')
```

### Step 6: Assign g = greenlet(...)

```python
g = greenlet(f)
```

### Step 7: Assign res = g.switch(...)

```python
res = g.switch()
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(res, 'ok')
```

### Step 9: Assign res = g.throw(...)

```python
res = g.throw(RuntimeError, 'ciao')
```

### Step 10: Call self.assertEqual()

```python
self.assertEqual(res, 'ok')
```

### Step 11: Call switch()

```python
switch('fail')
```

### Step 12: Call switch()

```python
switch('ok')
```

### Step 13: Assign val = value

```python
val = sys.exc_info()[1]
```

### Step 14: Call switch()

```python
switch('ok')
```


## Complete Example

```python
# Workflow
def f():
    try:
        switch('ok')
    except RuntimeError:
        val = sys.exc_info()[1]
        if str(val) == 'ciao':
            switch('ok')
            return
    switch('fail')
g = greenlet(f)
res = g.switch()
self.assertEqual(res, 'ok')
res = g.throw(RuntimeError('ciao'))
self.assertEqual(res, 'ok')
g = greenlet(f)
res = g.switch()
self.assertEqual(res, 'ok')
res = g.throw(RuntimeError, 'ciao')
self.assertEqual(res, 'ok')
```

## Next Steps


---

*Source: test_throw.py:26 | Complexity: Advanced | Last updated: 2026-06-02*