# How To: Replace Broadcasting

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace broadcasting

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core.multiarray`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array.view(...)

```python
a = np.array('0,0,0').view(np.char.chararray)
```

**Verification:**
```python
assert r1.dtype == a.dtype
```

### Step 2: Assign r1 = a.replace(...)

```python
r1 = a.replace('0', '1', count=np.arange(3))
```

**Verification:**
```python
assert_array_equal(r1, np.array(['0,0,0', '1,0,0', '1,1,0']))
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(r1, np.array(['0,0,0', '1,0,0', '1,1,0']))
```

**Verification:**
```python
assert_array_equal(r2, np.array([['1,0,0', '1,1,0', '1,1,1'], ['2,0,0', '2,2,0', '2,2,2']]))
```

### Step 4: Assign r2 = a.replace(...)

```python
r2 = a.replace('0', [['1'], ['2']], count=np.arange(1, 4))
```

**Verification:**
```python
assert_array_equal(r3, np.array(['X,X,X', 'X,0', 'X']))
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(r2, np.array([['1,0,0', '1,1,0', '1,1,1'], ['2,0,0', '2,2,0', '2,2,2']]))
```

### Step 6: Assign r3 = a.replace(...)

```python
r3 = a.replace(['0', '0,0', '0,0,0'], 'X')
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(r3, np.array(['X,X,X', 'X,0', 'X']))
```


## Complete Example

```python
# Workflow
a = np.array('0,0,0').view(np.char.chararray)
r1 = a.replace('0', '1', count=np.arange(3))
assert r1.dtype == a.dtype
assert_array_equal(r1, np.array(['0,0,0', '1,0,0', '1,1,0']))
r2 = a.replace('0', [['1'], ['2']], count=np.arange(1, 4))
assert_array_equal(r2, np.array([['1,0,0', '1,1,0', '1,1,1'], ['2,0,0', '2,2,0', '2,2,2']]))
r3 = a.replace(['0', '0,0', '0,0,0'], 'X')
assert_array_equal(r3, np.array(['X,X,X', 'X,0', 'X']))
```

## Next Steps


---

*Source: test_defchararray.py:523 | Complexity: Intermediate | Last updated: 2026-06-02*