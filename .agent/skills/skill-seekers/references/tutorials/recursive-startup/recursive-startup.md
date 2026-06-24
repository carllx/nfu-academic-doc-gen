# How To: Recursive Startup

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test recursive startup

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

### Step 1: Assign g = convoluted(...)

```python
g = convoluted()
```

### Step 2: Call self.assertEqual()

```python
self.assertEqual(g.switch(42), 43)
```

### Step 3: Assign self.expect_greenlet_leak = True

```python
self.expect_greenlet_leak = True
```

### Step 4: Call RawGreenlet.__init__()

```python
RawGreenlet.__init__(self)
```

### Step 5: Assign self.count = 0

```python
self.count = 0
```

### Step 6: Assign self.count = 1

```python
self.count = 1
```

### Step 7: Call self.switch()

```python
self.switch(43)
```

### Step 8: Call self.parent.switch()

```python
self.parent.switch(value)
```


## Complete Example

```python
# Workflow
class convoluted(RawGreenlet):

    def __init__(self):
        RawGreenlet.__init__(self)
        self.count = 0

    def __getattribute__(self, name):
        if name == 'run' and self.count == 0:
            self.count = 1
            self.switch(43)
        return RawGreenlet.__getattribute__(self, name)

    def run(self, value):
        while True:
            self.parent.switch(value)
g = convoluted()
self.assertEqual(g.switch(42), 43)
self.expect_greenlet_leak = True
```

## Next Steps


---

*Source: test_greenlet.py:513 | Complexity: Advanced | Last updated: 2026-06-02*