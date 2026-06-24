# How To: Connected Communities

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test connected communities

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
assert result in ground_truth
```

### Step 2: Call test.add_edge()

```python
test.add_edge('a', 'b')
```

### Step 3: Call test.add_edge()

```python
test.add_edge('c', 'a')
```

### Step 4: Call test.add_edge()

```python
test.add_edge('c', 'b')
```

### Step 5: Call test.add_edge()

```python
test.add_edge('d', 'a')
```

### Step 6: Call test.add_edge()

```python
test.add_edge('d', 'b')
```

### Step 7: Call test.add_edge()

```python
test.add_edge('d', 'c')
```

### Step 8: Call test.add_edge()

```python
test.add_edge('e', 'a')
```

### Step 9: Call test.add_edge()

```python
test.add_edge('e', 'b')
```

### Step 10: Call test.add_edge()

```python
test.add_edge('e', 'c')
```

### Step 11: Call test.add_edge()

```python
test.add_edge('e', 'd')
```

### Step 12: Call test.add_edge()

```python
test.add_edge('1', '2')
```

### Step 13: Call test.add_edge()

```python
test.add_edge('3', '1')
```

### Step 14: Call test.add_edge()

```python
test.add_edge('3', '2')
```

### Step 15: Call test.add_edge()

```python
test.add_edge('4', '1')
```

### Step 16: Call test.add_edge()

```python
test.add_edge('4', '2')
```

### Step 17: Call test.add_edge()

```python
test.add_edge('4', '3')
```

### Step 18: Call test.add_edge()

```python
test.add_edge('5', '1')
```

### Step 19: Call test.add_edge()

```python
test.add_edge('5', '2')
```

### Step 20: Call test.add_edge()

```python
test.add_edge('5', '3')
```

### Step 21: Call test.add_edge()

```python
test.add_edge('5', '4')
```

### Step 22: Call test.add_edge()

```python
test.add_edge('a', '1')
```

### Step 23: Call test.add_edge()

```python
test.add_edge('x', 'y')
```

### Step 24: Call test.add_node()

```python
test.add_node('z')
```

### Step 25: Assign ground_truth1 = value

```python
ground_truth1 = {frozenset(['a', 'b', 'c', 'd', 'e']), frozenset(['1', '2', '3', '4', '5']), frozenset(['x', 'y']), frozenset(['z'])}
```

### Step 26: Assign ground_truth2 = value

```python
ground_truth2 = {frozenset(['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']), frozenset(['x', 'y']), frozenset(['z'])}
```

### Step 27: Assign ground_truth = value

```python
ground_truth = (ground_truth1, ground_truth2)
```

### Step 28: Assign communities = nx.community.label_propagation_communities(...)

```python
communities = nx.community.label_propagation_communities(test)
```

### Step 29: Assign result = value

```python
result = {frozenset(c) for c in communities}
```

**Verification:**
```python
assert result in ground_truth
```


## Complete Example

```python
# Workflow
test = nx.Graph()
test.add_edge('a', 'b')
test.add_edge('c', 'a')
test.add_edge('c', 'b')
test.add_edge('d', 'a')
test.add_edge('d', 'b')
test.add_edge('d', 'c')
test.add_edge('e', 'a')
test.add_edge('e', 'b')
test.add_edge('e', 'c')
test.add_edge('e', 'd')
test.add_edge('1', '2')
test.add_edge('3', '1')
test.add_edge('3', '2')
test.add_edge('4', '1')
test.add_edge('4', '2')
test.add_edge('4', '3')
test.add_edge('5', '1')
test.add_edge('5', '2')
test.add_edge('5', '3')
test.add_edge('5', '4')
test.add_edge('a', '1')
test.add_edge('x', 'y')
test.add_node('z')
ground_truth1 = {frozenset(['a', 'b', 'c', 'd', 'e']), frozenset(['1', '2', '3', '4', '5']), frozenset(['x', 'y']), frozenset(['z'])}
ground_truth2 = {frozenset(['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']), frozenset(['x', 'y']), frozenset(['z'])}
ground_truth = (ground_truth1, ground_truth2)
communities = nx.community.label_propagation_communities(test)
result = {frozenset(c) for c in communities}
assert result in ground_truth
```

## Next Steps


---

*Source: test_label_propagation.py:57 | Complexity: Advanced | Last updated: 2026-06-02*