# How To: Custom Joint Degree Sequence

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom joint degree sequence

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign node = value

```python
node = [1, 1, 1, 2, 1, 2, 0, 0]
```

**Verification:**
```python
assert G.number_of_nodes() == 8
```

### Step 2: Assign tri = value

```python
tri = [0, 0, 0, 0, 0, 1, 1, 1]
```

**Verification:**
```python
assert G.number_of_edges() == 7
```

### Step 3: Assign joint_degree_sequence = zip(...)

```python
joint_degree_sequence = zip(node, tri)
```

### Step 4: Assign G = nx.random_clustered_graph(...)

```python
G = nx.random_clustered_graph(joint_degree_sequence)
```

**Verification:**
```python
assert G.number_of_nodes() == 8
```


## Complete Example

```python
# Workflow
node = [1, 1, 1, 2, 1, 2, 0, 0]
tri = [0, 0, 0, 0, 0, 1, 1, 1]
joint_degree_sequence = zip(node, tri)
G = nx.random_clustered_graph(joint_degree_sequence)
assert G.number_of_nodes() == 8
assert G.number_of_edges() == 7
```

## Next Steps


---

*Source: test_random_clustered.py:7 | Complexity: Intermediate | Last updated: 2026-06-02*