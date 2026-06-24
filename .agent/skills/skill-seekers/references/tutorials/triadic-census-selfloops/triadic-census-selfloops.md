# How To: Triadic Census Selfloops

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test triadic census selfloops

## Prerequisites

**Required Modules:**
- `itertools`
- `collections`
- `random`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign GG = nx.path_graph(...)

```python
GG = nx.path_graph('abc', create_using=nx.DiGraph)
```

**Verification:**
```python
assert expected == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
```

### Step 2: Assign expected = value

```python
expected = {'021C': 1}
```

**Verification:**
```python
assert tc == {tt: len(tbt[tt]) for tt in tc}
```

### Step 3: Assign GG = nx.path_graph(...)

```python
GG = nx.path_graph('abcde', create_using=nx.DiGraph)
```

### Step 4: Assign tbt = nx.triads_by_type(...)

```python
tbt = nx.triads_by_type(GG)
```

### Step 5: Assign tc = nx.triadic_census(...)

```python
tc = nx.triadic_census(GG)
```

**Verification:**
```python
assert tc == {tt: len(tbt[tt]) for tt in tc}
```

### Step 6: Assign G = GG.copy(...)

```python
G = GG.copy()
```

### Step 7: Call G.add_edge()

```python
G.add_edge(n, n)
```

### Step 8: Assign tc = nx.triadic_census(...)

```python
tc = nx.triadic_census(G)
```

**Verification:**
```python
assert expected == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
```

### Step 9: Call GG.add_edge()

```python
GG.add_edge(n, n)
```


## Complete Example

```python
# Workflow
GG = nx.path_graph('abc', create_using=nx.DiGraph)
expected = {'021C': 1}
for n in GG:
    G = GG.copy()
    G.add_edge(n, n)
    tc = nx.triadic_census(G)
    assert expected == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
GG = nx.path_graph('abcde', create_using=nx.DiGraph)
tbt = nx.triads_by_type(GG)
for n in GG:
    GG.add_edge(n, n)
tc = nx.triadic_census(GG)
assert tc == {tt: len(tbt[tt]) for tt in tc}
```

## Next Steps


---

*Source: test_triads.py:150 | Complexity: Advanced | Last updated: 2026-06-02*