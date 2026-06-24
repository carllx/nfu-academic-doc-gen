# How To: Trace Events Multiple Greenlets Switching Siblings

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test trace events multiple greenlets switching siblings

## Prerequisites

**Required Modules:**
- `__future__`
- `sys`
- `sysconfig`
- `greenlet`
- `unittest`


## Step-by-Step Guide

### Step 1: Assign tracer = PythonTracer(...)

```python
tracer = PythonTracer()
```

### Step 2: Assign g1 = None

```python
g1 = None
```

### Step 3: Assign g2 = None

```python
g2 = None
```

### Step 4: Assign g1 = greenlet.greenlet(...)

```python
g1 = greenlet.greenlet(g1_run)
```

### Step 5: Assign g2 = greenlet.greenlet(...)

```python
g2 = greenlet.greenlet(g2_run)
```

### Step 6: Call g1.switch()

```python
g1.switch()
```

### Step 7: Call g2.switch()

```python
g2.switch()
```

### Step 8: Assign x = g1.switch(...)

```python
x = g1.switch()
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(x, 42)
```

### Step 10: Call tpt_callback()

```python
tpt_callback()
```

### Step 11: Call self.assertEqual()

```python
self.assertEqual(tracer.actions, [('return', '__enter__'), ('call', 'tpt_callback'), ('return', 'tpt_callback'), ('c_call', 'g1_run'), ('call', 'tpt_callback'), ('return', 'tpt_callback'), ('call', '__exit__'), ('c_call', '__exit__')])
```

### Step 12: Call greenlet.getcurrent.parent.switch()

```python
greenlet.getcurrent().parent.switch()
```

### Step 13: Call tracer.__enter__()

```python
tracer.__enter__()
```

### Step 14: Call tpt_callback()

```python
tpt_callback()
```

### Step 15: Call g2.switch()

```python
g2.switch()
```

### Step 16: Call tpt_callback()

```python
tpt_callback()
```

### Step 17: Call greenlet.getcurrent.parent.switch()

```python
greenlet.getcurrent().parent.switch()
```

### Step 18: Call tpt_callback()

```python
tpt_callback()
```

### Step 19: Call tracer.__exit__()

```python
tracer.__exit__()
```

### Step 20: Call tpt_callback()

```python
tpt_callback()
```

### Step 21: Call g1.switch()

```python
g1.switch()
```


## Complete Example

```python
# Workflow
tracer = PythonTracer()
g1 = None
g2 = None

def g1_run():
    greenlet.getcurrent().parent.switch()
    tracer.__enter__()
    tpt_callback()
    g2.switch()
    tpt_callback()
    return 42

def g2_run():
    greenlet.getcurrent().parent.switch()
    tpt_callback()
    tracer.__exit__()
    tpt_callback()
    g1.switch()
g1 = greenlet.greenlet(g1_run)
g2 = greenlet.greenlet(g2_run)
g1.switch()
g2.switch()
x = g1.switch()
self.assertEqual(x, 42)
tpt_callback()
self.assertEqual(tracer.actions, [('return', '__enter__'), ('call', 'tpt_callback'), ('return', 'tpt_callback'), ('c_call', 'g1_run'), ('call', 'tpt_callback'), ('return', 'tpt_callback'), ('call', '__exit__'), ('c_call', '__exit__')])
```

## Next Steps


---

*Source: test_tracing.py:248 | Complexity: Advanced | Last updated: 2026-06-02*