# How To: Subgraph Centrality Big Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subgraph centrality big graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.centrality.subgraph_alg`


## Step-by-Step Guide

### Step 1: Assign g199 = nx.complete_graph(...)

```python
g199 = nx.complete_graph(199)
```

### Step 2: Assign g200 = nx.complete_graph(...)

```python
g200 = nx.complete_graph(200)
```

### Step 3: Assign comm199 = nx.subgraph_centrality(...)

```python
comm199 = nx.subgraph_centrality(g199)
```

### Step 4: Assign comm199_exp = nx.subgraph_centrality_exp(...)

```python
comm199_exp = nx.subgraph_centrality_exp(g199)
```

### Step 5: Assign comm200 = nx.subgraph_centrality(...)

```python
comm200 = nx.subgraph_centrality(g200)
```

### Step 6: Assign comm200_exp = nx.subgraph_centrality_exp(...)

```python
comm200_exp = nx.subgraph_centrality_exp(g200)
```


## Complete Example

```python
# Workflow
g199 = nx.complete_graph(199)
g200 = nx.complete_graph(200)
comm199 = nx.subgraph_centrality(g199)
comm199_exp = nx.subgraph_centrality_exp(g199)
comm200 = nx.subgraph_centrality(g200)
comm200_exp = nx.subgraph_centrality_exp(g200)
```

## Next Steps


---

*Source: test_subgraph.py:46 | Complexity: Intermediate | Last updated: 2026-06-02*