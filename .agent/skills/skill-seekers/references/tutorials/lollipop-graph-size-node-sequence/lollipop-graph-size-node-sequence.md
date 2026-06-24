# How To: Lollipop Graph Size Node Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test lollipop graph size node sequence

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `typing`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: m, n
```

## Step-by-Step Guide

### Step 1: Assign G = nx.lollipop_graph(...)

```python
G = nx.lollipop_graph(m, n)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == len(m) + len(n)
```


## Complete Example

```python
# Setup
# Fixtures: m, n

# Workflow
G = nx.lollipop_graph(m, n)
assert nx.number_of_nodes(G) == len(m) + len(n)
assert nx.number_of_edges(G) == len(m) * (len(m) - 1) / 2 + len(n)
```

## Next Steps


---

*Source: test_classic.py:355 | Complexity: Beginner | Last updated: 2026-06-02*