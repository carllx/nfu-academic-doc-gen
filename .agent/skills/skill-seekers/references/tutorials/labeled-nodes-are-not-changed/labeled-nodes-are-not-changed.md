# How To: Labeled Nodes Are Not Changed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test labeled nodes are not changed

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

**Verification:**
```python
assert predicted[i] == G.nodes[i][label_name]
```

### Step 2: Assign label_name = 'club'

```python
label_name = 'club'
```

### Step 3: Assign label_removed = value

```python
label_removed = {0, 1, 2, 3, 4, 5, 6, 7}
```

### Step 4: Assign predicted = node_classification.harmonic_function(...)

```python
predicted = node_classification.harmonic_function(G, label_name=label_name)
```

### Step 5: Assign label_not_removed = value

```python
label_not_removed = set(range(len(G))) - label_removed
```

**Verification:**
```python
assert predicted[i] == G.nodes[i][label_name]
```


## Complete Example

```python
# Workflow
G = nx.karate_club_graph()
label_name = 'club'
label_removed = {0, 1, 2, 3, 4, 5, 6, 7}
for i in label_removed:
    del G.nodes[i][label_name]
predicted = node_classification.harmonic_function(G, label_name=label_name)
label_not_removed = set(range(len(G))) - label_removed
for i in label_not_removed:
    assert predicted[i] == G.nodes[i][label_name]
```

## Next Steps


---

*Source: test_node_classification.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*