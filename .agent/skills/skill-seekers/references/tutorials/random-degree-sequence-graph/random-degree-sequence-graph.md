# How To: Random Degree Sequence Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random degree sequence graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign d = value

```python
d = [1, 2, 2, 3]
```

**Verification:**
```python
assert d == sorted((d for n, d in G.degree()))
```

### Step 2: Assign G = nx.random_degree_sequence_graph(...)

```python
G = nx.random_degree_sequence_graph(d, seed=42)
```

**Verification:**
```python
assert d == sorted((d for n, d in G.degree()))
```


## Complete Example

```python
# Workflow
d = [1, 2, 2, 3]
G = nx.random_degree_sequence_graph(d, seed=42)
assert d == sorted((d for n, d in G.degree()))
```

## Next Steps


---

*Source: test_degree_seq.py:201 | Complexity: Beginner | Last updated: 2026-06-02*