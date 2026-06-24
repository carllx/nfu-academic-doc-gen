# How To: Recarrays

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test record arrays.

## Prerequisites

**Required Modules:**
- `itertools`
- `os`
- `re`
- `sys`
- `warnings`
- `weakref`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `datetime`


## Step-by-Step Guide

### Step 1: 'Test record arrays.'

```python
'Test record arrays.'
```

### Step 2: Assign a = np.empty(...)

```python
a = np.empty(2, [('floupi', float), ('floupa', float)])
```

### Step 3: Assign unknown = value

```python
a['floupi'] = [1, 2]
```

### Step 4: Assign unknown = value

```python
a['floupa'] = [1, 2]
```

### Step 5: Assign b = a.copy(...)

```python
b = a.copy()
```

### Step 6: Call self._test_equal()

```python
self._test_equal(a, b)
```

### Step 7: Assign c = np.empty(...)

```python
c = np.empty(2, [('floupipi', float), ('floupi', float), ('floupa', float)])
```

### Step 8: Assign unknown = unknown.copy(...)

```python
c['floupipi'] = a['floupi'].copy()
```

### Step 9: Assign unknown = unknown.copy(...)

```python
c['floupa'] = a['floupa'].copy()
```

### Step 10: Call self._test_not_equal()

```python
self._test_not_equal(c, b)
```


## Complete Example

```python
# Workflow
'Test record arrays.'
a = np.empty(2, [('floupi', float), ('floupa', float)])
a['floupi'] = [1, 2]
a['floupa'] = [1, 2]
b = a.copy()
self._test_equal(a, b)
c = np.empty(2, [('floupipi', float), ('floupi', float), ('floupa', float)])
c['floupipi'] = a['floupi'].copy()
c['floupa'] = a['floupa'].copy()
with pytest.raises(TypeError):
    self._test_not_equal(c, b)
```

## Next Steps


---

*Source: test_utils.py:175 | Complexity: Advanced | Last updated: 2026-06-02*