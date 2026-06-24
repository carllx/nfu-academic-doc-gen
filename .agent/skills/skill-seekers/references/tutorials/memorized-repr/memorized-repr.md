# How To: Memorized Repr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memorized repr

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

### Step 1: Assign func = MemorizedFunc(...)

```python
func = MemorizedFunc(f, tmpdir.strpath)
```

**Verification:**
```python
assert result.get() == result2.get()
```

### Step 2: Assign result = func.call_and_shelve(...)

```python
result = func.call_and_shelve(2)
```

**Verification:**
```python
assert repr(func) == repr(func2)
```

### Step 3: Assign func2 = MemorizedFunc(...)

```python
func2 = MemorizedFunc(f, tmpdir.strpath)
```

### Step 4: Assign result2 = func2.call_and_shelve(...)

```python
result2 = func2.call_and_shelve(2)
```

**Verification:**
```python
assert result.get() == result2.get()
```

### Step 5: Assign func = NotMemorizedFunc(...)

```python
func = NotMemorizedFunc(f)
```

### Step 6: Call repr()

```python
repr(func)
```

### Step 7: Call repr()

```python
repr(func.call_and_shelve(2))
```

### Step 8: Assign func = MemorizedFunc(...)

```python
func = MemorizedFunc(f, tmpdir.strpath, verbose=11, timestamp=time.time())
```

### Step 9: Assign result = func.call_and_shelve(...)

```python
result = func.call_and_shelve(11)
```

### Step 10: Call result.get()

```python
result.get()
```

### Step 11: Assign func = MemorizedFunc(...)

```python
func = MemorizedFunc(f, tmpdir.strpath, verbose=11)
```

### Step 12: Assign result = func.call_and_shelve(...)

```python
result = func.call_and_shelve(11)
```

### Step 13: Call result.get()

```python
result.get()
```

### Step 14: Assign func = MemorizedFunc(...)

```python
func = MemorizedFunc(f, tmpdir.strpath, verbose=5, timestamp=time.time())
```

### Step 15: Assign result = func.call_and_shelve(...)

```python
result = func.call_and_shelve(11)
```

### Step 16: Call result.get()

```python
result.get()
```

### Step 17: Assign func = MemorizedFunc(...)

```python
func = MemorizedFunc(f, tmpdir.strpath, verbose=5)
```

### Step 18: Assign result = func.call_and_shelve(...)

```python
result = func.call_and_shelve(11)
```

### Step 19: Call result.get()

```python
result.get()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
func = MemorizedFunc(f, tmpdir.strpath)
result = func.call_and_shelve(2)
func2 = MemorizedFunc(f, tmpdir.strpath)
result2 = func2.call_and_shelve(2)
assert result.get() == result2.get()
assert repr(func) == repr(func2)
func = NotMemorizedFunc(f)
repr(func)
repr(func.call_and_shelve(2))
func = MemorizedFunc(f, tmpdir.strpath, verbose=11, timestamp=time.time())
result = func.call_and_shelve(11)
result.get()
func = MemorizedFunc(f, tmpdir.strpath, verbose=11)
result = func.call_and_shelve(11)
result.get()
func = MemorizedFunc(f, tmpdir.strpath, verbose=5, timestamp=time.time())
result = func.call_and_shelve(11)
result.get()
func = MemorizedFunc(f, tmpdir.strpath, verbose=5)
result = func.call_and_shelve(11)
result.get()
```

## Next Steps


---

*Source: test_memory.py:709 | Complexity: Advanced | Last updated: 2026-06-02*