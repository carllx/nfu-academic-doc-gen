# How To: Ptp

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ptp

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

### Step 1: Assign unknown = self._create_data(...)

```python
_, X, _, m, mx, mX, _ = self._create_data()
```

**Verification:**
```python
assert_equal(mx.ptp(), np.ptp(mx.compressed()))
```

### Step 2: Assign unknown = value

```python
n, m = X.shape
```

**Verification:**
```python
assert_(eq(mX.ptp(0), cols))
```

### Step 3: Call assert_equal()

```python
assert_equal(mx.ptp(), np.ptp(mx.compressed()))
```

**Verification:**
```python
assert_(eq(mX.ptp(1), rows))
```

### Step 4: Assign rows = np.zeros(...)

```python
rows = np.zeros(n, np.float64)
```

### Step 5: Assign cols = np.zeros(...)

```python
cols = np.zeros(m, np.float64)
```

### Step 6: Call assert_()

```python
assert_(eq(mX.ptp(0), cols))
```

### Step 7: Call assert_()

```python
assert_(eq(mX.ptp(1), rows))
```

### Step 8: Assign unknown = np.ptp(...)

```python
cols[k] = np.ptp(mX[:, k].compressed())
```

### Step 9: Assign unknown = np.ptp(...)

```python
rows[k] = np.ptp(mX[k].compressed())
```


## Complete Example

```python
# Workflow
_, X, _, m, mx, mX, _ = self._create_data()
n, m = X.shape
assert_equal(mx.ptp(), np.ptp(mx.compressed()))
rows = np.zeros(n, np.float64)
cols = np.zeros(m, np.float64)
for k in range(m):
    cols[k] = np.ptp(mX[:, k].compressed())
for k in range(n):
    rows[k] = np.ptp(mX[k].compressed())
assert_(eq(mX.ptp(0), cols))
assert_(eq(mX.ptp(1), rows))
```

## Next Steps


---

*Source: test_old_ma.py:884 | Complexity: Advanced | Last updated: 2026-06-02*