# How To: On Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test on complete graph

## Prerequisites

**Required Modules:**
- `collections`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

**Verification:**
```python
assert nx.is_eulerian(nx.eulerize(G))
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(4)
assert nx.is_eulerian(nx.eulerize(G))
assert nx.is_eulerian(nx.eulerize(nx.MultiGraph(G)))
```

## Next Steps


---

*Source: test_euler.py:291 | Complexity: Beginner | Last updated: 2026-06-02*