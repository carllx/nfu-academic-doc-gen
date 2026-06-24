# How To: Testminmax2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test testMinMax2

## Prerequisites

**Required Modules:**
- `pickle`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Call assert_()

```python
assert_(eq(minimum([1, 2, 3], [4, 0, 9]), [1, 0, 3]))
```

**Verification:**
```python
assert_(eq(minimum([1, 2, 3], [4, 0, 9]), [1, 0, 3]))
```

### Step 2: Call assert_()

```python
assert_(eq(maximum([1, 2, 3], [4, 0, 9]), [4, 2, 9]))
```

**Verification:**
```python
assert_(eq(maximum([1, 2, 3], [4, 0, 9]), [4, 2, 9]))
```

### Step 3: Assign x = arange(...)

```python
x = arange(5)
```

**Verification:**
```python
assert_(eq(minimum(x, y), where(less(x, y), x, y)))
```

### Step 4: Assign y = value

```python
y = arange(5) - 2
```

**Verification:**
```python
assert_(eq(maximum(x, y), where(greater(x, y), x, y)))
```

### Step 5: Assign unknown = masked

```python
x[3] = masked
```

**Verification:**
```python
assert_(minimum.reduce(x) == 0)
```

### Step 6: Assign unknown = masked

```python
y[0] = masked
```

**Verification:**
```python
assert_(maximum.reduce(x) == 4)
```

### Step 7: Call assert_()

```python
assert_(eq(minimum(x, y), where(less(x, y), x, y)))
```

### Step 8: Call assert_()

```python
assert_(eq(maximum(x, y), where(greater(x, y), x, y)))
```

### Step 9: Call assert_()

```python
assert_(minimum.reduce(x) == 0)
```

### Step 10: Call assert_()

```python
assert_(maximum.reduce(x) == 4)
```


## Complete Example

```python
# Workflow
assert_(eq(minimum([1, 2, 3], [4, 0, 9]), [1, 0, 3]))
assert_(eq(maximum([1, 2, 3], [4, 0, 9]), [4, 2, 9]))
x = arange(5)
y = arange(5) - 2
x[3] = masked
y[0] = masked
assert_(eq(minimum(x, y), where(less(x, y), x, y)))
assert_(eq(maximum(x, y), where(greater(x, y), x, y)))
assert_(minimum.reduce(x) == 0)
assert_(maximum.reduce(x) == 4)
```

## Next Steps


---

*Source: test_old_ma.py:527 | Complexity: Advanced | Last updated: 2026-06-02*