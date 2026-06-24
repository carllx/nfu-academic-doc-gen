# How To: Graph New Extra Args

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that subclasses can accept additional arguments.

See: https://github.com/networkx/networkx/issues/8367

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

### Step 1: 'Test that subclasses can accept additional arguments.\n\n    See: https://github.com/networkx/networkx/issues/8367\n    '

```python
'Test that subclasses can accept additional arguments.\n\n    See: https://github.com/networkx/networkx/issues/8367\n    '
```

**Verification:**
```python
assert G.extra_arg == 'extra arg'
```

### Step 2: Assign G = MyGraph(...)

```python
G = MyGraph(extra_arg='extra arg')
```

**Verification:**
```python
assert G.extra_arg == 'extra arg'
```

### Step 3: Assign G = MyGraph(...)

```python
G = MyGraph([], 'extra arg')
```

**Verification:**
```python
assert G.extra_arg == 'foo'
```

### Step 4: Assign G = MyGraph(...)

```python
G = MyGraph([(0, 1)], extra_arg='foo', name='bar')
```

**Verification:**
```python
assert G.graph['name'] == 'bar'
```

### Step 5: Call super.__init__()

```python
super().__init__(incoming_graph_data, **attr)
```

**Verification:**
```python
assert nx.utils.edges_equal(G.edges, [(0, 1)])
```

### Step 6: Assign self.extra_arg = extra_arg

```python
self.extra_arg = extra_arg
```


## Complete Example

```python
# Workflow
'Test that subclasses can accept additional arguments.\n\n    See: https://github.com/networkx/networkx/issues/8367\n    '

class MyGraph(nx.Graph):

    def __init__(self, incoming_graph_data=None, extra_arg=None, **attr):
        super().__init__(incoming_graph_data, **attr)
        self.extra_arg = extra_arg
G = MyGraph(extra_arg='extra arg')
assert G.extra_arg == 'extra arg'
G = MyGraph([], 'extra arg')
assert G.extra_arg == 'extra arg'
G = MyGraph([(0, 1)], extra_arg='foo', name='bar')
assert G.extra_arg == 'foo'
assert G.graph['name'] == 'bar'
assert nx.utils.edges_equal(G.edges, [(0, 1)])
```

## Next Steps


---

*Source: test_graph.py:930 | Complexity: Intermediate | Last updated: 2026-06-02*