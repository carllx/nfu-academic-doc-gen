# How To: Complete Directed Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test a complete directed graph.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.approximation`


## Step-by-Step Guide

### Step 1: 'Test a complete directed graph.'

```python
'Test a complete directed graph.'
```

**Verification:**
```python
assert diameter(graph) == 1
```

### Step 2: Assign graph = nx.complete_graph(...)

```python
graph = nx.complete_graph(10, create_using=nx.DiGraph())
```

**Verification:**
```python
assert diameter(graph) == 1
```


## Complete Example

```python
# Workflow
'Test a complete directed graph.'
graph = nx.complete_graph(10, create_using=nx.DiGraph())
assert diameter(graph) == 1
```

## Next Steps


---

*Source: test_distance_measures.py:40 | Complexity: Beginner | Last updated: 2026-06-02*