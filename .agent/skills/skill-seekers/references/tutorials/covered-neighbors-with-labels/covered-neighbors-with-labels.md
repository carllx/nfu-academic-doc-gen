# How To: Covered Neighbors With Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test covered neighbors with labels

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.isomorphism.vf2pp`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph()
```

**Verification:**
```python
assert candidates == {self.mapped[u]}
```

### Step 2: Call G1.add_edges_from()

```python
G1.add_edges_from(self.G1_edges)
```

**Verification:**
```python
assert candidates == {self.mapped[u]}
```

### Step 3: Call G1.add_node()

```python
G1.add_node(0)
```

**Verification:**
```python
assert candidates == {self.mapped[u], self.mapped[2]}
```

### Step 4: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, self.mapped)
```

### Step 5: Assign G1_degree = dict(...)

```python
G1_degree = dict(G1.degree)
```

### Step 6: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_many))), 'label')
```

### Step 7: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G2, dict(zip([self.mapped[n] for n in G1], it.cycle(labels_many))), 'label')
```

### Step 8: Assign l1 = dict(...)

```python
l1 = dict(G1.nodes(data='label', default=-1))
```

### Step 9: Assign l2 = dict(...)

```python
l2 = dict(G2.nodes(data='label', default=-1))
```

### Step 10: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
```

### Step 11: Assign m = value

```python
m = {9: self.mapped[9], 1: self.mapped[1]}
```

### Step 12: Assign m_rev = value

```python
m_rev = {self.mapped[9]: 9, self.mapped[1]: 1}
```

### Step 13: Assign T1 = value

```python
T1 = {7, 8, 2, 4, 5, 6}
```

### Step 14: Assign T1_tilde = value

```python
T1_tilde = {0, 3}
```

### Step 15: Assign T2 = value

```python
T2 = {'g', 'h', 'b', 'd', 'e', 'f'}
```

### Step 16: Assign T2_tilde = value

```python
T2_tilde = {'x', 'c'}
```

### Step 17: Assign sparams = _StateParameters(...)

```python
sparams = _StateParameters(m, m_rev, T1, None, T1_tilde, None, T2, None, T2_tilde, None)
```

### Step 18: Assign u = 5

```python
u = 5
```

### Step 19: Assign candidates = _find_candidates(...)

```python
candidates = _find_candidates(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u]}
```

### Step 20: Assign u = 6

```python
u = 6
```

### Step 21: Assign candidates = _find_candidates(...)

```python
candidates = _find_candidates(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u]}
```

### Step 22: Assign unknown = value

```python
G1.nodes[2]['label'] = G1.nodes[u]['label']
```

### Step 23: Assign unknown = value

```python
G2.nodes[self.mapped[2]]['label'] = G1.nodes[u]['label']
```

### Step 24: Assign l1 = dict(...)

```python
l1 = dict(G1.nodes(data='label', default=-1))
```

### Step 25: Assign l2 = dict(...)

```python
l2 = dict(G2.nodes(data='label', default=-1))
```

### Step 26: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
```

### Step 27: Assign candidates = _find_candidates(...)

```python
candidates = _find_candidates(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u], self.mapped[2]}
```


## Complete Example

```python
# Workflow
G1 = nx.Graph()
G1.add_edges_from(self.G1_edges)
G1.add_node(0)
G2 = nx.relabel_nodes(G1, self.mapped)
G1_degree = dict(G1.degree)
nx.set_node_attributes(G1, dict(zip(G1, it.cycle(labels_many))), 'label')
nx.set_node_attributes(G2, dict(zip([self.mapped[n] for n in G1], it.cycle(labels_many))), 'label')
l1 = dict(G1.nodes(data='label', default=-1))
l2 = dict(G2.nodes(data='label', default=-1))
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
m = {9: self.mapped[9], 1: self.mapped[1]}
m_rev = {self.mapped[9]: 9, self.mapped[1]: 1}
T1 = {7, 8, 2, 4, 5, 6}
T1_tilde = {0, 3}
T2 = {'g', 'h', 'b', 'd', 'e', 'f'}
T2_tilde = {'x', 'c'}
sparams = _StateParameters(m, m_rev, T1, None, T1_tilde, None, T2, None, T2_tilde, None)
u = 5
candidates = _find_candidates(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u]}
u = 6
candidates = _find_candidates(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u]}
G1.nodes[2]['label'] = G1.nodes[u]['label']
G2.nodes[self.mapped[2]]['label'] = G1.nodes[u]['label']
l1 = dict(G1.nodes(data='label', default=-1))
l2 = dict(G2.nodes(data='label', default=-1))
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
candidates = _find_candidates(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u], self.mapped[2]}
```

## Next Steps


---

*Source: test_vf2pp_helpers.py:410 | Complexity: Advanced | Last updated: 2026-06-02*