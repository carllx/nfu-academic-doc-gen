# How To: Dual Barabasi Albert

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the dual BA random graph generated behaves consistently.

Tests the exceptions are raised as expected.

The graphs generation are repeated several times to prevent lucky shots

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: m1, m2, p
```

## Step-by-Step Guide

### Step 1: '\n        Tests that the dual BA random graph generated behaves consistently.\n\n        Tests the exceptions are raised as expected.\n\n        The graphs generation are repeated several times to prevent lucky shots\n\n        '

```python
'\n        Tests that the dual BA random graph generated behaves consistently.\n\n        Tests the exceptions are raised as expected.\n\n        The graphs generation are repeated several times to prevent lucky shots\n\n        '
```

**Verification:**
```python
assert BA1.edges() == DBA1.edges()
```

### Step 2: Assign seeds = value

```python
seeds = [42, 314, 2718]
```

**Verification:**
```python
assert BA2.edges() == DBA2.edges()
```

### Step 3: Assign initial_graph = nx.complete_graph(...)

```python
initial_graph = nx.complete_graph(10)
```

**Verification:**
```python
assert BA3.size() == DBA3.size()
```

### Step 4: Assign dbag = value

```python
dbag = nx.dual_barabasi_albert_graph
```

**Verification:**
```python
assert min(BA1.size(), BA2.size()) <= DBA.size() <= max(BA1.size(), BA2.size())
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, dbag, m1, m1, m2, 0)
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, dbag, m2, m1, m2, 0)
```

### Step 7: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, dbag, 100, m1, m2, -0.5)
```

### Step 8: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, dbag, 100, m1, m2, 1.5)
```

### Step 9: Assign initial = nx.complete_graph(...)

```python
initial = nx.complete_graph(max(m1, m2) - 1)
```

### Step 10: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, dbag, 100, m1, m2, p, initial_graph=initial)
```

### Step 11: Assign BA1 = nx.barabasi_albert_graph(...)

```python
BA1 = nx.barabasi_albert_graph(100, m1, seed)
```

### Step 12: Assign DBA1 = nx.dual_barabasi_albert_graph(...)

```python
DBA1 = nx.dual_barabasi_albert_graph(100, m1, m2, 1, seed)
```

**Verification:**
```python
assert BA1.edges() == DBA1.edges()
```

### Step 13: Assign BA2 = nx.barabasi_albert_graph(...)

```python
BA2 = nx.barabasi_albert_graph(100, m2, seed)
```

### Step 14: Assign DBA2 = nx.dual_barabasi_albert_graph(...)

```python
DBA2 = nx.dual_barabasi_albert_graph(100, m1, m2, 0, seed)
```

**Verification:**
```python
assert BA2.edges() == DBA2.edges()
```

### Step 15: Assign BA3 = nx.barabasi_albert_graph(...)

```python
BA3 = nx.barabasi_albert_graph(100, m1, seed)
```

### Step 16: Assign DBA3 = nx.dual_barabasi_albert_graph(...)

```python
DBA3 = nx.dual_barabasi_albert_graph(100, m1, m1, p, seed)
```

**Verification:**
```python
assert BA3.size() == DBA3.size()
```

### Step 17: Assign DBA = nx.dual_barabasi_albert_graph(...)

```python
DBA = nx.dual_barabasi_albert_graph(100, m1, m2, p, seed, initial_graph)
```

### Step 18: Assign BA1 = nx.barabasi_albert_graph(...)

```python
BA1 = nx.barabasi_albert_graph(100, m1, seed, initial_graph)
```

### Step 19: Assign BA2 = nx.barabasi_albert_graph(...)

```python
BA2 = nx.barabasi_albert_graph(100, m2, seed, initial_graph)
```

**Verification:**
```python
assert min(BA1.size(), BA2.size()) <= DBA.size() <= max(BA1.size(), BA2.size())
```


## Complete Example

```python
# Setup
# Fixtures: m1, m2, p

# Workflow
'\n        Tests that the dual BA random graph generated behaves consistently.\n\n        Tests the exceptions are raised as expected.\n\n        The graphs generation are repeated several times to prevent lucky shots\n\n        '
seeds = [42, 314, 2718]
initial_graph = nx.complete_graph(10)
for seed in seeds:
    BA1 = nx.barabasi_albert_graph(100, m1, seed)
    DBA1 = nx.dual_barabasi_albert_graph(100, m1, m2, 1, seed)
    assert BA1.edges() == DBA1.edges()
    BA2 = nx.barabasi_albert_graph(100, m2, seed)
    DBA2 = nx.dual_barabasi_albert_graph(100, m1, m2, 0, seed)
    assert BA2.edges() == DBA2.edges()
    BA3 = nx.barabasi_albert_graph(100, m1, seed)
    DBA3 = nx.dual_barabasi_albert_graph(100, m1, m1, p, seed)
    assert BA3.size() == DBA3.size()
    DBA = nx.dual_barabasi_albert_graph(100, m1, m2, p, seed, initial_graph)
    BA1 = nx.barabasi_albert_graph(100, m1, seed, initial_graph)
    BA2 = nx.barabasi_albert_graph(100, m2, seed, initial_graph)
    assert min(BA1.size(), BA2.size()) <= DBA.size() <= max(BA1.size(), BA2.size())
dbag = nx.dual_barabasi_albert_graph
pytest.raises(nx.NetworkXError, dbag, m1, m1, m2, 0)
pytest.raises(nx.NetworkXError, dbag, m2, m1, m2, 0)
pytest.raises(nx.NetworkXError, dbag, 100, m1, m2, -0.5)
pytest.raises(nx.NetworkXError, dbag, 100, m1, m2, 1.5)
initial = nx.complete_graph(max(m1, m2) - 1)
pytest.raises(nx.NetworkXError, dbag, 100, m1, m2, p, initial_graph=initial)
```

## Next Steps


---

*Source: test_random_graphs.py:175 | Complexity: Advanced | Last updated: 2026-06-02*