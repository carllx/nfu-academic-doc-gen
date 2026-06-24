# How To: Stringdtype Multithreaded Access And Mutation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test stringdtype multithreaded access and mutation

## Prerequisites

**Required Modules:**
- `concurrent.futures`
- `sys`
- `threading`
- `pytest`
- `numpy`
- `numpy._core`
- `numpy._core.tests.test_stringdtype`
- `numpy.testing`
- `numpy.testing._private.utils`
- `concurrent.futures`
- `inspect`
- `inspect`


## Step-by-Step Guide

### Step 1: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(80991187)
```

### Step 2: Assign string_list = random_unicode_string_list(...)

```python
string_list = random_unicode_string_list()
```

### Step 3: Assign rnd = rng.random(...)

```python
rnd = rng.random()
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array(string_list, dtype='T')
```

### Step 5: Assign futures = value

```python
futures = [tpe.submit(func, arr) for _ in range(500)]
```

### Step 6: Assign num = np.random.randint(...)

```python
num = np.random.randint(0, arr.size)
```

### Step 7: Assign unknown = value

```python
arr[num] = arr[num] + 'hello'
```

### Step 8: Call f.result()

```python
f.result()
```

### Step 9: Call np.add()

```python
np.add(arr, arr)
```

### Step 10: Call np.add()

```python
np.add(arr, arr, out=arr)
```

### Step 11: Assign unknown = string_list

```python
arr[:] = string_list
```

### Step 12: Call np.multiply()

```python
np.multiply(arr, np.int64(2))
```

### Step 13: Call np.multiply()

```python
np.multiply(arr, np.int64(2), out=arr)
```


## Complete Example

```python
# Workflow
rng = np.random.default_rng(80991187)
string_list = random_unicode_string_list()

def func(arr):
    rnd = rng.random()
    if rnd < 0.25:
        num = np.random.randint(0, arr.size)
        arr[num] = arr[num] + 'hello'
    elif rnd < 0.5:
        if rnd < 0.375:
            np.add(arr, arr)
        else:
            np.add(arr, arr, out=arr)
    elif rnd < 0.75:
        if rnd < 0.875:
            np.multiply(arr, np.int64(2))
        else:
            np.multiply(arr, np.int64(2), out=arr)
    else:
        arr[:] = string_list
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as tpe:
    arr = np.array(string_list, dtype='T')
    futures = [tpe.submit(func, arr) for _ in range(500)]
    for f in futures:
        f.result()
```

## Next Steps


---

*Source: test_multithreading.py:237 | Complexity: Advanced | Last updated: 2026-06-02*