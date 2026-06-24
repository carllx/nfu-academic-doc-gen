# How To: Data Types

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test data types

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [True, False, 10 ** 20, -2e+33, "'", '"&&amp;&&#34;"', [{(b'\xfd',): '\x7f', chr(17476): (1, 2)}, (2, '3')]]
```

**Verification:**
```python
assert data == G.name
```

### Step 2: Call data.append()

```python
data.append(chr(83012))
```

**Verification:**
```python
assert {'name': data, 'data': data} == G.graph
```

### Step 3: Call data.append()

```python
data.append(literal_eval('{2.3j, 1 - 2.3j, ()}'))
```

**Verification:**
```python
assert list(G.nodes(data=True)) == [(0, {'int': -1, 'data': {'data': data}})]
```

### Step 4: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert list(G.edges(data=True)) == [(0, 0, {'float': -2.5, 'data': data})]
```

### Step 5: Assign G.name = data

```python
G.name = data
```

**Verification:**
```python
assert G.graph['data'] == 'frozenset([1, 2, 3])'
```

### Step 6: Assign unknown = data

```python
G.graph['data'] = data
```

### Step 7: Call G.add_node()

```python
G.add_node(0, int=-1, data={'data': data})
```

### Step 8: Call G.add_edge()

```python
G.add_edge(0, 0, float=-2.5, data=data)
```

### Step 9: Assign gml = unknown.join(...)

```python
gml = '\n'.join(nx.generate_gml(G, stringizer=literal_stringizer))
```

### Step 10: Assign G = nx.parse_gml(...)

```python
G = nx.parse_gml(gml, destringizer=literal_destringizer)
```

**Verification:**
```python
assert data == G.name
```

### Step 11: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 12: Assign unknown = 'frozenset([1, 2, 3])'

```python
G.graph['data'] = 'frozenset([1, 2, 3])'
```

### Step 13: Assign G = nx.parse_gml(...)

```python
G = nx.parse_gml(nx.generate_gml(G), destringizer=literal_eval)
```

**Verification:**
```python
assert G.graph['data'] == 'frozenset([1, 2, 3])'
```


## Complete Example

```python
# Workflow
data = [True, False, 10 ** 20, -2e+33, "'", '"&&amp;&&#34;"', [{(b'\xfd',): '\x7f', chr(17476): (1, 2)}, (2, '3')]]
data.append(chr(83012))
data.append(literal_eval('{2.3j, 1 - 2.3j, ()}'))
G = nx.Graph()
G.name = data
G.graph['data'] = data
G.add_node(0, int=-1, data={'data': data})
G.add_edge(0, 0, float=-2.5, data=data)
gml = '\n'.join(nx.generate_gml(G, stringizer=literal_stringizer))
G = nx.parse_gml(gml, destringizer=literal_destringizer)
assert data == G.name
assert {'name': data, 'data': data} == G.graph
assert list(G.nodes(data=True)) == [(0, {'int': -1, 'data': {'data': data}})]
assert list(G.edges(data=True)) == [(0, 0, {'float': -2.5, 'data': data})]
G = nx.Graph()
G.graph['data'] = 'frozenset([1, 2, 3])'
G = nx.parse_gml(nx.generate_gml(G), destringizer=literal_eval)
assert G.graph['data'] == 'frozenset([1, 2, 3])'
```

## Next Steps


---

*Source: test_gml.py:430 | Complexity: Advanced | Last updated: 2026-06-02*