# How To: Type

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test type

## Prerequisites

**Required Modules:**
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: Assign a = value

```python
a = np.arange(10) + 0.5
```

**Verification:**
```python
assert_(np.issubdtype(h.dtype, np.integer))
```

### Step 2: Assign unknown = histogram(...)

```python
h, b = histogram(a)
```

**Verification:**
```python
assert_(np.issubdtype(h.dtype, np.floating))
```

### Step 3: Call assert_()

```python
assert_(np.issubdtype(h.dtype, np.integer))
```

**Verification:**
```python
assert_(np.issubdtype(h.dtype, np.integer))
```

### Step 4: Assign unknown = histogram(...)

```python
h, b = histogram(a, density=True)
```

**Verification:**
```python
assert_(np.issubdtype(h.dtype, np.floating))
```

### Step 5: Call assert_()

```python
assert_(np.issubdtype(h.dtype, np.floating))
```

### Step 6: Assign unknown = histogram(...)

```python
h, b = histogram(a, weights=np.ones(10, int))
```

### Step 7: Call assert_()

```python
assert_(np.issubdtype(h.dtype, np.integer))
```

### Step 8: Assign unknown = histogram(...)

```python
h, b = histogram(a, weights=np.ones(10, float))
```

### Step 9: Call assert_()

```python
assert_(np.issubdtype(h.dtype, np.floating))
```


## Complete Example

```python
# Workflow
a = np.arange(10) + 0.5
h, b = histogram(a)
assert_(np.issubdtype(h.dtype, np.integer))
h, b = histogram(a, density=True)
assert_(np.issubdtype(h.dtype, np.floating))
h, b = histogram(a, weights=np.ones(10, int))
assert_(np.issubdtype(h.dtype, np.integer))
h, b = histogram(a, weights=np.ones(10, float))
assert_(np.issubdtype(h.dtype, np.floating))
```

## Next Steps


---

*Source: test_histograms.py:111 | Complexity: Advanced | Last updated: 2026-06-02*