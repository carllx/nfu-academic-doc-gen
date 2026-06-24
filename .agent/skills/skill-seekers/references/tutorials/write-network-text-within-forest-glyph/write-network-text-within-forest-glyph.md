# How To: Write Network Text Within Forest Glyph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write network text within forest glyph

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

### Step 1: Assign g = nx.DiGraph(...)

```python
g = nx.DiGraph()
```

**Verification:**
```python
assert text == target
```

### Step 2: Call g.add_nodes_from()

```python
g.add_nodes_from([1, 2, 3, 4])
```

### Step 3: Call g.add_edge()

```python
g.add_edge(2, 4)
```

### Step 4: Assign lines = value

```python
lines = []
```

### Step 5: Assign write = value

```python
write = lines.append
```

### Step 6: Call nx.write_network_text()

```python
nx.write_network_text(g, path=write, end='')
```

### Step 7: Call nx.write_network_text()

```python
nx.write_network_text(g, path=write, ascii_only=True, end='')
```

### Step 8: Assign text = unknown.join(...)

```python
text = '\n'.join(lines)
```

### Step 9: Assign target = dedent.strip(...)

```python
target = dedent('\n        ╟── 1\n        ╟── 2\n        ╎   └─╼ 4\n        ╙── 3\n        +-- 1\n        +-- 2\n        :   L-> 4\n        +-- 3\n        ').strip()
```

**Verification:**
```python
assert text == target
```


## Complete Example

```python
# Workflow
g = nx.DiGraph()
g.add_nodes_from([1, 2, 3, 4])
g.add_edge(2, 4)
lines = []
write = lines.append
nx.write_network_text(g, path=write, end='')
nx.write_network_text(g, path=write, ascii_only=True, end='')
text = '\n'.join(lines)
target = dedent('\n        ╟── 1\n        ╟── 2\n        ╎   └─╼ 4\n        ╙── 3\n        +-- 1\n        +-- 2\n        :   L-> 4\n        +-- 3\n        ').strip()
assert text == target
```

## Next Steps


---

*Source: test_text.py:61 | Complexity: Advanced | Last updated: 2026-06-02*