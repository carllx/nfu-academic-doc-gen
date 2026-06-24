# How To: Complete Undirected Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test a complete undirected graph.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.approximation`


## Step-by-Step Guide

### Step 1: 'Test a complete undirected graph.'

```python
'Test a complete undirected graph.'
```

**Verification:**
```python
assert diameter(graph) == 1
```

### Step 2: Assign graph = nx.complete_graph(...)

```python
graph = nx.complete_graph(10)
```

**Verification:**
```python
assert diameter(graph) == 1
```


## Complete Example

```python
# Workflow
'Test a complete undirected graph.'
graph = nx.complete_graph(10)
assert diameter(graph) == 1
```

## Next Steps


---

*Source: test_distance_measures.py:35 | Complexity: Beginner | Last updated: 2026-06-02*