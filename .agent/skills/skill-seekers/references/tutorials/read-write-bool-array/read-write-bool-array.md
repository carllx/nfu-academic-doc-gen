# How To: Read Write Bool Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read write bool array

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy.testing`
- `time`
- `multiprocessing`
- `multiprocessing`
- `concurrent.futures`
- `multiprocessing`


## Step-by-Step Guide

### Step 1: Assign n = 10000

```python
n = 10000
```

### Step 2: Assign shm = shared_memory.SharedMemory(...)

```python
shm = shared_memory.SharedMemory(create=True, size=n)
```

### Step 3: Call shm.unlink()

```python
shm.unlink()
```

### Step 4: Call f_writer.result()

```python
f_writer.result()
```

### Step 5: Call f_reader.result()

```python
f_reader.result()
```

### Step 6: Assign f_writer = executor.submit(...)

```python
f_writer = executor.submit(bool_array_writer, shm.name, n)
```

### Step 7: Assign f_reader = executor.submit(...)

```python
f_reader = executor.submit(bool_array_reader, shm.name, n)
```


## Complete Example

```python
# Workflow
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import shared_memory
n = 10000
shm = shared_memory.SharedMemory(create=True, size=n)
with ProcessPoolExecutor(max_workers=2) as executor:
    f_writer = executor.submit(bool_array_writer, shm.name, n)
    f_reader = executor.submit(bool_array_reader, shm.name, n)
shm.unlink()
f_writer.result()
f_reader.result()
```

## Next Steps


---

*Source: test_multiprocessing.py:35 | Complexity: Intermediate | Last updated: 2026-06-02*