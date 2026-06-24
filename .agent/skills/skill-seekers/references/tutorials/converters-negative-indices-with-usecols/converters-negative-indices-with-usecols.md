# How To: Converters Negative Indices With Usecols

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test converters negative indices with usecols

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
txt = StringIO('1.5,2.5,3.5\n3.0,4.0,XXX\n5.5,6.0,7.5\n')
```

**Verification:**
```python
assert_equal(res, expected)
```

### Step 2: Assign conv = value

```python
conv = {-1: lambda s: np.nan if s == 'XXX' else float(s)}
```

**Verification:**
```python
assert_array_equal(res, [[0, -1], [0, -1]])
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([[1.5, 3.5], [3.0, np.nan], [5.5, 7.5]])
```

### Step 4: Assign res = np.loadtxt(...)

```python
res = np.loadtxt(txt, dtype=np.float64, delimiter=',', converters=conv, usecols=[0, -1])
```

### Step 5: Call assert_equal()

```python
assert_equal(res, expected)
```

### Step 6: Assign res = np.loadtxt(...)

```python
res = np.loadtxt(StringIO('0,1,2\n0,1,2,3,4'), delimiter=',', usecols=[0, -1], converters={-1: lambda x: -1})
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(res, [[0, -1], [0, -1]])
```


## Complete Example

```python
# Workflow
txt = StringIO('1.5,2.5,3.5\n3.0,4.0,XXX\n5.5,6.0,7.5\n')
conv = {-1: lambda s: np.nan if s == 'XXX' else float(s)}
expected = np.array([[1.5, 3.5], [3.0, np.nan], [5.5, 7.5]])
res = np.loadtxt(txt, dtype=np.float64, delimiter=',', converters=conv, usecols=[0, -1])
assert_equal(res, expected)
res = np.loadtxt(StringIO('0,1,2\n0,1,2,3,4'), delimiter=',', usecols=[0, -1], converters={-1: lambda x: -1})
assert_array_equal(res, [[0, -1], [0, -1]])
```

## Next Steps


---

*Source: test_loadtxt.py:225 | Complexity: Intermediate | Last updated: 2026-06-02*