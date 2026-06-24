# How To: Concurrent Safe

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Concurrent calls to spawn should have consistent results.

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `sysconfig`
- `threading`
- `unittest.mock`
- `distutils.errors`
- `distutils.tests`
- `distutils.util`
- `pytest`
- `distutils`


## Step-by-Step Guide

### Step 1: '\n        Concurrent calls to spawn should have consistent results.\n        '

```python
'\n        Concurrent calls to spawn should have consistent results.\n        '
```

**Verification:**
```python
assert all(threads)
```

### Step 2: Assign compiler = msvc.Compiler(...)

```python
compiler = msvc.Compiler()
```

### Step 3: Assign compiler._paths = 'expected'

```python
compiler._paths = 'expected'
```

### Step 4: Assign inner_cmd = 'import os; assert os.environ["PATH"] == "expected"'

```python
inner_cmd = 'import os; assert os.environ["PATH"] == "expected"'
```

### Step 5: Assign command = value

```python
command = [sys.executable, '-c', inner_cmd]
```

### Step 6: Assign threads = value

```python
threads = [CheckThread(target=compiler.spawn, args=[command]) for n in range(100)]
```

**Verification:**
```python
assert all(threads)
```

### Step 7: Call thread.start()

```python
thread.start()
```

### Step 8: Call thread.join()

```python
thread.join()
```


## Complete Example

```python
# Workflow
'\n        Concurrent calls to spawn should have consistent results.\n        '
compiler = msvc.Compiler()
compiler._paths = 'expected'
inner_cmd = 'import os; assert os.environ["PATH"] == "expected"'
command = [sys.executable, '-c', inner_cmd]
threads = [CheckThread(target=compiler.spawn, args=[command]) for n in range(100)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
assert all(threads)
```

## Next Steps


---

*Source: test_msvc.py:101 | Complexity: Advanced | Last updated: 2026-06-02*