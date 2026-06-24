# How To: Memmapping Temp Folder Thread Safety

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test memmapping temp folder thread safety

## Prerequisites

**Required Modules:**
- `faulthandler`
- `gc`
- `itertools`
- `mmap`
- `os`
- `pickle`
- `platform`
- `subprocess`
- `sys`
- `threading`
- `time`
- `pytest`
- `joblib._memmapping_reducer`
- `joblib._memmapping_reducer`
- `joblib.backports`
- `joblib.executor`
- `joblib.parallel`
- `joblib.pool`
- `joblib.test.common`
- `joblib.testing`
- `joblib._memmapping_reducer`


## Step-by-Step Guide

### Step 1: Assign array = np.arange(...)

```python
array = np.arange(int(100.0))
```

**Verification:**
```python
assert len(temp_dirs_thread_1) == 1
```

### Step 2: Assign temp_dirs_thread_1 = set(...)

```python
temp_dirs_thread_1 = set()
```

**Verification:**
```python
assert len(temp_dirs_thread_2) == 1
```

### Step 3: Assign temp_dirs_thread_2 = set(...)

```python
temp_dirs_thread_2 = set()
```

**Verification:**
```python
assert temp_dirs_thread_1 != temp_dirs_thread_2
```

### Step 4: Assign t1 = threading.Thread(...)

```python
t1 = threading.Thread(target=concurrent_get_filename, args=(array, temp_dirs_thread_1))
```

### Step 5: Assign t2 = threading.Thread(...)

```python
t2 = threading.Thread(target=concurrent_get_filename, args=(array, temp_dirs_thread_2))
```

### Step 6: Call t1.start()

```python
t1.start()
```

### Step 7: Call t2.start()

```python
t2.start()
```

### Step 8: Call t1.join()

```python
t1.join()
```

### Step 9: Call t2.join()

```python
t2.join()
```

**Verification:**
```python
assert len(temp_dirs_thread_1) == 1
```

### Step 10: Assign unknown = p(...)

```python
[filename] = p((delayed(getattr)(array, 'filename') for _ in range(1)))
```

### Step 11: Call temp_dirs.add()

```python
temp_dirs.add(os.path.dirname(filename))
```


## Complete Example

```python
# Workflow
array = np.arange(int(100.0))
temp_dirs_thread_1 = set()
temp_dirs_thread_2 = set()

def concurrent_get_filename(array, temp_dirs):
    with Parallel(backend='loky', n_jobs=2, max_nbytes=10) as p:
        for i in range(10):
            [filename] = p((delayed(getattr)(array, 'filename') for _ in range(1)))
            temp_dirs.add(os.path.dirname(filename))
t1 = threading.Thread(target=concurrent_get_filename, args=(array, temp_dirs_thread_1))
t2 = threading.Thread(target=concurrent_get_filename, args=(array, temp_dirs_thread_2))
t1.start()
t2.start()
t1.join()
t2.join()
assert len(temp_dirs_thread_1) == 1
assert len(temp_dirs_thread_2) == 1
assert temp_dirs_thread_1 != temp_dirs_thread_2
```

## Next Steps


---

*Source: test_memmapping.py:514 | Complexity: Advanced | Last updated: 2026-06-02*