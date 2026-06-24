# How To: Setitem Preserves Views

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem preserves views

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = NumpyExtensionArray(...)

```python
arr = NumpyExtensionArray(np.array([1, 2, 3]))
```

**Verification:**
```python
assert view1[0] == 9
```

### Step 2: Assign view1 = arr.view(...)

```python
view1 = arr.view()
```

**Verification:**
```python
assert view2[0] == 9
```

### Step 3: Assign view2 = value

```python
view2 = arr[:]
```

**Verification:**
```python
assert view3[0] == 9
```

### Step 4: Assign view3 = np.asarray(...)

```python
view3 = np.asarray(arr)
```

**Verification:**
```python
assert arr[-1] == 5
```

### Step 5: Assign unknown = 9

```python
arr[0] = 9
```

**Verification:**
```python
assert view1[0] == 9
```

### Step 6: Assign unknown = 2.5

```python
arr[-1] = 2.5
```

### Step 7: Assign unknown = 5

```python
view1[-1] = 5
```

**Verification:**
```python
assert arr[-1] == 5
```


## Complete Example

```python
# Workflow
arr = NumpyExtensionArray(np.array([1, 2, 3]))
view1 = arr.view()
view2 = arr[:]
view3 = np.asarray(arr)
arr[0] = 9
assert view1[0] == 9
assert view2[0] == 9
assert view3[0] == 9
arr[-1] = 2.5
view1[-1] = 5
assert arr[-1] == 5
```

## Next Steps


---

*Source: test_numpy.py:286 | Complexity: Intermediate | Last updated: 2026-06-02*