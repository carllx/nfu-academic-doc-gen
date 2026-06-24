# How To: Unconnected Communities

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unconnected communities

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

### Step 2: Call test.add_edge()

```python
test.add_edge('a', 'c')
```

### Step 3: Call test.add_edge()

```python
test.add_edge('a', 'd')
```

### Step 4: Call test.add_edge()

```python
test.add_edge('d', 'c')
```

### Step 5: Call test.add_edge()

```python
test.add_edge('b', 'e')
```

### Step 6: Call test.add_edge()

```python
test.add_edge('e', 'f')
```

### Step 7: Call test.add_edge()

```python
test.add_edge('f', 'b')
```

### Step 8: Assign ground_truth = value

```python
ground_truth = {frozenset(['a', 'c', 'd']), frozenset(['b', 'e', 'f'])}
```

### Step 9: Assign communities = nx.community.label_propagation_communities(...)

```python
communities = nx.community.label_propagation_communities(test)
```

### Step 10: Assign result = value

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
test.add_edge('a', 'c')
test.add_edge('a', 'd')
test.add_edge('d', 'c')
test.add_edge('b', 'e')
test.add_edge('e', 'f')
test.add_edge('f', 'b')
ground_truth = {frozenset(['a', 'c', 'd']), frozenset(['b', 'e', 'f'])}
communities = nx.community.label_propagation_communities(test)
result = {frozenset(c) for c in communities}
assert result == ground_truth
```

## Next Steps


---

*Source: test_label_propagation.py:38 | Complexity: Advanced | Last updated: 2026-06-02*