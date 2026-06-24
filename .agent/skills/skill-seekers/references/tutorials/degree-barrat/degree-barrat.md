# How To: Degree Barrat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test degree barrat

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.star_graph(...)

```python
G = nx.star_graph(5)
```

**Verification:**
```python
assert nd == 1.8
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(5, 6), (5, 7), (5, 8), (5, 9)])
```

**Verification:**
```python
assert nd == pytest.approx(3.222222, abs=1e-05)
```

### Step 3: Assign unknown = 5

```python
G[0][5]['weight'] = 5
```

### Step 4: Assign nd = value

```python
nd = nx.average_degree_connectivity(G)[5]
```

**Verification:**
```python
assert nd == 1.8
```

### Step 5: Assign nd = value

```python
nd = nx.average_degree_connectivity(G, weight='weight')[5]
```

**Verification:**
```python
assert nd == pytest.approx(3.222222, abs=1e-05)
```


## Complete Example

```python
# Workflow
G = nx.star_graph(5)
G.add_edges_from([(5, 6), (5, 7), (5, 8), (5, 9)])
G[0][5]['weight'] = 5
nd = nx.average_degree_connectivity(G)[5]
assert nd == 1.8
nd = nx.average_degree_connectivity(G, weight='weight')[5]
assert nd == pytest.approx(3.222222, abs=1e-05)
```

## Next Steps


---

*Source: test_connectivity.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*