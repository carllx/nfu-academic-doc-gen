# How To: Threshold Sequence Graph Test

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test threshold sequence graph test

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.threshold`


## Step-by-Step Guide

### Step 1: Assign G = nx.star_graph(...)

```python
G = nx.star_graph(10)
```

**Verification:**
```python
assert nxt.is_threshold_graph(G)
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(10)
```

**Verification:**
```python
assert nxt.is_threshold_sequence([d for n, d in G.degree()])
```

### Step 3: Assign deg = value

```python
deg = [3, 2, 2, 1, 1, 1]
```

**Verification:**
```python
assert nxt.is_threshold_graph(G)
```

### Step 4: Assign deg = value

```python
deg = [3, 2, 2, 1]
```

**Verification:**
```python
assert nxt.is_threshold_sequence([d for n, d in G.degree()])
```

### Step 5: Assign G = nx.generators.havel_hakimi_graph(...)

```python
G = nx.generators.havel_hakimi_graph(deg)
```

**Verification:**
```python
assert not nxt.is_threshold_sequence(deg)
```


## Complete Example

```python
# Workflow
G = nx.star_graph(10)
assert nxt.is_threshold_graph(G)
assert nxt.is_threshold_sequence([d for n, d in G.degree()])
G = nx.complete_graph(10)
assert nxt.is_threshold_graph(G)
assert nxt.is_threshold_sequence([d for n, d in G.degree()])
deg = [3, 2, 2, 1, 1, 1]
assert not nxt.is_threshold_sequence(deg)
deg = [3, 2, 2, 1]
assert nxt.is_threshold_sequence(deg)
G = nx.generators.havel_hakimi_graph(deg)
assert nxt.is_threshold_graph(G)
```

## Next Steps


---

*Source: test_threshold.py:21 | Complexity: Intermediate | Last updated: 2026-06-02*