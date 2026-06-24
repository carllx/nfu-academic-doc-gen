# How To: Group Betweenness Disconnected Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Group betweenness centrality in a disconnected graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n        Group betweenness centrality in a disconnected graph\n        '

```python
'\n        Group betweenness centrality in a disconnected graph\n        '
```

**Verification:**
```python
assert b == b_answer
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(5)
```

### Step 3: Call G.remove_edge()

```python
G.remove_edge(0, 1)
```

### Step 4: Assign C = value

```python
C = [1]
```

### Step 5: Assign b = nx.group_betweenness_centrality(...)

```python
b = nx.group_betweenness_centrality(G, C, weight=None, normalized=False)
```

### Step 6: Assign b_answer = 0.0

```python
b_answer = 0.0
```

**Verification:**
```python
assert b == b_answer
```


## Complete Example

```python
# Workflow
'\n        Group betweenness centrality in a disconnected graph\n        '
G = nx.path_graph(5)
G.remove_edge(0, 1)
C = [1]
b = nx.group_betweenness_centrality(G, C, weight=None, normalized=False)
b_answer = 0.0
assert b == b_answer
```

## Next Steps


---

*Source: test_group.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*