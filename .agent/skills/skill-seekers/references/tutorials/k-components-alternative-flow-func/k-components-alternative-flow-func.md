# How To: K Components Alternative Flow Func

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test k components alternative flow func

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity.kcomponents`

**Setup Required:**
```python
# Fixtures: flow_func
```

## Step-by-Step Guide

### Step 1: Assign G = nx.lollipop_graph(...)

```python
G = nx.lollipop_graph(5, 5)
```

### Step 2: Assign result = nx.k_components(...)

```python
result = nx.k_components(G, flow_func=flow_func)
```

### Step 3: Call _check_connectivity()

```python
_check_connectivity(G, result)
```


## Complete Example

```python
# Setup
# Fixtures: flow_func

# Workflow
G = nx.lollipop_graph(5, 5)
result = nx.k_components(G, flow_func=flow_func)
_check_connectivity(G, result)
```

## Next Steps


---

*Source: test_kcomponents.py:96 | Complexity: Beginner | Last updated: 2026-06-02*