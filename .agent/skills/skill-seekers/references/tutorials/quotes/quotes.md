# How To: Quotes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quotes

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

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(1)
```

**Verification:**
```python
assert data == answer
```

### Step 2: Assign G.name = 'path_graph(1)'

```python
G.name = 'path_graph(1)'
```

### Step 3: Assign attr = value

```python
attr = 'This is "quoted" and this is a copyright: ' + chr(169)
```

### Step 4: Assign unknown = attr

```python
G.nodes[0]['demo'] = attr
```

### Step 5: Assign answer = 'graph [\n  name "path_graph(1)"\n  node [\n    id 0\n    label "0"\n    demo "This is &#34;quoted&#34; and this is a copyright: &#169;"\n  ]\n]'

```python
answer = 'graph [\n  name "path_graph(1)"\n  node [\n    id 0\n    label "0"\n    demo "This is &#34;quoted&#34; and this is a copyright: &#169;"\n  ]\n]'
```

**Verification:**
```python
assert data == answer
```

### Step 6: Call nx.write_gml()

```python
nx.write_gml(G, fobj)
```

### Step 7: Call fobj.seek()

```python
fobj.seek(0)
```

### Step 8: Assign data = fobj.read.strip.decode(...)

```python
data = fobj.read().strip().decode('ascii')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
G = nx.path_graph(1)
G.name = 'path_graph(1)'
attr = 'This is "quoted" and this is a copyright: ' + chr(169)
G.nodes[0]['demo'] = attr
with open(tmp_path / 'test.gml', 'w+b') as fobj:
    nx.write_gml(G, fobj)
    fobj.seek(0)
    data = fobj.read().strip().decode('ascii')
answer = 'graph [\n  name "path_graph(1)"\n  node [\n    id 0\n    label "0"\n    demo "This is &#34;quoted&#34; and this is a copyright: &#169;"\n  ]\n]'
assert data == answer
```

## Next Steps


---

*Source: test_gml.py:233 | Complexity: Advanced | Last updated: 2026-06-02*