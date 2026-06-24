# How To: Unaffected By Self Loops

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unaffected by self loops

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign graph = two_node_graph(...)

```python
graph = two_node_graph()
```

**Verification:**
```python
assert verify_clique(graph, clique, weight, 30, 'weight')
```

### Step 2: Call graph.add_edge()

```python
graph.add_edge(1, 1)
```

**Verification:**
```python
assert verify_clique(graph, clique, weight, 20, 'weight')
```

### Step 3: Call graph.add_edge()

```python
graph.add_edge(2, 2)
```

### Step 4: Assign unknown = nx.algorithms.max_weight_clique(...)

```python
clique, weight = nx.algorithms.max_weight_clique(graph, 'weight')
```

**Verification:**
```python
assert verify_clique(graph, clique, weight, 30, 'weight')
```

### Step 5: Assign graph = three_node_independent_set(...)

```python
graph = three_node_independent_set()
```

### Step 6: Call graph.add_edge()

```python
graph.add_edge(1, 1)
```

### Step 7: Assign unknown = nx.algorithms.max_weight_clique(...)

```python
clique, weight = nx.algorithms.max_weight_clique(graph, 'weight')
```

**Verification:**
```python
assert verify_clique(graph, clique, weight, 20, 'weight')
```


## Complete Example

```python
# Workflow
graph = two_node_graph()
graph.add_edge(1, 1)
graph.add_edge(2, 2)
clique, weight = nx.algorithms.max_weight_clique(graph, 'weight')
assert verify_clique(graph, clique, weight, 30, 'weight')
graph = three_node_independent_set()
graph.add_edge(1, 1)
clique, weight = nx.algorithms.max_weight_clique(graph, 'weight')
assert verify_clique(graph, clique, weight, 20, 'weight')
```

## Next Steps


---

*Source: test_max_weight_clique.py:32 | Complexity: Intermediate | Last updated: 2026-06-02*