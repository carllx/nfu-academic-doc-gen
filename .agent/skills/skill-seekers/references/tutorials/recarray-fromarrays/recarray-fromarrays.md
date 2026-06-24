# How To: Recarray Fromarrays

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test recarray fromarrays

## Prerequisites

**Required Modules:**
- `collections.abc`
- `pickle`
- `textwrap`
- `io`
- `os`
- `pathlib`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x1 = np.array(...)

```python
x1 = np.array([1, 2, 3, 4])
```

**Verification:**
```python
assert_equal(r[1].item(), (2, 'dd', 2.0))
```

### Step 2: Assign x2 = np.array(...)

```python
x2 = np.array(['a', 'dd', 'xyz', '12'])
```

**Verification:**
```python
assert_equal(r.a, np.array([1, 2, 3, 4]))
```

### Step 3: Assign x3 = np.array(...)

```python
x3 = np.array([1.1, 2, 3, 4])
```

### Step 4: Assign r = np.rec.fromarrays(...)

```python
r = np.rec.fromarrays([x1, x2, x3], names='a,b,c')
```

### Step 5: Call assert_equal()

```python
assert_equal(r[1].item(), (2, 'dd', 2.0))
```

### Step 6: Assign unknown = 34

```python
x1[1] = 34
```

### Step 7: Call assert_equal()

```python
assert_equal(r.a, np.array([1, 2, 3, 4]))
```


## Complete Example

```python
# Workflow
x1 = np.array([1, 2, 3, 4])
x2 = np.array(['a', 'dd', 'xyz', '12'])
x3 = np.array([1.1, 2, 3, 4])
r = np.rec.fromarrays([x1, x2, x3], names='a,b,c')
assert_equal(r[1].item(), (2, 'dd', 2.0))
x1[1] = 34
assert_equal(r.a, np.array([1, 2, 3, 4]))
```

## Next Steps


---

*Source: test_records.py:83 | Complexity: Intermediate | Last updated: 2026-06-02*