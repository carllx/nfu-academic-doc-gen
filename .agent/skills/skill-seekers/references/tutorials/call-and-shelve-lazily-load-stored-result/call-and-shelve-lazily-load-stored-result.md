# How To: Call And Shelve Lazily Load Stored Result

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check call_and_shelve only load stored data if needed.

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

### Step 1: 'Check call_and_shelve only load stored data if needed.'

```python
'Check call_and_shelve only load stored data if needed.'
```

**Verification:**
```python
assert test_access_time_file.read() == 'test_access'
```

### Step 2: Assign test_access_time_file = tmpdir.join(...)

```python
test_access_time_file = tmpdir.join('test_access')
```

**Verification:**
```python
assert func(2) == 5
```

### Step 3: Call test_access_time_file.write()

```python
test_access_time_file.write('test_access')
```

**Verification:**
```python
assert isinstance(result, MemorizedResult)
```

### Step 4: Assign test_access_time = value

```python
test_access_time = os.stat(test_access_time_file.strpath).st_atime
```

**Verification:**
```python
assert os.stat(result_path).st_atime == first_access_time
```

### Step 5: Call time.sleep()

```python
time.sleep(0.5)
```

**Verification:**
```python
assert result.get() == 5
```

### Step 6: Assign memory = Memory(...)

```python
memory = Memory(location=tmpdir.strpath, verbose=0)
```

**Verification:**
```python
assert os.stat(result_path).st_atime > first_access_time
```

### Step 7: Assign func = memory.cache(...)

```python
func = memory.cache(f)
```

### Step 8: Assign args_id = func._get_args_id(...)

```python
args_id = func._get_args_id(2)
```

### Step 9: Assign result_path = os.path.join(...)

```python
result_path = os.path.join(memory.store_backend.location, func.func_id, args_id, 'output.pkl')
```

**Verification:**
```python
assert func(2) == 5
```

### Step 10: Assign first_access_time = value

```python
first_access_time = os.stat(result_path).st_atime
```

### Step 11: Call time.sleep()

```python
time.sleep(1)
```

### Step 12: Assign result = func.call_and_shelve(...)

```python
result = func.call_and_shelve(2)
```

**Verification:**
```python
assert isinstance(result, MemorizedResult)
```

### Step 13: Call time.sleep()

```python
time.sleep(1)
```

**Verification:**
```python
assert result.get() == 5
```

### Step 14: Call pytest.skip()

```python
pytest.skip('filesystem does not support fine-grained access time attribute')
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir

# Workflow
'Check call_and_shelve only load stored data if needed.'
test_access_time_file = tmpdir.join('test_access')
test_access_time_file.write('test_access')
test_access_time = os.stat(test_access_time_file.strpath).st_atime
time.sleep(0.5)
assert test_access_time_file.read() == 'test_access'
if test_access_time == os.stat(test_access_time_file.strpath).st_atime:
    pytest.skip('filesystem does not support fine-grained access time attribute')
memory = Memory(location=tmpdir.strpath, verbose=0)
func = memory.cache(f)
args_id = func._get_args_id(2)
result_path = os.path.join(memory.store_backend.location, func.func_id, args_id, 'output.pkl')
assert func(2) == 5
first_access_time = os.stat(result_path).st_atime
time.sleep(1)
result = func.call_and_shelve(2)
assert isinstance(result, MemorizedResult)
assert os.stat(result_path).st_atime == first_access_time
time.sleep(1)
assert result.get() == 5
assert os.stat(result_path).st_atime > first_access_time
```

## Next Steps


---

*Source: test_memory.py:661 | Complexity: Advanced | Last updated: 2026-06-02*