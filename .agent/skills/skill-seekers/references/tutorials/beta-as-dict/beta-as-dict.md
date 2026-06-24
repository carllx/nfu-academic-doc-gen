# How To: Beta As Dict

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test beta as dict

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign alpha = 0.1

```python
alpha = 0.1
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=0.0001)
```

### Step 2: Assign beta = value

```python
beta = {0: 1.0, 1: 1.0, 2: 1.0}
```

### Step 3: Assign b_answer = value

```python
b_answer = {0: 0.5598852584152165, 1: 0.6107839182711449, 2: 0.5598852584152162}
```

### Step 4: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3)
```

### Step 5: Assign b = nx.katz_centrality_numpy(...)

```python
b = nx.katz_centrality_numpy(G, alpha, beta)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=0.0001)
```


## Complete Example

```python
# Workflow
alpha = 0.1
beta = {0: 1.0, 1: 1.0, 2: 1.0}
b_answer = {0: 0.5598852584152165, 1: 0.6107839182711449, 2: 0.5598852584152162}
G = nx.path_graph(3)
b = nx.katz_centrality_numpy(G, alpha, beta)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=0.0001)
```

## Next Steps


---

*Source: test_katz_centrality.py:152 | Complexity: Intermediate | Last updated: 2026-06-02*