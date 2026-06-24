# How To: Mixing Backend Graphs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test mixing backend graphs

## Prerequisites

**Required Modules:**
- `pickle`
- `pytest`
- `networkx`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests.dispatch_interface`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert set(nx.intersection(G, H)) == {2, 3}
```

### Step 2: Call G.add_edge()

```python
G.add_edge(1, 2)
```

**Verification:**
```python
assert set(nx.intersection(G2, H)) == {2, 3}
```

### Step 3: Call G.add_edge()

```python
G.add_edge(2, 3)
```

**Verification:**
```python
assert set(nx.intersection(G, H2)) == {2, 3}
```

### Step 4: Assign H = nx.Graph(...)

```python
H = nx.Graph()
```

### Step 5: Call H.add_edge()

```python
H.add_edge(2, 3)
```

### Step 6: Assign rv = nx.intersection(...)

```python
rv = nx.intersection(G, H)
```

**Verification:**
```python
assert set(nx.intersection(G, H)) == {2, 3}
```

### Step 7: Assign G2 = dispatch_interface.convert(...)

```python
G2 = dispatch_interface.convert(G)
```

### Step 8: Assign H2 = dispatch_interface.convert(...)

```python
H2 = dispatch_interface.convert(H)
```

**Verification:**
```python
assert set(nx.intersection(G2, H)) == {2, 3}
```

### Step 9: Call nx.intersection()

```python
nx.intersection(G2, H)
```

### Step 10: Call nx.intersection()

```python
nx.intersection(G, H2)
```


## Complete Example

```python
# Workflow
from networkx.classes.tests import dispatch_interface
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
H = nx.Graph()
H.add_edge(2, 3)
rv = nx.intersection(G, H)
assert set(nx.intersection(G, H)) == {2, 3}
G2 = dispatch_interface.convert(G)
H2 = dispatch_interface.convert(H)
if 'nx_loopback' in nx.config.backend_priority:
    assert set(nx.intersection(G2, H)) == {2, 3}
    assert set(nx.intersection(G, H2)) == {2, 3}
elif not nx.config.backend_priority and 'nx_loopback' not in nx.config.backends:
    with pytest.raises(ImportError, match='backend is not installed'):
        nx.intersection(G2, H)
    with pytest.raises(ImportError, match='backend is not installed'):
        nx.intersection(G, H2)
```

## Next Steps


---

*Source: test_backends.py:136 | Complexity: Advanced | Last updated: 2026-06-02*