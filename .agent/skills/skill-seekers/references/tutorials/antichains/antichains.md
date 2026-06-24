# How To: Antichains

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test antichains

## Prerequisites

**Required Modules:**
- `collections`
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign antichains = value

```python
antichains = nx.algorithms.dag.antichains
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (2, 3), (3, 4)])
```

### Step 3: Assign solution = value

```python
solution = [[], [4], [3], [2], [1]]
```

### Step 4: Call self._check_antichains()

```python
self._check_antichains(list(antichains(G)), solution)
```

### Step 5: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (2, 3), (2, 4), (3, 5), (5, 6), (5, 7)])
```

### Step 6: Assign solution = value

```python
solution = [[], [4], [7], [7, 4], [6], [6, 4], [6, 7], [6, 7, 4], [5], [5, 4], [3], [3, 4], [2], [1]]
```

### Step 7: Call self._check_antichains()

```python
self._check_antichains(list(antichains(G)), solution)
```

### Step 8: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (1, 3), (3, 4), (3, 5), (5, 6)])
```

### Step 9: Assign solution = value

```python
solution = [[], [6], [5], [4], [4, 6], [4, 5], [3], [2], [2, 6], [2, 5], [2, 4], [2, 4, 6], [2, 4, 5], [2, 3], [1]]
```

### Step 10: Call self._check_antichains()

```python
self._check_antichains(list(antichains(G)), solution)
```

### Step 11: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph({0: [1, 2], 1: [4], 2: [3], 3: [4]})
```

### Step 12: Assign solution = value

```python
solution = [[], [4], [3], [2], [1], [1, 3], [1, 2], [0]]
```

### Step 13: Call self._check_antichains()

```python
self._check_antichains(list(antichains(G)), solution)
```

### Step 14: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 15: Call self._check_antichains()

```python
self._check_antichains(list(antichains(G)), [[]])
```

### Step 16: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 17: Call G.add_nodes_from()

```python
G.add_nodes_from([0, 1, 2])
```

### Step 18: Assign solution = value

```python
solution = [[], [0], [1], [1, 0], [2], [2, 0], [2, 1], [2, 1, 0]]
```

### Step 19: Call self._check_antichains()

```python
self._check_antichains(list(antichains(G)), solution)
```

### Step 20: Assign G = nx.Graph(...)

```python
G = nx.Graph([(1, 2), (2, 3), (3, 4)])
```

### Step 21: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, f, G)
```

### Step 22: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
```

### Step 23: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnfeasible, f, G)
```


## Complete Example

```python
# Workflow
antichains = nx.algorithms.dag.antichains
G = nx.DiGraph([(1, 2), (2, 3), (3, 4)])
solution = [[], [4], [3], [2], [1]]
self._check_antichains(list(antichains(G)), solution)
G = nx.DiGraph([(1, 2), (2, 3), (2, 4), (3, 5), (5, 6), (5, 7)])
solution = [[], [4], [7], [7, 4], [6], [6, 4], [6, 7], [6, 7, 4], [5], [5, 4], [3], [3, 4], [2], [1]]
self._check_antichains(list(antichains(G)), solution)
G = nx.DiGraph([(1, 2), (1, 3), (3, 4), (3, 5), (5, 6)])
solution = [[], [6], [5], [4], [4, 6], [4, 5], [3], [2], [2, 6], [2, 5], [2, 4], [2, 4, 6], [2, 4, 5], [2, 3], [1]]
self._check_antichains(list(antichains(G)), solution)
G = nx.DiGraph({0: [1, 2], 1: [4], 2: [3], 3: [4]})
solution = [[], [4], [3], [2], [1], [1, 3], [1, 2], [0]]
self._check_antichains(list(antichains(G)), solution)
G = nx.DiGraph()
self._check_antichains(list(antichains(G)), [[]])
G = nx.DiGraph()
G.add_nodes_from([0, 1, 2])
solution = [[], [0], [1], [1, 0], [2], [2, 0], [2, 1], [2, 1, 0]]
self._check_antichains(list(antichains(G)), solution)

def f(x):
    return list(antichains(x))
G = nx.Graph([(1, 2), (2, 3), (3, 4)])
pytest.raises(nx.NetworkXNotImplemented, f, G)
G = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
pytest.raises(nx.NetworkXUnfeasible, f, G)
```

## Next Steps


---

*Source: test_dag.py:478 | Complexity: Advanced | Last updated: 2026-06-02*