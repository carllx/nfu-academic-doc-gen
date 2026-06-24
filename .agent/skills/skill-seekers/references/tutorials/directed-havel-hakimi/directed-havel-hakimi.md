# How To: Directed Havel Hakimi

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed havel hakimi

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
n, r = (100, 10)
```

**Verification:**
```python
assert sorted(din1) == sorted(din2)
```

### Step 2: Assign p = value

```python
p = 1.0 / r
```

**Verification:**
```python
assert sorted(dout1) == sorted(dout2)
```

### Step 3: Assign dout = value

```python
dout = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
```

**Verification:**
```python
assert sorted(dout) == sorted(dout2)
```

### Step 4: Assign din = value

```python
din = [103, 102, 102, 102, 102, 102, 102, 102, 102, 102]
```

**Verification:**
```python
assert sorted(din) == sorted(din2)
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.exception.NetworkXError, nx.directed_havel_hakimi_graph, din, dout)
```

### Step 6: Assign dout = value

```python
dout = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
```

### Step 7: Assign din = value

```python
din = [2, 2, 2, 2, 2, 2, 2, 2, 0, 2]
```

### Step 8: Assign G2 = nx.directed_havel_hakimi_graph(...)

```python
G2 = nx.directed_havel_hakimi_graph(din, dout)
```

### Step 9: Assign dout2 = value

```python
dout2 = (d for n, d in G2.out_degree())
```

### Step 10: Assign din2 = value

```python
din2 = (d for n, d in G2.in_degree())
```

**Verification:**
```python
assert sorted(dout) == sorted(dout2)
```

### Step 11: Assign din = value

```python
din = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
```

### Step 12: Call pytest.raises()

```python
pytest.raises(nx.exception.NetworkXError, nx.directed_havel_hakimi_graph, din, dout)
```

### Step 13: Assign din = value

```python
din = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, -2]
```

### Step 14: Call pytest.raises()

```python
pytest.raises(nx.exception.NetworkXError, nx.directed_havel_hakimi_graph, din, dout)
```

### Step 15: Assign G1 = nx.erdos_renyi_graph(...)

```python
G1 = nx.erdos_renyi_graph(n, p * (i + 1), None, True)
```

### Step 16: Assign din1 = value

```python
din1 = [d for n, d in G1.in_degree()]
```

### Step 17: Assign dout1 = value

```python
dout1 = [d for n, d in G1.out_degree()]
```

### Step 18: Assign G2 = nx.directed_havel_hakimi_graph(...)

```python
G2 = nx.directed_havel_hakimi_graph(din1, dout1)
```

### Step 19: Assign din2 = value

```python
din2 = [d for n, d in G2.in_degree()]
```

### Step 20: Assign dout2 = value

```python
dout2 = [d for n, d in G2.out_degree()]
```

**Verification:**
```python
assert sorted(din1) == sorted(din2)
```


## Complete Example

```python
# Workflow
n, r = (100, 10)
p = 1.0 / r
for i in range(r):
    G1 = nx.erdos_renyi_graph(n, p * (i + 1), None, True)
    din1 = [d for n, d in G1.in_degree()]
    dout1 = [d for n, d in G1.out_degree()]
    G2 = nx.directed_havel_hakimi_graph(din1, dout1)
    din2 = [d for n, d in G2.in_degree()]
    dout2 = [d for n, d in G2.out_degree()]
    assert sorted(din1) == sorted(din2)
    assert sorted(dout1) == sorted(dout2)
dout = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
din = [103, 102, 102, 102, 102, 102, 102, 102, 102, 102]
pytest.raises(nx.exception.NetworkXError, nx.directed_havel_hakimi_graph, din, dout)
dout = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
din = [2, 2, 2, 2, 2, 2, 2, 2, 0, 2]
G2 = nx.directed_havel_hakimi_graph(din, dout)
dout2 = (d for n, d in G2.out_degree())
din2 = (d for n, d in G2.in_degree())
assert sorted(dout) == sorted(dout2)
assert sorted(din) == sorted(din2)
din = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
pytest.raises(nx.exception.NetworkXError, nx.directed_havel_hakimi_graph, din, dout)
din = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, -2]
pytest.raises(nx.exception.NetworkXError, nx.directed_havel_hakimi_graph, din, dout)
```

## Next Steps


---

*Source: test_degree_seq.py:128 | Complexity: Advanced | Last updated: 2026-06-02*