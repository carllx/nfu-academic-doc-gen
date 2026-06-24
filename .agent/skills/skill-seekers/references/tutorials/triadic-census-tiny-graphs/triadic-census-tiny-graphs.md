# How To: Triadic Census Tiny Graphs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test triadic census tiny graphs

## Prerequisites

**Required Modules:**
- `itertools`
- `collections`
- `random`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign tc = nx.triadic_census(...)

```python
tc = nx.triadic_census(nx.empty_graph(0, create_using=nx.DiGraph))
```

**Verification:**
```python
assert {} == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
```

### Step 2: Assign tc = nx.triadic_census(...)

```python
tc = nx.triadic_census(nx.empty_graph(1, create_using=nx.DiGraph))
```

**Verification:**
```python
assert {} == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
```

### Step 3: Assign tc = nx.triadic_census(...)

```python
tc = nx.triadic_census(nx.empty_graph(2, create_using=nx.DiGraph))
```

**Verification:**
```python
assert {} == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
```

### Step 4: Assign tc = nx.triadic_census(...)

```python
tc = nx.triadic_census(nx.DiGraph([(1, 2)]))
```

**Verification:**
```python
assert {} == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
```


## Complete Example

```python
# Workflow
tc = nx.triadic_census(nx.empty_graph(0, create_using=nx.DiGraph))
assert {} == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
tc = nx.triadic_census(nx.empty_graph(1, create_using=nx.DiGraph))
assert {} == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
tc = nx.triadic_census(nx.empty_graph(2, create_using=nx.DiGraph))
assert {} == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
tc = nx.triadic_census(nx.DiGraph([(1, 2)]))
assert {} == {typ: cnt for typ, cnt in tc.items() if cnt > 0}
```

## Next Steps


---

*Source: test_triads.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*