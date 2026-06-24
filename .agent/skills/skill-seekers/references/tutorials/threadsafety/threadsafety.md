# How To: Threadsafety

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test threadsafety

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

### Step 1: Assign errors = value

```python
errors = []
```

**Verification:**
```python
assert r == 123
```

### Step 2: Assign threads = value

```python
threads = [threading.Thread(target=runner, args=(arg,)) for arg in ('t', 't2') for n in range(20)]
```

**Verification:**
```python
assert r == 42
```

### Step 3: Assign errors = unknown.join(...)

```python
errors = '\n\n'.join(errors)
```

### Step 4: Call time.sleep()

```python
time.sleep(0.001)
```

### Step 5: Assign r = self.module.t(...)

```python
r = self.module.t(lambda: 123)
```

**Verification:**
```python
assert r == 123
```

### Step 6: Call t.start()

```python
t.start()
```

### Step 7: Call t.join()

```python
t.join()
```

### Step 8: Assign r = self.module.t(...)

```python
r = self.module.t(cb)
```

**Verification:**
```python
assert r == 42
```

### Step 9: Call self.check_function()

```python
self.check_function(name)
```

### Step 10: Call errors.append()

```python
errors.append(traceback.format_exc())
```


## Complete Example

```python
# Workflow
errors = []

def cb():
    time.sleep(0.001)
    r = self.module.t(lambda: 123)
    assert r == 123
    return 42

def runner(name):
    try:
        for j in range(50):
            r = self.module.t(cb)
            assert r == 42
            self.check_function(name)
    except Exception:
        errors.append(traceback.format_exc())
threads = [threading.Thread(target=runner, args=(arg,)) for arg in ('t', 't2') for n in range(20)]
for t in threads:
    t.start()
for t in threads:
    t.join()
errors = '\n\n'.join(errors)
if errors:
    raise AssertionError(errors)
```

## Next Steps


---

*Source: test_callback.py:126 | Complexity: Advanced | Last updated: 2026-06-02*