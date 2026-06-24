# How To: Weight Function

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that a callable weight is interpreted as a weight
function instead of an edge attribute.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `random`


## Step-by-Step Guide

### Step 1: 'Tests that a callable weight is interpreted as a weight\n        function instead of an edge attribute.\n\n        '

```python
'Tests that a callable weight is interpreted as a weight\n        function instead of an edge attribute.\n\n        '
```

**Verification:**
```python
assert distance == 2
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(3)
```

**Verification:**
```python
assert path == [0, 1, 2]
```

### Step 3: Assign unknown = 10

```python
G.adj[0][2]['weight'] = 10
```

**Verification:**
```python
assert distance == 1 / 10
```

### Step 4: Assign unknown = 1

```python
G.adj[0][1]['weight'] = 1
```

**Verification:**
```python
assert path == [0, 2]
```

### Step 5: Assign unknown = 1

```python
G.adj[1][2]['weight'] = 1
```

### Step 6: Assign unknown = nx.single_source_dijkstra(...)

```python
distance, path = nx.single_source_dijkstra(G, 0, 2)
```

**Verification:**
```python
assert distance == 2
```

### Step 7: Assign unknown = nx.single_source_dijkstra(...)

```python
distance, path = nx.single_source_dijkstra(G, 0, 2, weight=weight)
```

**Verification:**
```python
assert distance == 1 / 10
```


## Complete Example

```python
# Workflow
'Tests that a callable weight is interpreted as a weight\n        function instead of an edge attribute.\n\n        '
G = nx.complete_graph(3)
G.adj[0][2]['weight'] = 10
G.adj[0][1]['weight'] = 1
G.adj[1][2]['weight'] = 1

def weight(u, v, d):
    return 1 / d['weight']
distance, path = nx.single_source_dijkstra(G, 0, 2)
assert distance == 2
assert path == [0, 1, 2]
distance, path = nx.single_source_dijkstra(G, 0, 2, weight=weight)
assert distance == 1 / 10
assert path == [0, 2]
```

## Next Steps


---

*Source: test_weighted.py:358 | Complexity: Intermediate | Last updated: 2026-06-02*