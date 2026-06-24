# How To: Stochastic Block Model

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test stochastic block model

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign sizes = value

```python
sizes = [75, 75, 300]
```

**Verification:**
```python
assert len(C) == 3
```

### Step 2: Assign probs = value

```python
probs = [[0.25, 0.05, 0.02], [0.05, 0.35, 0.07], [0.02, 0.07, 0.4]]
```

**Verification:**
```python
assert len(G) == 450
```

### Step 3: Assign G = nx.stochastic_block_model(...)

```python
G = nx.stochastic_block_model(sizes, probs, seed=0)
```

**Verification:**
```python
assert G.size() == 22160
```

### Step 4: Assign C = value

```python
C = G.graph['partition']
```

**Verification:**
```python
assert G.nodes == GG.nodes
```

### Step 5: Assign GG = nx.stochastic_block_model(...)

```python
GG = nx.stochastic_block_model(sizes, probs, range(450), seed=0)
```

**Verification:**
```python
assert G.nodes == GG.nodes
```

### Step 6: Assign sbm = value

```python
sbm = nx.stochastic_block_model
```

**Verification:**
```python
assert G.nodes == GG.nodes
```

### Step 7: Assign badnodelist = list(...)

```python
badnodelist = list(range(400))
```

**Verification:**
```python
assert G.nodes == GG.nodes
```

### Step 8: Assign badprobs1 = value

```python
badprobs1 = [[0.25, 0.05, 1.02], [0.05, 0.35, 0.07], [0.02, 0.07, 0.4]]
```

### Step 9: Assign badprobs2 = value

```python
badprobs2 = [[0.25, 0.05, 0.02], [0.05, -0.35, 0.07], [0.02, 0.07, 0.4]]
```

### Step 10: Assign probs_rect1 = value

```python
probs_rect1 = [[0.25, 0.05, 0.02], [0.05, -0.35, 0.07]]
```

### Step 11: Assign probs_rect2 = value

```python
probs_rect2 = [[0.25, 0.05], [0.05, -0.35], [0.02, 0.07]]
```

### Step 12: Assign asymprobs = value

```python
asymprobs = [[0.25, 0.05, 0.01], [0.05, -0.35, 0.07], [0.02, 0.07, 0.4]]
```

### Step 13: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, sbm, sizes, badprobs1)
```

### Step 14: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, sbm, sizes, badprobs2)
```

### Step 15: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, sbm, sizes, probs_rect1, directed=True)
```

### Step 16: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, sbm, sizes, probs_rect2, directed=True)
```

### Step 17: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, sbm, sizes, asymprobs, directed=False)
```

### Step 18: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, sbm, sizes, probs, badnodelist)
```

### Step 19: Assign nodelist = value

```python
nodelist = [0] + list(range(449))
```

### Step 20: Call pytest.raises()

```python
pytest.raises(nx.NetworkXException, sbm, sizes, probs, nodelist)
```

### Step 21: Assign GG = nx.stochastic_block_model(...)

```python
GG = nx.stochastic_block_model(sizes, probs, seed=0, selfloops=True)
```

**Verification:**
```python
assert G.nodes == GG.nodes
```

### Step 22: Assign GG = nx.stochastic_block_model(...)

```python
GG = nx.stochastic_block_model(sizes, probs, selfloops=True, directed=True)
```

**Verification:**
```python
assert G.nodes == GG.nodes
```

### Step 23: Assign GG = nx.stochastic_block_model(...)

```python
GG = nx.stochastic_block_model(sizes, probs, seed=0, sparse=False)
```

**Verification:**
```python
assert G.nodes == GG.nodes
```


## Complete Example

```python
# Workflow
sizes = [75, 75, 300]
probs = [[0.25, 0.05, 0.02], [0.05, 0.35, 0.07], [0.02, 0.07, 0.4]]
G = nx.stochastic_block_model(sizes, probs, seed=0)
C = G.graph['partition']
assert len(C) == 3
assert len(G) == 450
assert G.size() == 22160
GG = nx.stochastic_block_model(sizes, probs, range(450), seed=0)
assert G.nodes == GG.nodes
sbm = nx.stochastic_block_model
badnodelist = list(range(400))
badprobs1 = [[0.25, 0.05, 1.02], [0.05, 0.35, 0.07], [0.02, 0.07, 0.4]]
badprobs2 = [[0.25, 0.05, 0.02], [0.05, -0.35, 0.07], [0.02, 0.07, 0.4]]
probs_rect1 = [[0.25, 0.05, 0.02], [0.05, -0.35, 0.07]]
probs_rect2 = [[0.25, 0.05], [0.05, -0.35], [0.02, 0.07]]
asymprobs = [[0.25, 0.05, 0.01], [0.05, -0.35, 0.07], [0.02, 0.07, 0.4]]
pytest.raises(nx.NetworkXException, sbm, sizes, badprobs1)
pytest.raises(nx.NetworkXException, sbm, sizes, badprobs2)
pytest.raises(nx.NetworkXException, sbm, sizes, probs_rect1, directed=True)
pytest.raises(nx.NetworkXException, sbm, sizes, probs_rect2, directed=True)
pytest.raises(nx.NetworkXException, sbm, sizes, asymprobs, directed=False)
pytest.raises(nx.NetworkXException, sbm, sizes, probs, badnodelist)
nodelist = [0] + list(range(449))
pytest.raises(nx.NetworkXException, sbm, sizes, probs, nodelist)
GG = nx.stochastic_block_model(sizes, probs, seed=0, selfloops=True)
assert G.nodes == GG.nodes
GG = nx.stochastic_block_model(sizes, probs, selfloops=True, directed=True)
assert G.nodes == GG.nodes
GG = nx.stochastic_block_model(sizes, probs, seed=0, sparse=False)
assert G.nodes == GG.nodes
```

## Next Steps


---

*Source: test_community.py:185 | Complexity: Advanced | Last updated: 2026-06-02*