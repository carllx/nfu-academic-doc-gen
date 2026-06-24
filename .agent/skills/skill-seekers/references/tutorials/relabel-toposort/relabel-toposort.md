# How To: Relabel Toposort

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relabel toposort

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators.classic`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign K5 = nx.complete_graph(...)

```python
K5 = nx.complete_graph(4)
```

**Verification:**
```python
assert nx.is_isomorphic(K5, G)
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

**Verification:**
```python
assert nx.is_isomorphic(K5, G)
```

### Step 3: Assign G = nx.relabel_nodes(...)

```python
G = nx.relabel_nodes(G, {i: i + 1 for i in range(4)}, copy=False)
```

**Verification:**
```python
assert nx.is_isomorphic(K5, G)
```

### Step 4: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

### Step 5: Assign G = nx.relabel_nodes(...)

```python
G = nx.relabel_nodes(G, {i: i - 1 for i in range(4)}, copy=False)
```

**Verification:**
```python
assert nx.is_isomorphic(K5, G)
```


## Complete Example

```python
# Workflow
K5 = nx.complete_graph(4)
G = nx.complete_graph(4)
G = nx.relabel_nodes(G, {i: i + 1 for i in range(4)}, copy=False)
assert nx.is_isomorphic(K5, G)
G = nx.complete_graph(4)
G = nx.relabel_nodes(G, {i: i - 1 for i in range(4)}, copy=False)
assert nx.is_isomorphic(K5, G)
```

## Next Steps


---

*Source: test_relabel.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*