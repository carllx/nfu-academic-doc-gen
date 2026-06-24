# How To: Havel Hakimi Graph

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test havel hakimi graph

## Prerequisites

**Required Modules:**
- `numbers`
- `pytest`
- `networkx`
- `generators`


## Step-by-Step Guide

### Step 1: Assign aseq = value

```python
aseq = []
```

**Verification:**
```python
assert len(G) == 0
```

### Step 2: Assign bseq = value

```python
bseq = []
```

**Verification:**
```python
assert len(G) == 4
```

### Step 3: Assign G = havel_hakimi_graph(...)

```python
G = havel_hakimi_graph(aseq, bseq)
```

**Verification:**
```python
assert G.number_of_edges() == 0
```

### Step 4: Assign aseq = value

```python
aseq = [0, 0]
```

**Verification:**
```python
assert sorted((d for n, d in G.degree())) == [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
```

### Step 5: Assign bseq = value

```python
bseq = [0, 0]
```

**Verification:**
```python
assert G.is_multigraph()
```

### Step 6: Assign G = havel_hakimi_graph(...)

```python
G = havel_hakimi_graph(aseq, bseq)
```

**Verification:**
```python
assert not G.is_directed()
```

### Step 7: Assign aseq = value

```python
aseq = [3, 3, 3, 3]
```

**Verification:**
```python
assert sorted((d for n, d in G.degree())) == [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
```

### Step 8: Assign bseq = value

```python
bseq = [2, 2, 2, 2, 2]
```

**Verification:**
```python
assert GU.number_of_nodes() == 6
```

### Step 9: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, havel_hakimi_graph, aseq, bseq)
```

**Verification:**
```python
assert GD.number_of_nodes() == 4
```

### Step 10: Assign bseq = value

```python
bseq = [2, 2, 2, 2, 2, 2]
```

**Verification:**
```python
assert not G.is_multigraph()
```

### Step 11: Assign G = havel_hakimi_graph(...)

```python
G = havel_hakimi_graph(aseq, bseq)
```

**Verification:**
```python
assert not G.is_directed()
```

### Step 12: Assign aseq = value

```python
aseq = [2, 2, 2, 2, 2, 2]
```

### Step 13: Assign bseq = value

```python
bseq = [3, 3, 3, 3]
```

### Step 14: Assign G = havel_hakimi_graph(...)

```python
G = havel_hakimi_graph(aseq, bseq)
```

**Verification:**
```python
assert G.is_multigraph()
```

### Step 15: Assign GU = nx.projected_graph(...)

```python
GU = nx.projected_graph(nx.Graph(G), range(len(aseq)))
```

**Verification:**
```python
assert GU.number_of_nodes() == 6
```

### Step 16: Assign GD = nx.projected_graph(...)

```python
GD = nx.projected_graph(nx.Graph(G), range(len(aseq), len(aseq) + len(bseq)))
```

**Verification:**
```python
assert GD.number_of_nodes() == 4
```

### Step 17: Assign G = reverse_havel_hakimi_graph(...)

```python
G = reverse_havel_hakimi_graph(aseq, bseq, create_using=nx.Graph)
```

**Verification:**
```python
assert not G.is_multigraph()
```

### Step 18: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, havel_hakimi_graph, aseq, bseq, create_using=nx.DiGraph)
```

### Step 19: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, havel_hakimi_graph, aseq, bseq, create_using=nx.DiGraph)
```

### Step 20: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, havel_hakimi_graph, aseq, bseq, create_using=nx.MultiDiGraph)
```


## Complete Example

```python
# Workflow
aseq = []
bseq = []
G = havel_hakimi_graph(aseq, bseq)
assert len(G) == 0
aseq = [0, 0]
bseq = [0, 0]
G = havel_hakimi_graph(aseq, bseq)
assert len(G) == 4
assert G.number_of_edges() == 0
aseq = [3, 3, 3, 3]
bseq = [2, 2, 2, 2, 2]
pytest.raises(nx.NetworkXError, havel_hakimi_graph, aseq, bseq)
bseq = [2, 2, 2, 2, 2, 2]
G = havel_hakimi_graph(aseq, bseq)
assert sorted((d for n, d in G.degree())) == [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
aseq = [2, 2, 2, 2, 2, 2]
bseq = [3, 3, 3, 3]
G = havel_hakimi_graph(aseq, bseq)
assert G.is_multigraph()
assert not G.is_directed()
assert sorted((d for n, d in G.degree())) == [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
GU = nx.projected_graph(nx.Graph(G), range(len(aseq)))
assert GU.number_of_nodes() == 6
GD = nx.projected_graph(nx.Graph(G), range(len(aseq), len(aseq) + len(bseq)))
assert GD.number_of_nodes() == 4
G = reverse_havel_hakimi_graph(aseq, bseq, create_using=nx.Graph)
assert not G.is_multigraph()
assert not G.is_directed()
pytest.raises(nx.NetworkXError, havel_hakimi_graph, aseq, bseq, create_using=nx.DiGraph)
pytest.raises(nx.NetworkXError, havel_hakimi_graph, aseq, bseq, create_using=nx.DiGraph)
pytest.raises(nx.NetworkXError, havel_hakimi_graph, aseq, bseq, create_using=nx.MultiDiGraph)
```

## Next Steps


---

*Source: test_generators.py:143 | Complexity: Advanced | Last updated: 2026-06-02*