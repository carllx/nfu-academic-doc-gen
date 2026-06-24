# How To: Wf Improved

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wf improved

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.union(...)

```python
G = nx.union(nx.path_graph(4), nx.path_graph([4, 5, 6]))
```

**Verification:**
```python
assert c[n] == pytest.approx(res[n], abs=0.001)
```

### Step 2: Assign c = nx.closeness_centrality(...)

```python
c = nx.closeness_centrality(G)
```

**Verification:**
```python
assert cwf[n] == pytest.approx(wf_res[n], abs=0.001)
```

### Step 3: Assign cwf = nx.closeness_centrality(...)

```python
cwf = nx.closeness_centrality(G, wf_improved=False)
```

### Step 4: Assign res = value

```python
res = {0: 0.25, 1: 0.375, 2: 0.375, 3: 0.25, 4: 0.222, 5: 0.333, 6: 0.222}
```

### Step 5: Assign wf_res = value

```python
wf_res = {0: 0.5, 1: 0.75, 2: 0.75, 3: 0.5, 4: 0.667, 5: 1.0, 6: 0.667}
```

**Verification:**
```python
assert c[n] == pytest.approx(res[n], abs=0.001)
```


## Complete Example

```python
# Workflow
G = nx.union(nx.path_graph(4), nx.path_graph([4, 5, 6]))
c = nx.closeness_centrality(G)
cwf = nx.closeness_centrality(G, wf_improved=False)
res = {0: 0.25, 1: 0.375, 2: 0.375, 3: 0.25, 4: 0.222, 5: 0.333, 6: 0.222}
wf_res = {0: 0.5, 1: 0.75, 2: 0.75, 3: 0.5, 4: 0.667, 5: 1.0, 6: 0.667}
for n in G:
    assert c[n] == pytest.approx(res[n], abs=0.001)
    assert cwf[n] == pytest.approx(wf_res[n], abs=0.001)
```

## Next Steps


---

*Source: test_closeness_centrality.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*