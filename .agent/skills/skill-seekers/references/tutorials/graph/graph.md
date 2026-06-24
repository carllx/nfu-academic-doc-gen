# How To: Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(5, 0)
```

**Verification:**
```python
assert expected == expansion
```

### Step 2: Assign S = set(...)

```python
S = set(range(5))
```

### Step 3: Assign T = value

```python
T = set(G) - S
```

### Step 4: Assign expansion = nx.mixing_expansion(...)

```python
expansion = nx.mixing_expansion(G, S, T)
```

### Step 5: Assign expected = value

```python
expected = 1 / (2 * (5 * 4 + 1))
```

**Verification:**
```python
assert expected == expansion
```


## Complete Example

```python
# Workflow
G = nx.barbell_graph(5, 0)
S = set(range(5))
T = set(G) - S
expansion = nx.mixing_expansion(G, S, T)
expected = 1 / (2 * (5 * 4 + 1))
assert expected == expansion
```

## Next Steps


---

*Source: test_cuts.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*