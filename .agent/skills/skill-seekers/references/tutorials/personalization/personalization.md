# How To: Personalization

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test personalization

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.link_analysis.pagerank_alg`
- `networkx.classes.tests`

**Setup Required:**
```python
# Fixtures: alg
```

## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

**Verification:**
```python
assert p[n] == pytest.approx(answer[n], abs=0.0001)
```

### Step 2: Assign personalize = value

```python
personalize = {0: 1, 1: 1, 2: 4, 3: 4}
```

### Step 3: Assign answer = value

```python
answer = {0: 0.23246732615667579, 1: 0.23246732615667579, 2: 0.267532673843324, 3: 0.2675326738433241}
```

### Step 4: Assign p = alg(...)

```python
p = alg(G, alpha=0.85, personalization=personalize)
```

**Verification:**
```python
assert p[n] == pytest.approx(answer[n], abs=0.0001)
```


## Complete Example

```python
# Setup
# Fixtures: alg

# Workflow
G = nx.complete_graph(4)
personalize = {0: 1, 1: 1, 2: 4, 3: 4}
answer = {0: 0.23246732615667579, 1: 0.23246732615667579, 2: 0.267532673843324, 3: 0.2675326738433241}
p = alg(G, alpha=0.85, personalization=personalize)
for n in G:
    assert p[n] == pytest.approx(answer[n], abs=0.0001)
```

## Next Steps


---

*Source: test_pagerank.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*