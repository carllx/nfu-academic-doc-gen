# How To: Weighted Incidence Matrix

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weighted incidence matrix

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.exception`


## Step-by-Step Guide

### Step 1: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=True, dtype=int).todense()
```

### Step 2: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, self.OI)
```

### Step 3: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=False, dtype=int).todense()
```

### Step 4: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, np.abs(self.OI))
```

### Step 5: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=True, weight='weight').todense()
```

### Step 6: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, 0.5 * self.OI)
```

### Step 7: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=False, weight='weight').todense()
```

### Step 8: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, np.abs(0.5 * self.OI))
```

### Step 9: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=True, weight='other').todense()
```

### Step 10: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, 0.3 * self.OI)
```

### Step 11: Assign WMG = nx.MultiGraph(...)

```python
WMG = nx.MultiGraph(self.WG)
```

### Step 12: Call WMG.add_edge()

```python
WMG.add_edge(0, 1, weight=0.5, other=0.3)
```

### Step 13: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(WMG, nodelist=sorted(WMG), edgelist=sorted(WMG.edges(keys=True)), oriented=True, weight='weight').todense()
```

### Step 14: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, 0.5 * self.MGOI)
```

### Step 15: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(WMG, nodelist=sorted(WMG), edgelist=sorted(WMG.edges(keys=True)), oriented=False, weight='weight').todense()
```

### Step 16: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, np.abs(0.5 * self.MGOI))
```

### Step 17: Assign I = nx.incidence_matrix.todense(...)

```python
I = nx.incidence_matrix(WMG, nodelist=sorted(WMG), edgelist=sorted(WMG.edges(keys=True)), oriented=True, weight='other').todense()
```

### Step 18: Call np.testing.assert_equal()

```python
np.testing.assert_equal(I, 0.3 * self.MGOI)
```


## Complete Example

```python
# Workflow
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=True, dtype=int).todense()
np.testing.assert_equal(I, self.OI)
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=False, dtype=int).todense()
np.testing.assert_equal(I, np.abs(self.OI))
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=True, weight='weight').todense()
np.testing.assert_equal(I, 0.5 * self.OI)
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=False, weight='weight').todense()
np.testing.assert_equal(I, np.abs(0.5 * self.OI))
I = nx.incidence_matrix(self.WG, nodelist=sorted(self.WG), edgelist=sorted(self.WG.edges()), oriented=True, weight='other').todense()
np.testing.assert_equal(I, 0.3 * self.OI)
WMG = nx.MultiGraph(self.WG)
WMG.add_edge(0, 1, weight=0.5, other=0.3)
I = nx.incidence_matrix(WMG, nodelist=sorted(WMG), edgelist=sorted(WMG.edges(keys=True)), oriented=True, weight='weight').todense()
np.testing.assert_equal(I, 0.5 * self.MGOI)
I = nx.incidence_matrix(WMG, nodelist=sorted(WMG), edgelist=sorted(WMG.edges(keys=True)), oriented=False, weight='weight').todense()
np.testing.assert_equal(I, np.abs(0.5 * self.MGOI))
I = nx.incidence_matrix(WMG, nodelist=sorted(WMG), edgelist=sorted(WMG.edges(keys=True)), oriented=True, weight='other').todense()
np.testing.assert_equal(I, 0.3 * self.MGOI)
```

## Next Steps


---

*Source: test_graphmatrix.py:162 | Complexity: Advanced | Last updated: 2026-06-02*