# How To: Loops Larger

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loops larger

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign g = nx.DiGraph(...)

```python
g = nx.DiGraph()
```

**Verification:**
```python
assert set(df[n]) == set(answer[n])
```

### Step 2: Assign edges = value

```python
edges = [('entry', 'exit'), ('entry', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', 'exit'), ('6', '2'), ('5', '3'), ('4', '4')]
```

### Step 3: Call g.add_edges_from()

```python
g.add_edges_from(edges)
```

### Step 4: Assign df = nx.dominance_frontiers(...)

```python
df = nx.dominance_frontiers(g, 'entry')
```

### Step 5: Assign answer = value

```python
answer = {'entry': set(), '1': {'exit'}, '2': {'exit', '2'}, '3': {'exit', '3', '2'}, '4': {'exit', '4', '3', '2'}, '5': {'exit', '3', '2'}, '6': {'exit', '2'}, 'exit': set()}
```

**Verification:**
```python
assert set(df[n]) == set(answer[n])
```


## Complete Example

```python
# Workflow
g = nx.DiGraph()
edges = [('entry', 'exit'), ('entry', '1'), ('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), ('6', 'exit'), ('6', '2'), ('5', '3'), ('4', '4')]
g.add_edges_from(edges)
df = nx.dominance_frontiers(g, 'entry')
answer = {'entry': set(), '1': {'exit'}, '2': {'exit', '2'}, '3': {'exit', '3', '2'}, '4': {'exit', '4', '3', '2'}, '5': {'exit', '3', '2'}, '6': {'exit', '2'}, 'exit': set()}
for n in df:
    assert set(df[n]) == set(answer[n])
```

## Next Steps


---

*Source: test_dominance.py:268 | Complexity: Advanced | Last updated: 2026-06-02*