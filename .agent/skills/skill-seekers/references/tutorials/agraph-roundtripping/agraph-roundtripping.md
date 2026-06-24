# How To: Agraph Roundtripping

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test agraph roundtripping

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `warnings`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: G, tmp_path
```

## Step-by-Step Guide

### Step 1: Assign G = self.build_graph(...)

```python
G = self.build_graph(G)
```

### Step 2: Assign A = nx.nx_agraph.to_agraph(...)

```python
A = nx.nx_agraph.to_agraph(G)
```

### Step 3: Assign H = nx.nx_agraph.from_agraph(...)

```python
H = nx.nx_agraph.from_agraph(A)
```

### Step 4: Call self.assert_equal()

```python
self.assert_equal(G, H)
```

### Step 5: Assign fname = value

```python
fname = tmp_path / 'test.dot'
```

### Step 6: Call nx.drawing.nx_agraph.write_dot()

```python
nx.drawing.nx_agraph.write_dot(H, fname)
```

### Step 7: Assign Hin = nx.nx_agraph.read_dot(...)

```python
Hin = nx.nx_agraph.read_dot(fname)
```

### Step 8: Call self.assert_equal()

```python
self.assert_equal(H, Hin)
```

### Step 9: Assign fname = value

```python
fname = tmp_path / 'fh_test.dot'
```

### Step 10: Call self.assert_equal()

```python
self.assert_equal(H, Hin)
```

### Step 11: Call nx.drawing.nx_agraph.write_dot()

```python
nx.drawing.nx_agraph.write_dot(H, fh)
```

### Step 12: Assign Hin = nx.nx_agraph.read_dot(...)

```python
Hin = nx.nx_agraph.read_dot(fh)
```


## Complete Example

```python
# Setup
# Fixtures: G, tmp_path

# Workflow
G = self.build_graph(G)
A = nx.nx_agraph.to_agraph(G)
H = nx.nx_agraph.from_agraph(A)
self.assert_equal(G, H)
fname = tmp_path / 'test.dot'
nx.drawing.nx_agraph.write_dot(H, fname)
Hin = nx.nx_agraph.read_dot(fname)
self.assert_equal(H, Hin)
fname = tmp_path / 'fh_test.dot'
with open(fname, 'w') as fh:
    nx.drawing.nx_agraph.write_dot(H, fh)
with open(fname) as fh:
    Hin = nx.nx_agraph.read_dot(fh)
self.assert_equal(H, Hin)
```

## Next Steps


---

*Source: test_agraph.py:29 | Complexity: Advanced | Last updated: 2026-06-02*