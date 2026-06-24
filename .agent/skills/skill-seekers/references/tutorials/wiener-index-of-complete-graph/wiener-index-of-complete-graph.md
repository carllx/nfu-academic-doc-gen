# How To: Wiener Index Of Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wiener index of complete graph

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign n = 10

```python
n = 10
```

**Verification:**
```python
assert nx.wiener_index(G) == n * (n - 1) / 2
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(n)
```

**Verification:**
```python
assert nx.wiener_index(G) == n * (n - 1) / 2
```


## Complete Example

```python
# Workflow
n = 10
G = nx.complete_graph(n)
assert nx.wiener_index(G) == n * (n - 1) / 2
```

## Next Steps


---

*Source: test_wiener.py:14 | Complexity: Beginner | Last updated: 2026-06-02*