# How To: Bethe Hessian Spectrum

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Bethe Hessian eigenvalues

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Bethe Hessian eigenvalues'

```python
'Bethe Hessian eigenvalues'
```

### Step 2: Assign evals = np.array(...)

```python
evals = np.array([0.5 * (9 - np.sqrt(33)), 4, 0.5 * (9 + np.sqrt(33))])
```

### Step 3: Assign e = sorted(...)

```python
e = sorted(nx.bethe_hessian_spectrum(self.P, r=2))
```

### Step 4: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(e, evals)
```

### Step 5: Assign e1 = sorted(...)

```python
e1 = sorted(nx.bethe_hessian_spectrum(self.P, r=1))
```

### Step 6: Assign e2 = sorted(...)

```python
e2 = sorted(nx.laplacian_spectrum(self.P))
```

### Step 7: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(e1, e2)
```


## Complete Example

```python
# Workflow
'Bethe Hessian eigenvalues'
evals = np.array([0.5 * (9 - np.sqrt(33)), 4, 0.5 * (9 + np.sqrt(33))])
e = sorted(nx.bethe_hessian_spectrum(self.P, r=2))
np.testing.assert_almost_equal(e, evals)
e1 = sorted(nx.bethe_hessian_spectrum(self.P, r=1))
e2 = sorted(nx.laplacian_spectrum(self.P))
np.testing.assert_almost_equal(e1, e2)
```

## Next Steps


---

*Source: test_spectrum.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*