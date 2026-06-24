# How To: Polynomial Mapdomain

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test polynomial mapdomain

## Prerequisites

**Required Modules:**
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dom1 = value

```python
dom1 = [0, 4]
```

**Verification:**
```python
assert_(isinstance(res, np.matrix))
```

### Step 2: Assign dom2 = value

```python
dom2 = [1, 3]
```

### Step 3: Assign x = np.matrix(...)

```python
x = np.matrix([dom1, dom1])
```

### Step 4: Assign res = np.polynomial.polyutils.mapdomain(...)

```python
res = np.polynomial.polyutils.mapdomain(x, dom1, dom2)
```

### Step 5: Call assert_()

```python
assert_(isinstance(res, np.matrix))
```


## Complete Example

```python
# Workflow
dom1 = [0, 4]
dom2 = [1, 3]
x = np.matrix([dom1, dom1])
res = np.polynomial.polyutils.mapdomain(x, dom1, dom2)
assert_(isinstance(res, np.matrix))
```

## Next Steps


---

*Source: test_interaction.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*