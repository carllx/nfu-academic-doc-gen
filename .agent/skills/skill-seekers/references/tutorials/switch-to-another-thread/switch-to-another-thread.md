# How To: Switch To Another Thread

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test switch to another thread

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

### Step 1: Assign data = value

```python
data = {}
```

### Step 2: Assign created_event = threading.Event(...)

```python
created_event = threading.Event()
```

### Step 3: Assign done_event = threading.Event(...)

```python
done_event = threading.Event()
```

### Step 4: Assign thread = threading.Thread(...)

```python
thread = threading.Thread(target=run)
```

### Step 5: Call thread.start()

```python
thread.start()
```

### Step 6: Call created_event.wait()

```python
created_event.wait(10)
```

### Step 7: Call done_event.set()

```python
done_event.set()
```

### Step 8: Call thread.join()

```python
thread.join(10)
```

### Step 9: Call data.clear()

```python
data.clear()
```

### Step 10: Assign unknown = RawGreenlet(...)

```python
data['g'] = RawGreenlet(lambda: None)
```

### Step 11: Call created_event.set()

```python
created_event.set()
```

### Step 12: Call done_event.wait()

```python
done_event.wait(10)
```

### Step 13: Call unknown.switch()

```python
data['g'].switch()
```


## Complete Example

```python
# Workflow
data = {}
created_event = threading.Event()
done_event = threading.Event()

def run():
    data['g'] = RawGreenlet(lambda: None)
    created_event.set()
    done_event.wait(10)
thread = threading.Thread(target=run)
thread.start()
created_event.wait(10)
with self.assertRaises(greenlet.error):
    data['g'].switch()
done_event.set()
thread.join(10)
data.clear()
```

## Next Steps


---

*Source: test_greenlet.py:334 | Complexity: Advanced | Last updated: 2026-06-02*