# How To: K5 Endpoints

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Betweenness centrality: K5 endpoints

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Betweenness centrality: K5 endpoints'

```python
'Betweenness centrality: K5 endpoints'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 3: Assign b = nx.betweenness_centrality(...)

```python
b = nx.betweenness_centrality(G, weight=None, normalized=False, endpoints=True)
```

### Step 4: Assign b_answer = value

```python
b_answer = {0: 4.0, 1: 4.0, 2: 4.0, 3: 4.0, 4: 4.0}
```

### Step 5: Assign b = nx.betweenness_centrality(...)

```python
b = nx.betweenness_centrality(G, weight=None, normalized=True, endpoints=True)
```

### Step 6: Assign b_answer = value

```python
b_answer = {0: 0.4, 1: 0.4, 2: 0.4, 3: 0.4, 4: 0.4}
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Betweenness centrality: K5 endpoints'
G = nx.complete_graph(5)
b = nx.betweenness_centrality(G, weight=None, normalized=False, endpoints=True)
b_answer = {0: 4.0, 1: 4.0, 2: 4.0, 3: 4.0, 4: 4.0}
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
b = nx.betweenness_centrality(G, weight=None, normalized=True, endpoints=True)
b_answer = {0: 0.4, 1: 0.4, 2: 0.4, 3: 0.4, 4: 0.4}
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality.py:32 | Complexity: Intermediate | Last updated: 2026-06-02*