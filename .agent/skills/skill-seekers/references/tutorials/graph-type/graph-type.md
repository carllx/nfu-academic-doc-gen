# How To: Graph Type

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph type

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.complete_graph(...)

```python
G1 = nx.complete_graph(self.N, nx.MultiDiGraph())
```

### Step 2: Assign G2 = nx.MultiGraph(...)

```python
G2 = nx.MultiGraph(G1)
```

### Step 3: Assign G3 = nx.DiGraph(...)

```python
G3 = nx.DiGraph(G1)
```

### Step 4: Assign G4 = nx.Graph(...)

```python
G4 = nx.Graph(G1)
```

### Step 5: Assign truth = value

```python
truth = {frozenset(G1)}
```

### Step 6: Call self._check_communities()

```python
self._check_communities(G1, truth)
```

### Step 7: Call self._check_communities()

```python
self._check_communities(G2, truth)
```

### Step 8: Call self._check_communities()

```python
self._check_communities(G3, truth)
```

### Step 9: Call self._check_communities()

```python
self._check_communities(G4, truth)
```


## Complete Example

```python
# Workflow
G1 = nx.complete_graph(self.N, nx.MultiDiGraph())
G2 = nx.MultiGraph(G1)
G3 = nx.DiGraph(G1)
G4 = nx.Graph(G1)
truth = {frozenset(G1)}
self._check_communities(G1, truth)
self._check_communities(G2, truth)
self._check_communities(G3, truth)
self._check_communities(G4, truth)
```

## Next Steps


---

*Source: test_label_propagation.py:215 | Complexity: Advanced | Last updated: 2026-06-02*