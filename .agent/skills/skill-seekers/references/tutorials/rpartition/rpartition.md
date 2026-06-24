# How To: Rpartition

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rpartition

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `sys`
- `pytest`
- `numpy`
- `numpy._core._exceptions`
- `numpy.testing`
- `numpy.testing._private.utils`

**Setup Required:**
```python
# Fixtures: buf, sep, res1, res2, res3, dt
```

## Step-by-Step Guide

### Step 1: Assign buf = np.array(...)

```python
buf = np.array(buf, dtype=dt)
```

**Verification:**
```python
assert_array_equal(act1, res1)
```

### Step 2: Assign sep = np.array(...)

```python
sep = np.array(sep, dtype=dt)
```

**Verification:**
```python
assert_array_equal(act2, res2)
```

### Step 3: Assign res1 = np.array(...)

```python
res1 = np.array(res1, dtype=dt)
```

**Verification:**
```python
assert_array_equal(act3, res3)
```

### Step 4: Assign res2 = np.array(...)

```python
res2 = np.array(res2, dtype=dt)
```

**Verification:**
```python
assert_array_equal(act1 + act2 + act3, buf)
```

### Step 5: Assign res3 = np.array(...)

```python
res3 = np.array(res3, dtype=dt)
```

### Step 6: Assign unknown = np.strings.rpartition(...)

```python
act1, act2, act3 = np.strings.rpartition(buf, sep)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(act1, res1)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(act2, res2)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(act3, res3)
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(act1 + act2 + act3, buf)
```


## Complete Example

```python
# Setup
# Fixtures: buf, sep, res1, res2, res3, dt

# Workflow
buf = np.array(buf, dtype=dt)
sep = np.array(sep, dtype=dt)
res1 = np.array(res1, dtype=dt)
res2 = np.array(res2, dtype=dt)
res3 = np.array(res3, dtype=dt)
act1, act2, act3 = np.strings.rpartition(buf, sep)
assert_array_equal(act1, res1)
assert_array_equal(act2, res2)
assert_array_equal(act3, res3)
assert_array_equal(act1 + act2 + act3, buf)
```

## Next Steps


---

*Source: test_strings.py:1283 | Complexity: Advanced | Last updated: 2026-06-02*