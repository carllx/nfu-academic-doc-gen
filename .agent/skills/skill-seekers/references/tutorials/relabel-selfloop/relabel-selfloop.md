# How To: Relabel Selfloop

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relabel selfloop

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators.classic`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 1), (1, 2), (2, 3)])
```

**Verification:**
```python
assert nodes_equal(G.nodes(), ['One', 'Three', 'Two'])
```

### Step 2: Assign G = nx.relabel_nodes(...)

```python
G = nx.relabel_nodes(G, {1: 'One', 2: 'Two', 3: 'Three'}, copy=False)
```

**Verification:**
```python
assert nodes_equal(G.nodes(), ['One', 'Three', 'Two'])
```

### Step 3: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph([(1, 1), (1, 2), (2, 3)])
```

**Verification:**
```python
assert nodes_equal(G.nodes(), [0])
```

### Step 4: Assign G = nx.relabel_nodes(...)

```python
G = nx.relabel_nodes(G, {1: 'One', 2: 'Two', 3: 'Three'}, copy=False)
```

**Verification:**
```python
assert nodes_equal(G.nodes(), ['One', 'Three', 'Two'])
```

### Step 5: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph([(1, 1)])
```

### Step 6: Assign G = nx.relabel_nodes(...)

```python
G = nx.relabel_nodes(G, {1: 0}, copy=False)
```

**Verification:**
```python
assert nodes_equal(G.nodes(), [0])
```


## Complete Example

```python
# Workflow
G = nx.DiGraph([(1, 1), (1, 2), (2, 3)])
G = nx.relabel_nodes(G, {1: 'One', 2: 'Two', 3: 'Three'}, copy=False)
assert nodes_equal(G.nodes(), ['One', 'Three', 'Two'])
G = nx.MultiDiGraph([(1, 1), (1, 2), (2, 3)])
G = nx.relabel_nodes(G, {1: 'One', 2: 'Two', 3: 'Three'}, copy=False)
assert nodes_equal(G.nodes(), ['One', 'Three', 'Two'])
G = nx.MultiDiGraph([(1, 1)])
G = nx.relabel_nodes(G, {1: 0}, copy=False)
assert nodes_equal(G.nodes(), [0])
```

## Next Steps


---

*Source: test_relabel.py:197 | Complexity: Intermediate | Last updated: 2026-06-02*