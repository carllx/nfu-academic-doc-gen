# How To: Find Cliques3

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test find cliques3

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign cl = list(...)

```python
cl = list(nx.find_cliques(self.G, [2]))
```

**Verification:**
```python
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
```

### Step 2: Assign rcl = nx.find_cliques_recursive(...)

```python
rcl = nx.find_cliques_recursive(self.G, [2])
```

**Verification:**
```python
assert sorted(map(sorted, cl)) == sorted(map(sorted, expected))
```

### Step 3: Assign expected = value

```python
expected = [[2, 6, 1, 3], [2, 6, 4]]
```

**Verification:**
```python
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
```

### Step 4: Assign cl = list(...)

```python
cl = list(nx.find_cliques(self.G, [2, 3]))
```

**Verification:**
```python
assert sorted(map(sorted, cl)) == sorted(map(sorted, expected))
```

### Step 5: Assign rcl = nx.find_cliques_recursive(...)

```python
rcl = nx.find_cliques_recursive(self.G, [2, 3])
```

**Verification:**
```python
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
```

### Step 6: Assign expected = value

```python
expected = [[2, 6, 1, 3]]
```

**Verification:**
```python
assert sorted(map(sorted, cl)) == sorted(map(sorted, expected))
```

### Step 7: Assign cl = list(...)

```python
cl = list(nx.find_cliques(self.G, [2, 6, 4]))
```

**Verification:**
```python
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
```

### Step 8: Assign rcl = nx.find_cliques_recursive(...)

```python
rcl = nx.find_cliques_recursive(self.G, [2, 6, 4])
```

**Verification:**
```python
assert sorted(map(sorted, cl)) == sorted(map(sorted, expected))
```

### Step 9: Assign expected = value

```python
expected = [[2, 6, 4]]
```

**Verification:**
```python
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
```

### Step 10: Assign cl = list(...)

```python
cl = list(nx.find_cliques(self.G, [2, 6, 4]))
```

### Step 11: Assign rcl = nx.find_cliques_recursive(...)

```python
rcl = nx.find_cliques_recursive(self.G, [2, 6, 4])
```

### Step 12: Assign expected = value

```python
expected = [[2, 6, 4]]
```

**Verification:**
```python
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
```

### Step 13: Call list()

```python
list(nx.find_cliques(self.G, [2, 6, 4, 1]))
```

### Step 14: Call list()

```python
list(nx.find_cliques_recursive(self.G, [2, 6, 4, 1]))
```


## Complete Example

```python
# Workflow
cl = list(nx.find_cliques(self.G, [2]))
rcl = nx.find_cliques_recursive(self.G, [2])
expected = [[2, 6, 1, 3], [2, 6, 4]]
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
assert sorted(map(sorted, cl)) == sorted(map(sorted, expected))
cl = list(nx.find_cliques(self.G, [2, 3]))
rcl = nx.find_cliques_recursive(self.G, [2, 3])
expected = [[2, 6, 1, 3]]
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
assert sorted(map(sorted, cl)) == sorted(map(sorted, expected))
cl = list(nx.find_cliques(self.G, [2, 6, 4]))
rcl = nx.find_cliques_recursive(self.G, [2, 6, 4])
expected = [[2, 6, 4]]
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
assert sorted(map(sorted, cl)) == sorted(map(sorted, expected))
cl = list(nx.find_cliques(self.G, [2, 6, 4]))
rcl = nx.find_cliques_recursive(self.G, [2, 6, 4])
expected = [[2, 6, 4]]
assert sorted(map(sorted, rcl)) == sorted(map(sorted, expected))
assert sorted(map(sorted, cl)) == sorted(map(sorted, expected))
with pytest.raises(ValueError):
    list(nx.find_cliques(self.G, [2, 6, 4, 1]))
with pytest.raises(ValueError):
    list(nx.find_cliques_recursive(self.G, [2, 6, 4, 1]))
```

## Next Steps


---

*Source: test_clique.py:37 | Complexity: Advanced | Last updated: 2026-06-02*