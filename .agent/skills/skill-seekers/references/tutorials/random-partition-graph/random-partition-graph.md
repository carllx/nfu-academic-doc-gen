# How To: Random Partition Graph

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random partition graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.random_partition_graph(...)

```python
G = nx.random_partition_graph([3, 3, 3], 1, 0, seed=42)
```

**Verification:**
```python
assert C == [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
```

### Step 2: Assign C = value

```python
C = G.graph['partition']
```

**Verification:**
```python
assert len(G) == 9
```

### Step 3: Assign G = nx.random_partition_graph(...)

```python
G = nx.random_partition_graph([3, 3, 3], 0, 1)
```

**Verification:**
```python
assert len(list(G.edges())) == 9
```

### Step 4: Assign C = value

```python
C = G.graph['partition']
```

**Verification:**
```python
assert C == [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
```

### Step 5: Assign G = nx.random_partition_graph(...)

```python
G = nx.random_partition_graph([3, 3, 3], 1, 0, directed=True)
```

**Verification:**
```python
assert len(G) == 9
```

### Step 6: Assign C = value

```python
C = G.graph['partition']
```

**Verification:**
```python
assert len(list(G.edges())) == 27
```

### Step 7: Assign G = nx.random_partition_graph(...)

```python
G = nx.random_partition_graph([3, 3, 3], 0, 1, directed=True)
```

**Verification:**
```python
assert C == [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
```

### Step 8: Assign C = value

```python
C = G.graph['partition']
```

**Verification:**
```python
assert len(G) == 9
```

### Step 9: Assign G = nx.random_partition_graph(...)

```python
G = nx.random_partition_graph([1, 2, 3, 4, 5], 0.5, 0.1)
```

**Verification:**
```python
assert len(list(G.edges())) == 18
```

### Step 10: Assign C = value

```python
C = G.graph['partition']
```

**Verification:**
```python
assert C == [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
```

### Step 11: Assign rpg = value

```python
rpg = nx.random_partition_graph
```

**Verification:**
```python
assert len(G) == 9
```

### Step 12: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, rpg, [1, 2, 3], 1.1, 0.1)
```

**Verification:**
```python
assert len(list(G.edges())) == 54
```

### Step 13: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, rpg, [1, 2, 3], -0.1, 0.1)
```

**Verification:**
```python
assert C == [{0}, {1, 2}, {3, 4, 5}, {6, 7, 8, 9}, {10, 11, 12, 13, 14}]
```

### Step 14: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, rpg, [1, 2, 3], 0.1, 1.1)
```

**Verification:**
```python
assert len(G) == 15
```

### Step 15: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, rpg, [1, 2, 3], 0.1, -0.1)
```


## Complete Example

```python
# Workflow
G = nx.random_partition_graph([3, 3, 3], 1, 0, seed=42)
C = G.graph['partition']
assert C == [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
assert len(G) == 9
assert len(list(G.edges())) == 9
G = nx.random_partition_graph([3, 3, 3], 0, 1)
C = G.graph['partition']
assert C == [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
assert len(G) == 9
assert len(list(G.edges())) == 27
G = nx.random_partition_graph([3, 3, 3], 1, 0, directed=True)
C = G.graph['partition']
assert C == [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
assert len(G) == 9
assert len(list(G.edges())) == 18
G = nx.random_partition_graph([3, 3, 3], 0, 1, directed=True)
C = G.graph['partition']
assert C == [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}]
assert len(G) == 9
assert len(list(G.edges())) == 54
G = nx.random_partition_graph([1, 2, 3, 4, 5], 0.5, 0.1)
C = G.graph['partition']
assert C == [{0}, {1, 2}, {3, 4, 5}, {6, 7, 8, 9}, {10, 11, 12, 13, 14}]
assert len(G) == 15
rpg = nx.random_partition_graph
pytest.raises(nx.NetworkXError, rpg, [1, 2, 3], 1.1, 0.1)
pytest.raises(nx.NetworkXError, rpg, [1, 2, 3], -0.1, 0.1)
pytest.raises(nx.NetworkXError, rpg, [1, 2, 3], 0.1, 1.1)
pytest.raises(nx.NetworkXError, rpg, [1, 2, 3], 0.1, -0.1)
```

## Next Steps


---

*Source: test_community.py:6 | Complexity: Advanced | Last updated: 2026-06-02*