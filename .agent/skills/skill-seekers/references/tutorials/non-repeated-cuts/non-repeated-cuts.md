# How To: Non Repeated Cuts

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non repeated cuts

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity.kcutsets`


## Step-by-Step Guide

### Step 1: Assign K = nx.karate_club_graph(...)

```python
K = nx.karate_club_graph()
```

**Verification:**
```python
assert len(solution) == len(cuts)
```

### Step 2: Assign bcc = max(...)

```python
bcc = max(list(nx.biconnected_components(K)), key=len)
```

**Verification:**
```python
assert cut in solution
```

### Step 3: Assign G = K.subgraph(...)

```python
G = K.subgraph(bcc)
```

### Step 4: Assign solution = value

```python
solution = [{32, 33}, {2, 33}, {0, 3}, {0, 1}, {29, 33}]
```

### Step 5: Assign cuts = list(...)

```python
cuts = list(nx.all_node_cuts(G))
```

**Verification:**
```python
assert len(solution) == len(cuts)
```


## Complete Example

```python
# Workflow
K = nx.karate_club_graph()
bcc = max(list(nx.biconnected_components(K)), key=len)
G = K.subgraph(bcc)
solution = [{32, 33}, {2, 33}, {0, 3}, {0, 1}, {29, 33}]
cuts = list(nx.all_node_cuts(G))
assert len(solution) == len(cuts)
for cut in cuts:
    assert cut in solution
```

## Next Steps


---

*Source: test_kcutsets.py:234 | Complexity: Intermediate | Last updated: 2026-06-02*