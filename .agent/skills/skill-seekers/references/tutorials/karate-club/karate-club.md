# How To: Karate Club

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test karate club

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

**Verification:**
```python
assert set(map(frozenset, split)) == set(map(frozenset, soln))
```

### Step 2: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

### Step 3: Assign MrHi = value

```python
MrHi = {v for v, club in G.nodes.data('club') if club == 'Mr. Hi'}
```

### Step 4: Assign Officer = value

```python
Officer = {v for v, club in G.nodes.data('club') if club == 'Officer'}
```

### Step 5: Assign split = nx.community.spectral_modularity_bipartition(...)

```python
split = nx.community.spectral_modularity_bipartition(G)
```

### Step 6: Call MrHi.remove()

```python
MrHi.remove(8)
```

### Step 7: Call Officer.add()

```python
Officer.add(8)
```

### Step 8: Assign soln = value

```python
soln = (MrHi, Officer)
```

**Verification:**
```python
assert set(map(frozenset, split)) == set(map(frozenset, soln))
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
G = nx.karate_club_graph()
MrHi = {v for v, club in G.nodes.data('club') if club == 'Mr. Hi'}
Officer = {v for v, club in G.nodes.data('club') if club == 'Officer'}
split = nx.community.spectral_modularity_bipartition(G)
MrHi.remove(8)
Officer.add(8)
soln = (MrHi, Officer)
assert set(map(frozenset, split)) == set(map(frozenset, soln))
```

## Next Steps


---

*Source: test_bipartitions.py:117 | Complexity: Advanced | Last updated: 2026-06-02*