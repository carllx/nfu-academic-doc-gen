# How To: Same In Out Degrees No Candidate

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test same in out degrees no candidate

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.isomorphism.vf2pp`


## Step-by-Step Guide

### Step 1: Assign g1 = nx.DiGraph(...)

```python
g1 = nx.DiGraph([(4, 1), (4, 2), (3, 4), (5, 4), (6, 4)])
```

**Verification:**
```python
assert candidates == set()
```

### Step 2: Assign g2 = nx.DiGraph(...)

```python
g2 = nx.DiGraph([(1, 4), (2, 4), (3, 4), (4, 5), (4, 6)])
```

**Verification:**
```python
assert _find_candidates(u, gparams, sparams, g1_degree) == {4}
```

### Step 3: Assign l1 = dict(...)

```python
l1 = dict(g1.nodes(data=None, default=-1))
```

### Step 4: Assign l2 = dict(...)

```python
l2 = dict(g2.nodes(data=None, default=-1))
```

### Step 5: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(g1, g2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups({node: (in_degree, out_degree) for (node, in_degree), (_, out_degree) in zip(g2.in_degree(), g2.out_degree())}))
```

### Step 6: Assign g1_degree = value

```python
g1_degree = {n: (in_degree, out_degree) for (n, in_degree), (_, out_degree) in zip(g1.in_degree, g1.out_degree)}
```

### Step 7: Assign m = value

```python
m = {1: 1, 2: 2, 3: 3}
```

### Step 8: Assign m_rev = m.copy(...)

```python
m_rev = m.copy()
```

### Step 9: Assign T1_out = value

```python
T1_out = {4}
```

### Step 10: Assign T1_in = value

```python
T1_in = {4}
```

### Step 11: Assign T1_tilde = value

```python
T1_tilde = {5, 6}
```

### Step 12: Assign T2_out = value

```python
T2_out = {4}
```

### Step 13: Assign T2_in = value

```python
T2_in = {4}
```

### Step 14: Assign T2_tilde = value

```python
T2_tilde = {5, 6}
```

### Step 15: Assign sparams = _StateParameters(...)

```python
sparams = _StateParameters(m, m_rev, T1_out, T1_in, T1_tilde, None, T2_out, T2_in, T2_tilde, None)
```

### Step 16: Assign u = 4

```python
u = 4
```

### Step 17: Assign candidates = _find_candidates_Di(...)

```python
candidates = _find_candidates_Di(u, gparams, sparams, g1_degree)
```

**Verification:**
```python
assert candidates == set()
```


## Complete Example

```python
# Workflow
g1 = nx.DiGraph([(4, 1), (4, 2), (3, 4), (5, 4), (6, 4)])
g2 = nx.DiGraph([(1, 4), (2, 4), (3, 4), (4, 5), (4, 6)])
l1 = dict(g1.nodes(data=None, default=-1))
l2 = dict(g2.nodes(data=None, default=-1))
gparams = _GraphParameters(g1, g2, l1, l2, nx.utils.groups(l1), nx.utils.groups(l2), nx.utils.groups({node: (in_degree, out_degree) for (node, in_degree), (_, out_degree) in zip(g2.in_degree(), g2.out_degree())}))
g1_degree = {n: (in_degree, out_degree) for (n, in_degree), (_, out_degree) in zip(g1.in_degree, g1.out_degree)}
m = {1: 1, 2: 2, 3: 3}
m_rev = m.copy()
T1_out = {4}
T1_in = {4}
T1_tilde = {5, 6}
T2_out = {4}
T2_in = {4}
T2_tilde = {5, 6}
sparams = _StateParameters(m, m_rev, T1_out, T1_in, T1_tilde, None, T2_out, T2_in, T2_tilde, None)
u = 4
candidates = _find_candidates_Di(u, gparams, sparams, g1_degree)
assert candidates == set()
assert _find_candidates(u, gparams, sparams, g1_degree) == {4}
```

## Next Steps


---

*Source: test_vf2pp_helpers.py:915 | Complexity: Advanced | Last updated: 2026-06-02*