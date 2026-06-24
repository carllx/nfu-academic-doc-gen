# How To: Weighted Path

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weighted path

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(6)
```

**Verification:**
```python
assert nodes_equal(M, [0, 1, 2])
```

### Step 2: Assign partition = value

```python
partition = [{0, 1}, {2, 3}, {4, 5}]
```

**Verification:**
```python
assert edges_equal(M.edges(), [(0, 1), (1, 2)])
```

### Step 3: Assign M = nx.quotient_graph(...)

```python
M = nx.quotient_graph(G, partition, weight='w', relabel=True)
```

**Verification:**
```python
assert M[0][1]['weight'] == 2
```

### Step 4: Assign unknown = value

```python
G[i][i + 1]['w'] = i + 1
```

**Verification:**
```python
assert M[1][2]['weight'] == 4
```


## Complete Example

```python
# Workflow
G = nx.path_graph(6)
for i in range(5):
    G[i][i + 1]['w'] = i + 1
partition = [{0, 1}, {2, 3}, {4, 5}]
M = nx.quotient_graph(G, partition, weight='w', relabel=True)
assert nodes_equal(M, [0, 1, 2])
assert edges_equal(M.edges(), [(0, 1), (1, 2)])
assert M[0][1]['weight'] == 2
assert M[1][2]['weight'] == 4
for n in M:
    assert M.nodes[n]['nedges'] == 1
    assert M.nodes[n]['nnodes'] == 2
    assert M.nodes[n]['density'] == 1
```

## Next Steps


---

*Source: test_contraction.py:206 | Complexity: Intermediate | Last updated: 2026-06-02*