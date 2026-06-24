# How To: Is Triad

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests the is_triad function

## Prerequisites

**Required Modules:**
- `itertools`
- `collections`
- `random`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Tests the is_triad function'

```python
'Tests the is_triad function'
```

**Verification:**
```python
assert nx.is_triad(G2)
```

### Step 2: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

### Step 3: Assign G = G.to_directed(...)

```python
G = G.to_directed()
```

### Step 4: Assign nodes = sample(...)

```python
nodes = sample(sorted(G.nodes()), 3)
```

### Step 5: Assign G2 = G.subgraph(...)

```python
G2 = G.subgraph(nodes)
```

**Verification:**
```python
assert nx.is_triad(G2)
```


## Complete Example

```python
# Workflow
'Tests the is_triad function'
G = nx.karate_club_graph()
G = G.to_directed()
for i in range(100):
    nodes = sample(sorted(G.nodes()), 3)
    G2 = G.subgraph(nodes)
    assert nx.is_triad(G2)
```

## Next Steps


---

*Source: test_triads.py:38 | Complexity: Intermediate | Last updated: 2026-06-02*