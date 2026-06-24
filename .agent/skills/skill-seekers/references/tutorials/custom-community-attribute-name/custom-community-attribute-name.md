# How To: Custom Community Attribute Name

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom community attribute name

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
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])
```

### Step 3: Assign unknown = 0

```python
G.nodes[0]['cmty'] = 0
```

### Step 4: Assign unknown = 0

```python
G.nodes[1]['cmty'] = 0
```

### Step 5: Assign unknown = 0

```python
G.nodes[2]['cmty'] = 0
```

### Step 6: Assign unknown = 1

```python
G.nodes[3]['cmty'] = 1
```

### Step 7: Call self.test()

```python
self.test(G, [(0, 3)], [(0, 3, 2)], community='cmty')
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])
G.nodes[0]['cmty'] = 0
G.nodes[1]['cmty'] = 0
G.nodes[2]['cmty'] = 0
G.nodes[3]['cmty'] = 1
self.test(G, [(0, 3)], [(0, 3, 2)], community='cmty')
```

## Next Steps


---

*Source: test_link_prediction.py:348 | Complexity: Intermediate | Last updated: 2026-06-02*