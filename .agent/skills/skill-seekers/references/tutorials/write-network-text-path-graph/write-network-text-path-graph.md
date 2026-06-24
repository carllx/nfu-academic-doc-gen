# How To: Write Network Text Path Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write network text path graph

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `textwrap`
- `pytest`
- `networkx`
- `random`
- `networkx.readwrite.text`


## Step-by-Step Guide

### Step 1: Assign graph = nx.path_graph(...)

```python
graph = nx.path_graph(3, create_using=nx.Graph)
```

**Verification:**
```python
assert target == text
```

### Step 2: Assign lines = value

```python
lines = []
```

### Step 3: Assign write = value

```python
write = lines.append
```

### Step 4: Call nx.write_network_text()

```python
nx.write_network_text(graph, path=write, end='')
```

### Step 5: Assign text = unknown.join(...)

```python
text = '\n'.join(lines)
```

### Step 6: Assign target = dedent.strip(...)

```python
target = dedent('\n        ╙── 0\n            └── 1\n                └── 2\n        ').strip()
```

**Verification:**
```python
assert target == text
```


## Complete Example

```python
# Workflow
graph = nx.path_graph(3, create_using=nx.Graph)
lines = []
write = lines.append
nx.write_network_text(graph, path=write, end='')
text = '\n'.join(lines)
target = dedent('\n        ╙── 0\n            └── 1\n                └── 2\n        ').strip()
assert target == text
```

## Next Steps


---

*Source: test_text.py:951 | Complexity: Intermediate | Last updated: 2026-06-02*