# How To: Untracked Memory Doesnt Increase

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test untracked memory doesnt increase

## Prerequisites

**Required Modules:**
- `__future__`
- `sys`
- `gc`
- `time`
- `weakref`
- `threading`
- `greenlet`
- `leakcheck`
- `leakcheck`
- `leakcheck`


## Step-by-Step Guide

### Step 1: Call self._only_test_some_versions()

```python
self._only_test_some_versions()
```

### Step 2: Assign ITER = 10000

```python
ITER = 10000
```

### Step 3: Assign uss_before = self.get_process_uss(...)

```python
uss_before = self.get_process_uss()
```

### Step 4: Call self.assertLessEqual()

```python
self.assertLessEqual(uss_after, uss_before)
```

### Step 5: Call run_it()

```python
run_it()
```

### Step 6: Assign uss_before = max(...)

```python
uss_before = max(uss_before, self.get_process_uss())
```

### Step 7: Call run_it()

```python
run_it()
```

### Step 8: Assign uss_after = self.get_process_uss(...)

```python
uss_after = self.get_process_uss()
```

### Step 9: Call greenlet.greenlet.switch()

```python
greenlet.greenlet(f).switch()
```


## Complete Example

```python
# Workflow
self._only_test_some_versions()

def f():
    return 1
ITER = 10000

def run_it():
    for _ in range(ITER):
        greenlet.greenlet(f).switch()
for _ in range(3):
    run_it()
uss_before = self.get_process_uss()
for count in range(self.UNTRACK_ATTEMPTS):
    uss_before = max(uss_before, self.get_process_uss())
    run_it()
    uss_after = self.get_process_uss()
    if uss_after <= uss_before and count > 1:
        break
self.assertLessEqual(uss_after, uss_before)
```

## Next Steps


---

*Source: test_leaks.py:333 | Complexity: Advanced | Last updated: 2026-06-02*