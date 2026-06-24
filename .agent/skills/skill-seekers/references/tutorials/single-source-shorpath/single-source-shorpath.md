# How To: Single Source Shorpath

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single source shortest path

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign p = nx.shortest_path(...)

```python
p = nx.shortest_path(self.cycle, 0)
```

**Verification:**
```python
assert p[3] == [0, 1, 2, 3]
```

### Step 2: Assign p = nx.shortest_path(...)

```python
p = nx.shortest_path(self.grid, 1)
```

**Verification:**
```python
assert p == nx.single_source_shortest_path(self.cycle, 0)
```

### Step 3: Call validate_grid_path()

```python
validate_grid_path(4, 4, 1, 12, p[12])
```

**Verification:**
```python
assert p[3] == [0, 1, 2, 3]
```

### Step 4: Assign p = nx.shortest_path(...)

```python
p = nx.shortest_path(self.cycle, 0, weight='weight')
```

**Verification:**
```python
assert p == nx.single_source_dijkstra_path(self.cycle, 0)
```

### Step 5: Assign p = nx.shortest_path(...)

```python
p = nx.shortest_path(self.grid, 1, weight='weight')
```

**Verification:**
```python
assert p[3] == [0, 1, 2, 3]
```

### Step 6: Call validate_grid_path()

```python
validate_grid_path(4, 4, 1, 12, p[12])
```

**Verification:**
```python
assert p == nx.single_source_shortest_path(self.cycle, 0)
```

### Step 7: Assign p = nx.shortest_path(...)

```python
p = nx.shortest_path(self.cycle, 0, method='dijkstra', weight='weight')
```

**Verification:**
```python
assert p[3] == [0, 1, 2, 3]
```

### Step 8: Assign p = nx.shortest_path(...)

```python
p = nx.shortest_path(self.cycle, 0, method='bellman-ford', weight='weight')
```

**Verification:**
```python
assert p == nx.single_source_shortest_path(self.cycle, 0)
```


## Complete Example

```python
# Workflow
p = nx.shortest_path(self.cycle, 0)
assert p[3] == [0, 1, 2, 3]
assert p == nx.single_source_shortest_path(self.cycle, 0)
p = nx.shortest_path(self.grid, 1)
validate_grid_path(4, 4, 1, 12, p[12])
p = nx.shortest_path(self.cycle, 0, weight='weight')
assert p[3] == [0, 1, 2, 3]
assert p == nx.single_source_dijkstra_path(self.cycle, 0)
p = nx.shortest_path(self.grid, 1, weight='weight')
validate_grid_path(4, 4, 1, 12, p[12])
p = nx.shortest_path(self.cycle, 0, method='dijkstra', weight='weight')
assert p[3] == [0, 1, 2, 3]
assert p == nx.single_source_shortest_path(self.cycle, 0)
p = nx.shortest_path(self.cycle, 0, method='bellman-ford', weight='weight')
assert p[3] == [0, 1, 2, 3]
assert p == nx.single_source_shortest_path(self.cycle, 0)
```

## Next Steps


---

*Source: test_generic.py:190 | Complexity: Advanced | Last updated: 2026-06-02*