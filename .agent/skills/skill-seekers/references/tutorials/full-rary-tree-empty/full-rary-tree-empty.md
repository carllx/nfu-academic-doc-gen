# How To: Full Rary Tree Empty

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test full rary tree empty

## Prerequisites

**Required Modules:**
- `itertools`
- `typing`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign t = nx.full_rary_tree(...)

```python
t = nx.full_rary_tree(0, 10)
```

**Verification:**
```python
assert nx.could_be_isomorphic(t, nx.empty_graph(10))
```

### Step 2: Assign t = nx.full_rary_tree(...)

```python
t = nx.full_rary_tree(3, 0)
```

**Verification:**
```python
assert nx.could_be_isomorphic(t, nx.empty_graph(0))
```


## Complete Example

```python
# Workflow
t = nx.full_rary_tree(0, 10)
assert nx.could_be_isomorphic(t, nx.empty_graph(10))
t = nx.full_rary_tree(3, 0)
assert nx.could_be_isomorphic(t, nx.empty_graph(0))
```

## Next Steps


---

*Source: test_classic.py:75 | Complexity: Beginner | Last updated: 2026-06-02*