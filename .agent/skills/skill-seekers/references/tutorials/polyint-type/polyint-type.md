# How To: Polyint Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test polyint type

## Prerequisites

**Required Modules:**
- `os`
- `numpy`
- `numpy.testing`
- `numpy.lib.recfunctions`
- `io`


## Step-by-Step Guide

### Step 1: Assign msg = 'Wrong type, should be complex'

```python
msg = 'Wrong type, should be complex'
```

**Verification:**
```python
assert_(np.polyint(x).dtype == complex, msg)
```

### Step 2: Assign x = np.ones(...)

```python
x = np.ones(3, dtype=complex)
```

**Verification:**
```python
assert_(np.polyint(x).dtype == float, msg)
```

### Step 3: Call assert_()

```python
assert_(np.polyint(x).dtype == complex, msg)
```

### Step 4: Assign msg = 'Wrong type, should be float'

```python
msg = 'Wrong type, should be float'
```

### Step 5: Assign x = np.ones(...)

```python
x = np.ones(3, dtype=int)
```

### Step 6: Call assert_()

```python
assert_(np.polyint(x).dtype == float, msg)
```


## Complete Example

```python
# Workflow
msg = 'Wrong type, should be complex'
x = np.ones(3, dtype=complex)
assert_(np.polyint(x).dtype == complex, msg)
msg = 'Wrong type, should be float'
x = np.ones(3, dtype=int)
assert_(np.polyint(x).dtype == float, msg)
```

## Next Steps


---

*Source: test_regression.py:121 | Complexity: Intermediate | Last updated: 2026-06-02*