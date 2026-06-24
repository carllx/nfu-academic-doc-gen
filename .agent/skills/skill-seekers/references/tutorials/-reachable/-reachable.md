# How To:  Reachable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test  reachable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: large_collider_graph
```

## Step-by-Step Guide

### Step 1: Assign reachable = value

```python
reachable = nx.algorithms.d_separation._reachable
```

**Verification:**
```python
assert reachable(g, x, ancestors, {'B'}) == {'B', 'F', 'D'}
```

### Step 2: Assign g = large_collider_graph

```python
g = large_collider_graph
```

**Verification:**
```python
assert reachable(g, x, ancestors, set()) == ancestors
```

### Step 3: Assign x = value

```python
x = {'F', 'D'}
```

### Step 4: Assign ancestors = value

```python
ancestors = {'A', 'B', 'C', 'D', 'F'}
```

**Verification:**
```python
assert reachable(g, x, ancestors, {'B'}) == {'B', 'F', 'D'}
```


## Complete Example

```python
# Setup
# Fixtures: large_collider_graph

# Workflow
reachable = nx.algorithms.d_separation._reachable
g = large_collider_graph
x = {'F', 'D'}
ancestors = {'A', 'B', 'C', 'D', 'F'}
assert reachable(g, x, ancestors, {'B'}) == {'B', 'F', 'D'}
assert reachable(g, x, ancestors, set()) == ancestors
```

## Next Steps


---

*Source: test_d_separation.py:334 | Complexity: Intermediate | Last updated: 2026-06-02*