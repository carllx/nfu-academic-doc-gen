# How To: Dict To Numpy Array B

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dict to numpy array b

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
np.testing.assert_allclose(a, np.array([1, 2]))
```

### Step 5: Assign a = _dict_to_numpy_array1(...)

```python
a = _dict_to_numpy_array1(d)
```

### Step 6: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(a.sum(), 3)
```


## Complete Example

```python
# Workflow
d = {'a': 1, 'b': 2}
mapping = {'a': 0, 'b': 1}
a = dict_to_numpy_array(d, mapping=mapping)
np.testing.assert_allclose(a, np.array([1, 2]))
a = _dict_to_numpy_array1(d)
np.testing.assert_allclose(a.sum(), 3)
```

## Next Steps


---

*Source: test_misc.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*