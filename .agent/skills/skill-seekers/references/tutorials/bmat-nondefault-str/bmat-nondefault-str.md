# How To: Bmat Nondefault Str

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bmat nondefault str

## Prerequisites

**Required Modules:**
- `collections.abc`
- `numpy`
- `numpy`
- `numpy.linalg`
- `numpy.testing`
- `numpy.linalg`
- `numpy.linalg`


## Step-by-Step Guide

### Step 1: Assign A = np.array(...)

```python
A = np.array([[1, 2], [3, 4]])
```

**Verification:**
```python
assert_(np.all(bmat('A,A;A,A') == Aresult))
```

### Step 2: Assign B = np.array(...)

```python
B = np.array([[5, 6], [7, 8]])
```

**Verification:**
```python
assert_(np.all(bmat('A,A;A,A', ldict={'A': B}) == Aresult))
```

### Step 3: Assign Aresult = np.array(...)

```python
Aresult = np.array([[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]])
```

**Verification:**
```python
assert_raises(TypeError, bmat, 'A,A;A,A', gdict={'A': B})
```

### Step 4: Assign mixresult = np.array(...)

```python
mixresult = np.array([[1, 2, 5, 6], [3, 4, 7, 8], [5, 6, 1, 2], [7, 8, 3, 4]])
```

**Verification:**
```python
assert_(np.all(bmat('A,A;A,A', ldict={'A': A}, gdict={'A': B}) == Aresult))
```

### Step 5: Call assert_()

```python
assert_(np.all(bmat('A,A;A,A') == Aresult))
```

**Verification:**
```python
assert_(np.all(b2 == mixresult))
```

### Step 6: Call assert_()

```python
assert_(np.all(bmat('A,A;A,A', ldict={'A': B}) == Aresult))
```

### Step 7: Call assert_raises()

```python
assert_raises(TypeError, bmat, 'A,A;A,A', gdict={'A': B})
```

### Step 8: Call assert_()

```python
assert_(np.all(bmat('A,A;A,A', ldict={'A': A}, gdict={'A': B}) == Aresult))
```

### Step 9: Assign b2 = bmat(...)

```python
b2 = bmat('A,B;C,D', ldict={'A': A, 'B': B}, gdict={'C': B, 'D': A})
```

### Step 10: Call assert_()

```python
assert_(np.all(b2 == mixresult))
```


## Complete Example

```python
# Workflow
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
Aresult = np.array([[1, 2, 1, 2], [3, 4, 3, 4], [1, 2, 1, 2], [3, 4, 3, 4]])
mixresult = np.array([[1, 2, 5, 6], [3, 4, 7, 8], [5, 6, 1, 2], [7, 8, 3, 4]])
assert_(np.all(bmat('A,A;A,A') == Aresult))
assert_(np.all(bmat('A,A;A,A', ldict={'A': B}) == Aresult))
assert_raises(TypeError, bmat, 'A,A;A,A', gdict={'A': B})
assert_(np.all(bmat('A,A;A,A', ldict={'A': A}, gdict={'A': B}) == Aresult))
b2 = bmat('A,B;C,D', ldict={'A': A, 'B': B}, gdict={'C': B, 'D': A})
assert_(np.all(b2 == mixresult))
```

## Next Steps


---

*Source: test_defmatrix.py:43 | Complexity: Advanced | Last updated: 2026-06-02*