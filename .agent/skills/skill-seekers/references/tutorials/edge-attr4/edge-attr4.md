# How To: Edge Attr4

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test edge attr4

## Prerequisites

**Required Modules:**
- `gc`
- `pickle`
- `platform`
- `weakref`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = self.Graph(...)

```python
G = self.Graph()
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), [(1, 2, {'data': 7, 'spam': 'bar', 'bar': 'foo'})])
```

### Step 2: Call G.add_edge()

```python
G.add_edge(1, 2, data=7, spam='bar', bar='foo')
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), [(1, 2, {'data': 10, 'spam': 'bar', 'bar': 'foo'})])
```

### Step 3: Assign unknown = 10

```python
G[1][2]['data'] = 10
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), [(1, 2, {'data': 20, 'spam': 'bar', 'bar': 'foo'})])
```

### Step 4: Assign unknown = 20

```python
G.adj[1][2]['data'] = 20
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), [(1, 2, {'data': 21, 'spam': 'bar', 'bar': 'foo'})])
```

### Step 5: Assign unknown = 21

```python
G.edges[1, 2]['data'] = 21
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), [(1, 2, dd)])
```

### Step 6: Assign unknown = value

```python
G.adj[1][2]['listdata'] = [20, 200]
```

### Step 7: Assign unknown = 20

```python
G.adj[1][2]['weight'] = 20
```

### Step 8: Assign dd = value

```python
dd = {'data': 21, 'spam': 'bar', 'bar': 'foo', 'listdata': [20, 200], 'weight': 20}
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), [(1, 2, dd)])
```


## Complete Example

```python
# Workflow
G = self.Graph()
G.add_edge(1, 2, data=7, spam='bar', bar='foo')
assert edges_equal(G.edges(data=True), [(1, 2, {'data': 7, 'spam': 'bar', 'bar': 'foo'})])
G[1][2]['data'] = 10
assert edges_equal(G.edges(data=True), [(1, 2, {'data': 10, 'spam': 'bar', 'bar': 'foo'})])
G.adj[1][2]['data'] = 20
assert edges_equal(G.edges(data=True), [(1, 2, {'data': 20, 'spam': 'bar', 'bar': 'foo'})])
G.edges[1, 2]['data'] = 21
assert edges_equal(G.edges(data=True), [(1, 2, {'data': 21, 'spam': 'bar', 'bar': 'foo'})])
G.adj[1][2]['listdata'] = [20, 200]
G.adj[1][2]['weight'] = 20
dd = {'data': 21, 'spam': 'bar', 'bar': 'foo', 'listdata': [20, 200], 'weight': 20}
assert edges_equal(G.edges(data=True), [(1, 2, dd)])
```

## Next Steps


---

*Source: test_graph.py:470 | Complexity: Advanced | Last updated: 2026-06-02*