# How To: Normalized Laplacian

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Generalized Graph Laplacian

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Generalized Graph Laplacian'

```python
'Generalized Graph Laplacian'
```

### Step 2: Assign G = np.array(...)

```python
G = np.array([[1.0, -0.408, -0.408, -0.577, 0.0], [-0.408, 1.0, -0.5, 0.0, 0.0], [-0.408, -0.5, 1.0, 0.0, 0.0], [-0.577, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]])
```

### Step 3: Assign GL = np.array(...)

```python
GL = np.array([[1.0, -0.408, -0.408, -0.577, 0.0], [-0.408, 1.0, -0.5, 0.0, 0.0], [-0.408, -0.5, 1.0, 0.0, 0.0], [-0.577, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]])
```

### Step 4: Assign Lsl = np.array(...)

```python
Lsl = np.array([[0.75, -0.2887, -0.2887, -0.3536, 0.0], [-0.2887, 0.6667, -0.3333, 0.0, 0.0], [-0.2887, -0.3333, 0.6667, 0.0, 0.0], [-0.3536, 0.0, 0.0, 0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]])
```

### Step 5: Assign DiG = np.array(...)

```python
DiG = np.array([[1.0, 0.0, -0.4082, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-0.4082, 0.0, 1.0, 0.0, -0.4082, 0.0], [0.0, 0.0, 0.0, 1.0, -0.5, -0.7071], [0.0, 0.0, 0.0, -0.5, 1.0, -0.7071], [0.0, 0.0, 0.0, -0.7071, 0.0, 1.0]])
```

### Step 6: Assign DiGL = np.array(...)

```python
DiGL = np.array([[1.0, 0.0, -0.4082, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-0.4082, 0.0, 1.0, -0.4082, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, -0.5, -0.7071], [0.0, 0.0, 0.0, -0.5, 1.0, -0.7071], [0.0, 0.0, 0.0, 0.0, -0.7071, 1.0]])
```

### Step 7: Assign DiLsl = np.array(...)

```python
DiLsl = np.array([[0.6667, -0.5774, -0.2887, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-0.2887, -0.5, 0.75, -0.2887, 0.0, 0.0], [0.0, 0.0, 0.0, 0.6667, -0.3333, -0.4082], [0.0, 0.0, 0.0, -0.3333, 0.6667, -0.4082], [0.0, 0.0, 0.0, 0.0, -0.4082, 0.5]])
```

### Step 8: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.G, nodelist=range(5)).todense(), G, decimal=3)
```

### Step 9: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.G).todense(), GL, decimal=3)
```

### Step 10: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.MG).todense(), GL, decimal=3)
```

### Step 11: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.WG).todense(), GL, decimal=3)
```

### Step 12: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.WG, weight='other').todense(), GL, decimal=3)
```

### Step 13: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.Gsl).todense(), Lsl, decimal=3)
```

### Step 14: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiG, nodelist=range(1, 1 + 6)).todense(), DiG, decimal=3)
```

### Step 15: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiG).todense(), DiGL, decimal=3)
```

### Step 16: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiMG).todense(), DiGL, decimal=3)
```

### Step 17: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiWG).todense(), DiGL, decimal=3)
```

### Step 18: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiWG, weight='other').todense(), DiGL, decimal=3)
```

### Step 19: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiGsl).todense(), DiLsl, decimal=3)
```


## Complete Example

```python
# Workflow
'Generalized Graph Laplacian'
G = np.array([[1.0, -0.408, -0.408, -0.577, 0.0], [-0.408, 1.0, -0.5, 0.0, 0.0], [-0.408, -0.5, 1.0, 0.0, 0.0], [-0.577, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]])
GL = np.array([[1.0, -0.408, -0.408, -0.577, 0.0], [-0.408, 1.0, -0.5, 0.0, 0.0], [-0.408, -0.5, 1.0, 0.0, 0.0], [-0.577, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]])
Lsl = np.array([[0.75, -0.2887, -0.2887, -0.3536, 0.0], [-0.2887, 0.6667, -0.3333, 0.0, 0.0], [-0.2887, -0.3333, 0.6667, 0.0, 0.0], [-0.3536, 0.0, 0.0, 0.5, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0]])
DiG = np.array([[1.0, 0.0, -0.4082, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-0.4082, 0.0, 1.0, 0.0, -0.4082, 0.0], [0.0, 0.0, 0.0, 1.0, -0.5, -0.7071], [0.0, 0.0, 0.0, -0.5, 1.0, -0.7071], [0.0, 0.0, 0.0, -0.7071, 0.0, 1.0]])
DiGL = np.array([[1.0, 0.0, -0.4082, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-0.4082, 0.0, 1.0, -0.4082, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, -0.5, -0.7071], [0.0, 0.0, 0.0, -0.5, 1.0, -0.7071], [0.0, 0.0, 0.0, 0.0, -0.7071, 1.0]])
DiLsl = np.array([[0.6667, -0.5774, -0.2887, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [-0.2887, -0.5, 0.75, -0.2887, 0.0, 0.0], [0.0, 0.0, 0.0, 0.6667, -0.3333, -0.4082], [0.0, 0.0, 0.0, -0.3333, 0.6667, -0.4082], [0.0, 0.0, 0.0, 0.0, -0.4082, 0.5]])
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.G, nodelist=range(5)).todense(), G, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.G).todense(), GL, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.MG).todense(), GL, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.WG).todense(), GL, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.WG, weight='other').todense(), GL, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.Gsl).todense(), Lsl, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiG, nodelist=range(1, 1 + 6)).todense(), DiG, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiG).todense(), DiGL, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiMG).todense(), DiGL, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiWG).todense(), DiGL, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiWG, weight='other').todense(), DiGL, decimal=3)
np.testing.assert_almost_equal(nx.normalized_laplacian_matrix(self.DiGsl).todense(), DiLsl, decimal=3)
```

## Next Steps


---

*Source: test_laplacian.py:97 | Complexity: Advanced | Last updated: 2026-06-02*