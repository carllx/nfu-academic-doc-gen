# How To: Incremental

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test incremental

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: undirected_G
```

## Step-by-Step Guide

### Step 1: Assign unknown = undirected_G

```python
G, _ = undirected_G
```

**Verification:**
```python
assert set(test_cc.items()) == set(real_cc.items())
```

### Step 2: Assign prev_cc = None

```python
prev_cc = None
```

### Step 3: Assign test_cc = nx.incremental_closeness_centrality(...)

```python
test_cc = nx.incremental_closeness_centrality(G, edge, prev_cc, insert)
```

### Step 4: Assign real_cc = nx.closeness_centrality(...)

```python
real_cc = nx.closeness_centrality(G)
```

**Verification:**
```python
assert set(test_cc.items()) == set(real_cc.items())
```

### Step 5: Assign prev_cc = test_cc

```python
prev_cc = test_cc
```

### Step 6: Assign insert = False

```python
insert = False
```

### Step 7: Assign edge = self.pick_remove_edge(...)

```python
edge = self.pick_remove_edge(G)
```

### Step 8: Assign insert = True

```python
insert = True
```

### Step 9: Assign edge = self.pick_add_edge(...)

```python
edge = self.pick_add_edge(G)
```

### Step 10: Call G.add_edges_from()

```python
G.add_edges_from([edge])
```

### Step 11: Call G.remove_edges_from()

```python
G.remove_edges_from([edge])
```


## Complete Example

```python
# Setup
# Fixtures: undirected_G

# Workflow
G, _ = undirected_G
prev_cc = None
for i in range(5):
    if i % 2 == 0:
        insert = False
        edge = self.pick_remove_edge(G)
    else:
        insert = True
        edge = self.pick_add_edge(G)
    test_cc = nx.incremental_closeness_centrality(G, edge, prev_cc, insert)
    if insert:
        G.add_edges_from([edge])
    else:
        G.remove_edges_from([edge])
    real_cc = nx.closeness_centrality(G)
    assert set(test_cc.items()) == set(real_cc.items())
    prev_cc = test_cc
```

## Next Steps


---

*Source: test_closeness_centrality.py:249 | Complexity: Advanced | Last updated: 2026-06-02*