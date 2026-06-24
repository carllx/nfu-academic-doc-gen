# How To: Latin1 Issue

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test latin1 issue

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `textwrap`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Assign name1 = value

```python
name1 = chr(2344) + chr(123) + chr(6543)
```

### Step 3: Assign name2 = value

```python
name2 = chr(5543) + chr(1543) + chr(324)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(name1, 'Radiohead', **{name2: 3})
```

### Step 5: Assign fname = value

```python
fname = tmp_path / 'el.txt'
```

### Step 6: Call nx.write_edgelist()

```python
nx.write_edgelist(G, fname, encoding='latin-1')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
G = nx.Graph()
name1 = chr(2344) + chr(123) + chr(6543)
name2 = chr(5543) + chr(1543) + chr(324)
G.add_edge(name1, 'Radiohead', **{name2: 3})
fname = tmp_path / 'el.txt'
with pytest.raises(UnicodeEncodeError):
    nx.write_edgelist(G, fname, encoding='latin-1')
```

## Next Steps


---

*Source: test_edgelist.py:231 | Complexity: Intermediate | Last updated: 2026-06-02*