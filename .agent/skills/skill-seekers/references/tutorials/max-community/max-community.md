# How To: Max Community

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test max community

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign n = 250

```python
n = 250
```

**Verification:**
```python
assert len(G) == 250
```

### Step 2: Assign tau1 = 3

```python
tau1 = 3
```

**Verification:**
```python
assert nx.community.is_partition(G.nodes(), C)
```

### Step 3: Assign tau2 = 1.5

```python
tau2 = 1.5
```

### Step 4: Assign mu = 0.1

```python
mu = 0.1
```

### Step 5: Assign G = nx.LFR_benchmark_graph(...)

```python
G = nx.LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=5, max_degree=100, min_community=50, max_community=200, seed=10)
```

**Verification:**
```python
assert len(G) == 250
```

### Step 6: Assign C = value

```python
C = {frozenset(G.nodes[v]['community']) for v in G}
```

**Verification:**
```python
assert nx.community.is_partition(G.nodes(), C)
```


## Complete Example

```python
# Workflow
n = 250
tau1 = 3
tau2 = 1.5
mu = 0.1
G = nx.LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=5, max_degree=100, min_community=50, max_community=200, seed=10)
assert len(G) == 250
C = {frozenset(G.nodes[v]['community']) for v in G}
assert nx.community.is_partition(G.nodes(), C)
```

## Next Steps


---

*Source: test_community.py:321 | Complexity: Intermediate | Last updated: 2026-06-02*