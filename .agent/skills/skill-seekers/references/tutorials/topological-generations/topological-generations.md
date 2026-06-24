# How To: Topological Generations

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test topological generations

## Prerequisites

**Required Modules:**
- `collections`
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph.reverse(...)

```python
G = nx.DiGraph({1: [2, 3], 2: [4, 5], 3: [7], 4: [], 5: [6, 7], 6: [], 7: []}).reverse()
```

**Verification:**
```python
assert generations == expected
```

### Step 2: Assign generations = value

```python
generations = [sorted(gen) for gen in nx.topological_generations(G)]
```

**Verification:**
```python
assert generations == expected
```

### Step 3: Assign expected = value

```python
expected = [[4, 6, 7], [3, 5], [2], [1]]
```

**Verification:**
```python
assert generations == expected
```

### Step 4: Assign MG = nx.MultiDiGraph(...)

```python
MG = nx.MultiDiGraph(G.edges)
```

### Step 5: Call MG.add_edge()

```python
MG.add_edge(2, 1)
```

### Step 6: Assign generations = value

```python
generations = [sorted(gen) for gen in nx.topological_generations(MG)]
```

**Verification:**
```python
assert generations == expected
```


## Complete Example

```python
# Workflow
G = nx.DiGraph({1: [2, 3], 2: [4, 5], 3: [7], 4: [], 5: [6, 7], 6: [], 7: []}).reverse()
generations = [sorted(gen) for gen in nx.topological_generations(G)]
expected = [[4, 6, 7], [3, 5], [2], [1]]
assert generations == expected
MG = nx.MultiDiGraph(G.edges)
MG.add_edge(2, 1)
generations = [sorted(gen) for gen in nx.topological_generations(MG)]
assert generations == expected
```

## Next Steps


---

*Source: test_dag.py:585 | Complexity: Intermediate | Last updated: 2026-06-02*