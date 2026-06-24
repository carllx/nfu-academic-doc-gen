# How To:  Dict To Numpy Array2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test  dict to numpy array2

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
d = {'a': {'a': 1, 'b': 2}, 'b': {'a': 10, 'b': 20}}
```

### Step 2: Assign mapping = value

```python
mapping = {'a': 1, 'b': 0}
```

### Step 3: Assign a = _dict_to_numpy_array2(...)

```python
a = _dict_to_numpy_array2(d, mapping=mapping)
```

### Step 4: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a, np.array([[20, 10], [2, 1]]))
```

### Step 5: Assign a = _dict_to_numpy_array2(...)

```python
a = _dict_to_numpy_array2(d)
```

### Step 6: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a.sum(), 33)
```


## Complete Example

```python
# Workflow
d = {'a': {'a': 1, 'b': 2}, 'b': {'a': 10, 'b': 20}}
mapping = {'a': 1, 'b': 0}
a = _dict_to_numpy_array2(d, mapping=mapping)
np.testing.assert_allclose(a, np.array([[20, 10], [2, 1]]))
a = _dict_to_numpy_array2(d)
np.testing.assert_allclose(a.sum(), 33)
```

## Next Steps


---

*Source: test_misc.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*