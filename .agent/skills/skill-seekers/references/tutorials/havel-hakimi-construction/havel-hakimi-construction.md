# How To: Havel Hakimi Construction

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test havel hakimi construction

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.havel_hakimi_graph(...)

```python
G = nx.havel_hakimi_graph([])
```

**Verification:**
```python
assert len(G) == 0
```

### Step 2: Assign z = value

```python
z = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
```

### Step 3: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.havel_hakimi_graph, z)
```

### Step 4: Assign z = value

```python
z = ['A', 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.havel_hakimi_graph, z)
```

### Step 6: Assign z = value

```python
z = [5, 4, 3, 3, 3, 2, 2, 2]
```

### Step 7: Assign G = nx.havel_hakimi_graph(...)

```python
G = nx.havel_hakimi_graph(z)
```

### Step 8: Assign G = nx.configuration_model(...)

```python
G = nx.configuration_model(z)
```

### Step 9: Assign z = value

```python
z = [6, 5, 4, 4, 2, 1, 1, 1]
```

### Step 10: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.havel_hakimi_graph, z)
```

### Step 11: Assign z = value

```python
z = [10, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2]
```

### Step 12: Assign G = nx.havel_hakimi_graph(...)

```python
G = nx.havel_hakimi_graph(z)
```

### Step 13: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.havel_hakimi_graph, z, create_using=nx.DiGraph())
```


## Complete Example

```python
# Workflow
G = nx.havel_hakimi_graph([])
assert len(G) == 0
z = [1000, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
pytest.raises(nx.NetworkXError, nx.havel_hakimi_graph, z)
z = ['A', 3, 3, 3, 3, 2, 2, 2, 1, 1, 1]
pytest.raises(nx.NetworkXError, nx.havel_hakimi_graph, z)
z = [5, 4, 3, 3, 3, 2, 2, 2]
G = nx.havel_hakimi_graph(z)
G = nx.configuration_model(z)
z = [6, 5, 4, 4, 2, 1, 1, 1]
pytest.raises(nx.NetworkXError, nx.havel_hakimi_graph, z)
z = [10, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2]
G = nx.havel_hakimi_graph(z)
pytest.raises(nx.NetworkXError, nx.havel_hakimi_graph, z, create_using=nx.DiGraph())
```

## Next Steps


---

*Source: test_degree_seq.py:106 | Complexity: Advanced | Last updated: 2026-06-02*