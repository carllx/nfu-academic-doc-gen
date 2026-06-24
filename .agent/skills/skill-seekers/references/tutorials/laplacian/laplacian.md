# How To: Laplacian

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Graph Laplacian

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Graph Laplacian'

```python
'Graph Laplacian'
```

### Step 2: Assign NL = np.array(...)

```python
NL = np.array([[3, -1, -1, -1, 0], [-1, 2, -1, 0, 0], [-1, -1, 2, 0, 0], [-1, 0, 0, 1, 0], [0, 0, 0, 0, 0]])
```

### Step 3: Assign WL = value

```python
WL = 0.5 * NL
```

### Step 4: Assign OL = value

```python
OL = 0.3 * NL
```

### Step 5: Assign DiNL = np.array(...)

```python
DiNL = np.array([[2, -1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [-1, -1, 3, -1, 0, 0], [0, 0, 0, 2, -1, -1], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 1]])
```

### Step 6: Assign DiWL = value

```python
DiWL = 0.5 * DiNL
```

### Step 7: Assign DiOL = value

```python
DiOL = 0.3 * DiNL
```

### Step 8: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.G).todense(), NL)
```

### Step 9: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.MG).todense(), NL)
```

### Step 10: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.G, nodelist=[0, 1]).todense(), np.array([[1, -1], [-1, 1]]))
```

### Step 11: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.WG).todense(), WL)
```

### Step 12: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.WG, weight=None).todense(), NL)
```

### Step 13: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.WG, weight='other').todense(), OL)
```

### Step 14: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.DiG).todense(), DiNL)
```

### Step 15: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.DiMG).todense(), DiNL)
```

### Step 16: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.DiG, nodelist=[1, 2]).todense(), np.array([[1, -1], [0, 0]]))
```

### Step 17: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.DiWG).todense(), DiWL)
```

### Step 18: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.DiWG, weight=None).todense(), DiNL)
```

### Step 19: Call np.testing.assert_equal()

```python
np.testing.assert_equal(nx.laplacian_matrix(self.DiWG, weight='other').todense(), DiOL)
```


## Complete Example

```python
# Workflow
'Graph Laplacian'
NL = np.array([[3, -1, -1, -1, 0], [-1, 2, -1, 0, 0], [-1, -1, 2, 0, 0], [-1, 0, 0, 1, 0], [0, 0, 0, 0, 0]])
WL = 0.5 * NL
OL = 0.3 * NL
DiNL = np.array([[2, -1, -1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [-1, -1, 3, -1, 0, 0], [0, 0, 0, 2, -1, -1], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 1]])
DiWL = 0.5 * DiNL
DiOL = 0.3 * DiNL
np.testing.assert_equal(nx.laplacian_matrix(self.G).todense(), NL)
np.testing.assert_equal(nx.laplacian_matrix(self.MG).todense(), NL)
np.testing.assert_equal(nx.laplacian_matrix(self.G, nodelist=[0, 1]).todense(), np.array([[1, -1], [-1, 1]]))
np.testing.assert_equal(nx.laplacian_matrix(self.WG).todense(), WL)
np.testing.assert_equal(nx.laplacian_matrix(self.WG, weight=None).todense(), NL)
np.testing.assert_equal(nx.laplacian_matrix(self.WG, weight='other').todense(), OL)
np.testing.assert_equal(nx.laplacian_matrix(self.DiG).todense(), DiNL)
np.testing.assert_equal(nx.laplacian_matrix(self.DiMG).todense(), DiNL)
np.testing.assert_equal(nx.laplacian_matrix(self.DiG, nodelist=[1, 2]).todense(), np.array([[1, -1], [0, 0]]))
np.testing.assert_equal(nx.laplacian_matrix(self.DiWG).todense(), DiWL)
np.testing.assert_equal(nx.laplacian_matrix(self.DiWG, weight=None).todense(), DiNL)
np.testing.assert_equal(nx.laplacian_matrix(self.DiWG, weight='other').todense(), DiOL)
```

## Next Steps


---

*Source: test_laplacian.py:50 | Complexity: Advanced | Last updated: 2026-06-02*