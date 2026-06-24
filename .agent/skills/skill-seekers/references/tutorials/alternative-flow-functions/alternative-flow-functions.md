# How To: Alternative Flow Functions

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test alternative flow functions

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity.kcutsets`

**Setup Required:**
```python
# Fixtures: G, flow_func
```

## Step-by-Step Guide

### Step 1: Assign node_conn = nx.node_connectivity(...)

```python
node_conn = nx.node_connectivity(G)
```

**Verification:**
```python
assert node_conn == len(cut)
```

### Step 2: Assign all_cuts = nx.all_node_cuts(...)

```python
all_cuts = nx.all_node_cuts(G, flow_func=flow_func)
```

**Verification:**
```python
assert not nx.is_connected(nx.restricted_view(G, cut, []))
```


## Complete Example

```python
# Setup
# Fixtures: G, flow_func

# Workflow
node_conn = nx.node_connectivity(G)
all_cuts = nx.all_node_cuts(G, flow_func=flow_func)
for cut in itertools.islice(all_cuts, MAX_CUTSETS_TO_TEST):
    assert node_conn == len(cut)
    assert not nx.is_connected(nx.restricted_view(G, cut, []))
```

## Next Steps


---

*Source: test_kcutsets.py:213 | Complexity: Beginner | Last updated: 2026-06-02*