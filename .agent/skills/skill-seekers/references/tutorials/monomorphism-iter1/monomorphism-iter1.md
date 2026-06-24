# How To: Monomorphism Iter1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test monomorphism iter1

## Prerequisites

**Required Modules:**
- `importlib.resources`
- `random`
- `struct`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.generators`


## Step-by-Step Guide

### Step 1: Assign g1 = nx.DiGraph(...)

```python
g1 = nx.DiGraph(['AB', 'BC', 'CA'])
```

**Verification:**
```python
assert {'A': 'X', 'B': 'Y', 'C': 'Z'} in x
```

### Step 2: Assign g2 = nx.DiGraph(...)

```python
g2 = nx.DiGraph(['XY', 'YZ'])
```

**Verification:**
```python
assert {'A': 'Y', 'B': 'Z', 'C': 'X'} in x
```

### Step 3: Assign gm12 = iso.DiGraphMatcher(...)

```python
gm12 = iso.DiGraphMatcher(g1, g2)
```

**Verification:**
```python
assert {'A': 'Z', 'B': 'X', 'C': 'Y'} in x
```

### Step 4: Assign x = list(...)

```python
x = list(gm12.subgraph_monomorphisms_iter())
```

**Verification:**
```python
assert len(x) == 3
```

### Step 5: Assign gm21 = iso.DiGraphMatcher(...)

```python
gm21 = iso.DiGraphMatcher(g2, g1)
```

**Verification:**
```python
assert not gm21.subgraph_is_monomorphic()
```


## Complete Example

```python
# Workflow
g1 = nx.DiGraph(['AB', 'BC', 'CA'])
g2 = nx.DiGraph(['XY', 'YZ'])
gm12 = iso.DiGraphMatcher(g1, g2)
x = list(gm12.subgraph_monomorphisms_iter())
assert {'A': 'X', 'B': 'Y', 'C': 'Z'} in x
assert {'A': 'Y', 'B': 'Z', 'C': 'X'} in x
assert {'A': 'Z', 'B': 'X', 'C': 'Y'} in x
assert len(x) == 3
gm21 = iso.DiGraphMatcher(g2, g1)
assert not gm21.subgraph_is_monomorphic()
```

## Next Steps


---

*Source: test_isomorphvf2.py:360 | Complexity: Intermediate | Last updated: 2026-06-02*