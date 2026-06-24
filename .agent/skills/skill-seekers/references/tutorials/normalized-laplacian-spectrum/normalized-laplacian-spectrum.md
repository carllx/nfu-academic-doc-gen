# How To: Normalized Laplacian Spectrum

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Normalized Laplacian eigenvalues

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Normalized Laplacian eigenvalues'

```python
'Normalized Laplacian eigenvalues'
```

### Step 2: Assign evals = np.array(...)

```python
evals = np.array([0, 0, 0.7712864461218, 1.5, 1.7287135538781])
```

### Step 3: Assign e = sorted(...)

```python
e = sorted(nx.normalized_laplacian_spectrum(self.G))
```

### Step 4: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(e, evals)
```

### Step 5: Assign e = sorted(...)

```python
e = sorted(nx.normalized_laplacian_spectrum(self.WG, weight=None))
```

### Step 6: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(e, evals)
```

### Step 7: Assign e = sorted(...)

```python
e = sorted(nx.normalized_laplacian_spectrum(self.WG))
```

### Step 8: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(e, evals)
```

### Step 9: Assign e = sorted(...)

```python
e = sorted(nx.normalized_laplacian_spectrum(self.WG, weight='other'))
```

### Step 10: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(e, evals)
```


## Complete Example

```python
# Workflow
'Normalized Laplacian eigenvalues'
evals = np.array([0, 0, 0.7712864461218, 1.5, 1.7287135538781])
e = sorted(nx.normalized_laplacian_spectrum(self.G))
np.testing.assert_almost_equal(e, evals)
e = sorted(nx.normalized_laplacian_spectrum(self.WG, weight=None))
np.testing.assert_almost_equal(e, evals)
e = sorted(nx.normalized_laplacian_spectrum(self.WG))
np.testing.assert_almost_equal(e, evals)
e = sorted(nx.normalized_laplacian_spectrum(self.WG, weight='other'))
np.testing.assert_almost_equal(e, evals)
```

## Next Steps


---

*Source: test_spectrum.py:34 | Complexity: Advanced | Last updated: 2026-06-02*