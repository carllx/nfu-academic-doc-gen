# How To: Extended Barabasi Albert

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the extended BA random graph generated behaves consistently.

Tests the exceptions are raised as expected.

The graphs generation are repeated several times to prevent lucky-shots

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: m
```

## Step-by-Step Guide

### Step 1: '\n        Tests that the extended BA random graph generated behaves consistently.\n\n        Tests the exceptions are raised as expected.\n\n        The graphs generation are repeated several times to prevent lucky-shots\n\n        '

```python
'\n        Tests that the extended BA random graph generated behaves consistently.\n\n        Tests the exceptions are raised as expected.\n\n        The graphs generation are repeated several times to prevent lucky-shots\n\n        '
```

**Verification:**
```python
assert G1.size() == BA_model_edges
```

### Step 2: Assign seeds = value

```python
seeds = [42, 314, 2718]
```

**Verification:**
```python
assert G1.size() > BA_model_edges * 2
```

### Step 3: Assign ebag = value

```python
ebag = nx.extended_barabasi_albert_graph
```

**Verification:**
```python
assert G2.size() == BA_model_edges
```

### Step 4: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, ebag, m, m, 0, 0)
```

**Verification:**
```python
assert G3.size() > G2.size()
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, ebag, 1, 0.5, 0, 0)
```

**Verification:**
```python
assert G3.size() < G1.size()
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, ebag, 100, 2, 0.5, 0.5)
```

### Step 7: Assign BA_model = nx.barabasi_albert_graph(...)

```python
BA_model = nx.barabasi_albert_graph(100, m, seed)
```

### Step 8: Assign BA_model_edges = BA_model.number_of_edges(...)

```python
BA_model_edges = BA_model.number_of_edges()
```

### Step 9: Assign G1 = nx.extended_barabasi_albert_graph(...)

```python
G1 = nx.extended_barabasi_albert_graph(100, m, 0, 0, seed)
```

**Verification:**
```python
assert G1.size() == BA_model_edges
```

### Step 10: Assign G1 = nx.extended_barabasi_albert_graph(...)

```python
G1 = nx.extended_barabasi_albert_graph(100, m, 0.8, 0, seed)
```

**Verification:**
```python
assert G1.size() > BA_model_edges * 2
```

### Step 11: Assign G2 = nx.extended_barabasi_albert_graph(...)

```python
G2 = nx.extended_barabasi_albert_graph(100, m, 0, 0.8, seed)
```

**Verification:**
```python
assert G2.size() == BA_model_edges
```

### Step 12: Assign G3 = nx.extended_barabasi_albert_graph(...)

```python
G3 = nx.extended_barabasi_albert_graph(100, m, 0.3, 0.3, seed)
```

**Verification:**
```python
assert G3.size() > G2.size()
```


## Complete Example

```python
# Setup
# Fixtures: m

# Workflow
'\n        Tests that the extended BA random graph generated behaves consistently.\n\n        Tests the exceptions are raised as expected.\n\n        The graphs generation are repeated several times to prevent lucky-shots\n\n        '
seeds = [42, 314, 2718]
for seed in seeds:
    BA_model = nx.barabasi_albert_graph(100, m, seed)
    BA_model_edges = BA_model.number_of_edges()
    G1 = nx.extended_barabasi_albert_graph(100, m, 0, 0, seed)
    assert G1.size() == BA_model_edges
    G1 = nx.extended_barabasi_albert_graph(100, m, 0.8, 0, seed)
    assert G1.size() > BA_model_edges * 2
    G2 = nx.extended_barabasi_albert_graph(100, m, 0, 0.8, seed)
    assert G2.size() == BA_model_edges
    G3 = nx.extended_barabasi_albert_graph(100, m, 0.3, 0.3, seed)
    assert G3.size() > G2.size()
    assert G3.size() < G1.size()
ebag = nx.extended_barabasi_albert_graph
pytest.raises(nx.NetworkXError, ebag, m, m, 0, 0)
pytest.raises(nx.NetworkXError, ebag, 1, 0.5, 0, 0)
pytest.raises(nx.NetworkXError, ebag, 100, 2, 0.5, 0.5)
```

## Next Steps


---

*Source: test_random_graphs.py:220 | Complexity: Advanced | Last updated: 2026-06-02*