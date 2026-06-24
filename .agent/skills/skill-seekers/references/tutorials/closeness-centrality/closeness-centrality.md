# How To: Closeness Centrality

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test closeness centrality

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign c = bipartite.closeness_centrality(...)

```python
c = bipartite.closeness_centrality(self.P4, [1, 3])
```

**Verification:**
```python
assert c == answer
```

### Step 2: Assign answer = value

```python
answer = {0: 2.0 / 3, 1: 1.0, 2: 1.0, 3: 2.0 / 3}
```

**Verification:**
```python
assert c == answer
```

### Step 3: Assign c = bipartite.closeness_centrality(...)

```python
c = bipartite.closeness_centrality(self.K3, [0, 1, 2])
```

**Verification:**
```python
assert c == answer
```

### Step 4: Assign answer = value

```python
answer = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0}
```

**Verification:**
```python
assert c == {0: 0.0, 1: 0.0}
```

### Step 5: Assign c = bipartite.closeness_centrality(...)

```python
c = bipartite.closeness_centrality(self.C4, [0, 2])
```

**Verification:**
```python
assert c == {0: 0.0, 1: 0.0}
```

### Step 6: Assign answer = value

```python
answer = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
```

**Verification:**
```python
assert c == answer
```

### Step 7: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 8: Call G.add_node()

```python
G.add_node(0)
```

### Step 9: Call G.add_node()

```python
G.add_node(1)
```

### Step 10: Assign c = bipartite.closeness_centrality(...)

```python
c = bipartite.closeness_centrality(G, [0])
```

**Verification:**
```python
assert c == {0: 0.0, 1: 0.0}
```

### Step 11: Assign c = bipartite.closeness_centrality(...)

```python
c = bipartite.closeness_centrality(G, [1])
```

**Verification:**
```python
assert c == {0: 0.0, 1: 0.0}
```


## Complete Example

```python
# Workflow
c = bipartite.closeness_centrality(self.P4, [1, 3])
answer = {0: 2.0 / 3, 1: 1.0, 2: 1.0, 3: 2.0 / 3}
assert c == answer
c = bipartite.closeness_centrality(self.K3, [0, 1, 2])
answer = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0}
assert c == answer
c = bipartite.closeness_centrality(self.C4, [0, 2])
answer = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
assert c == answer
G = nx.Graph()
G.add_node(0)
G.add_node(1)
c = bipartite.closeness_centrality(G, [0])
assert c == {0: 0.0, 1: 0.0}
c = bipartite.closeness_centrality(G, [1])
assert c == {0: 0.0, 1: 0.0}
```

## Next Steps


---

*Source: test_centrality.py:40 | Complexity: Advanced | Last updated: 2026-06-02*