# How To: Start Stop Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test start stop array

## Prerequisites

**Required Modules:**
- `platform`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy._core.function_base`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign start = array(...)

```python
start = array([0.0, 1.0])
```

**Verification:**
```python
assert_equal(t1, t2)
```

### Step 2: Assign stop = array(...)

```python
stop = array([6.0, 7.0])
```

**Verification:**
```python
assert_equal(t3, t4)
```

### Step 3: Assign t1 = logspace(...)

```python
t1 = logspace(start, stop, 6)
```

**Verification:**
```python
assert_equal(t5, t2.T)
```

### Step 4: Assign t2 = stack(...)

```python
t2 = stack([logspace(_start, _stop, 6) for _start, _stop in zip(start, stop)], axis=1)
```

### Step 5: Call assert_equal()

```python
assert_equal(t1, t2)
```

### Step 6: Assign t3 = logspace(...)

```python
t3 = logspace(start, stop[0], 6)
```

### Step 7: Assign t4 = stack(...)

```python
t4 = stack([logspace(_start, stop[0], 6) for _start in start], axis=1)
```

### Step 8: Call assert_equal()

```python
assert_equal(t3, t4)
```

### Step 9: Assign t5 = logspace(...)

```python
t5 = logspace(start, stop, 6, axis=-1)
```

### Step 10: Call assert_equal()

```python
assert_equal(t5, t2.T)
```


## Complete Example

```python
# Workflow
start = array([0.0, 1.0])
stop = array([6.0, 7.0])
t1 = logspace(start, stop, 6)
t2 = stack([logspace(_start, _stop, 6) for _start, _stop in zip(start, stop)], axis=1)
assert_equal(t1, t2)
t3 = logspace(start, stop[0], 6)
t4 = stack([logspace(_start, stop[0], 6) for _start in start], axis=1)
assert_equal(t3, t4)
t5 = logspace(start, stop, 6, axis=-1)
assert_equal(t5, t2.T)
```

## Next Steps


---

*Source: test_function_base.py:82 | Complexity: Advanced | Last updated: 2026-06-02*