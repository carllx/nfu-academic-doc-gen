# How To:  Dict To Numpy Array1

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test  dict to numpy array1

## Prerequisites

**Required Modules:**
- `random`
- `copy`
- `pytest`
- `networkx`
- `networkx.utils`
- `networkx.utils.misc`


## Step-by-Step Guide

### Step 1: Assign d = value

```python
d = {'a': 1, 'b': 2}
```

### Step 2: Assign a = _dict_to_numpy_array1(...)

```python
a = _dict_to_numpy_array1(d, mapping={'a': 0, 'b': 1})
```

### Step 3: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a, np.array([1, 2]))
```

### Step 4: Assign a = _dict_to_numpy_array1(...)

```python
a = _dict_to_numpy_array1(d, mapping={'b': 0, 'a': 1})
```

### Step 5: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a, np.array([2, 1]))
```

### Step 6: Assign a = _dict_to_numpy_array1(...)

```python
a = _dict_to_numpy_array1(d)
```

### Step 7: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a.sum(), 3)
```


## Complete Example

```python
# Workflow
d = {'a': 1, 'b': 2}
a = _dict_to_numpy_array1(d, mapping={'a': 0, 'b': 1})
np.testing.assert_allclose(a, np.array([1, 2]))
a = _dict_to_numpy_array1(d, mapping={'b': 0, 'a': 1})
np.testing.assert_allclose(a, np.array([2, 1]))
a = _dict_to_numpy_array1(d)
np.testing.assert_allclose(a.sum(), 3)
```

## Next Steps


---

*Source: test_misc.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*