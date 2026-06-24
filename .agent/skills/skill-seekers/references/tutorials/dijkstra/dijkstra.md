# How To: Dijkstra

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dijkstra

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `random`


## Step-by-Step Guide

### Step 1: Assign unknown = nx.single_source_dijkstra(...)

```python
D, P = nx.single_source_dijkstra(self.XG, 's')
```

**Verification:**
```python
assert D['v'] == 9
```

### Step 2: Call validate_path()

```python
validate_path(self.XG, 's', 'v', 9, P['v'])
```

**Verification:**
```python
assert nx.single_source_dijkstra_path_length(self.XG, 's')['v'] == 9
```

### Step 3: Call validate_path()

```python
validate_path(self.XG, 's', 'v', 9, nx.single_source_dijkstra_path(self.XG, 's')['v'])
```

**Verification:**
```python
assert D['v'] == 8
```

### Step 4: Call validate_path()

```python
validate_path(self.XG, 's', 'v', 9, nx.single_source_dijkstra(self.XG, 's')[1]['v'])
```

**Verification:**
```python
assert nx.dijkstra_path_length(GG, 's', 'v') == 8
```

### Step 5: Call validate_path()

```python
validate_path(self.MXG, 's', 'v', 9, nx.single_source_dijkstra_path(self.MXG, 's')['v'])
```

**Verification:**
```python
assert nx.dijkstra_path_length(self.XG3, 0, 3) == 15
```

### Step 6: Assign GG = self.XG.to_undirected(...)

```python
GG = self.XG.to_undirected()
```

**Verification:**
```python
assert nx.dijkstra_path_length(self.XG4, 0, 2) == 4
```

### Step 7: Assign unknown = 2

```python
GG['u']['x']['weight'] = 2
```

**Verification:**
```python
assert nx.dijkstra_path_length(self.G, 's', 'v') == 2
```

### Step 8: Assign unknown = nx.single_source_dijkstra(...)

```python
D, P = nx.single_source_dijkstra(GG, 's')
```

**Verification:**
```python
assert nx.single_source_dijkstra(self.cycle, 0, 0) == (0, [0])
```

### Step 9: Call validate_path()

```python
validate_path(GG, 's', 'v', 8, P['v'])
```

**Verification:**
```python
assert D['v'] == 8
```

### Step 10: Call validate_path()

```python
validate_path(GG, 's', 'v', 8, nx.dijkstra_path(GG, 's', 'v'))
```

**Verification:**
```python
assert nx.dijkstra_path_length(GG, 's', 'v') == 8
```

### Step 11: Call validate_path()

```python
validate_path(self.XG2, 1, 3, 4, nx.dijkstra_path(self.XG2, 1, 3))
```

### Step 12: Call validate_path()

```python
validate_path(self.XG3, 0, 3, 15, nx.dijkstra_path(self.XG3, 0, 3))
```

**Verification:**
```python
assert nx.dijkstra_path_length(self.XG3, 0, 3) == 15
```

### Step 13: Call validate_path()

```python
validate_path(self.XG4, 0, 2, 4, nx.dijkstra_path(self.XG4, 0, 2))
```

**Verification:**
```python
assert nx.dijkstra_path_length(self.XG4, 0, 2) == 4
```

### Step 14: Call validate_path()

```python
validate_path(self.MXG4, 0, 2, 4, nx.dijkstra_path(self.MXG4, 0, 2))
```

### Step 15: Call validate_path()

```python
validate_path(self.G, 's', 'v', 2, nx.single_source_dijkstra(self.G, 's', 'v')[1])
```

### Step 16: Call validate_path()

```python
validate_path(self.G, 's', 'v', 2, nx.single_source_dijkstra(self.G, 's')[1]['v'])
```

### Step 17: Call validate_path()

```python
validate_path(self.G, 's', 'v', 2, nx.dijkstra_path(self.G, 's', 'v'))
```

**Verification:**
```python
assert nx.dijkstra_path_length(self.G, 's', 'v') == 2
```

### Step 18: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNoPath, nx.dijkstra_path, self.G, 's', 'moon')
```

### Step 19: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNoPath, nx.dijkstra_path_length, self.G, 's', 'moon')
```

### Step 20: Call validate_path()

```python
validate_path(self.cycle, 0, 3, 3, nx.dijkstra_path(self.cycle, 0, 3))
```

### Step 21: Call validate_path()

```python
validate_path(self.cycle, 0, 4, 3, nx.dijkstra_path(self.cycle, 0, 4))
```

**Verification:**
```python
assert nx.single_source_dijkstra(self.cycle, 0, 0) == (0, [0])
```


## Complete Example

```python
# Workflow
D, P = nx.single_source_dijkstra(self.XG, 's')
validate_path(self.XG, 's', 'v', 9, P['v'])
assert D['v'] == 9
validate_path(self.XG, 's', 'v', 9, nx.single_source_dijkstra_path(self.XG, 's')['v'])
assert nx.single_source_dijkstra_path_length(self.XG, 's')['v'] == 9
validate_path(self.XG, 's', 'v', 9, nx.single_source_dijkstra(self.XG, 's')[1]['v'])
validate_path(self.MXG, 's', 'v', 9, nx.single_source_dijkstra_path(self.MXG, 's')['v'])
GG = self.XG.to_undirected()
GG['u']['x']['weight'] = 2
D, P = nx.single_source_dijkstra(GG, 's')
validate_path(GG, 's', 'v', 8, P['v'])
assert D['v'] == 8
validate_path(GG, 's', 'v', 8, nx.dijkstra_path(GG, 's', 'v'))
assert nx.dijkstra_path_length(GG, 's', 'v') == 8
validate_path(self.XG2, 1, 3, 4, nx.dijkstra_path(self.XG2, 1, 3))
validate_path(self.XG3, 0, 3, 15, nx.dijkstra_path(self.XG3, 0, 3))
assert nx.dijkstra_path_length(self.XG3, 0, 3) == 15
validate_path(self.XG4, 0, 2, 4, nx.dijkstra_path(self.XG4, 0, 2))
assert nx.dijkstra_path_length(self.XG4, 0, 2) == 4
validate_path(self.MXG4, 0, 2, 4, nx.dijkstra_path(self.MXG4, 0, 2))
validate_path(self.G, 's', 'v', 2, nx.single_source_dijkstra(self.G, 's', 'v')[1])
validate_path(self.G, 's', 'v', 2, nx.single_source_dijkstra(self.G, 's')[1]['v'])
validate_path(self.G, 's', 'v', 2, nx.dijkstra_path(self.G, 's', 'v'))
assert nx.dijkstra_path_length(self.G, 's', 'v') == 2
pytest.raises(nx.NetworkXNoPath, nx.dijkstra_path, self.G, 's', 'moon')
pytest.raises(nx.NetworkXNoPath, nx.dijkstra_path_length, self.G, 's', 'moon')
validate_path(self.cycle, 0, 3, 3, nx.dijkstra_path(self.cycle, 0, 3))
validate_path(self.cycle, 0, 4, 3, nx.dijkstra_path(self.cycle, 0, 4))
assert nx.single_source_dijkstra(self.cycle, 0, 0) == (0, [0])
```

## Next Steps


---

*Source: test_weighted.py:113 | Complexity: Advanced | Last updated: 2026-06-02*