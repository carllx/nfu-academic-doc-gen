# How To: Dynamic Graph Has Timeformat

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Ensure that graphs which have a 'start' or 'stop' attribute get a
'timeformat' attribute upon parsing. See gh-7914.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `time`
- `pytest`
- `networkx`
- `math`

**Setup Required:**
```python
# Fixtures: time_attr, dyn_attr, tmp_path
```

## Step-by-Step Guide

### Step 1: "Ensure that graphs which have a 'start' or 'stop' attribute get a\n    'timeformat' attribute upon parsing. See gh-7914."

```python
"Ensure that graphs which have a 'start' or 'stop' attribute get a\n    'timeformat' attribute upon parsing. See gh-7914."
```

**Verification:**
```python
assert 'timeformat="long"' in fh.read()
```

### Step 2: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph(mode=dyn_attr)
```

**Verification:**
```python
assert H.graph['mode'] == 'dynamic'
```

### Step 3: Call G.add_node()

```python
G.add_node(0)
```

**Verification:**
```python
assert nx.utils.nodes_equal(G.edges, H.edges)
```

### Step 4: Assign unknown = 1

```python
G.nodes[0][time_attr] = 1
```

### Step 5: Assign fname = value

```python
fname = tmp_path / 'foo.gexf'
```

### Step 6: Call nx.write_gexf()

```python
nx.write_gexf(G, fname)
```

### Step 7: Assign H = nx.read_gexf(...)

```python
H = nx.read_gexf(fname)
```

**Verification:**
```python
assert H.graph['mode'] == 'dynamic'
```


## Complete Example

```python
# Setup
# Fixtures: time_attr, dyn_attr, tmp_path

# Workflow
"Ensure that graphs which have a 'start' or 'stop' attribute get a\n    'timeformat' attribute upon parsing. See gh-7914."
G = nx.MultiGraph(mode=dyn_attr)
G.add_node(0)
G.nodes[0][time_attr] = 1
fname = tmp_path / 'foo.gexf'
nx.write_gexf(G, fname)
with open(fname) as fh:
    assert 'timeformat="long"' in fh.read()
H = nx.read_gexf(fname)
assert H.graph['mode'] == 'dynamic'
assert nx.utils.nodes_equal(G.edges, H.edges)
```

## Next Steps


---

*Source: test_gexf.py:44 | Complexity: Intermediate | Last updated: 2026-06-02*