# How To: Isomorphic

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: graph hashes should be invariant to node-relabeling (when the output is reindexed
by the same mapping)

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n    graph hashes should be invariant to node-relabeling (when the output is reindexed\n    by the same mapping)\n    '

```python
'\n    graph hashes should be invariant to node-relabeling (when the output is reindexed\n    by the same mapping)\n    '
```

**Verification:**
```python
assert g1_hash == g2_hash
```

### Step 2: Assign unknown = value

```python
n, r = (100, 10)
```

### Step 3: Assign p = value

```python
p = 1.0 / r
```

### Step 4: Assign G1 = nx.erdos_renyi_graph(...)

```python
G1 = nx.erdos_renyi_graph(n, p * i, seed=200 + i)
```

### Step 5: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, {u: -1 * u for u in G1.nodes()})
```

### Step 6: Assign g1_hash = nx.weisfeiler_lehman_graph_hash(...)

```python
g1_hash = nx.weisfeiler_lehman_graph_hash(G1)
```

### Step 7: Assign g2_hash = nx.weisfeiler_lehman_graph_hash(...)

```python
g2_hash = nx.weisfeiler_lehman_graph_hash(G2)
```

**Verification:**
```python
assert g1_hash == g2_hash
```


## Complete Example

```python
# Workflow
'\n    graph hashes should be invariant to node-relabeling (when the output is reindexed\n    by the same mapping)\n    '
n, r = (100, 10)
p = 1.0 / r
for i in range(1, r + 1):
    G1 = nx.erdos_renyi_graph(n, p * i, seed=200 + i)
    G2 = nx.relabel_nodes(G1, {u: -1 * u for u in G1.nodes()})
    g1_hash = nx.weisfeiler_lehman_graph_hash(G1)
    g2_hash = nx.weisfeiler_lehman_graph_hash(G2)
    assert g1_hash == g2_hash
```

## Next Steps


---

*Source: test_graph_hashing.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*