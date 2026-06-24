# How To: P3 Load

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test p3 load

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.P3
```

**Verification:**
```python
assert c[n] == pytest.approx(d[n], abs=0.001)
```

### Step 2: Assign c = nx.load_centrality(...)

```python
c = nx.load_centrality(G)
```

**Verification:**
```python
assert c == pytest.approx(1.0, abs=1e-07)
```

### Step 3: Assign d = value

```python
d = {0: 0.0, 1: 1.0, 2: 0.0}
```

**Verification:**
```python
assert c == pytest.approx(1.0, abs=1e-07)
```

### Step 4: Assign c = nx.load_centrality(...)

```python
c = nx.load_centrality(G, v=1)
```

**Verification:**
```python
assert c == pytest.approx(1.0, abs=1e-07)
```

### Step 5: Assign c = nx.load_centrality(...)

```python
c = nx.load_centrality(G, v=1, normalized=True)
```

**Verification:**
```python
assert c == pytest.approx(1.0, abs=1e-07)
```


## Complete Example

```python
# Workflow
G = self.P3
c = nx.load_centrality(G)
d = {0: 0.0, 1: 1.0, 2: 0.0}
for n in sorted(G):
    assert c[n] == pytest.approx(d[n], abs=0.001)
c = nx.load_centrality(G, v=1)
assert c == pytest.approx(1.0, abs=1e-07)
c = nx.load_centrality(G, v=1, normalized=True)
assert c == pytest.approx(1.0, abs=1e-07)
```

## Next Steps


---

*Source: test_load_centrality.py:63 | Complexity: Intermediate | Last updated: 2026-06-02*