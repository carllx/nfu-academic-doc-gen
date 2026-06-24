# How To: Dfs Tree

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dfs tree

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign exp_nodes = sorted(...)

```python
exp_nodes = sorted(self.G.nodes())
```

**Verification:**
```python
assert sorted(T.nodes()) == exp_nodes
```

### Step 2: Assign exp_edges = value

```python
exp_edges = [(0, 1), (1, 2), (1, 3), (2, 4)]
```

**Verification:**
```python
assert sorted(T.edges()) == exp_edges
```

### Step 3: Assign T = nx.dfs_tree(...)

```python
T = nx.dfs_tree(self.G, source=0)
```

**Verification:**
```python
assert sorted(T.nodes()) == exp_nodes
```

### Step 4: Assign T = nx.dfs_tree(...)

```python
T = nx.dfs_tree(self.G, source=None)
```

**Verification:**
```python
assert sorted(T.edges()) == exp_edges
```

### Step 5: Assign T = nx.dfs_tree(...)

```python
T = nx.dfs_tree(self.G)
```

**Verification:**
```python
assert sorted(T.nodes()) == exp_nodes
```


## Complete Example

```python
# Workflow
exp_nodes = sorted(self.G.nodes())
exp_edges = [(0, 1), (1, 2), (1, 3), (2, 4)]
T = nx.dfs_tree(self.G, source=0)
assert sorted(T.nodes()) == exp_nodes
assert sorted(T.edges()) == exp_edges
T = nx.dfs_tree(self.G, source=None)
assert sorted(T.nodes()) == exp_nodes
assert sorted(T.edges()) == exp_edges
T = nx.dfs_tree(self.G)
assert sorted(T.nodes()) == exp_nodes
assert sorted(T.edges()) == exp_edges
```

## Next Steps


---

*Source: test_dfs.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*