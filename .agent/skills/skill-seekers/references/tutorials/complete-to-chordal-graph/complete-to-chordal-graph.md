# How To: Complete To Chordal Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete to chordal graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign fgrg = value

```python
fgrg = nx.fast_gnp_random_graph
```

**Verification:**
```python
assert nx.is_chordal(H)
```

### Step 2: Assign test_graphs = value

```python
test_graphs = [nx.barbell_graph(6, 2), nx.cycle_graph(15), nx.wheel_graph(20), nx.grid_graph([10, 4]), nx.ladder_graph(15), nx.star_graph(5), nx.bull_graph(), fgrg(20, 0.3, seed=1)]
```

**Verification:**
```python
assert len(a) == H.number_of_nodes()
```

### Step 3: Assign unknown = nx.complete_to_chordal_graph(...)

```python
H, a = nx.complete_to_chordal_graph(G)
```

**Verification:**
```python
assert G.number_of_edges() == H.number_of_edges()
```


## Complete Example

```python
# Workflow
fgrg = nx.fast_gnp_random_graph
test_graphs = [nx.barbell_graph(6, 2), nx.cycle_graph(15), nx.wheel_graph(20), nx.grid_graph([10, 4]), nx.ladder_graph(15), nx.star_graph(5), nx.bull_graph(), fgrg(20, 0.3, seed=1)]
for G in test_graphs:
    H, a = nx.complete_to_chordal_graph(G)
    assert nx.is_chordal(H)
    assert len(a) == H.number_of_nodes()
    if nx.is_chordal(G):
        assert G.number_of_edges() == H.number_of_edges()
        assert set(a.values()) == {0}
    else:
        assert len(set(a.values())) == H.number_of_nodes()
```

## Next Steps


---

*Source: test_chordal.py:109 | Complexity: Beginner | Last updated: 2026-06-02*