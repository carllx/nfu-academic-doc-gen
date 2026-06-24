# How To: Trace Events Multiple Greenlets Switching

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test trace events multiple greenlets switching

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

### Step 6: Assign x = g1.switch(...)

```python
x = g1.switch()
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(x, 42)
```

### Step 8: Call tpt_callback()

```python
tpt_callback()
```

### Step 9: Call self.assertEqual()

```python
self.assertEqual(tracer.actions, [('return', '__enter__'), ('call', 'tpt_callback'), ('return', 'tpt_callback'), ('c_call', 'g1_run'), ('call', 'g2_run'), ('call', 'tpt_callback'), ('return', 'tpt_callback'), ('call', '__exit__'), ('c_call', '__exit__')])
```

### Step 10: Call tracer.__enter__()

```python
tracer.__enter__()
```

### Step 11: Call tpt_callback()

```python
tpt_callback()
```

### Step 12: Call g2.switch()

```python
g2.switch()
```

### Step 13: Call tpt_callback()

```python
tpt_callback()
```

### Step 14: Call tpt_callback()

```python
tpt_callback()
```

### Step 15: Call tracer.__exit__()

```python
tracer.__exit__()
```

### Step 16: Call tpt_callback()

```python
tpt_callback()
```

### Step 17: Call g1.switch()

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
    tracer.__enter__()
    tpt_callback()
    g2.switch()
    tpt_callback()
    return 42

def g2_run():
    tpt_callback()
    tracer.__exit__()
    tpt_callback()
    g1.switch()
g1 = greenlet.greenlet(g1_run)
g2 = greenlet.greenlet(g2_run)
x = g1.switch()
self.assertEqual(x, 42)
tpt_callback()
self.assertEqual(tracer.actions, [('return', '__enter__'), ('call', 'tpt_callback'), ('return', 'tpt_callback'), ('c_call', 'g1_run'), ('call', 'g2_run'), ('call', 'tpt_callback'), ('return', 'tpt_callback'), ('call', '__exit__'), ('c_call', '__exit__')])
```

## Next Steps


---

*Source: test_tracing.py:210 | Complexity: Advanced | Last updated: 2026-06-02*