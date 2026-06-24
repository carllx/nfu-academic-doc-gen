# How To: Const Covered Neighbors

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test const covered neighbors

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
G1 = nx.Graph([(0, 1), (1, 2), (3, 0), (3, 2)])
```

**Verification:**
```python
assert _consistent_PT(u, v, gparams, sparams)
```

### Step 2: Assign G2 = nx.Graph(...)

```python
G2 = nx.Graph([('a', 'b'), ('b', 'c'), ('k', 'a'), ('k', 'c')])
```

### Step 3: Assign gparams = _GraphParameters(...)

```python
gparams = _GraphParameters(G1, G2, None, None, None, None, None)
```

### Step 4: Assign sparams = _StateParameters(...)

```python
sparams = _StateParameters({0: 'a', 1: 'b', 2: 'c'}, {'a': 0, 'b': 1, 'c': 2}, None, None, None, None, None, None, None, None)
```

### Step 5: Assign unknown = value

```python
u, v = (3, 'k')
```

**Verification:**
```python
assert _consistent_PT(u, v, gparams, sparams)
```


## Complete Example

```python
# Workflow
G1 = nx.Graph([(0, 1), (1, 2), (3, 0), (3, 2)])
G2 = nx.Graph([('a', 'b'), ('b', 'c'), ('k', 'a'), ('k', 'c')])
gparams = _GraphParameters(G1, G2, None, None, None, None, None)
sparams = _StateParameters({0: 'a', 1: 'b', 2: 'c'}, {'a': 0, 'b': 1, 'c': 2}, None, None, None, None, None, None, None, None)
u, v = (3, 'k')
assert _consistent_PT(u, v, gparams, sparams)
```

## Next Steps


---

*Source: test_vf2pp_helpers.py:966 | Complexity: Intermediate | Last updated: 2026-06-02*