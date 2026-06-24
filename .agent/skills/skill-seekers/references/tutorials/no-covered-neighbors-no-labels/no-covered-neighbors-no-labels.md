# How To: No Covered Neighbors No Labels

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no covered neighbors no labels

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
assert candidates == {self.mapped[u], self.mapped[8], self.mapped[3], self.mapped[9]}
```

### Step 4: Assign G2 = nx.relabel_nodes(...)

```python
G2 = nx.relabel_nodes(G1, self.mapped)
```

### Step 5: Assign G1_degree = dict(...)

```python
G1_degree = dict(G1.degree)
```

### Step 6: Assign l1 = dict(...)

```python
l1 = dict(G1.nodes(data='label', default=-1))
```

### Step 7: Assign l2 = dict(...)

```python
l2 = dict(G2.nodes(data='label', default=-1))
```

### Step 8: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
```

### Step 9: Assign m = value

```python
m = {9: self.mapped[9], 1: self.mapped[1]}
```

### Step 10: Assign m_rev = value

```python
m_rev = {self.mapped[9]: 9, self.mapped[1]: 1}
```

### Step 11: Assign T1 = value

```python
T1 = {7, 8, 2, 4, 5}
```

### Step 12: Assign T1_tilde = value

```python
T1_tilde = {0, 3, 6}
```

### Step 13: Assign T2 = value

```python
T2 = {'g', 'h', 'b', 'd', 'e'}
```

### Step 14: Assign T2_tilde = value

```python
T2_tilde = {'x', 'c', 'f'}
```

### Step 15: Assign sparams = _StateParameters(...)

```python
sparams = _StateParameters(m, m_rev, T1, None, T1_tilde, None, T2, None, T2_tilde, None)
```

### Step 16: Assign u = 3

```python
u = 3
```

### Step 17: Assign candidates = _find_candidates(...)

```python
candidates = _find_candidates(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u]}
```

### Step 18: Assign u = 0

```python
u = 0
```

### Step 19: Assign candidates = _find_candidates(...)

```python
candidates = _find_candidates(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u]}
```

### Step 20: Call m.pop()

```python
m.pop(9)
```

### Step 21: Call m_rev.pop()

```python
m_rev.pop(self.mapped[9])
```

### Step 22: Assign T1 = value

```python
T1 = {2, 4, 5, 6}
```

### Step 23: Assign T1_tilde = value

```python
T1_tilde = {0, 3, 7, 8, 9}
```

### Step 24: Assign T2 = value

```python
T2 = {'g', 'h', 'b', 'd', 'e', 'f'}
```

### Step 25: Assign T2_tilde = value

```python
T2_tilde = {'x', 'c', 'g', 'h', 'i'}
```

### Step 26: Assign sparams = _StateParameters(...)

```python
sparams = _StateParameters(m, m_rev, T1, None, T1_tilde, None, T2, None, T2_tilde, None)
```

### Step 27: Assign u = 7

```python
u = 7
```

### Step 28: Assign candidates = _find_candidates(...)

```python
candidates = _find_candidates(u, gparams, sparams, G1_degree)
```

**Verification:**
```python
assert candidates == {self.mapped[u], self.mapped[8], self.mapped[3], self.mapped[9]}
```


## Complete Example

```python
# Workflow
G1 = nx.Graph()
G1.add_edges_from(self.G1_edges)
G1.add_node(0)
G2 = nx.relabel_nodes(G1, self.mapped)
G1_degree = dict(G1.degree)
l1 = dict(G1.nodes(data='label', default=-1))
l2 = dict(G2.nodes(data='label', default=-1))
gparams = _GraphParameters(G1, G2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups(dict(G2.degree())))
m = {9: self.mapped[9], 1: self.mapped[1]}
m_rev = {self.mapped[9]: 9, self.mapped[1]: 1}
T1 = {7, 8, 2, 4, 5}
T1_tilde = {0, 3, 6}
T2 = {'g', 'h', 'b', 'd', 'e'}
T2_tilde = {'x', 'c', 'f'}
sparams = _StateParameters(m, m_rev, T1, None, T1_tilde, None, T2, None, T2_tilde, None)
u = 3
candidates = _find_candidates(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u]}
u = 0
candidates = _find_candidates(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u]}
m.pop(9)
m_rev.pop(self.mapped[9])
T1 = {2, 4, 5, 6}
T1_tilde = {0, 3, 7, 8, 9}
T2 = {'g', 'h', 'b', 'd', 'e', 'f'}
T2_tilde = {'x', 'c', 'g', 'h', 'i'}
sparams = _StateParameters(m, m_rev, T1, None, T1_tilde, None, T2, None, T2_tilde, None)
u = 7
candidates = _find_candidates(u, gparams, sparams, G1_degree)
assert candidates == {self.mapped[u], self.mapped[8], self.mapped[3], self.mapped[9]}
```

## Next Steps


---

*Source: test_vf2pp_helpers.py:206 | Complexity: Advanced | Last updated: 2026-06-02*