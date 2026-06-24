# How To: Disconnected Graph Root Node

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test for a single component of a disconnected graph.

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Test for a single component of a disconnected graph.'

```python
'Test for a single component of a disconnected graph.'
```

**Verification:**
```python
assert len(chains) == len(expected)
```

### Step 2: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(3, 0)
```

### Step 3: Assign H = nx.barbell_graph(...)

```python
H = nx.barbell_graph(3, 0)
```

### Step 4: Assign mapping = dict(...)

```python
mapping = dict(zip(range(6), 'abcdef'))
```

### Step 5: Call nx.relabel_nodes()

```python
nx.relabel_nodes(H, mapping, copy=False)
```

### Step 6: Assign G = nx.union(...)

```python
G = nx.union(G, H)
```

### Step 7: Assign chains = list(...)

```python
chains = list(nx.chain_decomposition(G, root='a'))
```

### Step 8: Assign expected = value

```python
expected = [[('a', 'b'), ('b', 'c'), ('c', 'a')], [('d', 'e'), ('e', 'f'), ('f', 'd')]]
```

**Verification:**
```python
assert len(chains) == len(expected)
```

### Step 9: Call self.assertContainsChain()

```python
self.assertContainsChain(chain, expected)
```


## Complete Example

```python
# Workflow
'Test for a single component of a disconnected graph.'
G = nx.barbell_graph(3, 0)
H = nx.barbell_graph(3, 0)
mapping = dict(zip(range(6), 'abcdef'))
nx.relabel_nodes(H, mapping, copy=False)
G = nx.union(G, H)
chains = list(nx.chain_decomposition(G, root='a'))
expected = [[('a', 'b'), ('b', 'c'), ('c', 'a')], [('d', 'e'), ('e', 'f'), ('f', 'd')]]
assert len(chains) == len(expected)
for chain in chains:
    self.assertContainsChain(chain, expected)
```

## Next Steps


---

*Source: test_chains.py:115 | Complexity: Advanced | Last updated: 2026-06-02*