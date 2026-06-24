# How To: Attribute Mixing Matrix Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attribute mixing matrix float

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `base_test`


## Step-by-Step Guide

### Step 1: Assign mapping = value

```python
mapping = {0.5: 1, 1.5: 0}
```

### Step 2: Assign a_result = np.array(...)

```python
a_result = np.array([[6.0, 1.0], [1.0, 0.0]])
```

### Step 3: Assign a = nx.attribute_mixing_matrix(...)

```python
a = nx.attribute_mixing_matrix(self.F, 'margin', mapping=mapping, normalized=False)
```

### Step 4: Call np.testing.assert_equal()

```python
np.testing.assert_equal(a, a_result)
```

### Step 5: Assign a = nx.attribute_mixing_matrix(...)

```python
a = nx.attribute_mixing_matrix(self.F, 'margin', mapping=mapping)
```

### Step 6: Call np.testing.assert_equal()

```python
np.testing.assert_equal(a, a_result / a_result.sum())
```


## Complete Example

```python
# Workflow
mapping = {0.5: 1, 1.5: 0}
a_result = np.array([[6.0, 1.0], [1.0, 0.0]])
a = nx.attribute_mixing_matrix(self.F, 'margin', mapping=mapping, normalized=False)
np.testing.assert_equal(a, a_result)
a = nx.attribute_mixing_matrix(self.F, 'margin', mapping=mapping)
np.testing.assert_equal(a, a_result / a_result.sum())
```

## Next Steps


---

*Source: test_mixing.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*