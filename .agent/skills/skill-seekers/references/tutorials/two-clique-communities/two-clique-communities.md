# How To: Two Clique Communities

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test two clique communities

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign test = Graph(...)

```python
test = Graph()
```

**Verification:**
```python
assert result == ground_truth
```

### Step 2: Call test.add_edge()

```python
test.add_edge('a', 'b')
```

### Step 3: Call test.add_edge()

```python
test.add_edge('a', 'c')
```

### Step 4: Call test.add_edge()

```python
test.add_edge('b', 'c')
```

### Step 5: Call test.add_edge()

```python
test.add_edge('c', 'd')
```

### Step 6: Call test.add_edge()

```python
test.add_edge('d', 'e')
```

### Step 7: Call test.add_edge()

```python
test.add_edge('d', 'f')
```

### Step 8: Call test.add_edge()

```python
test.add_edge('f', 'e')
```

### Step 9: Assign ground_truth = value

```python
ground_truth = {frozenset(['a', 'c', 'b']), frozenset(['e', 'd', 'f'])}
```

### Step 10: Assign communities = asyn_fluidc(...)

```python
communities = asyn_fluidc(test, 2, seed=7)
```

### Step 11: Assign result = value

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
test = Graph()
test.add_edge('a', 'b')
test.add_edge('a', 'c')
test.add_edge('b', 'c')
test.add_edge('c', 'd')
test.add_edge('d', 'e')
test.add_edge('d', 'f')
test.add_edge('f', 'e')
ground_truth = {frozenset(['a', 'c', 'b']), frozenset(['e', 'd', 'f'])}
communities = asyn_fluidc(test, 2, seed=7)
result = {frozenset(c) for c in communities}
assert result == ground_truth
```

## Next Steps


---

*Source: test_asyn_fluid.py:53 | Complexity: Advanced | Last updated: 2026-06-02*