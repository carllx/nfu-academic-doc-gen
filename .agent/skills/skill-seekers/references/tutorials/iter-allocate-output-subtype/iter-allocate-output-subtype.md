# How To: Iter Allocate Output Subtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iter allocate output subtype

## Prerequisites

**Required Modules:**
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.matrix(...)

```python
a = np.matrix([[1, 2], [3, 4]])
```

**Verification:**
```python
assert_(type(i.operands[2]) is np.matrix)
```

### Step 2: Assign b = value

```python
b = np.arange(4).reshape(2, 2).T
```

**Verification:**
```python
assert_(type(i.operands[2]) is not np.ndarray)
```

### Step 3: Assign i = np.nditer(...)

```python
i = np.nditer([a, b, None], [], [['readonly'], ['readonly'], ['writeonly', 'allocate']])
```

**Verification:**
```python
assert_equal(i.operands[2].shape, (2, 2))
```

### Step 4: Call assert_()

```python
assert_(type(i.operands[2]) is np.matrix)
```

**Verification:**
```python
assert_raises(RuntimeError, np.nditer, [a, b, None], [], [['readonly'], ['readonly'], ['writeonly', 'allocate']])
```

### Step 5: Call assert_()

```python
assert_(type(i.operands[2]) is not np.ndarray)
```

**Verification:**
```python
assert_(type(i.operands[2]) is np.ndarray)
```

### Step 6: Call assert_equal()

```python
assert_equal(i.operands[2].shape, (2, 2))
```

**Verification:**
```python
assert_(type(i.operands[2]) is not np.matrix)
```

### Step 7: Assign b = np.arange.reshape(...)

```python
b = np.arange(4).reshape(1, 2, 2)
```

**Verification:**
```python
assert_equal(i.operands[2].shape, (1, 2, 2))
```

### Step 8: Call assert_raises()

```python
assert_raises(RuntimeError, np.nditer, [a, b, None], [], [['readonly'], ['readonly'], ['writeonly', 'allocate']])
```

### Step 9: Assign i = np.nditer(...)

```python
i = np.nditer([a, b, None], [], [['readonly'], ['readonly'], ['writeonly', 'allocate', 'no_subtype']])
```

### Step 10: Call assert_()

```python
assert_(type(i.operands[2]) is np.ndarray)
```

### Step 11: Call assert_()

```python
assert_(type(i.operands[2]) is not np.matrix)
```

### Step 12: Call assert_equal()

```python
assert_equal(i.operands[2].shape, (1, 2, 2))
```


## Complete Example

```python
# Workflow
a = np.matrix([[1, 2], [3, 4]])
b = np.arange(4).reshape(2, 2).T
i = np.nditer([a, b, None], [], [['readonly'], ['readonly'], ['writeonly', 'allocate']])
assert_(type(i.operands[2]) is np.matrix)
assert_(type(i.operands[2]) is not np.ndarray)
assert_equal(i.operands[2].shape, (2, 2))
b = np.arange(4).reshape(1, 2, 2)
assert_raises(RuntimeError, np.nditer, [a, b, None], [], [['readonly'], ['readonly'], ['writeonly', 'allocate']])
i = np.nditer([a, b, None], [], [['readonly'], ['readonly'], ['writeonly', 'allocate', 'no_subtype']])
assert_(type(i.operands[2]) is np.ndarray)
assert_(type(i.operands[2]) is not np.matrix)
assert_equal(i.operands[2].shape, (1, 2, 2))
```

## Next Steps


---

*Source: test_interaction.py:94 | Complexity: Advanced | Last updated: 2026-06-02*