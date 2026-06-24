# How To: Multipartite Layout Layer Order

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Return the layers in sorted order if the layers of the multipartite
graph are sortable. See gh-5691

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: 'Return the layers in sorted order if the layers of the multipartite\n    graph are sortable. See gh-5691'

```python
'Return the layers in sorted order if the layers of the multipartite\n    graph are sortable. See gh-5691'
```

**Verification:**
```python
assert n1 == n2 and (p1 == p2).all()
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert pos['a'][-1] == pos['d'][-1]
```

### Step 3: Assign node_group = dict(...)

```python
node_group = dict(zip(('a', 'b', 'c', 'd', 'e'), (2, 3, 1, 2, 4)))
```

**Verification:**
```python
assert pos['c'][-1] < pos['a'][-1] < pos['b'][-1] < pos['e'][-1]
```

### Step 4: Assign pos = nx.multipartite_layout(...)

```python
pos = nx.multipartite_layout(G, align='horizontal')
```

**Verification:**
```python
assert pos_nosort.keys() == pos.keys()
```

### Step 5: Assign layers = nx.utils.groups(...)

```python
layers = nx.utils.groups(node_group)
```

### Step 6: Assign pos_from_layers = nx.multipartite_layout(...)

```python
pos_from_layers = nx.multipartite_layout(G, align='horizontal', subset_key=layers)
```

**Verification:**
```python
assert pos['a'][-1] == pos['d'][-1]
```

### Step 7: Assign unknown = 'layer_0'

```python
G.nodes['a']['subset'] = 'layer_0'
```

### Step 8: Assign pos_nosort = nx.multipartite_layout(...)

```python
pos_nosort = nx.multipartite_layout(G)
```

**Verification:**
```python
assert pos_nosort.keys() == pos.keys()
```

### Step 9: Call G.add_node()

```python
G.add_node(node, subset=layer)
```

**Verification:**
```python
assert n1 == n2 and (p1 == p2).all()
```


## Complete Example

```python
# Workflow
'Return the layers in sorted order if the layers of the multipartite\n    graph are sortable. See gh-5691'
G = nx.Graph()
node_group = dict(zip(('a', 'b', 'c', 'd', 'e'), (2, 3, 1, 2, 4)))
for node, layer in node_group.items():
    G.add_node(node, subset=layer)
pos = nx.multipartite_layout(G, align='horizontal')
layers = nx.utils.groups(node_group)
pos_from_layers = nx.multipartite_layout(G, align='horizontal', subset_key=layers)
for (n1, p1), (n2, p2) in zip(pos.items(), pos_from_layers.items()):
    assert n1 == n2 and (p1 == p2).all()
assert pos['a'][-1] == pos['d'][-1]
assert pos['c'][-1] < pos['a'][-1] < pos['b'][-1] < pos['e'][-1]
G.nodes['a']['subset'] = 'layer_0'
pos_nosort = nx.multipartite_layout(G)
assert pos_nosort.keys() == pos.keys()
```

## Next Steps


---

*Source: test_layout.py:494 | Complexity: Advanced | Last updated: 2026-06-02*