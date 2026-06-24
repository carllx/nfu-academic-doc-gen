# How To: Hashes Stay The Same With Numpy Objects

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hashes stay the same with numpy objects

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

### Step 1: Assign to_hash_list_one = create_objects_to_hash(...)

```python
to_hash_list_one = create_objects_to_hash()
```

**Verification:**
```python
assert hash_1 == hash_2
```

### Step 2: Assign to_hash_list_two = create_objects_to_hash(...)

```python
to_hash_list_two = create_objects_to_hash()
```

**Verification:**
```python
assert hash_1 == hash_3
```

### Step 3: Assign e1 = ProcessPoolExecutor(...)

```python
e1 = ProcessPoolExecutor(max_workers=1)
```

### Step 4: Assign e2 = ProcessPoolExecutor(...)

```python
e2 = ProcessPoolExecutor(max_workers=1)
```

### Step 5: Assign rng = np.random.RandomState(...)

```python
rng = np.random.RandomState(42)
```

### Step 6: Assign to_hash_list = value

```python
to_hash_list = [rng.randint(-1000, high=1000, size=50).astype('<i8'), tuple((rng.randn(3).astype('<f4') for _ in range(5))), [rng.randn(3).astype('<f4') for _ in range(5)], {-3333: rng.randn(3, 5).astype('<f4'), 0: [rng.randint(10, size=20).astype('<i8'), rng.randn(10).astype('<f4')]}, np.arange(100, dtype='<i8').reshape((10, 10)), np.asfortranarray(np.arange(100, dtype='<i8').reshape((10, 10))), np.arange(100, dtype='<i8').reshape((10, 10))[:, :2]]
```

### Step 7: Call e1.shutdown()

```python
e1.shutdown()
```

### Step 8: Call e2.shutdown()

```python
e2.shutdown()
```

### Step 9: Assign hash_1 = e1.submit.result(...)

```python
hash_1 = e1.submit(hash, obj_1).result()
```

### Step 10: Assign hash_2 = e2.submit.result(...)

```python
hash_2 = e2.submit(hash, obj_1).result()
```

**Verification:**
```python
assert hash_1 == hash_2
```

### Step 11: Assign hash_3 = e1.submit.result(...)

```python
hash_3 = e1.submit(hash, obj_2).result()
```

**Verification:**
```python
assert hash_1 == hash_3
```


## Complete Example

```python
# Workflow
def create_objects_to_hash():
    rng = np.random.RandomState(42)
    to_hash_list = [rng.randint(-1000, high=1000, size=50).astype('<i8'), tuple((rng.randn(3).astype('<f4') for _ in range(5))), [rng.randn(3).astype('<f4') for _ in range(5)], {-3333: rng.randn(3, 5).astype('<f4'), 0: [rng.randint(10, size=20).astype('<i8'), rng.randn(10).astype('<f4')]}, np.arange(100, dtype='<i8').reshape((10, 10)), np.asfortranarray(np.arange(100, dtype='<i8').reshape((10, 10))), np.arange(100, dtype='<i8').reshape((10, 10))[:, :2]]
    return to_hash_list
to_hash_list_one = create_objects_to_hash()
to_hash_list_two = create_objects_to_hash()
e1 = ProcessPoolExecutor(max_workers=1)
e2 = ProcessPoolExecutor(max_workers=1)
try:
    for obj_1, obj_2 in zip(to_hash_list_one, to_hash_list_two):
        hash_1 = e1.submit(hash, obj_1).result()
        hash_2 = e2.submit(hash, obj_1).result()
        assert hash_1 == hash_2
        hash_3 = e1.submit(hash, obj_2).result()
        assert hash_1 == hash_3
finally:
    e1.shutdown()
    e2.shutdown()
```

## Next Steps


---

*Source: test_hashing.py:438 | Complexity: Advanced | Last updated: 2026-06-02*