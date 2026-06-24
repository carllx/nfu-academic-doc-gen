# How To: Betweenness Centrality

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test betweenness centrality

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign c = bipartite.betweenness_centrality(...)

```python
c = bipartite.betweenness_centrality(self.P4, [1, 3])
```

**Verification:**
```python
assert c == answer
```

### Step 2: Assign answer = value

```python
answer = {0: 0.0, 1: 1.0, 2: 1.0, 3: 0.0}
```

**Verification:**
```python
assert c == answer
```

### Step 3: Assign c = bipartite.betweenness_centrality(...)

```python
c = bipartite.betweenness_centrality(self.K3, [0, 1, 2])
```

**Verification:**
```python
assert c == answer
```

### Step 4: Assign answer = value

```python
answer = {0: 0.125, 1: 0.125, 2: 0.125, 3: 0.125, 4: 0.125, 5: 0.125}
```

**Verification:**
```python
assert c == answer
```

### Step 5: Assign c = bipartite.betweenness_centrality(...)

```python
c = bipartite.betweenness_centrality(self.C4, [0, 2])
```

### Step 6: Assign answer = value

```python
answer = {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}
```

**Verification:**
```python
assert c == answer
```


## Complete Example

```python
# Workflow
c = bipartite.betweenness_centrality(self.P4, [1, 3])
answer = {0: 0.0, 1: 1.0, 2: 1.0, 3: 0.0}
assert c == answer
c = bipartite.betweenness_centrality(self.K3, [0, 1, 2])
answer = {0: 0.125, 1: 0.125, 2: 0.125, 3: 0.125, 4: 0.125, 5: 0.125}
assert c == answer
c = bipartite.betweenness_centrality(self.C4, [0, 2])
answer = {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}
assert c == answer
```

## Next Steps


---

*Source: test_centrality.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*