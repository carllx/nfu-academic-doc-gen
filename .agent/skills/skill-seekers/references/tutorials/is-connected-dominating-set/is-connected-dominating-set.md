# How To: Is Connected Dominating Set

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is connected dominating set

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4)
```

**Verification:**
```python
assert nx.is_connected_dominating_set(G, D)
```

### Step 2: Assign D = value

```python
D = {1, 2}
```

**Verification:**
```python
assert not nx.is_connected_dominating_set(G, D)
```

### Step 3: Assign D = value

```python
D = {1, 3}
```

**Verification:**
```python
assert nx.is_connected(nx.subgraph(G, D))
```

### Step 4: Assign D = value

```python
D = {2, 3}
```

**Verification:**
```python
assert not nx.is_connected_dominating_set(G, D)
```


## Complete Example

```python
# Workflow
G = nx.path_graph(4)
D = {1, 2}
assert nx.is_connected_dominating_set(G, D)
D = {1, 3}
assert not nx.is_connected_dominating_set(G, D)
D = {2, 3}
assert nx.is_connected(nx.subgraph(G, D))
assert not nx.is_connected_dominating_set(G, D)
```

## Next Steps


---

*Source: test_dominating.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*