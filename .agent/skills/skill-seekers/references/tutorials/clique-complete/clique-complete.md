# How To: Clique Complete

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test clique complete

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.centrality`


## Step-by-Step Guide

### Step 1: Assign c = harmonic_centrality(...)

```python
c = harmonic_centrality(self.K5)
```

**Verification:**
```python
assert c[n] == pytest.approx(d[n], abs=0.001)
```

### Step 2: Assign d = value

```python
d = {0: 4, 1: 4, 2: 4, 3: 4, 4: 4}
```

**Verification:**
```python
assert c[n] == pytest.approx(d[n], abs=0.001)
```


## Complete Example

```python
# Workflow
c = harmonic_centrality(self.K5)
d = {0: 4, 1: 4, 2: 4, 3: 4, 4: 4}
for n in sorted(self.P3):
    assert c[n] == pytest.approx(d[n], abs=0.001)
```

## Next Steps


---

*Source: test_harmonic_centrality.py:40 | Complexity: Beginner | Last updated: 2026-06-02*