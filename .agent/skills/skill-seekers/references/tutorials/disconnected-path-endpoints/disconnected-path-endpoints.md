# How To: Disconnected Path Endpoints

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Betweenness centrality: disconnected path endpoints

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Betweenness centrality: disconnected path endpoints'

```python
'Betweenness centrality: disconnected path endpoints'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n] / 21, abs=1e-07)
```

### Step 3: Call nx.add_path()

```python
nx.add_path(G, [0, 1, 2])
```

### Step 4: Call nx.add_path()

```python
nx.add_path(G, [3, 4, 5, 6])
```

### Step 5: Assign b_answer = value

```python
b_answer = {0: 2, 1: 3, 2: 2, 3: 3, 4: 5, 5: 5, 6: 3}
```

### Step 6: Assign b = nx.betweenness_centrality(...)

```python
b = nx.betweenness_centrality(G, weight=None, normalized=False, endpoints=True)
```

### Step 7: Assign b = nx.betweenness_centrality(...)

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
'Betweenness centrality: disconnected path endpoints'
G = nx.Graph()
nx.add_path(G, [0, 1, 2])
nx.add_path(G, [3, 4, 5, 6])
b_answer = {0: 2, 1: 3, 2: 2, 3: 3, 4: 5, 5: 5, 6: 3}
b = nx.betweenness_centrality(G, weight=None, normalized=False, endpoints=True)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
b = nx.betweenness_centrality(G, weight=None, normalized=True, endpoints=True)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n] / 21, abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality.py:261 | Complexity: Intermediate | Last updated: 2026-06-02*