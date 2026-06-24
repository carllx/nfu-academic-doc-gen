# How To: Read Huge Row

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read huge row

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `io`
- `tempfile`
- `pytest`
- `numpy`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign row = value

```python
row = '1.5, 2.5,' * 50000
```

**Verification:**
```python
assert_equal(res, np.tile([1.5, 2.5], (2, 50000)))
```

### Step 2: Assign row = value

```python
row = row[:-1] + '\n'
```

### Step 3: Assign txt = StringIO(...)

```python
txt = StringIO(row * 2)
```

### Step 4: Assign res = np.loadtxt(...)

```python
res = np.loadtxt(txt, delimiter=',', dtype=float)
```

### Step 5: Call assert_equal()

```python
assert_equal(res, np.tile([1.5, 2.5], (2, 50000)))
```


## Complete Example

```python
# Workflow
row = '1.5, 2.5,' * 50000
row = row[:-1] + '\n'
txt = StringIO(row * 2)
res = np.loadtxt(txt, delimiter=',', dtype=float)
assert_equal(res, np.tile([1.5, 2.5], (2, 50000)))
```

## Next Steps


---

*Source: test_loadtxt.py:328 | Complexity: Intermediate | Last updated: 2026-06-02*