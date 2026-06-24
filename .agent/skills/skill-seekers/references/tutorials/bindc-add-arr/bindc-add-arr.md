# How To: Bindc Add Arr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bindc add arr

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.testing`
- `numpy.f2py.auxfuncs`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3])
```

**Verification:**
```python
assert_allclose(out, exp_out)
```

### Step 2: Assign b = np.array(...)

```python
b = np.array([1, 2, 3])
```

### Step 3: Assign out = self.module.coddity.add_arr(...)

```python
out = self.module.coddity.add_arr(a, b)
```

### Step 4: Assign exp_out = value

```python
exp_out = a * 2
```

### Step 5: Call assert_allclose()

```python
assert_allclose(out, exp_out)
```


## Complete Example

```python
# Workflow
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
out = self.module.coddity.add_arr(a, b)
exp_out = a * 2
assert_allclose(out, exp_out)
```

## Next Steps


---

*Source: test_isoc.py:34 | Complexity: Intermediate | Last updated: 2026-06-02*