# How To: P5 Multiple Target

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Edge betweenness subset centrality: P5 multiple target

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Edge betweenness subset centrality: P5 multiple target'

```python
'Edge betweenness subset centrality: P5 multiple target'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call nx.add_path()

```python
nx.add_path(G, range(5))
```

### Step 4: Assign b_answer = dict.fromkeys(...)

```python
b_answer = dict.fromkeys(G.edges(), 0)
```

### Step 5: Assign unknown, unknown, unknown = 1

```python
b_answer[0, 1] = b_answer[1, 2] = b_answer[2, 3] = 1
```

### Step 6: Assign unknown = 0.5

```python
b_answer[3, 4] = 0.5
```

### Step 7: Assign b = nx.edge_betweenness_centrality_subset(...)

```python
b = nx.edge_betweenness_centrality_subset(G, sources=[0], targets=[3, 4], weight=None)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Edge betweenness subset centrality: P5 multiple target'
G = nx.Graph()
nx.add_path(G, range(5))
b_answer = dict.fromkeys(G.edges(), 0)
b_answer[0, 1] = b_answer[1, 2] = b_answer[2, 3] = 1
b_answer[3, 4] = 0.5
b = nx.edge_betweenness_centrality_subset(G, sources=[0], targets=[3, 4], weight=None)
for n in sorted(G.edges()):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality_subset.py:201 | Complexity: Intermediate | Last updated: 2026-06-02*