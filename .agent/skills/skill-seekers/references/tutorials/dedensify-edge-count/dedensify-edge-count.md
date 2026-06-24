# How To: Dedensify Edge Count

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Verifies that dedensify produced the correct number of edges in an
undirected graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n        Verifies that dedensify produced the correct number of edges in an\n        undirected graph\n        '

```python
'\n        Verifies that dedensify produced the correct number of edges in an\n        undirected graph\n        '
```

**Verification:**
```python
assert compressed_edge_count <= verified_original_edge_count
```

### Step 2: Assign G = self.build_original_graph(...)

```python
G = self.build_original_graph()
```

**Verification:**
```python
assert compressed_edge_count == verified_compressed_edge_count
```

### Step 3: Assign unknown = nx.dedensify(...)

```python
c_G, c_nodes = nx.dedensify(G, threshold=2, copy=True)
```

### Step 4: Assign compressed_edge_count = len(...)

```python
compressed_edge_count = len(c_G.edges())
```

### Step 5: Assign verified_original_edge_count = len(...)

```python
verified_original_edge_count = len(G.edges())
```

**Verification:**
```python
assert compressed_edge_count <= verified_original_edge_count
```

### Step 6: Assign verified_compressed_G = self.build_compressed_graph(...)

```python
verified_compressed_G = self.build_compressed_graph()
```

### Step 7: Assign verified_compressed_edge_count = len(...)

```python
verified_compressed_edge_count = len(verified_compressed_G.edges())
```

**Verification:**
```python
assert compressed_edge_count == verified_compressed_edge_count
```


## Complete Example

```python
# Workflow
'\n        Verifies that dedensify produced the correct number of edges in an\n        undirected graph\n        '
G = self.build_original_graph()
c_G, c_nodes = nx.dedensify(G, threshold=2, copy=True)
compressed_edge_count = len(c_G.edges())
verified_original_edge_count = len(G.edges())
assert compressed_edge_count <= verified_original_edge_count
verified_compressed_G = self.build_compressed_graph()
verified_compressed_edge_count = len(verified_compressed_G.edges())
assert compressed_edge_count == verified_compressed_edge_count
```

## Next Steps


---

*Source: test_summarization.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*