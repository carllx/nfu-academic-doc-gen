# How To: Already Branching

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that a directed acyclic graph that is already a
branching produces an isomorphic branching as output.

## Prerequisites

**Required Modules:**
- `collections`
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests that a directed acyclic graph that is already a\n        branching produces an isomorphic branching as output.\n\n        '

```python
'Tests that a directed acyclic graph that is already a\n        branching produces an isomorphic branching as output.\n\n        '
```

**Verification:**
```python
assert nx.is_isomorphic(G, B)
```

### Step 2: Assign T1 = nx.balanced_tree(...)

```python
T1 = nx.balanced_tree(2, 2, create_using=nx.DiGraph())
```

### Step 3: Assign T2 = nx.balanced_tree(...)

```python
T2 = nx.balanced_tree(2, 2, create_using=nx.DiGraph())
```

### Step 4: Assign G = nx.disjoint_union(...)

```python
G = nx.disjoint_union(T1, T2)
```

### Step 5: Assign B = nx.dag_to_branching(...)

```python
B = nx.dag_to_branching(G)
```

**Verification:**
```python
assert nx.is_isomorphic(G, B)
```


## Complete Example

```python
# Workflow
'Tests that a directed acyclic graph that is already a\n        branching produces an isomorphic branching as output.\n\n        '
T1 = nx.balanced_tree(2, 2, create_using=nx.DiGraph())
T2 = nx.balanced_tree(2, 2, create_using=nx.DiGraph())
G = nx.disjoint_union(T1, T2)
B = nx.dag_to_branching(G)
assert nx.is_isomorphic(G, B)
```

## Next Steps


---

*Source: test_dag.py:750 | Complexity: Intermediate | Last updated: 2026-06-02*