# How To: Comparision Different Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comparision different types

## Prerequisites

**Required Modules:**
- `contextlib`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `hypothesis.strategies`
- `numpy`
- `numpy._core._rational_tests`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array(1)
```

**Verification:**
```python
assert eq is np.bool_(False)
```

### Step 2: Assign y = np.array(...)

```python
y = np.array('s')
```

**Verification:**
```python
assert neq is np.bool_(True)
```

### Step 3: Assign eq = value

```python
eq = x == y
```

### Step 4: Assign neq = value

```python
neq = x != y
```

**Verification:**
```python
assert eq is np.bool_(False)
```


## Complete Example

```python
# Workflow
x = np.array(1)
y = np.array('s')
eq = x == y
neq = x != y
assert eq is np.bool_(False)
assert neq is np.bool_(True)
```

## Next Steps


---

*Source: test_scalarmath.py:401 | Complexity: Intermediate | Last updated: 2026-06-02*