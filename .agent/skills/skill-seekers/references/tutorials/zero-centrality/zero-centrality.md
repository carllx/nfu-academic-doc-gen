# How To: Zero Centrality

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zero centrality

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3)
```

**Verification:**
```python
assert len(shared_items) == len(real_cc)
```

### Step 2: Assign prev_cc = nx.closeness_centrality(...)

```python
prev_cc = nx.closeness_centrality(G)
```

**Verification:**
```python
assert 0 in test_cc.values()
```

### Step 3: Assign edge = self.pick_remove_edge(...)

```python
edge = self.pick_remove_edge(G)
```

### Step 4: Assign test_cc = nx.incremental_closeness_centrality(...)

```python
test_cc = nx.incremental_closeness_centrality(G, edge, prev_cc, insertion=False)
```

### Step 5: Call G.remove_edges_from()

```python
G.remove_edges_from([edge])
```

### Step 6: Assign real_cc = nx.closeness_centrality(...)

```python
real_cc = nx.closeness_centrality(G)
```

### Step 7: Assign shared_items = value

```python
shared_items = set(test_cc.items()) & set(real_cc.items())
```

**Verification:**
```python
assert len(shared_items) == len(real_cc)
```


## Complete Example

```python
# Workflow
G = nx.path_graph(3)
prev_cc = nx.closeness_centrality(G)
edge = self.pick_remove_edge(G)
test_cc = nx.incremental_closeness_centrality(G, edge, prev_cc, insertion=False)
G.remove_edges_from([edge])
real_cc = nx.closeness_centrality(G)
shared_items = set(test_cc.items()) & set(real_cc.items())
assert len(shared_items) == len(real_cc)
assert 0 in test_cc.values()
```

## Next Steps


---

*Source: test_closeness_centrality.py:238 | Complexity: Intermediate | Last updated: 2026-06-02*