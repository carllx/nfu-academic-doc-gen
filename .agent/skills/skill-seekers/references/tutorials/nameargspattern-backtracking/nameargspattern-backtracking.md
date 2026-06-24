# How To: Nameargspattern Backtracking

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: address ReDOS vulnerability:
https://github.com/numpy/numpy/issues/23338

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `importlib`
- `io`
- `textwrap`
- `time`
- `pytest`
- `numpy`
- `numpy.f2py`
- `numpy.f2py.crackfortran`

**Setup Required:**
```python
# Fixtures: adversary
```

## Step-by-Step Guide

### Step 1: 'address ReDOS vulnerability:\n        https://github.com/numpy/numpy/issues/23338'

```python
'address ReDOS vulnerability:\n        https://github.com/numpy/numpy/issues/23338'
```

**Verification:**
```python
assert np.median(times) < 0.2
```

### Step 2: Assign trials_per_batch = 12

```python
trials_per_batch = 12
```

**Verification:**
```python
assert not mtch
```

### Step 3: Assign batches_per_regex = 4

```python
batches_per_regex = 4
```

**Verification:**
```python
assert nameargspattern.search(good_version_of_adversary)
```

### Step 4: Assign unknown = value

```python
start_reps, end_reps = (15, 25)
```

### Step 5: Assign repeated_adversary = value

```python
repeated_adversary = adversary * ii
```

**Verification:**
```python
assert not mtch
```

### Step 6: Assign good_version_of_adversary = value

```python
good_version_of_adversary = repeated_adversary + '@)@'
```

**Verification:**
```python
assert nameargspattern.search(good_version_of_adversary)
```

### Step 7: Assign times = value

```python
times = []
```

**Verification:**
```python
assert np.median(times) < 0.2
```

### Step 8: Assign t0 = time.perf_counter(...)

```python
t0 = time.perf_counter()
```

### Step 9: Assign mtch = nameargspattern.search(...)

```python
mtch = nameargspattern.search(repeated_adversary)
```

### Step 10: Call times.append()

```python
times.append(time.perf_counter() - t0)
```


## Complete Example

```python
# Setup
# Fixtures: adversary

# Workflow
'address ReDOS vulnerability:\n        https://github.com/numpy/numpy/issues/23338'
trials_per_batch = 12
batches_per_regex = 4
start_reps, end_reps = (15, 25)
for ii in range(start_reps, end_reps):
    repeated_adversary = adversary * ii
    for _ in range(batches_per_regex):
        times = []
        for _ in range(trials_per_batch):
            t0 = time.perf_counter()
            mtch = nameargspattern.search(repeated_adversary)
            times.append(time.perf_counter() - t0)
        assert np.median(times) < 0.2
    assert not mtch
    good_version_of_adversary = repeated_adversary + '@)@'
    assert nameargspattern.search(good_version_of_adversary)
```

## Next Steps


---

*Source: test_crackfortran.py:309 | Complexity: Advanced | Last updated: 2026-06-02*