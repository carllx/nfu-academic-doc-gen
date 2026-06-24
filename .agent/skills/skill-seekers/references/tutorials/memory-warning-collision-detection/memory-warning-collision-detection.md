# How To: Memory Warning Collision Detection

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memory warning collision detection

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: tmpdir
```

## Step-by-Step Guide

### Step 1: Assign memory = Memory(...)

```python
memory = Memory(location=tmpdir.strpath, verbose=0)
```

**Verification:**
```python
assert len(warninfo) == 2
```

### Step 2: Assign a1 = eval(...)

```python
a1 = eval('lambda x: x')
```

**Verification:**
```python
assert 'cannot detect' in str(warninfo[0].message).lower()
```

### Step 3: Assign a1 = memory.cache(...)

```python
a1 = memory.cache(a1)
```

### Step 4: Assign b1 = eval(...)

```python
b1 = eval('lambda x: x+1')
```

### Step 5: Assign b1 = memory.cache(...)

```python
b1 = memory.cache(b1)
```

**Verification:**
```python
assert len(warninfo) == 2
```

### Step 6: Call a1()

```python
a1(1)
```

### Step 7: Call b1()

```python
b1(1)
```

### Step 8: Call a1()

```python
a1(0)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
memory = Memory(location=tmpdir.strpath, verbose=0)
a1 = eval('lambda x: x')
a1 = memory.cache(a1)
b1 = eval('lambda x: x+1')
b1 = memory.cache(b1)
with warns(JobLibCollisionWarning) as warninfo:
    a1(1)
    b1(1)
    a1(0)
assert len(warninfo) == 2
assert 'cannot detect' in str(warninfo[0].message).lower()
```

## Next Steps


---

*Source: test_memory.py:330 | Complexity: Advanced | Last updated: 2026-06-02*