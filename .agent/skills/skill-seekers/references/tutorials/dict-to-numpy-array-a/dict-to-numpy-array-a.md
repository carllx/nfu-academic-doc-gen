# How To: Dict To Numpy Array A

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dict to numpy array a

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
mapping = {'a': 0, 'b': 1}
```

### Step 3: Assign a = dict_to_numpy_array(...)

```python
a = dict_to_numpy_array(d, mapping=mapping)
```

### Step 4: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a, np.array([[1, 2], [10, 20]]))
```

### Step 5: Assign mapping = value

```python
mapping = {'a': 1, 'b': 0}
```

### Step 6: Assign a = dict_to_numpy_array(...)

```python
a = dict_to_numpy_array(d, mapping=mapping)
```

### Step 7: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a, np.array([[20, 10], [2, 1]]))
```

### Step 8: Assign a = _dict_to_numpy_array2(...)

```python
a = _dict_to_numpy_array2(d)
```

### Step 9: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a.sum(), 33)
```


## Complete Example

```python
# Workflow
d = {'a': {'a': 1, 'b': 2}, 'b': {'a': 10, 'b': 20}}
mapping = {'a': 0, 'b': 1}
a = dict_to_numpy_array(d, mapping=mapping)
np.testing.assert_allclose(a, np.array([[1, 2], [10, 20]]))
mapping = {'a': 1, 'b': 0}
a = dict_to_numpy_array(d, mapping=mapping)
np.testing.assert_allclose(a, np.array([[20, 10], [2, 1]]))
a = _dict_to_numpy_array2(d)
np.testing.assert_allclose(a.sum(), 33)
```

## Next Steps


---

*Source: test_misc.py:114 | Complexity: Advanced | Last updated: 2026-06-02*