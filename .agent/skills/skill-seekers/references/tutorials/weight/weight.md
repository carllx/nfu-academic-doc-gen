# How To: Weight

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test weight

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign inf = float(...)

```python
inf = float('inf')
```

**Verification:**
```python
assert set(nx.local_bridges(G, weight='weight')) == expected
```

### Step 2: Assign G = self.square.copy(...)

```python
G = self.square.copy()
```

**Verification:**
```python
assert set(lb) == expected
```

### Step 3: Assign unknown = 2

```python
G.edges[1, 2]['weight'] = 2
```

### Step 4: Assign expected = value

```python
expected = {(u, v, 5 - wt) for u, v, wt in G.edges(data='weight', default=1)}
```

**Verification:**
```python
assert set(nx.local_bridges(G, weight='weight')) == expected
```

### Step 5: Assign expected = value

```python
expected = {(u, v, 6) for u, v in G.edges}
```

### Step 6: Assign lb = nx.local_bridges(...)

```python
lb = nx.local_bridges(G, weight=lambda u, v, d: 2)
```

**Verification:**
```python
assert set(lb) == expected
```


## Complete Example

```python
# Workflow
inf = float('inf')
G = self.square.copy()
G.edges[1, 2]['weight'] = 2
expected = {(u, v, 5 - wt) for u, v, wt in G.edges(data='weight', default=1)}
assert set(nx.local_bridges(G, weight='weight')) == expected
expected = {(u, v, 6) for u, v in G.edges}
lb = nx.local_bridges(G, weight=lambda u, v, d: 2)
assert set(lb) == expected
```

## Next Steps


---

*Source: test_bridges.py:134 | Complexity: Intermediate | Last updated: 2026-06-02*