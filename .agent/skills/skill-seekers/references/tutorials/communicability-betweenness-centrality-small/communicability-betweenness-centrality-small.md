# How To: Communicability Betweenness Centrality Small

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test communicability betweenness centrality small

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.centrality.subgraph_alg`


## Step-by-Step Guide

### Step 1: Assign result = communicability_betweenness_centrality(...)

```python
result = communicability_betweenness_centrality(nx.path_graph(2))
```

**Verification:**
```python
assert result == {0: 0, 1: 0}
```

### Step 2: Assign result = communicability_betweenness_centrality(...)

```python
result = communicability_betweenness_centrality(nx.path_graph(1))
```

**Verification:**
```python
assert result == {0: 0}
```

### Step 3: Assign result = communicability_betweenness_centrality(...)

```python
result = communicability_betweenness_centrality(nx.path_graph(0))
```

**Verification:**
```python
assert result == {}
```

### Step 4: Assign answer = value

```python
answer = {0: 0.1411224421177313, 1: 1.0, 2: 0.1411224421177313}
```

**Verification:**
```python
assert answer[k] == pytest.approx(v, abs=1e-07)
```

### Step 5: Assign result = communicability_betweenness_centrality(...)

```python
result = communicability_betweenness_centrality(nx.path_graph(3))
```

**Verification:**
```python
assert 0.49786143366223296 == pytest.approx(v, abs=1e-07)
```

### Step 6: Assign result = communicability_betweenness_centrality(...)

```python
result = communicability_betweenness_centrality(nx.complete_graph(3))
```

**Verification:**
```python
assert answer[k] == pytest.approx(v, abs=1e-07)
```


## Complete Example

```python
# Workflow
result = communicability_betweenness_centrality(nx.path_graph(2))
assert result == {0: 0, 1: 0}
result = communicability_betweenness_centrality(nx.path_graph(1))
assert result == {0: 0}
result = communicability_betweenness_centrality(nx.path_graph(0))
assert result == {}
answer = {0: 0.1411224421177313, 1: 1.0, 2: 0.1411224421177313}
result = communicability_betweenness_centrality(nx.path_graph(3))
for k, v in result.items():
    assert answer[k] == pytest.approx(v, abs=1e-07)
result = communicability_betweenness_centrality(nx.complete_graph(3))
for k, v in result.items():
    assert 0.49786143366223296 == pytest.approx(v, abs=1e-07)
```

## Next Steps


---

*Source: test_subgraph.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*