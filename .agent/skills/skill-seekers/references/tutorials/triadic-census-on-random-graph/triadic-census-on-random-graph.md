# How To: Triadic Census On Random Graph

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test triadic census on random graph

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `collections`
- `random`
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: N
```

## Step-by-Step Guide

### Step 1: Assign G = nx.binomial_graph(...)

```python
G = nx.binomial_graph(N, 0.3, directed=True, seed=42)
```

**Verification:**
```python
assert tc1 == tc2
```

### Step 2: Assign tc1 = nx.triadic_census(...)

```python
tc1 = nx.triadic_census(G)
```

**Verification:**
```python
assert tc1 == tc2
```

### Step 3: Assign tbt = nx.triads_by_type(...)

```python
tbt = nx.triads_by_type(G)
```

**Verification:**
```python
assert tc1 == tc2
```

### Step 4: Assign tc2 = value

```python
tc2 = {tt: len(tbt[tt]) for tt in tc1}
```

**Verification:**
```python
assert tc1 == tc2
```

### Step 5: Assign tc1 = nx.triadic_census(...)

```python
tc1 = nx.triadic_census(G, nodelist={n})
```

### Step 6: Assign tc2 = value

```python
tc2 = {tt: sum((1 for t in tbt.get(tt, []) if n in t)) for tt in tc1}
```

**Verification:**
```python
assert tc1 == tc2
```

### Step 7: Assign ns = set(...)

```python
ns = set(ns)
```

### Step 8: Assign tc1 = nx.triadic_census(...)

```python
tc1 = nx.triadic_census(G, nodelist=ns)
```

### Step 9: Assign tc2 = value

```python
tc2 = {tt: sum((1 for t in tbt.get(tt, []) if any((n in ns for n in t)))) for tt in tc1}
```

**Verification:**
```python
assert tc1 == tc2
```

### Step 10: Assign ns = set(...)

```python
ns = set(ns)
```

### Step 11: Assign tc1 = nx.triadic_census(...)

```python
tc1 = nx.triadic_census(G, nodelist=ns)
```

### Step 12: Assign tc2 = value

```python
tc2 = {tt: sum((1 for t in tbt.get(tt, []) if any((n in ns for n in t)))) for tt in tc1}
```

**Verification:**
```python
assert tc1 == tc2
```


## Complete Example

```python
# Setup
# Fixtures: N

# Workflow
G = nx.binomial_graph(N, 0.3, directed=True, seed=42)
tc1 = nx.triadic_census(G)
tbt = nx.triads_by_type(G)
tc2 = {tt: len(tbt[tt]) for tt in tc1}
assert tc1 == tc2
for n in G:
    tc1 = nx.triadic_census(G, nodelist={n})
    tc2 = {tt: sum((1 for t in tbt.get(tt, []) if n in t)) for tt in tc1}
    assert tc1 == tc2
for ns in itertools.combinations(G, 2):
    ns = set(ns)
    tc1 = nx.triadic_census(G, nodelist=ns)
    tc2 = {tt: sum((1 for t in tbt.get(tt, []) if any((n in ns for n in t)))) for tt in tc1}
    assert tc1 == tc2
for ns in itertools.combinations(G, 3):
    ns = set(ns)
    tc1 = nx.triadic_census(G, nodelist=ns)
    tc2 = {tt: sum((1 for t in tbt.get(tt, []) if any((n in ns for n in t)))) for tt in tc1}
    assert tc1 == tc2
```

## Next Steps


---

*Source: test_triads.py:222 | Complexity: Advanced | Last updated: 2026-06-02*