# How To: Attribute Mixing Matrix Directed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attribute mixing matrix directed

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `base_test`


## Step-by-Step Guide

### Step 1: Assign mapping = value

```python
mapping = {'one': 0, 'two': 1, 'red': 2, 'blue': 3}
```

### Step 2: Assign a_result = np.array(...)

```python
a_result = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
```

### Step 3: Assign a = nx.attribute_mixing_matrix(...)

```python
a = nx.attribute_mixing_matrix(self.D, 'fish', mapping=mapping, normalized=False)
```

### Step 4: Call np.testing.assert_equal()

```python
np.testing.assert_equal(a, a_result)
```

### Step 5: Assign a = nx.attribute_mixing_matrix(...)

```python
a = nx.attribute_mixing_matrix(self.D, 'fish', mapping=mapping)
```

### Step 6: Call np.testing.assert_equal()

```python
np.testing.assert_equal(a, a_result / a_result.sum())
```


## Complete Example

```python
# Workflow
mapping = {'one': 0, 'two': 1, 'red': 2, 'blue': 3}
a_result = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
a = nx.attribute_mixing_matrix(self.D, 'fish', mapping=mapping, normalized=False)
np.testing.assert_equal(a, a_result)
a = nx.attribute_mixing_matrix(self.D, 'fish', mapping=mapping)
np.testing.assert_equal(a, a_result / a_result.sum())
```

## Next Steps


---

*Source: test_mixing.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*