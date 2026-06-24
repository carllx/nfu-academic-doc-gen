# How To: Dedensify Edges

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Verifies that dedensify produced correct compressor nodes and the
correct edges to/from the compressor nodes in an undirected graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n        Verifies that dedensify produced correct compressor nodes and the\n        correct edges to/from the compressor nodes in an undirected graph\n        '

```python
'\n        Verifies that dedensify produced correct compressor nodes and the\n        correct edges to/from the compressor nodes in an undirected graph\n        '
```

**Verification:**
```python
assert has_compressed_edge == verified_has_compressed_edge
```

### Step 2: Assign G = self.build_original_graph(...)

```python
G = self.build_original_graph()
```

**Verification:**
```python
assert len(c_nodes) == len(self.c_nodes)
```

### Step 3: Assign unknown = nx.dedensify(...)

```python
c_G, c_nodes = nx.dedensify(G, threshold=2)
```

### Step 4: Assign v_compressed_G = self.build_compressed_graph(...)

```python
v_compressed_G = self.build_compressed_graph()
```

**Verification:**
```python
assert len(c_nodes) == len(self.c_nodes)
```

### Step 5: Assign o_s = unknown.join(...)

```python
o_s = ''.join(sorted(s))
```

### Step 6: Assign o_t = unknown.join(...)

```python
o_t = ''.join(sorted(t))
```

### Step 7: Assign has_compressed_edge = c_G.has_edge(...)

```python
has_compressed_edge = c_G.has_edge(s, t)
```

### Step 8: Assign verified_has_compressed_edge = v_compressed_G.has_edge(...)

```python
verified_has_compressed_edge = v_compressed_G.has_edge(o_s, o_t)
```

**Verification:**
```python
assert has_compressed_edge == verified_has_compressed_edge
```


## Complete Example

```python
# Workflow
'\n        Verifies that dedensify produced correct compressor nodes and the\n        correct edges to/from the compressor nodes in an undirected graph\n        '
G = self.build_original_graph()
c_G, c_nodes = nx.dedensify(G, threshold=2)
v_compressed_G = self.build_compressed_graph()
for s, t in c_G.edges():
    o_s = ''.join(sorted(s))
    o_t = ''.join(sorted(t))
    has_compressed_edge = c_G.has_edge(s, t)
    verified_has_compressed_edge = v_compressed_G.has_edge(o_s, o_t)
    assert has_compressed_edge == verified_has_compressed_edge
assert len(c_nodes) == len(self.c_nodes)
```

## Next Steps


---

*Source: test_summarization.py:192 | Complexity: Advanced | Last updated: 2026-06-02*