# How To: Wrong Nodes Prev Cc Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wrong nodes prev cc raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: undirected_G
```

## Step-by-Step Guide

### Step 1: Assign unknown = undirected_G

```python
G, prev_cc = undirected_G
```

### Step 2: Assign edge = self.pick_add_edge(...)

```python
edge = self.pick_add_edge(G)
```

### Step 3: Assign num_nodes = len(...)

```python
num_nodes = len(prev_cc)
```

### Step 4: Call prev_cc.pop()

```python
prev_cc.pop(0)
```

### Step 5: Assign unknown = 0.5

```python
prev_cc[num_nodes] = 0.5
```

### Step 6: Call nx.incremental_closeness_centrality()

```python
nx.incremental_closeness_centrality(G, edge, prev_cc, insertion=True)
```


## Complete Example

```python
# Setup
# Fixtures: undirected_G

# Workflow
G, prev_cc = undirected_G
edge = self.pick_add_edge(G)
num_nodes = len(prev_cc)
prev_cc.pop(0)
prev_cc[num_nodes] = 0.5
with pytest.raises(nx.NetworkXError):
    nx.incremental_closeness_centrality(G, edge, prev_cc, insertion=True)
```

## Next Steps


---

*Source: test_closeness_centrality.py:228 | Complexity: Intermediate | Last updated: 2026-06-02*