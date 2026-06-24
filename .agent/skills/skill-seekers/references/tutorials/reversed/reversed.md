# How To: Reversed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: A directed graph with no bi-directional edges should yield different a graph hash
to the same graph taken with edge directions reversed if there are no hash
collisions. Here we test a cycle graph which is the minimal counterexample

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n    A directed graph with no bi-directional edges should yield different a graph hash\n    to the same graph taken with edge directions reversed if there are no hash\n    collisions. Here we test a cycle graph which is the minimal counterexample\n    '

```python
'\n    A directed graph with no bi-directional edges should yield different a graph hash\n    to the same graph taken with edge directions reversed if there are no hash\n    collisions. Here we test a cycle graph which is the minimal counterexample\n    '
```

**Verification:**
```python
assert h != h_reversed
```

### Step 2: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(5, create_using=nx.DiGraph)
```

### Step 3: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, {n: str(n) for n in G.nodes()}, name='label')
```

### Step 4: Assign G_reversed = G.reverse(...)

```python
G_reversed = G.reverse()
```

### Step 5: Assign h = nx.weisfeiler_lehman_graph_hash(...)

```python
h = nx.weisfeiler_lehman_graph_hash(G, node_attr='label')
```

### Step 6: Assign h_reversed = nx.weisfeiler_lehman_graph_hash(...)

```python
h_reversed = nx.weisfeiler_lehman_graph_hash(G_reversed, node_attr='label')
```

**Verification:**
```python
assert h != h_reversed
```


## Complete Example

```python
# Workflow
'\n    A directed graph with no bi-directional edges should yield different a graph hash\n    to the same graph taken with edge directions reversed if there are no hash\n    collisions. Here we test a cycle graph which is the minimal counterexample\n    '
G = nx.cycle_graph(5, create_using=nx.DiGraph)
nx.set_node_attributes(G, {n: str(n) for n in G.nodes()}, name='label')
G_reversed = G.reverse()
h = nx.weisfeiler_lehman_graph_hash(G, node_attr='label')
h_reversed = nx.weisfeiler_lehman_graph_hash(G_reversed, node_attr='label')
assert h != h_reversed
```

## Next Steps


---

*Source: test_graph_hashing.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*