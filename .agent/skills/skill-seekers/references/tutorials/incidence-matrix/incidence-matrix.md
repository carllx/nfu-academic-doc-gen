# How To: Incidence Matrix

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Conversion to incidence matrix

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.exception`


## Step-by-Step Guide

### Step 1: 'Conversion to incidence matrix'

```python
'Conversion to incidence matrix'
```

**Verification:**
```python
assert I.dtype == np.uint8
```

### Step 2: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.G, nodelist=sorted(self.G), edgelist=sorted(self.G.edges()), oriented=True, dtype=int).todense()
```

### Step 3: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, self.OI)
```

### Step 4: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.G, nodelist=sorted(self.G), edgelist=sorted(self.G.edges()), oriented=False, dtype=int).todense()
```

### Step 5: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, np.abs(self.OI))
```

### Step 6: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.MG, nodelist=sorted(self.MG), edgelist=sorted(self.MG.edges()), oriented=True, dtype=int).todense()
```

### Step 7: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, self.OI)
```

### Step 8: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.MG, nodelist=sorted(self.MG), edgelist=sorted(self.MG.edges()), oriented=False, dtype=int).todense()
```

### Step 9: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, np.abs(self.OI))
```

### Step 10: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.MG2, nodelist=sorted(self.MG2), edgelist=sorted(self.MG2.edges()), oriented=True, dtype=int).todense()
```

### Step 11: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, self.MGOI)
```

### Step 12: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.MG2, nodelist=sorted(self.MG), edgelist=sorted(self.MG2.edges()), oriented=False, dtype=int).todense()
```

### Step 13: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, np.abs(self.MGOI))
```

### Step 14: Assign I = nx.incidence_matrix(...)

```python
I = nx.incidence_matrix(self.G, dtype=np.uint8)
```

**Verification:**
```python
assert I.dtype == np.uint8
```


## Complete Example

```python
# Workflow
'Conversion to incidence matrix'
I = nx.incidence_matrix(self.G, nodelist=sorted(self.G), edgelist=sorted(self.G.edges()), oriented=True, dtype=int).todense()
np.testing.assert_equal(I, self.OI)
I = nx.incidence_matrix(self.G, nodelist=sorted(self.G), edgelist=sorted(self.G.edges()), oriented=False, dtype=int).todense()
np.testing.assert_equal(I, np.abs(self.OI))
I = nx.incidence_matrix(self.MG, nodelist=sorted(self.MG), edgelist=sorted(self.MG.edges()), oriented=True, dtype=int).todense()
np.testing.assert_equal(I, self.OI)
I = nx.incidence_matrix(self.MG, nodelist=sorted(self.MG), edgelist=sorted(self.MG.edges()), oriented=False, dtype=int).todense()
np.testing.assert_equal(I, np.abs(self.OI))
I = nx.incidence_matrix(self.MG2, nodelist=sorted(self.MG2), edgelist=sorted(self.MG2.edges()), oriented=True, dtype=int).todense()
np.testing.assert_equal(I, self.MGOI)
I = nx.incidence_matrix(self.MG2, nodelist=sorted(self.MG), edgelist=sorted(self.MG2.edges()), oriented=False, dtype=int).todense()
np.testing.assert_equal(I, np.abs(self.MGOI))
I = nx.incidence_matrix(self.G, dtype=np.uint8)
assert I.dtype == np.uint8
```

## Next Steps


---

*Source: test_graphmatrix.py:103 | Complexity: Advanced | Last updated: 2026-06-02*