# How To: From Edgelist

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from edgelist

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(10)
```

**Verification:**
```python
assert nodes_equal(G.nodes(), GG.nodes())
```

### Step 2: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from(((u, v, u) for u, v in list(G.edges)))
```

**Verification:**
```python
assert edges_equal(G.edges(), GG.edges())
```

### Step 3: Assign edgelist = nx.to_edgelist(...)

```python
edgelist = nx.to_edgelist(G)
```

**Verification:**
```python
assert nodes_equal(G.nodes(), GW.nodes())
```

### Step 4: Assign source = value

```python
source = [s for s, t, d in edgelist]
```

**Verification:**
```python
assert edges_equal(G.edges(), GW.edges())
```

### Step 5: Assign target = value

```python
target = [t for s, t, d in edgelist]
```

### Step 6: Assign weight = value

```python
weight = [d['weight'] for s, t, d in edgelist]
```

### Step 7: Assign edges = pd.DataFrame(...)

```python
edges = pd.DataFrame({'source': source, 'target': target, 'weight': weight})
```

### Step 8: Assign GG = nx.from_pandas_edgelist(...)

```python
GG = nx.from_pandas_edgelist(edges, edge_attr='weight')
```

**Verification:**
```python
assert nodes_equal(G.nodes(), GG.nodes())
```

### Step 9: Assign GW = nx.to_networkx_graph(...)

```python
GW = nx.to_networkx_graph(edges, create_using=nx.Graph)
```

**Verification:**
```python
assert nodes_equal(G.nodes(), GW.nodes())
```


## Complete Example

```python
# Workflow
G = nx.cycle_graph(10)
G.add_weighted_edges_from(((u, v, u) for u, v in list(G.edges)))
edgelist = nx.to_edgelist(G)
source = [s for s, t, d in edgelist]
target = [t for s, t, d in edgelist]
weight = [d['weight'] for s, t, d in edgelist]
edges = pd.DataFrame({'source': source, 'target': target, 'weight': weight})
GG = nx.from_pandas_edgelist(edges, edge_attr='weight')
assert nodes_equal(G.nodes(), GG.nodes())
assert edges_equal(G.edges(), GG.edges())
GW = nx.to_networkx_graph(edges, create_using=nx.Graph)
assert nodes_equal(G.nodes(), GW.nodes())
assert edges_equal(G.edges(), GW.edges())
```

## Next Steps


---

*Source: test_convert_pandas.py:152 | Complexity: Advanced | Last updated: 2026-06-02*