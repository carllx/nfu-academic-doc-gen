# How To: Triadic Census Four Path Nodelist

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test triadic census four path nodelist

## Prerequisites

**Required Modules:**
- `itertools`
- `collections`
- `random`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph('abcd', create_using=nx.DiGraph)
```

**Verification:**
```python
assert expected_end == {typ: cnt for typ, cnt in a_triad_census.items() if cnt > 0}
```

### Step 2: Assign expected_end = value

```python
expected_end = {'012': 2, '021C': 1}
```

**Verification:**
```python
assert expected_mid == {typ: cnt for typ, cnt in b_triad_census.items() if cnt > 0}
```

### Step 3: Assign expected_mid = value

```python
expected_mid = {'012': 1, '021C': 2}
```

**Verification:**
```python
assert expected_mid == {typ: cnt for typ, cnt in c_triad_census.items() if cnt > 0}
```

### Step 4: Assign a_triad_census = nx.triadic_census(...)

```python
a_triad_census = nx.triadic_census(G, nodelist=['a'])
```

**Verification:**
```python
assert expected_end == {typ: cnt for typ, cnt in d_triad_census.items() if cnt > 0}
```

### Step 5: Assign b_triad_census = nx.triadic_census(...)

```python
b_triad_census = nx.triadic_census(G, nodelist=['b'])
```

**Verification:**
```python
assert expected_mid == {typ: cnt for typ, cnt in b_triad_census.items() if cnt > 0}
```

### Step 6: Assign c_triad_census = nx.triadic_census(...)

```python
c_triad_census = nx.triadic_census(G, nodelist=['c'])
```

**Verification:**
```python
assert expected_mid == {typ: cnt for typ, cnt in c_triad_census.items() if cnt > 0}
```

### Step 7: Assign d_triad_census = nx.triadic_census(...)

```python
d_triad_census = nx.triadic_census(G, nodelist=['d'])
```

**Verification:**
```python
assert expected_end == {typ: cnt for typ, cnt in d_triad_census.items() if cnt > 0}
```


## Complete Example

```python
# Workflow
G = nx.path_graph('abcd', create_using=nx.DiGraph)
expected_end = {'012': 2, '021C': 1}
expected_mid = {'012': 1, '021C': 2}
a_triad_census = nx.triadic_census(G, nodelist=['a'])
assert expected_end == {typ: cnt for typ, cnt in a_triad_census.items() if cnt > 0}
b_triad_census = nx.triadic_census(G, nodelist=['b'])
assert expected_mid == {typ: cnt for typ, cnt in b_triad_census.items() if cnt > 0}
c_triad_census = nx.triadic_census(G, nodelist=['c'])
assert expected_mid == {typ: cnt for typ, cnt in c_triad_census.items() if cnt > 0}
d_triad_census = nx.triadic_census(G, nodelist=['d'])
assert expected_end == {typ: cnt for typ, cnt in d_triad_census.items() if cnt > 0}
```

## Next Steps


---

*Source: test_triads.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*