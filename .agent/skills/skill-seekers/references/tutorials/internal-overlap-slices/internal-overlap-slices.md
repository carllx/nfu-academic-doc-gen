# How To: Internal Overlap Slices

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test internal overlap slices

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `numpy`
- `numpy._core`
- `numpy._core._multiarray_tests`
- `numpy.lib.stride_tricks`
- `numpy.testing`
- `numpy.lib._stride_tricks_impl`


## Step-by-Step Guide

### Step 1: Assign x = np.zeros(...)

```python
x = np.zeros([17, 34, 71, 97], dtype=np.int16)
```

**Verification:**
```python
assert_(not internal_overlap(a))
```

### Step 2: Assign rng = np.random.RandomState(...)

```python
rng = np.random.RandomState(1234)
```

### Step 3: Assign cases = 0

```python
cases = 0
```

### Step 4: Assign min_count = 5000

```python
min_count = 5000
```

### Step 5: Assign start = rng.randint(...)

```python
start = rng.randint(0, n + 1, dtype=np.intp)
```

### Step 6: Assign stop = rng.randint(...)

```python
stop = rng.randint(start, n + 1, dtype=np.intp)
```

### Step 7: Assign steps = tuple(...)

```python
steps = tuple((rng.randint(1, 11, dtype=np.intp) if rng.randint(0, 5, dtype=np.intp) == 0 else 1 for j in range(x.ndim)))
```

### Step 8: Assign t1 = np.arange(...)

```python
t1 = np.arange(x.ndim)
```

### Step 9: Call rng.shuffle()

```python
rng.shuffle(t1)
```

### Step 10: Assign s1 = tuple(...)

```python
s1 = tuple((random_slice(p, s) for p, s in zip(x.shape, steps)))
```

### Step 11: Assign a = unknown.transpose(...)

```python
a = x[s1].transpose(t1)
```

### Step 12: Call assert_()

```python
assert_(not internal_overlap(a))
```

### Step 13: Assign unknown = value

```python
stop, start = (start, stop)
```


## Complete Example

```python
# Workflow
x = np.zeros([17, 34, 71, 97], dtype=np.int16)
rng = np.random.RandomState(1234)

def random_slice(n, step):
    start = rng.randint(0, n + 1, dtype=np.intp)
    stop = rng.randint(start, n + 1, dtype=np.intp)
    if rng.randint(0, 2, dtype=np.intp) == 0:
        stop, start = (start, stop)
        step *= -1
    return slice(start, stop, step)
cases = 0
min_count = 5000
while cases < min_count:
    steps = tuple((rng.randint(1, 11, dtype=np.intp) if rng.randint(0, 5, dtype=np.intp) == 0 else 1 for j in range(x.ndim)))
    t1 = np.arange(x.ndim)
    rng.shuffle(t1)
    s1 = tuple((random_slice(p, s) for p, s in zip(x.shape, steps)))
    a = x[s1].transpose(t1)
    assert_(not internal_overlap(a))
    cases += 1
```

## Next Steps


---

*Source: test_mem_overlap.py:422 | Complexity: Advanced | Last updated: 2026-06-02*