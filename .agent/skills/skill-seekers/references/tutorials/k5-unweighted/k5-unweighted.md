# How To: K5 Unweighted

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Katz centrality: K5

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Katz centrality: K5'

```python
'Katz centrality: K5'
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
assert b[n] == pytest.approx(b_answer[n], abs=0.001)
```

### Step 3: Assign alpha = 0.1

```python
alpha = 0.1
```

### Step 4: Assign b = nx.katz_centrality(...)

```python
b = nx.katz_centrality(G, alpha, weight=None)
```

### Step 5: Assign v = math.sqrt(...)

```python
v = math.sqrt(1 / 5.0)
```

### Step 6: Assign b_answer = dict.fromkeys(...)

```python
b_answer = dict.fromkeys(G, v)
```

### Step 7: Assign b = nx.eigenvector_centrality_numpy(...)

```python
b = nx.eigenvector_centrality_numpy(G, weight=None)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Katz centrality: K5'
G = nx.complete_graph(5)
alpha = 0.1
b = nx.katz_centrality(G, alpha, weight=None)
v = math.sqrt(1 / 5.0)
b_answer = dict.fromkeys(G, v)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
b = nx.eigenvector_centrality_numpy(G, weight=None)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=0.001)
```

## Next Steps


---

*Source: test_katz_centrality.py:220 | Complexity: Intermediate | Last updated: 2026-06-02*