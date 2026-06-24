# How To: Random Degree Sequence Iterator

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random degree sequence iterator

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.fast_gnp_random_graph(...)

```python
G1 = nx.fast_gnp_random_graph(100, 0.1, seed=42)
```

**Verification:**
```python
assert len(G2) > 0
```

### Step 2: Assign d1 = value

```python
d1 = (d for n, d in G1.degree())
```

### Step 3: Assign G2 = nx.random_degree_sequence_graph(...)

```python
G2 = nx.random_degree_sequence_graph(d1, seed=42)
```

**Verification:**
```python
assert len(G2) > 0
```


## Complete Example

```python
# Workflow
G1 = nx.fast_gnp_random_graph(100, 0.1, seed=42)
d1 = (d for n, d in G1.degree())
G2 = nx.random_degree_sequence_graph(d1, seed=42)
assert len(G2) > 0
```

## Next Steps


---

*Source: test_degree_seq.py:220 | Complexity: Beginner | Last updated: 2026-06-02*