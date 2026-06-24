# How To: Triads By Type

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test triads by type

## Prerequisites

**Required Modules:**
- `itertools`
- `collections`
- `random`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert set(actual.keys()) == set(expected.keys())
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from(['01', '02', '03', '04', '05', '12', '16', '51', '56', '65'])
```

**Verification:**
```python
assert any((nx.is_isomorphic(a, e) for e in expected_Gs))
```

### Step 3: Assign all_triads = nx.all_triads(...)

```python
all_triads = nx.all_triads(G)
```

### Step 4: Assign expected = defaultdict(...)

```python
expected = defaultdict(list)
```

### Step 5: Assign actual = nx.triads_by_type(...)

```python
actual = nx.triads_by_type(G)
```

**Verification:**
```python
assert set(actual.keys()) == set(expected.keys())
```

### Step 6: Assign name = nx.triad_type(...)

```python
name = nx.triad_type(triad)
```

### Step 7: Call unknown.append()

```python
expected[name].append(triad)
```

### Step 8: Assign expected_Gs = value

```python
expected_Gs = expected[tri_type]
```

**Verification:**
```python
assert any((nx.is_isomorphic(a, e) for e in expected_Gs))
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edges_from(['01', '02', '03', '04', '05', '12', '16', '51', '56', '65'])
all_triads = nx.all_triads(G)
expected = defaultdict(list)
for triad in all_triads:
    name = nx.triad_type(triad)
    expected[name].append(triad)
actual = nx.triads_by_type(G)
assert set(actual.keys()) == set(expected.keys())
for tri_type, actual_Gs in actual.items():
    expected_Gs = expected[tri_type]
    for a in actual_Gs:
        assert any((nx.is_isomorphic(a, e) for e in expected_Gs))
```

## Next Steps


---

*Source: test_triads.py:106 | Complexity: Advanced | Last updated: 2026-06-02*