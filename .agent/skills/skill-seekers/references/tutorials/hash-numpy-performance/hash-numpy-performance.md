# How To: Hash Numpy Performance

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check the performance of hashing numpy arrays:

In [22]: a = np.random.random(1000000)

In [23]: %timeit hashlib.md5(a).hexdigest()
100 loops, best of 3: 20.7 ms per loop

In [24]: %timeit hashlib.md5(pickle.dumps(a, protocol=2)).hexdigest()
1 loops, best of 3: 73.1 ms per loop

In [25]: %timeit hashlib.md5(cPickle.dumps(a, protocol=2)).hexdigest()
10 loops, best of 3: 53.9 ms per loop

In [26]: %timeit hash(a)
100 loops, best of 3: 20.8 ms per loop

## Prerequisites

**Required Modules:**
- `collections`
- `gc`
- `hashlib`
- `io`
- `itertools`
- `pickle`
- `random`
- `sys`
- `time`
- `concurrent.futures`
- `decimal`
- `joblib.func_inspect`
- `joblib.hashing`
- `joblib.memory`
- `joblib.test.common`
- `joblib.testing`


## Step-by-Step Guide

### Step 1: 'Check the performance of hashing numpy arrays:\n\n    In [22]: a = np.random.random(1000000)\n\n    In [23]: %timeit hashlib.md5(a).hexdigest()\n    100 loops, best of 3: 20.7 ms per loop\n\n    In [24]: %timeit hashlib.md5(pickle.dumps(a, protocol=2)).hexdigest()\n    1 loops, best of 3: 73.1 ms per loop\n\n    In [25]: %timeit hashlib.md5(cPickle.dumps(a, protocol=2)).hexdigest()\n    10 loops, best of 3: 53.9 ms per loop\n\n    In [26]: %timeit hash(a)\n    100 loops, best of 3: 20.8 ms per loop\n    '

```python
'Check the performance of hashing numpy arrays:\n\n    In [22]: a = np.random.random(1000000)\n\n    In [23]: %timeit hashlib.md5(a).hexdigest()\n    100 loops, best of 3: 20.7 ms per loop\n\n    In [24]: %timeit hashlib.md5(pickle.dumps(a, protocol=2)).hexdigest()\n    1 loops, best of 3: 73.1 ms per loop\n\n    In [25]: %timeit hashlib.md5(cPickle.dumps(a, protocol=2)).hexdigest()\n    10 loops, best of 3: 53.9 ms per loop\n\n    In [26]: %timeit hash(a)\n    100 loops, best of 3: 20.8 ms per loop\n    '
```

**Verification:**
```python
assert relative_diff < 0.3
```

### Step 2: Assign rnd = np.random.RandomState(...)

```python
rnd = np.random.RandomState(0)
```

**Verification:**
```python
assert relative_diff < 0.3
```

### Step 3: Assign a = rnd.random_sample(...)

```python
a = rnd.random_sample(1000000)
```

### Step 4: Assign relative_diff = relative_time(...)

```python
relative_diff = relative_time(md5_hash, hash, a)
```

**Verification:**
```python
assert relative_diff < 0.3
```

### Step 5: Assign time_hashlib = value

```python
time_hashlib = 3 * time_func(md5_hash, a)
```

### Step 6: Assign time_hash = time_func(...)

```python
time_hash = time_func(hash, (a, a, a))
```

### Step 7: Assign relative_diff = value

```python
relative_diff = 0.5 * (abs(time_hash - time_hashlib) / (time_hash + time_hashlib))
```

**Verification:**
```python
assert relative_diff < 0.3
```


## Complete Example

```python
# Workflow
'Check the performance of hashing numpy arrays:\n\n    In [22]: a = np.random.random(1000000)\n\n    In [23]: %timeit hashlib.md5(a).hexdigest()\n    100 loops, best of 3: 20.7 ms per loop\n\n    In [24]: %timeit hashlib.md5(pickle.dumps(a, protocol=2)).hexdigest()\n    1 loops, best of 3: 73.1 ms per loop\n\n    In [25]: %timeit hashlib.md5(cPickle.dumps(a, protocol=2)).hexdigest()\n    10 loops, best of 3: 53.9 ms per loop\n\n    In [26]: %timeit hash(a)\n    100 loops, best of 3: 20.8 ms per loop\n    '
rnd = np.random.RandomState(0)
a = rnd.random_sample(1000000)

def md5_hash(x):
    return hashlib.md5(memoryview(x)).hexdigest()
relative_diff = relative_time(md5_hash, hash, a)
assert relative_diff < 0.3
time_hashlib = 3 * time_func(md5_hash, a)
time_hash = time_func(hash, (a, a, a))
relative_diff = 0.5 * (abs(time_hash - time_hashlib) / (time_hash + time_hashlib))
assert relative_diff < 0.3
```

## Next Steps


---

*Source: test_hashing.py:207 | Complexity: Intermediate | Last updated: 2026-06-02*