# How To: Outliers

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test outliers

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
assert_equal(h.sum(), 9)
```

### Step 2: Assign unknown = histogram(...)

```python
h, b = histogram(a, range=[0, 9])
```

**Verification:**
```python
assert_equal(h.sum(), 9)
```

### Step 3: Call assert_equal()

```python
assert_equal(h.sum(), 9)
```

**Verification:**
```python
assert_almost_equal((h * np.diff(b)).sum(), 1, decimal=15)
```

### Step 4: Assign unknown = histogram(...)

```python
h, b = histogram(a, range=[1, 10])
```

**Verification:**
```python
assert_equal((h * np.diff(b)).sum(), 1)
```

### Step 5: Call assert_equal()

```python
assert_equal(h.sum(), 9)
```

**Verification:**
```python
assert_equal(h, w[1:-1])
```

### Step 6: Assign unknown = histogram(...)

```python
h, b = histogram(a, range=[1, 9], density=True)
```

### Step 7: Call assert_almost_equal()

```python
assert_almost_equal((h * np.diff(b)).sum(), 1, decimal=15)
```

### Step 8: Assign w = value

```python
w = np.arange(10) + 0.5
```

### Step 9: Assign unknown = histogram(...)

```python
h, b = histogram(a, range=[1, 9], weights=w, density=True)
```

### Step 10: Call assert_equal()

```python
assert_equal((h * np.diff(b)).sum(), 1)
```

### Step 11: Assign unknown = histogram(...)

```python
h, b = histogram(a, bins=8, range=[1, 9], weights=w)
```

### Step 12: Call assert_equal()

```python
assert_equal(h, w[1:-1])
```


## Complete Example

```python
# Workflow
a = np.arange(10) + 0.5
h, b = histogram(a, range=[0, 9])
assert_equal(h.sum(), 9)
h, b = histogram(a, range=[1, 10])
assert_equal(h.sum(), 9)
h, b = histogram(a, range=[1, 9], density=True)
assert_almost_equal((h * np.diff(b)).sum(), 1, decimal=15)
w = np.arange(10) + 0.5
h, b = histogram(a, range=[1, 9], weights=w, density=True)
assert_equal((h * np.diff(b)).sum(), 1)
h, b = histogram(a, bins=8, range=[1, 9], weights=w)
assert_equal(h, w[1:-1])
```

## Next Steps


---

*Source: test_histograms.py:81 | Complexity: Advanced | Last updated: 2026-06-02*