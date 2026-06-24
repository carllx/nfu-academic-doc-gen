# How To: Edge Betweenness Partition

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test edge betweenness partition

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(3, 0)
```

**Verification:**
```python
assert len(C) == len(answer)
```

### Step 2: Assign C = nx.community.edge_betweenness_partition(...)

```python
C = nx.community.edge_betweenness_partition(G, 2)
```

**Verification:**
```python
assert s in C
```

### Step 3: Assign answer = value

```python
answer = [{0, 1, 2}, {3, 4, 5}]
```

**Verification:**
```python
assert len(C) == len(answer)
```

### Step 4: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(3, 1)
```

**Verification:**
```python
assert s in C
```

### Step 5: Assign C = nx.community.edge_betweenness_partition(...)

```python
C = nx.community.edge_betweenness_partition(G, 3)
```

**Verification:**
```python
assert len(C) == len(answer)
```

### Step 6: Assign answer = value

```python
answer = [{0, 1, 2}, {4, 5, 6}, {3}]
```

**Verification:**
```python
assert s in C
```

### Step 7: Assign C = nx.community.edge_betweenness_partition(...)

```python
C = nx.community.edge_betweenness_partition(G, 7)
```

**Verification:**
```python
assert C == [set(G)]
```

### Step 8: Assign answer = value

```python
answer = [{n} for n in G]
```

**Verification:**
```python
assert C == [set(G)]
```

### Step 9: Assign C = nx.community.edge_betweenness_partition(...)

```python
C = nx.community.edge_betweenness_partition(G, 1)
```

**Verification:**
```python
assert C == [set(G)]
```

### Step 10: Assign C = nx.community.edge_betweenness_partition(...)

```python
C = nx.community.edge_betweenness_partition(G, 1, weight='weight')
```

**Verification:**
```python
assert C == [set(G)]
```

### Step 11: Call nx.community.edge_betweenness_partition()

```python
nx.community.edge_betweenness_partition(G, 0)
```

### Step 12: Call nx.community.edge_betweenness_partition()

```python
nx.community.edge_betweenness_partition(G, -1)
```

### Step 13: Call nx.community.edge_betweenness_partition()

```python
nx.community.edge_betweenness_partition(G, 10)
```


## Complete Example

```python
# Workflow
G = nx.barbell_graph(3, 0)
C = nx.community.edge_betweenness_partition(G, 2)
answer = [{0, 1, 2}, {3, 4, 5}]
assert len(C) == len(answer)
for s in answer:
    assert s in C
G = nx.barbell_graph(3, 1)
C = nx.community.edge_betweenness_partition(G, 3)
answer = [{0, 1, 2}, {4, 5, 6}, {3}]
assert len(C) == len(answer)
for s in answer:
    assert s in C
C = nx.community.edge_betweenness_partition(G, 7)
answer = [{n} for n in G]
assert len(C) == len(answer)
for s in answer:
    assert s in C
C = nx.community.edge_betweenness_partition(G, 1)
assert C == [set(G)]
C = nx.community.edge_betweenness_partition(G, 1, weight='weight')
assert C == [set(G)]
with pytest.raises(nx.NetworkXError):
    nx.community.edge_betweenness_partition(G, 0)
with pytest.raises(nx.NetworkXError):
    nx.community.edge_betweenness_partition(G, -1)
with pytest.raises(nx.NetworkXError):
    nx.community.edge_betweenness_partition(G, 10)
```

## Next Steps


---

*Source: test_divisive.py:6 | Complexity: Advanced | Last updated: 2026-06-02*