# How To: Exception Multiple Graphs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test exception multiple graphs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: to_latex
```

## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3)
```

### Step 2: Assign pos_bad = value

```python
pos_bad = {0: (1, 2), 1: (0, 1)}
```

### Step 3: Assign pos_OK = value

```python
pos_OK = {0: (1, 2), 1: (0, 1), 2: (2, 1)}
```

### Step 4: Assign fourG = value

```python
fourG = [G, G, G, G]
```

### Step 5: Assign fourpos = value

```python
fourpos = [pos_OK, pos_OK, pos_OK, pos_OK]
```

### Step 6: Call to_latex()

```python
to_latex(fourG, pos_OK)
```

### Step 7: Call to_latex()

```python
to_latex(fourG, fourpos)
```

### Step 8: Call to_latex()

```python
to_latex(fourG, fourpos, sub_captions=['hi'] * 4, sub_labels=['lbl'] * 4)
```

### Step 9: Call to_latex()

```python
to_latex(fourG, pos_bad)
```

### Step 10: Call to_latex()

```python
to_latex(fourG, [pos_bad, pos_bad, pos_bad, pos_bad])
```

### Step 11: Call to_latex()

```python
to_latex(fourG, [pos_OK, pos_OK, pos_bad, pos_OK])
```

### Step 12: Call to_latex()

```python
to_latex(fourG, fourpos, sub_captions=['hi', 'hi'])
```

### Step 13: Call to_latex()

```python
to_latex(fourG, fourpos, sub_labels=['hi', 'hi'])
```


## Complete Example

```python
# Setup
# Fixtures: to_latex

# Workflow
G = nx.path_graph(3)
pos_bad = {0: (1, 2), 1: (0, 1)}
pos_OK = {0: (1, 2), 1: (0, 1), 2: (2, 1)}
fourG = [G, G, G, G]
fourpos = [pos_OK, pos_OK, pos_OK, pos_OK]
to_latex(fourG, pos_OK)
with pytest.raises(nx.NetworkXError):
    to_latex(fourG, pos_bad)
to_latex(fourG, fourpos)
with pytest.raises(nx.NetworkXError):
    to_latex(fourG, [pos_bad, pos_bad, pos_bad, pos_bad])
with pytest.raises(nx.NetworkXError):
    to_latex(fourG, [pos_OK, pos_OK, pos_bad, pos_OK])
with pytest.raises(nx.NetworkXError):
    to_latex(fourG, fourpos, sub_captions=['hi', 'hi'])
with pytest.raises(nx.NetworkXError):
    to_latex(fourG, fourpos, sub_labels=['hi', 'hi'])
to_latex(fourG, fourpos, sub_captions=['hi'] * 4, sub_labels=['lbl'] * 4)
```

## Next Steps


---

*Source: test_latex.py:249 | Complexity: Advanced | Last updated: 2026-06-02*