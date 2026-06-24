# How To: Degree Centrality

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test degree centrality

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign d = bipartite.degree_centrality(...)

```python
d = bipartite.degree_centrality(self.P4, [1, 3])
```

**Verification:**
```python
assert d == answer
```

### Step 2: Assign answer = value

```python
answer = {0: 0.5, 1: 1.0, 2: 1.0, 3: 0.5}
```

**Verification:**
```python
assert d == answer
```

### Step 3: Assign d = bipartite.degree_centrality(...)

```python
d = bipartite.degree_centrality(self.K3, [0, 1, 2])
```

**Verification:**
```python
assert d == answer
```

### Step 4: Assign answer = value

```python
answer = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0}
```

**Verification:**
```python
assert d == answer
```

### Step 5: Assign d = bipartite.degree_centrality(...)

```python
d = bipartite.degree_centrality(self.C4, [0, 2])
```

### Step 6: Assign answer = value

```python
answer = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
```

**Verification:**
```python
assert d == answer
```


## Complete Example

```python
# Workflow
d = bipartite.degree_centrality(self.P4, [1, 3])
answer = {0: 0.5, 1: 1.0, 2: 1.0, 3: 0.5}
assert d == answer
d = bipartite.degree_centrality(self.K3, [0, 1, 2])
answer = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0}
assert d == answer
d = bipartite.degree_centrality(self.C4, [0, 2])
answer = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0}
assert d == answer
```

## Next Steps


---

*Source: test_centrality.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*