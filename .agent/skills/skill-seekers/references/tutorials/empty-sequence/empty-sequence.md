# How To: Empty Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: Joining the empty sequence results in the tree with one node.

## Prerequisites

**Required Modules:**
- `itertools`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Joining the empty sequence results in the tree with one node.'

```python
'Joining the empty sequence results in the tree with one node.'
```

**Verification:**
```python
assert len(T) == 1
```

### Step 2: Assign T = nx.join_trees(...)

```python
T = nx.join_trees([])
```

**Verification:**
```python
assert T.number_of_edges() == 0
```


## Complete Example

```python
# Workflow
'Joining the empty sequence results in the tree with one node.'
T = nx.join_trees([])
assert len(T) == 1
assert T.number_of_edges() == 0
```

## Next Steps


---

*Source: test_operations.py:15 | Complexity: Beginner | Last updated: 2026-06-02*