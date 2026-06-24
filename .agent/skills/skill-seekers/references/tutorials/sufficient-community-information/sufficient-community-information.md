# How To: Sufficient Community Information

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sufficient community information

## Prerequisites

**Required Modules:**
- `math`
- `functools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
```

### Step 3: Assign unknown = 0

```python
G.nodes[1]['community'] = 0
```

### Step 4: Assign unknown = 0

```python
G.nodes[2]['community'] = 0
```

### Step 5: Assign unknown = 0

```python
G.nodes[3]['community'] = 0
```

### Step 6: Assign unknown = 0

```python
G.nodes[4]['community'] = 0
```

### Step 7: Call self.test()

```python
self.test(G, [(1, 4)], [(1, 4, 1)])
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
G.nodes[1]['community'] = 0
G.nodes[2]['community'] = 0
G.nodes[3]['community'] = 0
G.nodes[4]['community'] = 0
self.test(G, [(1, 4)], [(1, 4, 1)])
```

## Next Steps


---

*Source: test_link_prediction.py:454 | Complexity: Intermediate | Last updated: 2026-06-02*