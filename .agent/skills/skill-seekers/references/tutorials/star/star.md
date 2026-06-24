# How To: Star

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Approximate current-flow betweenness centrality: star

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Approximate current-flow betweenness centrality: star'

```python
'Approximate current-flow betweenness centrality: star'
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call nx.add_star()

```python
nx.add_star(G, ['a', 'b', 'c', 'd'])
```

### Step 4: Assign b = nx.current_flow_betweenness_centrality(...)

```python
b = nx.current_flow_betweenness_centrality(G, normalized=True)
```

### Step 5: Assign epsilon = 0.1

```python
epsilon = 0.1
```

### Step 6: Assign ba = approximate_cfbc(...)

```python
ba = approximate_cfbc(G, normalized=True, epsilon=0.5 * epsilon)
```

### Step 7: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(b[n], ba[n], atol=epsilon)
```


## Complete Example

```python
# Workflow
'Approximate current-flow betweenness centrality: star'
G = nx.Graph()
nx.add_star(G, ['a', 'b', 'c', 'd'])
b = nx.current_flow_betweenness_centrality(G, normalized=True)
epsilon = 0.1
ba = approximate_cfbc(G, normalized=True, epsilon=0.5 * epsilon)
for n in sorted(G):
    np.testing.assert_allclose(b[n], ba[n], atol=epsilon)
```

## Next Steps


---

*Source: test_current_flow_betweenness_centrality.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*