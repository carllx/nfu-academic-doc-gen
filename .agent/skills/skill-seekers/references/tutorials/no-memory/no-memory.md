# How To: No Memory

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test memory with location=None: no memoize

## Prerequisites

**Required Modules:**
- `datetime`
- `functools`
- `gc`
- `logging`
- `os`
- `os.path`
- `pickle`
- `shutil`
- `sys`
- `textwrap`
- `time`
- `pathlib`
- `pytest`
- `joblib._store_backends`
- `joblib.hashing`
- `joblib.memory`
- `joblib.parallel`
- `joblib.test.common`
- `joblib.testing`
- `functools`
- `tmp_joblib_`
- `tmp_joblib_`
- `datetime`
- `time`


## Step-by-Step Guide

### Step 1: 'Test memory with location=None: no memoize'

```python
'Test memory with location=None: no memoize'
```

**Verification:**
```python
assert len(accumulator) == current_accumulator + 1
```

### Step 2: Assign accumulator = list(...)

```python
accumulator = list()
```

### Step 3: Assign memory = Memory(...)

```python
memory = Memory(location=None, verbose=0)
```

### Step 4: Assign gg = memory.cache(...)

```python
gg = memory.cache(ff)
```

### Step 5: Call accumulator.append()

```python
accumulator.append(1)
```

### Step 6: Assign current_accumulator = len(...)

```python
current_accumulator = len(accumulator)
```

### Step 7: Call gg()

```python
gg(1)
```

**Verification:**
```python
assert len(accumulator) == current_accumulator + 1
```


## Complete Example

```python
# Workflow
'Test memory with location=None: no memoize'
accumulator = list()

def ff(arg):
    accumulator.append(1)
    return arg
memory = Memory(location=None, verbose=0)
gg = memory.cache(ff)
for _ in range(4):
    current_accumulator = len(accumulator)
    gg(1)
    assert len(accumulator) == current_accumulator + 1
```

## Next Steps


---

*Source: test_memory.py:244 | Complexity: Intermediate | Last updated: 2026-06-02*