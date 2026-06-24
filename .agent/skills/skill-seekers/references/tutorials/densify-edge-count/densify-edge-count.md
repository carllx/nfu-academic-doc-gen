# How To: Densify Edge Count

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Verifies that densification produces the correct number of edges in the
original directed graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n        Verifies that densification produces the correct number of edges in the\n        original directed graph\n        '

```python
'\n        Verifies that densification produces the correct number of edges in the\n        original directed graph\n        '
```

**Verification:**
```python
assert compressed_edge_count <= original_edge_count
```

### Step 2: Assign compressed_G = self.build_compressed_graph(...)

```python
compressed_G = self.build_compressed_graph()
```

**Verification:**
```python
assert original_edge_count == len(G.edges())
```

### Step 3: Assign compressed_edge_count = len(...)

```python
compressed_edge_count = len(compressed_G.edges())
```

### Step 4: Assign original_graph = self.densify(...)

```python
original_graph = self.densify(compressed_G, self.c_nodes)
```

### Step 5: Assign original_edge_count = len(...)

```python
original_edge_count = len(original_graph.edges())
```

**Verification:**
```python
assert compressed_edge_count <= original_edge_count
```

### Step 6: Assign G = self.build_original_graph(...)

```python
G = self.build_original_graph()
```

**Verification:**
```python
assert original_edge_count == len(G.edges())
```


## Complete Example

```python
# Workflow
'\n        Verifies that densification produces the correct number of edges in the\n        original directed graph\n        '
compressed_G = self.build_compressed_graph()
compressed_edge_count = len(compressed_G.edges())
original_graph = self.densify(compressed_G, self.c_nodes)
original_edge_count = len(original_graph.edges())
assert compressed_edge_count <= original_edge_count
G = self.build_original_graph()
assert original_edge_count == len(G.edges())
```

## Next Steps


---

*Source: test_summarization.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*