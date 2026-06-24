# How To: Boundaries Match Start And Stop Exactly

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boundaries match start and stop exactly

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

### Step 1: Assign start = 0.3

```python
start = 0.3
```

**Verification:**
```python
assert_equal(y[0], start)
```

### Step 2: Assign stop = 20.3

```python
stop = 20.3
```

**Verification:**
```python
assert_equal(y[0], start)
```

### Step 3: Assign y = geomspace(...)

```python
y = geomspace(start, stop, num=1)
```

**Verification:**
```python
assert_equal(y[0], start)
```

### Step 4: Call assert_equal()

```python
assert_equal(y[0], start)
```

**Verification:**
```python
assert_equal(y[-1], stop)
```

### Step 5: Assign y = geomspace(...)

```python
y = geomspace(start, stop, num=1, endpoint=False)
```

**Verification:**
```python
assert_equal(y[0], start)
```

### Step 6: Call assert_equal()

```python
assert_equal(y[0], start)
```

### Step 7: Assign y = geomspace(...)

```python
y = geomspace(start, stop, num=3)
```

### Step 8: Call assert_equal()

```python
assert_equal(y[0], start)
```

### Step 9: Call assert_equal()

```python
assert_equal(y[-1], stop)
```

### Step 10: Assign y = geomspace(...)

```python
y = geomspace(start, stop, num=3, endpoint=False)
```

### Step 11: Call assert_equal()

```python
assert_equal(y[0], start)
```


## Complete Example

```python
# Workflow
start = 0.3
stop = 20.3
y = geomspace(start, stop, num=1)
assert_equal(y[0], start)
y = geomspace(start, stop, num=1, endpoint=False)
assert_equal(y[0], start)
y = geomspace(start, stop, num=3)
assert_equal(y[0], start)
assert_equal(y[-1], stop)
y = geomspace(start, stop, num=3, endpoint=False)
assert_equal(y[0], start)
```

## Next Steps


---

*Source: test_function_base.py:171 | Complexity: Advanced | Last updated: 2026-06-02*