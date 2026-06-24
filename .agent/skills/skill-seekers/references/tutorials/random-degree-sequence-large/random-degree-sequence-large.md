# How To: Random Degree Sequence Large

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random degree sequence large

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
assert sorted(d1) == sorted(d2)
```

### Step 2: Assign d1 = value

```python
d1 = [d for n, d in G1.degree()]
```

### Step 3: Assign G2 = nx.random_degree_sequence_graph(...)

```python
G2 = nx.random_degree_sequence_graph(d1, seed=42)
```

### Step 4: Assign d2 = value

```python
d2 = [d for n, d in G2.degree()]
```

**Verification:**
```python
assert sorted(d1) == sorted(d2)
```


## Complete Example

```python
# Workflow
G1 = nx.fast_gnp_random_graph(100, 0.1, seed=42)
d1 = [d for n, d in G1.degree()]
G2 = nx.random_degree_sequence_graph(d1, seed=42)
d2 = [d for n, d in G2.degree()]
assert sorted(d1) == sorted(d2)
```

## Next Steps


---

*Source: test_degree_seq.py:212 | Complexity: Intermediate | Last updated: 2026-06-02*