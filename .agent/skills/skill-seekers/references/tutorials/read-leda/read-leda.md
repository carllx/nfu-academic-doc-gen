# How To: Read Leda

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read LEDA

## Prerequisites

**Required Modules:**
- `io`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(Gin.nodes())
```

### Step 2: Assign data = '#header section         \nLEDA.GRAPH \nstring\nint\n-1\n#nodes section\n5 \n|{v1}| \n|{v2}| \n|{v3}| \n|{v4}| \n|{v5}| \n\n#edges section\n7 \n1 2 0 |{4}| \n1 3 0 |{3}| \n2 3 0 |{2}| \n3 4 0 |{3}| \n3 5 0 |{7}| \n4 5 0 |{6}| \n5 1 0 |{foo}|'

```python
data = '#header section         \nLEDA.GRAPH \nstring\nint\n-1\n#nodes section\n5 \n|{v1}| \n|{v2}| \n|{v3}| \n|{v4}| \n|{v5}| \n\n#edges section\n7 \n1 2 0 |{4}| \n1 3 0 |{3}| \n2 3 0 |{2}| \n3 4 0 |{3}| \n3 5 0 |{7}| \n4 5 0 |{6}| \n5 1 0 |{foo}|'
```

**Verification:**
```python
assert sorted(G.edges()) == sorted(Gin.edges())
```

### Step 3: Assign G = nx.parse_leda(...)

```python
G = nx.parse_leda(data)
```

### Step 4: Call fh.write()

```python
fh.write(data.encode('UTF-8'))
```

### Step 5: Call fh.seek()

```python
fh.seek(0)
```

### Step 6: Assign Gin = nx.read_leda(...)

```python
Gin = nx.read_leda(fh)
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(Gin.nodes())
```


## Complete Example

```python
# Workflow
fh = io.BytesIO()
data = '#header section         \nLEDA.GRAPH \nstring\nint\n-1\n#nodes section\n5 \n|{v1}| \n|{v2}| \n|{v3}| \n|{v4}| \n|{v5}| \n\n#edges section\n7 \n1 2 0 |{4}| \n1 3 0 |{3}| \n2 3 0 |{2}| \n3 4 0 |{3}| \n3 5 0 |{7}| \n4 5 0 |{6}| \n5 1 0 |{foo}|'
G = nx.parse_leda(data)
fh.write(data.encode('UTF-8'))
fh.seek(0)
Gin = nx.read_leda(fh)
assert sorted(G.nodes()) == sorted(Gin.nodes())
assert sorted(G.edges()) == sorted(Gin.edges())
```

## Next Steps


---

*Source: test_leda.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*