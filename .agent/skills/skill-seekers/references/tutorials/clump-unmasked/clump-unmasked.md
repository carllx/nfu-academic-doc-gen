# How To: Clump Unmasked

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test clump unmasked

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.ma.core`
- `numpy.ma.extras`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign a = masked_array(...)

```python
a = masked_array(np.arange(10))
```

**Verification:**
```python
assert_equal(test, control)
```

### Step 2: Assign unknown = masked

```python
a[[0, 1, 2, 6, 8, 9]] = masked
```

### Step 3: Assign test = clump_unmasked(...)

```python
test = clump_unmasked(a)
```

### Step 4: Assign control = value

```python
control = [slice(3, 6), slice(7, 8)]
```

### Step 5: Call assert_equal()

```python
assert_equal(test, control)
```

### Step 6: Call self.check_clump()

```python
self.check_clump(clump_unmasked)
```


## Complete Example

```python
# Workflow
a = masked_array(np.arange(10))
a[[0, 1, 2, 6, 8, 9]] = masked
test = clump_unmasked(a)
control = [slice(3, 6), slice(7, 8)]
assert_equal(test, control)
self.check_clump(clump_unmasked)
```

## Next Steps


---

*Source: test_extras.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*