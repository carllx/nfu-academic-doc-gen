# How To: Triadic Census Nodelist

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests the triadic_census function.

## Prerequisites

**Required Modules:**
- `itertools`
- `collections`
- `random`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Tests the triadic_census function.'

```python
'Tests the triadic_census function.'
```

**Verification:**
```python
assert expected == actual
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from(['01', '02', '03', '04', '05', '12', '16', '51', '56', '65'])
```

### Step 4: Assign expected = value

```python
expected = {'030T': 2, '120C': 1, '210': 0, '120U': 0, '012': 9, '102': 3, '021U': 0, '111U': 0, '003': 8, '030C': 0, '021D': 9, '201': 0, '111D': 1, '300': 0, '120D': 0, '021C': 2}
```

### Step 5: Assign actual = value

```python
actual = {k: 0 for k in expected}
```

**Verification:**
```python
assert expected == actual
```

### Step 6: Assign node_triad_census = nx.triadic_census(...)

```python
node_triad_census = nx.triadic_census(G, nodelist=[node])
```


## Complete Example

```python
# Workflow
'Tests the triadic_census function.'
G = nx.DiGraph()
G.add_edges_from(['01', '02', '03', '04', '05', '12', '16', '51', '56', '65'])
expected = {'030T': 2, '120C': 1, '210': 0, '120U': 0, '012': 9, '102': 3, '021U': 0, '111U': 0, '003': 8, '030C': 0, '021D': 9, '201': 0, '111D': 1, '300': 0, '120D': 0, '021C': 2}
actual = {k: 0 for k in expected}
for node in G.nodes():
    node_triad_census = nx.triadic_census(G, nodelist=[node])
    for triad_key in expected:
        actual[triad_key] += node_triad_census[triad_key]
for k, v in actual.items():
    actual[k] //= 3
assert expected == actual
```

## Next Steps


---

*Source: test_triads.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*