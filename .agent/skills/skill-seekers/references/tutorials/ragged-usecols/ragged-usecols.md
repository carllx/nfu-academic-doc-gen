# How To: Ragged Usecols

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ragged usecols

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

### Step 1: Assign txt = StringIO(...)

```python
txt = StringIO('0,0,XXX\n0,XXX,0,XXX\n0,XXX,XXX,0,XXX\n')
```

**Verification:**
```python
assert_equal(res, expected)
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([[0, 0], [0, 0], [0, 0]])
```

### Step 3: Assign res = np.loadtxt(...)

```python
res = np.loadtxt(txt, dtype=float, delimiter=',', usecols=[0, -2])
```

### Step 4: Call assert_equal()

```python
assert_equal(res, expected)
```

### Step 5: Assign txt = StringIO(...)

```python
txt = StringIO('0,0,XXX\n0\n0,XXX,XXX,0,XXX\n')
```

### Step 6: Call np.loadtxt()

```python
np.loadtxt(txt, dtype=float, delimiter=',', usecols=[0, -2])
```


## Complete Example

```python
# Workflow
txt = StringIO('0,0,XXX\n0,XXX,0,XXX\n0,XXX,XXX,0,XXX\n')
expected = np.array([[0, 0], [0, 0], [0, 0]])
res = np.loadtxt(txt, dtype=float, delimiter=',', usecols=[0, -2])
assert_equal(res, expected)
txt = StringIO('0,0,XXX\n0\n0,XXX,XXX,0,XXX\n')
with pytest.raises(ValueError, match='invalid column index -2 at row 2 with 1 columns'):
    np.loadtxt(txt, dtype=float, delimiter=',', usecols=[0, -2])
```

## Next Steps


---

*Source: test_loadtxt.py:251 | Complexity: Intermediate | Last updated: 2026-06-02*