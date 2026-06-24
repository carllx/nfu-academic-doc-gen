# How To: Large

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test large

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign fname = value

```python
fname = importlib.resources.files('networkx.algorithms.flow.tests') / 'netgen-2.gpickle.bz2'
```

**Verification:**
```python
assert 6749969302 == flowCost
```

### Step 2: Assign unknown = nx.network_simplex(...)

```python
flowCost, flowDict = nx.network_simplex(G)
```

**Verification:**
```python
assert 6749969302 == nx.cost_of_flow(G, flowDict)
```

### Step 3: Assign unknown = nx.capacity_scaling(...)

```python
flowCost, flowDict = nx.capacity_scaling(G)
```

**Verification:**
```python
assert 6749969302 == flowCost
```

### Step 4: Assign G = pickle.load(...)

```python
G = pickle.load(f)
```

**Verification:**
```python
assert 6749969302 == nx.cost_of_flow(G, flowDict)
```


## Complete Example

```python
# Workflow
fname = importlib.resources.files('networkx.algorithms.flow.tests') / 'netgen-2.gpickle.bz2'
with bz2.BZ2File(fname, 'rb') as f:
    G = pickle.load(f)
flowCost, flowDict = nx.network_simplex(G)
assert 6749969302 == flowCost
assert 6749969302 == nx.cost_of_flow(G, flowDict)
flowCost, flowDict = nx.capacity_scaling(G)
assert 6749969302 == flowCost
assert 6749969302 == nx.cost_of_flow(G, flowDict)
```

## Next Steps


---

*Source: test_mincost.py:463 | Complexity: Intermediate | Last updated: 2026-06-02*