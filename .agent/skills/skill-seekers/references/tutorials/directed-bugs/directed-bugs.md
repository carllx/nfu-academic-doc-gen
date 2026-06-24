# How To: Directed Bugs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: These were bugs for directed graphs as discussed in issue #7806

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n    These were bugs for directed graphs as discussed in issue #7806\n    '

```python
'\n    These were bugs for directed graphs as discussed in issue #7806\n    '
```

**Verification:**
```python
assert Ga_hash != Gb_hash
```

### Step 2: Assign Ga = nx.DiGraph(...)

```python
Ga = nx.DiGraph()
```

**Verification:**
```python
assert Tree1_hash_short == Tree2_hash_short
```

### Step 3: Assign Gb = nx.DiGraph(...)

```python
Gb = nx.DiGraph()
```

**Verification:**
```python
assert Tree1_hash != Tree2_hash
```

### Step 4: Call Ga.add_nodes_from()

```python
Ga.add_nodes_from([1, 2, 3, 4])
```

### Step 5: Call Gb.add_nodes_from()

```python
Gb.add_nodes_from([1, 2, 3, 4])
```

### Step 6: Call Ga.add_edges_from()

```python
Ga.add_edges_from([(1, 2), (3, 2)])
```

### Step 7: Call Gb.add_edges_from()

```python
Gb.add_edges_from([(1, 2), (3, 4)])
```

### Step 8: Assign Ga_hash = nx.weisfeiler_lehman_graph_hash(...)

```python
Ga_hash = nx.weisfeiler_lehman_graph_hash(Ga)
```

### Step 9: Assign Gb_hash = nx.weisfeiler_lehman_graph_hash(...)

```python
Gb_hash = nx.weisfeiler_lehman_graph_hash(Gb)
```

**Verification:**
```python
assert Ga_hash != Gb_hash
```

### Step 10: Assign Tree1 = nx.DiGraph(...)

```python
Tree1 = nx.DiGraph()
```

### Step 11: Call Tree1.add_edges_from()

```python
Tree1.add_edges_from([(0, 4), (1, 5), (2, 6), (3, 7)])
```

### Step 12: Call Tree1.add_edges_from()

```python
Tree1.add_edges_from([(4, 8), (5, 8), (6, 9), (7, 9)])
```

### Step 13: Call Tree1.add_edges_from()

```python
Tree1.add_edges_from([(8, 10), (9, 10)])
```

### Step 14: Call nx.set_node_attributes()

```python
nx.set_node_attributes(Tree1, {10: 's', 8: 'a', 9: 'a', 4: 'b', 5: 'b', 6: 'b', 7: 'b'}, 'weight')
```

### Step 15: Assign Tree2 = copy.deepcopy(...)

```python
Tree2 = copy.deepcopy(Tree1)
```

### Step 16: Call nx.set_node_attributes()

```python
nx.set_node_attributes(Tree1, {0: 'd', 1: 'c', 2: 'd', 3: 'c'}, 'weight')
```

### Step 17: Call nx.set_node_attributes()

```python
nx.set_node_attributes(Tree2, {0: 'd', 1: 'd', 2: 'c', 3: 'c'}, 'weight')
```

### Step 18: Assign Tree1_hash_short = nx.weisfeiler_lehman_graph_hash(...)

```python
Tree1_hash_short = nx.weisfeiler_lehman_graph_hash(Tree1, iterations=1, node_attr='weight')
```

### Step 19: Assign Tree2_hash_short = nx.weisfeiler_lehman_graph_hash(...)

```python
Tree2_hash_short = nx.weisfeiler_lehman_graph_hash(Tree2, iterations=1, node_attr='weight')
```

**Verification:**
```python
assert Tree1_hash_short == Tree2_hash_short
```

### Step 20: Assign Tree1_hash = nx.weisfeiler_lehman_graph_hash(...)

```python
Tree1_hash = nx.weisfeiler_lehman_graph_hash(Tree1, node_attr='weight')
```

### Step 21: Assign Tree2_hash = nx.weisfeiler_lehman_graph_hash(...)

```python
Tree2_hash = nx.weisfeiler_lehman_graph_hash(Tree2, node_attr='weight')
```

**Verification:**
```python
assert Tree1_hash != Tree2_hash
```


## Complete Example

```python
# Workflow
'\n    These were bugs for directed graphs as discussed in issue #7806\n    '
Ga = nx.DiGraph()
Gb = nx.DiGraph()
Ga.add_nodes_from([1, 2, 3, 4])
Gb.add_nodes_from([1, 2, 3, 4])
Ga.add_edges_from([(1, 2), (3, 2)])
Gb.add_edges_from([(1, 2), (3, 4)])
Ga_hash = nx.weisfeiler_lehman_graph_hash(Ga)
Gb_hash = nx.weisfeiler_lehman_graph_hash(Gb)
assert Ga_hash != Gb_hash
Tree1 = nx.DiGraph()
Tree1.add_edges_from([(0, 4), (1, 5), (2, 6), (3, 7)])
Tree1.add_edges_from([(4, 8), (5, 8), (6, 9), (7, 9)])
Tree1.add_edges_from([(8, 10), (9, 10)])
nx.set_node_attributes(Tree1, {10: 's', 8: 'a', 9: 'a', 4: 'b', 5: 'b', 6: 'b', 7: 'b'}, 'weight')
Tree2 = copy.deepcopy(Tree1)
nx.set_node_attributes(Tree1, {0: 'd', 1: 'c', 2: 'd', 3: 'c'}, 'weight')
nx.set_node_attributes(Tree2, {0: 'd', 1: 'd', 2: 'c', 3: 'c'}, 'weight')
Tree1_hash_short = nx.weisfeiler_lehman_graph_hash(Tree1, iterations=1, node_attr='weight')
Tree2_hash_short = nx.weisfeiler_lehman_graph_hash(Tree2, iterations=1, node_attr='weight')
assert Tree1_hash_short == Tree2_hash_short
Tree1_hash = nx.weisfeiler_lehman_graph_hash(Tree1, node_attr='weight')
Tree2_hash = nx.weisfeiler_lehman_graph_hash(Tree2, node_attr='weight')
assert Tree1_hash != Tree2_hash
```

## Next Steps


---

*Source: test_graph_hashing.py:281 | Complexity: Advanced | Last updated: 2026-06-02*