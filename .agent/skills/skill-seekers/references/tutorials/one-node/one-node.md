# How To: One Node

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test one node

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign test = nx.Graph(...)

```python
test = nx.Graph()
```

**Verification:**
```python
assert result == ground_truth
```

### Step 2: Call test.add_node()

```python
test.add_node('a')
```

### Step 3: Assign ground_truth = value

```python
ground_truth = {frozenset(['a'])}
```

### Step 4: Assign communities = nx.community.label_propagation_communities(...)

```python
communities = nx.community.label_propagation_communities(test)
```

### Step 5: Assign result = value

```python
result = {frozenset(c) for c in communities}
```

**Verification:**
```python
assert result == ground_truth
```


## Complete Example

```python
# Workflow
test = nx.Graph()
test.add_node('a')
ground_truth = {frozenset(['a'])}
communities = nx.community.label_propagation_communities(test)
result = {frozenset(c) for c in communities}
assert result == ground_truth
```

## Next Steps


---

*Source: test_label_propagation.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*