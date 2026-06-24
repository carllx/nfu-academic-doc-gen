# How To: Laplacian Centrality K

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test laplacian centrality K

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign K = nx.krackhardt_kite_graph(...)

```python
K = nx.krackhardt_kite_graph()
```

**Verification:**
```python
assert exact[n] == pytest.approx(dc, abs=1e-07)
```

### Step 2: Assign d = nx.laplacian_centrality(...)

```python
d = nx.laplacian_centrality(K)
```

**Verification:**
```python
assert exact[n] * full_energy == pytest.approx(dc, abs=0.001)
```

### Step 3: Assign exact = value

```python
exact = {0: 0.3010753, 1: 0.3010753, 2: 0.2258065, 3: 0.483871, 4: 0.2258065, 5: 0.3870968, 6: 0.3870968, 7: 0.1935484, 8: 0.0752688, 9: 0.0322581}
```

### Step 4: Assign full_energy = 186

```python
full_energy = 186
```

### Step 5: Assign dnn = nx.laplacian_centrality(...)

```python
dnn = nx.laplacian_centrality(K, normalized=False)
```

**Verification:**
```python
assert exact[n] == pytest.approx(dc, abs=1e-07)
```


## Complete Example

```python
# Workflow
K = nx.krackhardt_kite_graph()
d = nx.laplacian_centrality(K)
exact = {0: 0.3010753, 1: 0.3010753, 2: 0.2258065, 3: 0.483871, 4: 0.2258065, 5: 0.3870968, 6: 0.3870968, 7: 0.1935484, 8: 0.0752688, 9: 0.0322581}
for n, dc in d.items():
    assert exact[n] == pytest.approx(dc, abs=1e-07)
full_energy = 186
dnn = nx.laplacian_centrality(K, normalized=False)
for n, dc in dnn.items():
    assert exact[n] * full_energy == pytest.approx(dc, abs=0.001)
```

## Next Steps


---

*Source: test_laplacian_centrality.py:134 | Complexity: Intermediate | Last updated: 2026-06-02*