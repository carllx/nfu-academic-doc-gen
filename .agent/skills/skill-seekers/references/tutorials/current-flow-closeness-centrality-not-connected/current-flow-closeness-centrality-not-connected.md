# How To: Current Flow Closeness Centrality Not Connected

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test current flow closeness centrality not connected

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Call G.add_nodes_from()

```python
G.add_nodes_from([1, 2, 3])
```

### Step 3: Call nx.current_flow_closeness_centrality()

```python
nx.current_flow_closeness_centrality(G)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
with pytest.raises(nx.NetworkXError):
    nx.current_flow_closeness_centrality(G)
```

## Next Steps


---

*Source: test_current_flow_closeness.py:35 | Complexity: Beginner | Last updated: 2026-06-02*