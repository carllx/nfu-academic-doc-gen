# How To: Empty Graph Hash

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: empty graphs should give hashes regardless of other params

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n    empty graphs should give hashes regardless of other params\n    '

```python
'\n    empty graphs should give hashes regardless of other params\n    '
```

**Verification:**
```python
assert h1 == h2
```

### Step 2: Assign G1 = nx.empty_graph(...)

```python
G1 = nx.empty_graph()
```

**Verification:**
```python
assert h1 == h3
```

### Step 3: Assign G2 = nx.empty_graph(...)

```python
G2 = nx.empty_graph()
```

**Verification:**
```python
assert h1 == h4
```

### Step 4: Assign h1 = nx.weisfeiler_lehman_graph_hash(...)

```python
h1 = nx.weisfeiler_lehman_graph_hash(G1)
```

**Verification:**
```python
assert h1 == h5
```

### Step 5: Assign h2 = nx.weisfeiler_lehman_graph_hash(...)

```python
h2 = nx.weisfeiler_lehman_graph_hash(G2)
```

**Verification:**
```python
assert h1 == h6
```

### Step 6: Assign h3 = nx.weisfeiler_lehman_graph_hash(...)

```python
h3 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr1')
```

### Step 7: Assign h4 = nx.weisfeiler_lehman_graph_hash(...)

```python
h4 = nx.weisfeiler_lehman_graph_hash(G2, node_attr='node_attr1')
```

### Step 8: Assign h5 = nx.weisfeiler_lehman_graph_hash(...)

```python
h5 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr1', node_attr='node_attr1')
```

### Step 9: Assign h6 = nx.weisfeiler_lehman_graph_hash(...)

```python
h6 = nx.weisfeiler_lehman_graph_hash(G2, iterations=10)
```

**Verification:**
```python
assert h1 == h2
```


## Complete Example

```python
# Workflow
'\n    empty graphs should give hashes regardless of other params\n    '
G1 = nx.empty_graph()
G2 = nx.empty_graph()
h1 = nx.weisfeiler_lehman_graph_hash(G1)
h2 = nx.weisfeiler_lehman_graph_hash(G2)
h3 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr1')
h4 = nx.weisfeiler_lehman_graph_hash(G2, node_attr='node_attr1')
h5 = nx.weisfeiler_lehman_graph_hash(G2, edge_attr='edge_attr1', node_attr='node_attr1')
h6 = nx.weisfeiler_lehman_graph_hash(G2, iterations=10)
assert h1 == h2
assert h1 == h3
assert h1 == h4
assert h1 == h5
assert h1 == h6
```

## Next Steps


---

*Source: test_graph_hashing.py:37 | Complexity: Advanced | Last updated: 2026-06-02*