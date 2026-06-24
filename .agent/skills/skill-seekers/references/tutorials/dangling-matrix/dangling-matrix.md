# How To: Dangling Matrix

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the google_matrix doesn't change except for the dangling
nodes.

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.link_analysis.pagerank_alg`
- `networkx.classes.tests`


## Step-by-Step Guide

### Step 1: "\n        Tests that the google_matrix doesn't change except for the dangling\n        nodes.\n        "

```python
"\n        Tests that the google_matrix doesn't change except for the dangling\n        nodes.\n        "
```

**Verification:**
```python
assert M2[i, j] == pytest.approx(dangling[j + 1] / dangling_sum, abs=0.0001)
```

### Step 2: Assign G = value

```python
G = self.G
```

**Verification:**
```python
assert M2[i, j] == pytest.approx(M1[i, j], abs=0.0001)
```

### Step 3: Assign dangling = value

```python
dangling = self.dangling_edges
```

### Step 4: Assign dangling_sum = sum(...)

```python
dangling_sum = sum(dangling.values())
```

### Step 5: Assign M1 = nx.google_matrix(...)

```python
M1 = nx.google_matrix(G, personalization=dangling)
```

### Step 6: Assign M2 = nx.google_matrix(...)

```python
M2 = nx.google_matrix(G, personalization=dangling, dangling=dangling)
```

**Verification:**
```python
assert M2[i, j] == pytest.approx(dangling[j + 1] / dangling_sum, abs=0.0001)
```


## Complete Example

```python
# Workflow
"\n        Tests that the google_matrix doesn't change except for the dangling\n        nodes.\n        "
G = self.G
dangling = self.dangling_edges
dangling_sum = sum(dangling.values())
M1 = nx.google_matrix(G, personalization=dangling)
M2 = nx.google_matrix(G, personalization=dangling, dangling=dangling)
for i in range(len(G)):
    for j in range(len(G)):
        if i == self.dangling_node_index and j + 1 in dangling:
            assert M2[i, j] == pytest.approx(dangling[j + 1] / dangling_sum, abs=0.0001)
        else:
            assert M2[i, j] == pytest.approx(M1[i, j], abs=0.0001)
```

## Next Steps


---

*Source: test_pagerank.py:141 | Complexity: Advanced | Last updated: 2026-06-02*