# How To: Mycielski Graph Generator

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mycielski graph generator

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.mycielski_graph(...)

```python
G = nx.mycielski_graph(1)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.empty_graph(1))
```

### Step 2: Assign G = nx.mycielski_graph(...)

```python
G = nx.mycielski_graph(2)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.path_graph(2))
```

### Step 3: Assign G = nx.mycielski_graph(...)

```python
G = nx.mycielski_graph(3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.cycle_graph(5))
```

### Step 4: Assign G = nx.mycielski_graph(...)

```python
G = nx.mycielski_graph(4)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.mycielskian(nx.cycle_graph(5)))
```

### Step 5: Call nx.mycielski_graph()

```python
nx.mycielski_graph(0)
```


## Complete Example

```python
# Workflow
G = nx.mycielski_graph(1)
assert nx.is_isomorphic(G, nx.empty_graph(1))
G = nx.mycielski_graph(2)
assert nx.is_isomorphic(G, nx.path_graph(2))
G = nx.mycielski_graph(3)
assert nx.is_isomorphic(G, nx.cycle_graph(5))
G = nx.mycielski_graph(4)
assert nx.is_isomorphic(G, nx.mycielskian(nx.cycle_graph(5)))
with pytest.raises(nx.NetworkXError, match='must satisfy n >= 1'):
    nx.mycielski_graph(0)
```

## Next Steps


---

*Source: test_mycielski.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*