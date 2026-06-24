# How To: P3 Endpoints

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Betweenness centrality: P3 endpoints

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Betweenness centrality: P3 endpoints'

```python
'Betweenness centrality: P3 endpoints'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 3: Assign b_answer = value

```python
b_answer = {0: 2.0, 1: 3.0, 2: 2.0}
```

### Step 4: Assign b = nx.betweenness_centrality(...)

```python
b = nx.betweenness_centrality(G, weight=None, normalized=False, endpoints=True)
```

### Step 5: Assign b_answer = value

```python
b_answer = {0: 2 / 3, 1: 1.0, 2: 2 / 3}
```

### Step 6: Assign b = nx.betweenness_centrality(...)

```python
b = nx.betweenness_centrality(G, weight=None, normalized=True, endpoints=True)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Betweenness centrality: P3 endpoints'
G = nx.path_graph(3)
b_answer = {0: 2.0, 1: 3.0, 2: 2.0}
b = nx.betweenness_centrality(G, weight=None, normalized=False, endpoints=True)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
b_answer = {0: 2 / 3, 1: 1.0, 2: 2 / 3}
b = nx.betweenness_centrality(G, weight=None, normalized=True, endpoints=True)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*