# How To: Default Flow Function Karate Club Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default flow function karate club graph

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

**Verification:**
```python
assert nx.is_tree(T)
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, 1, 'capacity')
```

**Verification:**
```python
assert nx.minimum_cut_value(G, u, v) == cut_value
```

### Step 3: Assign T = nx.gomory_hu_tree(...)

```python
T = nx.gomory_hu_tree(G)
```

**Verification:**
```python
assert nx.is_tree(T)
```

### Step 4: Assign unknown = self.minimum_edge_weight(...)

```python
cut_value, edge = self.minimum_edge_weight(T, u, v)
```

**Verification:**
```python
assert nx.minimum_cut_value(G, u, v) == cut_value
```


## Complete Example

```python
# Workflow
G = nx.karate_club_graph()
nx.set_edge_attributes(G, 1, 'capacity')
T = nx.gomory_hu_tree(G)
assert nx.is_tree(T)
for u, v in combinations(G, 2):
    cut_value, edge = self.minimum_edge_weight(T, u, v)
    assert nx.minimum_cut_value(G, u, v) == cut_value
```

## Next Steps


---

*Source: test_gomory_hu.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*