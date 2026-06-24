# How To: Outofrange Integers

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test outofrange integers

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `codecs`
- `io`
- `math`
- `ast`
- `contextlib`
- `textwrap`
- `pytest`
- `networkx`
- `networkx.readwrite.gml`
- `numpy`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert isinstance(value, str)
```

### Step 2: Assign numbers = value

```python
numbers = {'toosmall': -2 ** 31 - 1, 'small': -2 ** 31, 'med1': -4, 'med2': 0, 'med3': 17, 'big': 2 ** 31 - 1, 'toobig': 2 ** 31}
```

**Verification:**
```python
assert isinstance(value, int)
```

### Step 3: Call G.add_node()

```python
G.add_node('Node', **numbers)
```

### Step 4: Assign fname = value

```python
fname = tmp_path / 'test.gml'
```

### Step 5: Call nx.write_gml()

```python
nx.write_gml(G, fname)
```

### Step 6: Assign G2 = nx.read_gml(...)

```python
G2 = nx.read_gml(fname)
```

**Verification:**
```python
assert isinstance(value, str)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
G = nx.Graph()
numbers = {'toosmall': -2 ** 31 - 1, 'small': -2 ** 31, 'med1': -4, 'med2': 0, 'med3': 17, 'big': 2 ** 31 - 1, 'toobig': 2 ** 31}
G.add_node('Node', **numbers)
fname = tmp_path / 'test.gml'
nx.write_gml(G, fname)
G2 = nx.read_gml(fname)
for attr, value in G2.nodes['Node'].items():
    if attr == 'toosmall' or attr == 'toobig':
        assert isinstance(value, str)
    else:
        assert isinstance(value, int)
```

## Next Steps


---

*Source: test_gml.py:582 | Complexity: Intermediate | Last updated: 2026-06-02*