# How To: Solvers

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Approximate current-flow betweenness centrality: solvers

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Approximate current-flow betweenness centrality: solvers'

```python
'Approximate current-flow betweenness centrality: solvers'
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

### Step 3: Assign epsilon = 0.1

```python
epsilon = 0.1
```

### Step 4: Assign b = approximate_cfbc(...)

```python
b = approximate_cfbc(G, normalized=False, solver=solver, epsilon=0.5 * epsilon)
```

### Step 5: Assign b_answer = value

```python
b_answer = {0: 0.75, 1: 0.75, 2: 0.75, 3: 0.75}
```

### Step 6: Call np.testing.assert_allclose()

```python
np.testing.assert_allclose(b[n], b_answer[n], atol=epsilon)
```


## Complete Example

```python
# Workflow
'Approximate current-flow betweenness centrality: solvers'
G = nx.complete_graph(4)
epsilon = 0.1
for solver in ['full', 'lu', 'cg']:
    b = approximate_cfbc(G, normalized=False, solver=solver, epsilon=0.5 * epsilon)
    b_answer = {0: 0.75, 1: 0.75, 2: 0.75, 3: 0.75}
    for n in sorted(G):
        np.testing.assert_allclose(b[n], b_answer[n], atol=epsilon)
```

## Next Steps


---

*Source: test_current_flow_betweenness_centrality.py:125 | Complexity: Intermediate | Last updated: 2026-06-02*