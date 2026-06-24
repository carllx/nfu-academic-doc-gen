# How To: Isomorphism Iter1

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isomorphism iter1

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
g1 = nx.DiGraph(['AB', 'BC'])
```

**Verification:**
```python
assert {'A': 'Y', 'B': 'Z'} in x
```

### Step 2: Assign g2 = nx.DiGraph(...)

```python
g2 = nx.DiGraph(['YZ'])
```

**Verification:**
```python
assert {'B': 'Y', 'C': 'Z'} in x
```

### Step 3: Assign g3 = nx.DiGraph(...)

```python
g3 = nx.DiGraph(['ZY'])
```

**Verification:**
```python
assert {'A': 'Z', 'B': 'Y'} in y
```

### Step 4: Assign gm12 = iso.DiGraphMatcher(...)

```python
gm12 = iso.DiGraphMatcher(g1, g2)
```

**Verification:**
```python
assert {'B': 'Z', 'C': 'Y'} in y
```

### Step 5: Assign gm13 = iso.DiGraphMatcher(...)

```python
gm13 = iso.DiGraphMatcher(g1, g3)
```

**Verification:**
```python
assert len(x) == len(y)
```

### Step 6: Assign x = list(...)

```python
x = list(gm12.subgraph_isomorphisms_iter())
```

**Verification:**
```python
assert len(x) == 2
```

### Step 7: Assign y = list(...)

```python
y = list(gm13.subgraph_isomorphisms_iter())
```

**Verification:**
```python
assert {'A': 'Y', 'B': 'Z'} in x
```


## Complete Example

```python
# Workflow
g1 = nx.DiGraph(['AB', 'BC'])
g2 = nx.DiGraph(['YZ'])
g3 = nx.DiGraph(['ZY'])
gm12 = iso.DiGraphMatcher(g1, g2)
gm13 = iso.DiGraphMatcher(g1, g3)
x = list(gm12.subgraph_isomorphisms_iter())
y = list(gm13.subgraph_isomorphisms_iter())
assert {'A': 'Y', 'B': 'Z'} in x
assert {'B': 'Y', 'C': 'Z'} in x
assert {'A': 'Z', 'B': 'Y'} in y
assert {'B': 'Z', 'C': 'Y'} in y
assert len(x) == len(y)
assert len(x) == 2
```

## Next Steps


---

*Source: test_isomorphvf2.py:342 | Complexity: Intermediate | Last updated: 2026-06-02*