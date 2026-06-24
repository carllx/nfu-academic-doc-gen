# How To: K4 Normalized

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Edge flow betweenness centrality: K4

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Edge flow betweenness centrality: K4'

```python
'Edge flow betweenness centrality: K4'
```

**Verification:**
```python
assert v1 == pytest.approx(v2, abs=1e-07)
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

### Step 3: Assign b = edge_current_flow(...)

```python
b = edge_current_flow(G, normalized=False)
```

### Step 4: Assign b_answer = dict.fromkeys(...)

```python
b_answer = dict.fromkeys(G.edges(), 0.75)
```

### Step 5: Assign v2 = b.get(...)

```python
v2 = b.get((s, t), b.get((t, s)))
```

**Verification:**
```python
assert v1 == pytest.approx(v2, abs=1e-07)
```


## Complete Example

```python
# Workflow
'Edge flow betweenness centrality: K4'
G = nx.complete_graph(4)
b = edge_current_flow(G, normalized=False)
b_answer = dict.fromkeys(G.edges(), 0.75)
for (s, t), v1 in b_answer.items():
    v2 = b.get((s, t), b.get((t, s)))
    assert v1 == pytest.approx(v2, abs=1e-07)
```

## Next Steps


---

*Source: test_current_flow_betweenness_centrality.py:219 | Complexity: Intermediate | Last updated: 2026-06-02*