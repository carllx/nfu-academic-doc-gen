# How To: Covered Neighbors No Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test covered neighbors no labels

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.isomorphism.vf2pp`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.DiGraph(...)

```python
G1 = nx.DiGraph()
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

### Step 5: Assign G1_degree = value

```python
G1_degree = {n: (in_degree, out_degree) for (n, in_degree), (_, out_degree) in zip(G1.in_degree, G1.out_degree)}
```

### Step 6: Assign l1 = dict(...)

```python
l1 = dict(G1.nodes(data=None, default=-1))
```

### Step 7: Assign l2 = dict(...)

```python
l2 = dict(G2.nodes(data=None, default=-1))
```

### Step 8: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups({node: (in_degree, out_degree) for (node, in_degree), (_, out_degree) in zip(G2.in_degree(), G2.out_degree())}))
```

### Step 9: Assign m = value

```python
m = {9: self.mapped[9], 1: self.mapped[1]}
```

### Step 10: Assign m_rev = value

```python
m_rev = {self.mapped[9]: 9, self.mapped[1]: 1}
```

### Step 11: Assign T1_out = value

```python
T1_out = {2, 4, 6}
```

### Step 12: Assign T1_in = value

```python
T1_in = {5, 7, 8}
```

### Step 13: Assign T1_tilde = value

```python
T1_tilde = {0, 3}
```

### Step 14: Assign T2_out = value

```python
T2_out = {'b', 'd', 'f'}
```

### Step 15: Assign T2_in = value

```python
T2_in = {'e', 'g', 'h'}
```

### Step 16: Assign T2_tilde = value

```python
T2_tilde = {'x', 'c'}
```

### Step 17: Assign sparams = _StateParameters(...)

```python
sparams = _StateParameters(m, m_rev, T1_out, T1_in, T1_tilde, None, T2_out, T2_in, T2_tilde, None)
```

### Step 18: Assign u = 5

```python
u = 5
```

### Step 19: Assign candidates = _find_candidates_Di(...)

```python
candidates = _find_candidates_Di(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u]}
```

### Step 20: Assign u = 6

```python
u = 6
```

### Step 21: Assign candidates = _find_candidates_Di(...)

```python
candidates = _find_candidates_Di(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u]}
```

### Step 22: Call G1.remove_edge()

```python
G1.remove_edge(4, 2)
```

### Step 23: Call G1.add_edge()

```python
G1.add_edge(2, 4)
```

### Step 24: Call G2.remove_edge()

```python
G2.remove_edge('d', 'b')
```

### Step 25: Call G2.add_edge()

```python
G2.add_edge('b', 'd')
```

### Step 26: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups({node: (in_degree, out_degree) for (node, in_degree), (_, out_degree) in zip(G2.in_degree(), G2.out_degree())}))
```

### Step 27: Assign candidates = _find_candidates_Di(...)

```python
candidates = _find_candidates_Di(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u], self.mapped[2]}
```


## Complete Example

```python
# Workflow
G1 = nx.DiGraph()
G1.add_edges_from(self.G1_edges)
G1.add_node(0)
G2 = nx.relabel_nodes(G1, self.mapped)
G1_degree = {n: (in_degree, out_degree) for (n, in_degree), (_, out_degree) in zip(G1.in_degree, G1.out_degree)}
l1 = dict(G1.nodes(data=None, default=-1))
l2 = dict(G2.nodes(data=None, default=-1))
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups({node: (in_degree, out_degree) for (node, in_degree), (_, out_degree) in zip(G2.in_degree(), G2.out_degree())}))
m = {9: self.mapped[9], 1: self.mapped[1]}
m_rev = {self.mapped[9]: 9, self.mapped[1]: 1}
T1_out = {2, 4, 6}
T1_in = {5, 7, 8}
T1_tilde = {0, 3}
T2_out = {'b', 'd', 'f'}
T2_in = {'e', 'g', 'h'}
T2_tilde = {'x', 'c'}
sparams = _StateParameters(m, m_rev, T1_out, T1_in, T1_tilde, None, T2_out, T2_in, T2_tilde, None)
u = 5
candidates = _find_candidates_Di(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u]}
u = 6
candidates = _find_candidates_Di(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u]}
G1.remove_edge(4, 2)
G1.add_edge(2, 4)
G2.remove_edge('d', 'b')
G2.add_edge('b', 'd')
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups({node: (in_degree, out_degree) for (node, in_degree), (_, out_degree) in zip(G2.in_degree(), G2.out_degree())}))
candidates = _find_candidates_Di(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u], self.mapped[2]}
```

## Next Steps


---

*Source: test_vf2pp_helpers.py:714 | Complexity: Advanced | Last updated: 2026-06-02*