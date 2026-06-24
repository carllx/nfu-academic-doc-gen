# How To: Order

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test order

## Prerequisites

**Required Modules:**
- `decimal`
- `math`
- `operator`
- `sys`
- `warnings`
- `fractions`
- `functools`
- `hypothesis`
- `hypothesis.strategies`
- `pytest`
- `hypothesis.extra.numpy`
- `numpy`
- `numpy.lib._function_base_impl`
- `numpy`
- `numpy._core.numeric`
- `numpy.exceptions`
- `numpy.random`
- `numpy.testing`
- `random`
- `gc`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([[1, 2], [3, 4]])
```

**Verification:**
```python
assert_(a.flags.c_contiguous)
```

### Step 2: Call assert_()

```python
assert_(a.flags.c_contiguous)
```

**Verification:**
```python
assert_(not a.flags.f_contiguous)
```

### Step 3: Call assert_()

```python
assert_(not a.flags.f_contiguous)
```

**Verification:**
```python
assert_(not a_fort.flags.c_contiguous)
```

### Step 4: Assign a_fort = np.array(...)

```python
a_fort = np.array([[1, 2], [3, 4]], order='F')
```

**Verification:**
```python
assert_(a_fort.flags.f_contiguous)
```

### Step 5: Call assert_()

```python
assert_(not a_fort.flags.c_contiguous)
```

**Verification:**
```python
assert_(a_copy.flags.c_contiguous)
```

### Step 6: Call assert_()

```python
assert_(a_fort.flags.f_contiguous)
```

**Verification:**
```python
assert_(not a_copy.flags.f_contiguous)
```

### Step 7: Assign a_copy = np.copy(...)

```python
a_copy = np.copy(a)
```

**Verification:**
```python
assert_(not a_fort_copy.flags.c_contiguous)
```

### Step 8: Call assert_()

```python
assert_(a_copy.flags.c_contiguous)
```

**Verification:**
```python
assert_(a_fort_copy.flags.f_contiguous)
```

### Step 9: Call assert_()

```python
assert_(not a_copy.flags.f_contiguous)
```

### Step 10: Assign a_fort_copy = np.copy(...)

```python
a_fort_copy = np.copy(a_fort)
```

### Step 11: Call assert_()

```python
assert_(not a_fort_copy.flags.c_contiguous)
```

### Step 12: Call assert_()

```python
assert_(a_fort_copy.flags.f_contiguous)
```


## Complete Example

```python
# Workflow
a = np.array([[1, 2], [3, 4]])
assert_(a.flags.c_contiguous)
assert_(not a.flags.f_contiguous)
a_fort = np.array([[1, 2], [3, 4]], order='F')
assert_(not a_fort.flags.c_contiguous)
assert_(a_fort.flags.f_contiguous)
a_copy = np.copy(a)
assert_(a_copy.flags.c_contiguous)
assert_(not a_copy.flags.f_contiguous)
a_fort_copy = np.copy(a_fort)
assert_(not a_fort_copy.flags.c_contiguous)
assert_(a_fort_copy.flags.f_contiguous)
```

## Next Steps


---

*Source: test_function_base.py:308 | Complexity: Advanced | Last updated: 2026-06-02*