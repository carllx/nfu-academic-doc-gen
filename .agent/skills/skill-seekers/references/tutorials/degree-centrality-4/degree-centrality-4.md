# How To: Degree Centrality 4

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test degree centrality 4

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign d = nx.degree_centrality(...)

```python
d = nx.degree_centrality(self.F)
```

**Verification:**
```python
assert exact[n] == pytest.approx(float(f'{dc:.3f}'), abs=1e-07)
```

### Step 2: Assign names = sorted(...)

```python
names = sorted(self.F.nodes())
```

### Step 3: Assign dcs = value

```python
dcs = [0.071, 0.214, 0.143, 0.214, 0.214, 0.071, 0.286, 0.071, 0.429, 0.071, 0.214, 0.214, 0.143, 0.286, 0.214]
```

### Step 4: Assign exact = dict(...)

```python
exact = dict(zip(names, dcs))
```

**Verification:**
```python
assert exact[n] == pytest.approx(float(f'{dc:.3f}'), abs=1e-07)
```


## Complete Example

```python
# Workflow
d = nx.degree_centrality(self.F)
names = sorted(self.F.nodes())
dcs = [0.071, 0.214, 0.143, 0.214, 0.214, 0.071, 0.286, 0.071, 0.429, 0.071, 0.214, 0.214, 0.143, 0.286, 0.214]
exact = dict(zip(names, dcs))
for n, dc in d.items():
    assert exact[n] == pytest.approx(float(f'{dc:.3f}'), abs=1e-07)
```

## Next Steps


---

*Source: test_degree_centrality.py:79 | Complexity: Intermediate | Last updated: 2026-06-02*