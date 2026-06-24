# How To: Modularity Spectrum

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Modularity eigenvalues

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Modularity eigenvalues'

```python
'Modularity eigenvalues'
```

### Step 2: Assign evals = np.array(...)

```python
evals = np.array([-1.5, 0.0, 0.0])
```

### Step 3: Assign e = sorted(...)

```python
e = sorted(nx.modularity_spectrum(self.P))
```

### Step 4: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(e, evals)
```

### Step 5: Assign evals = np.array(...)

```python
evals = np.array([-0.5, 0.0, 0.0])
```

### Step 6: Assign e = sorted(...)

```python
e = sorted(nx.modularity_spectrum(self.DG))
```

### Step 7: Call np.testing.assert_almost_equal()

```python
np.testing.assert_almost_equal(e, evals)
```


## Complete Example

```python
# Workflow
'Modularity eigenvalues'
evals = np.array([-1.5, 0.0, 0.0])
e = sorted(nx.modularity_spectrum(self.P))
np.testing.assert_almost_equal(e, evals)
evals = np.array([-0.5, 0.0, 0.0])
e = sorted(nx.modularity_spectrum(self.DG))
np.testing.assert_almost_equal(e, evals)
```

## Next Steps


---

*Source: test_spectrum.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*