# How To: Grid

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Approximate current-flow betweenness centrality: 2d grid

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Approximate current-flow betweenness centrality: 2d grid'

```python
'Approximate current-flow betweenness centrality: 2d grid'
```

### Step 2: Assign G = nx.grid_2d_graph(...)

```python
G = nx.grid_2d_graph(4, 4)
```

### Step 3: Assign b = nx.current_flow_betweenness_centrality(...)

```python
b = nx.current_flow_betweenness_centrality(G, normalized=True)
```

### Step 4: Assign epsilon = 0.1

```python
epsilon = 0.1
```

### Step 5: Assign ba = approximate_cfbc(...)

```python
ba = approximate_cfbc(G, normalized=True, epsilon=0.5 * epsilon)
```

### Step 6: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(b[n], ba[n], atol=epsilon)
```


## Complete Example

```python
# Workflow
'Approximate current-flow betweenness centrality: 2d grid'
G = nx.grid_2d_graph(4, 4)
b = nx.current_flow_betweenness_centrality(G, normalized=True)
epsilon = 0.1
ba = approximate_cfbc(G, normalized=True, epsilon=0.5 * epsilon)
for n in sorted(G):
    np.testing.assert_allclose(b[n], ba[n], atol=epsilon)
```

## Next Steps


---

*Source: test_current_flow_betweenness_centrality.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*