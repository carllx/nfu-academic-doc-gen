# How To: Choice Retun Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test choice retun dtype

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `gc`
- `gc`


## Step-by-Step Guide

### Step 1: Assign c = np.random.choice(...)

```python
c = np.random.choice(10, p=[0.1] * 10, size=2)
```

**Verification:**
```python
assert c.dtype == np.dtype(np.long)
```

### Step 2: Assign c = np.random.choice(...)

```python
c = np.random.choice(10, p=[0.1] * 10, replace=False, size=2)
```

**Verification:**
```python
assert c.dtype == np.dtype(np.long)
```

### Step 3: Assign c = np.random.choice(...)

```python
c = np.random.choice(10, size=2)
```

**Verification:**
```python
assert c.dtype == np.dtype(np.long)
```

### Step 4: Assign c = np.random.choice(...)

```python
c = np.random.choice(10, replace=False, size=2)
```

**Verification:**
```python
assert c.dtype == np.dtype(np.long)
```


## Complete Example

```python
# Workflow
c = np.random.choice(10, p=[0.1] * 10, size=2)
assert c.dtype == np.dtype(np.long)
c = np.random.choice(10, p=[0.1] * 10, replace=False, size=2)
assert c.dtype == np.dtype(np.long)
c = np.random.choice(10, size=2)
assert c.dtype == np.dtype(np.long)
c = np.random.choice(10, replace=False, size=2)
assert c.dtype == np.dtype(np.long)
```

## Next Steps


---

*Source: test_randomstate_regression.py:164 | Complexity: Intermediate | Last updated: 2026-06-02*