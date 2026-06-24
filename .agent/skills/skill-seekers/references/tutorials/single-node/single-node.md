# How To: Single Node

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single node

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

### Step 2: Call test.add_node()

```python
test.add_node('a')
```

### Step 3: Assign ground_truth = value

```python
ground_truth = {frozenset(['a'])}
```

### Step 4: Assign communities = asyn_fluidc(...)

```python
communities = asyn_fluidc(test, 1)
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
test = Graph()
test.add_node('a')
ground_truth = {frozenset(['a'])}
communities = asyn_fluidc(test, 1)
result = {frozenset(c) for c in communities}
assert result == ground_truth
```

## Next Steps


---

*Source: test_asyn_fluid.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*