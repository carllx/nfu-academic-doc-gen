# How To: Directed Modularity

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Directed Modularity matrix

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Directed Modularity matrix'

```python
'Directed Modularity matrix'
```

### Step 2: Assign B = np.array(...)

```python
B = np.array([[-0.2, 0.6, 0.8, -0.4, -0.4, -0.4], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.7, 0.4, -0.3, -0.6, 0.4, -0.6], [-0.2, -0.4, -0.2, -0.4, 0.6, 0.6], [-0.2, -0.4, -0.2, 0.6, -0.4, 0.6], [-0.1, -0.2, -0.1, 0.8, -0.2, -0.2]])
```

### Step 3: Assign node_permutation = value

```python
node_permutation = [5, 1, 2, 3, 4, 6]
```

### Step 4: Assign idx_permutation = value

```python
idx_permutation = [4, 0, 1, 2, 3, 5]
```

### Step 5: Assign mm = nx.directed_modularity_matrix(...)

```python
mm = nx.directed_modularity_matrix(self.DG, nodelist=sorted(self.DG))
```

### Step 6: Call np.testing.assert_equal()

```python
np.testing.assert_equal(mm, B)
```

### Step 7: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.directed_modularity_matrix(self.DG, nodelist=node_permutation), B[np.ix_(idx_permutation, idx_permutation)])
```


## Complete Example

```python
# Workflow
'Directed Modularity matrix'
B = np.array([[-0.2, 0.6, 0.8, -0.4, -0.4, -0.4], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.7, 0.4, -0.3, -0.6, 0.4, -0.6], [-0.2, -0.4, -0.2, -0.4, 0.6, 0.6], [-0.2, -0.4, -0.2, 0.6, -0.4, 0.6], [-0.1, -0.2, -0.1, 0.8, -0.2, -0.2]])
node_permutation = [5, 1, 2, 3, 4, 6]
idx_permutation = [4, 0, 1, 2, 3, 5]
mm = nx.directed_modularity_matrix(self.DG, nodelist=sorted(self.DG))
np.testing.assert_equal(mm, B)
np.testing.assert_equal(nx.directed_modularity_matrix(self.DG, nodelist=node_permutation), B[np.ix_(idx_permutation, idx_permutation)])
```

## Next Steps


---

*Source: test_modularity.py:69 | Complexity: Intermediate | Last updated: 2026-06-02*