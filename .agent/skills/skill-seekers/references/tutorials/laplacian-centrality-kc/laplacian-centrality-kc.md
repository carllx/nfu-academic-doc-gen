# How To: Laplacian Centrality Kc

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test laplacian centrality KC

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign KC = nx.karate_club_graph(...)

```python
KC = nx.karate_club_graph()
```

**Verification:**
```python
assert exact[n] == pytest.approx(dc, abs=1e-07)
```

### Step 2: Assign d = nx.laplacian_centrality(...)

```python
d = nx.laplacian_centrality(KC)
```

**Verification:**
```python
assert exact[n] * full_energy == pytest.approx(dc, abs=0.001)
```

### Step 3: Assign exact = value

```python
exact = {0: 0.2543593, 1: 0.1724524, 2: 0.2166053, 3: 0.0964646, 4: 0.0350344, 5: 0.0571109, 6: 0.0540713, 7: 0.0788674, 8: 0.1222204, 9: 0.0217565, 10: 0.0308751, 11: 0.0215965, 12: 0.0174372, 13: 0.118861, 14: 0.0366341, 15: 0.0548712, 16: 0.0172772, 17: 0.0191969, 18: 0.0225564, 19: 0.0331147, 20: 0.0279955, 21: 0.0246361, 22: 0.0382339, 23: 0.1294193, 24: 0.0227164, 25: 0.0644697, 26: 0.0281555, 27: 0.075188, 28: 0.0364742, 29: 0.0707087, 30: 0.0708687, 31: 0.131019, 32: 0.2370821, 33: 0.3066709}
```

### Step 4: Assign full_energy = 12502

```python
full_energy = 12502
```

### Step 5: Assign dnn = nx.laplacian_centrality(...)

```python
dnn = nx.laplacian_centrality(KC, normalized=False)
```

**Verification:**
```python
assert exact[n] == pytest.approx(dc, abs=1e-07)
```


## Complete Example

```python
# Workflow
KC = nx.karate_club_graph()
d = nx.laplacian_centrality(KC)
exact = {0: 0.2543593, 1: 0.1724524, 2: 0.2166053, 3: 0.0964646, 4: 0.0350344, 5: 0.0571109, 6: 0.0540713, 7: 0.0788674, 8: 0.1222204, 9: 0.0217565, 10: 0.0308751, 11: 0.0215965, 12: 0.0174372, 13: 0.118861, 14: 0.0366341, 15: 0.0548712, 16: 0.0172772, 17: 0.0191969, 18: 0.0225564, 19: 0.0331147, 20: 0.0279955, 21: 0.0246361, 22: 0.0382339, 23: 0.1294193, 24: 0.0227164, 25: 0.0644697, 26: 0.0281555, 27: 0.075188, 28: 0.0364742, 29: 0.0707087, 30: 0.0708687, 31: 0.131019, 32: 0.2370821, 33: 0.3066709}
for n, dc in d.items():
    assert exact[n] == pytest.approx(dc, abs=1e-07)
full_energy = 12502
dnn = nx.laplacian_centrality(KC, normalized=False)
for n, dc in dnn.items():
    assert exact[n] * full_energy == pytest.approx(dc, abs=0.001)
```

## Next Steps


---

*Source: test_laplacian_centrality.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*