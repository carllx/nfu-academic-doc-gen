# How To: Hyper Wiener Of Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hyper wiener of complete graph

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign n = 5

```python
n = 5
```

**Verification:**
```python
assert nx.hyper_wiener_index(G) == n * (n - 1)
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(n)
```

**Verification:**
```python
assert nx.hyper_wiener_index(G) == n * (n - 1)
```


## Complete Example

```python
# Workflow
n = 5
G = nx.complete_graph(n)
assert nx.hyper_wiener_index(G) == n * (n - 1)
```

## Next Steps


---

*Source: test_wiener.py:126 | Complexity: Beginner | Last updated: 2026-06-02*