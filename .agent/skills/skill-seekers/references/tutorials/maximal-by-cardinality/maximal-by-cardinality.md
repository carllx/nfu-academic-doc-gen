# How To: Maximal By Cardinality

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the maximal clique is computed according to maximum
cardinality of the sets.

For more information, see pull request #1531.

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.algorithms.approximation`


## Step-by-Step Guide

### Step 1: 'Tests that the maximal clique is computed according to maximum\n        cardinality of the sets.\n\n        For more information, see pull request #1531.\n\n        '

```python
'Tests that the maximal clique is computed according to maximum\n        cardinality of the sets.\n\n        For more information, see pull request #1531.\n\n        '
```

**Verification:**
```python
assert len(clique) > 1
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert len(clique) > 2
```

### Step 3: Call G.add_edge()

```python
G.add_edge(4, 5)
```

### Step 4: Assign clique = max_clique(...)

```python
clique = max_clique(G)
```

**Verification:**
```python
assert len(clique) > 1
```

### Step 5: Assign G = nx.lollipop_graph(...)

```python
G = nx.lollipop_graph(30, 2)
```

### Step 6: Assign clique = max_clique(...)

```python
clique = max_clique(G)
```

**Verification:**
```python
assert len(clique) > 2
```


## Complete Example

```python
# Workflow
'Tests that the maximal clique is computed according to maximum\n        cardinality of the sets.\n\n        For more information, see pull request #1531.\n\n        '
G = nx.complete_graph(5)
G.add_edge(4, 5)
clique = max_clique(G)
assert len(clique) > 1
G = nx.lollipop_graph(30, 2)
clique = max_clique(G)
assert len(clique) > 2
```

## Next Steps


---

*Source: test_clique.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*