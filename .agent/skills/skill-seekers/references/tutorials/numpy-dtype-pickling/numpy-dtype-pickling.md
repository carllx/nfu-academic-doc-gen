# How To: Numpy Dtype Pickling

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy dtype pickling

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

### Step 1: Assign dt1 = np.dtype(...)

```python
dt1 = np.dtype('f4')
```

**Verification:**
```python
assert dt1 is dt2
```

### Step 2: Assign dt2 = np.dtype(...)

```python
dt2 = np.dtype('f4')
```

**Verification:**
```python
assert hash(dt1) == hash(dt2)
```

### Step 3: Assign dt1_roundtripped = pickle.loads(...)

```python
dt1_roundtripped = pickle.loads(pickle.dumps(dt1))
```

**Verification:**
```python
assert dt1 is not dt1_roundtripped
```

### Step 4: Assign complex_dt1 = np.dtype(...)

```python
complex_dt1 = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
```

**Verification:**
```python
assert hash(dt1) == hash(dt1_roundtripped)
```

### Step 5: Assign complex_dt2 = np.dtype(...)

```python
complex_dt2 = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
```

**Verification:**
```python
assert hash([dt1, dt1]) == hash([dt1_roundtripped, dt1_roundtripped])
```

### Step 6: Assign complex_dt1_roundtripped = pickle.loads(...)

```python
complex_dt1_roundtripped = pickle.loads(pickle.dumps(complex_dt1))
```

**Verification:**
```python
assert hash([dt1, dt1]) == hash([dt1, dt1_roundtripped])
```


## Complete Example

```python
# Workflow
dt1 = np.dtype('f4')
dt2 = np.dtype('f4')
assert dt1 is dt2
assert hash(dt1) == hash(dt2)
dt1_roundtripped = pickle.loads(pickle.dumps(dt1))
assert dt1 is not dt1_roundtripped
assert hash(dt1) == hash(dt1_roundtripped)
assert hash([dt1, dt1]) == hash([dt1_roundtripped, dt1_roundtripped])
assert hash([dt1, dt1]) == hash([dt1, dt1_roundtripped])
complex_dt1 = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
complex_dt2 = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
assert hash(complex_dt1) == hash(complex_dt2)
complex_dt1_roundtripped = pickle.loads(pickle.dumps(complex_dt1))
assert complex_dt1_roundtripped is not complex_dt1
assert hash(complex_dt1) == hash(complex_dt1_roundtripped)
assert hash([complex_dt1, complex_dt1]) == hash([complex_dt1_roundtripped, complex_dt1_roundtripped])
assert hash([complex_dt1, complex_dt1]) == hash([complex_dt1_roundtripped, complex_dt1])
```

## Next Steps


---

*Source: test_hashing.py:355 | Complexity: Intermediate | Last updated: 2026-06-02*