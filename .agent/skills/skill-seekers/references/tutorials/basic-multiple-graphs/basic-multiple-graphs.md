# How To: Basic Multiple Graphs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic multiple graphs

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign H1 = nx.path_graph(...)

```python
H1 = nx.path_graph(4)
```

**Verification:**
```python
assert 'begin{document}' in latex_code
```

### Step 2: Assign H2 = nx.complete_graph(...)

```python
H2 = nx.complete_graph(4)
```

**Verification:**
```python
assert 'begin{figure}' in latex_code
```

### Step 3: Assign H3 = nx.path_graph(...)

```python
H3 = nx.path_graph(8)
```

**Verification:**
```python
assert latex_code.count('begin{subfigure}') == 4
```

### Step 4: Assign H4 = nx.complete_graph(...)

```python
H4 = nx.complete_graph(8)
```

**Verification:**
```python
assert latex_code.count('tikzpicture') == 8
```

### Step 5: Assign captions = value

```python
captions = ['Path on 4 nodes', 'Complete graph on 4 nodes', 'Path on 8 nodes', 'Complete graph on 8 nodes']
```

**Verification:**
```python
assert latex_code.count('[-]') == 4
```

### Step 6: Assign labels = value

```python
labels = ['fig2a', 'fig2b', 'fig2c', 'fig2d']
```

### Step 7: Assign latex_code = nx.to_latex(...)

```python
latex_code = nx.to_latex([H1, H2, H3, H4], n_rows=2, sub_captions=captions, sub_labels=labels)
```

**Verification:**
```python
assert 'begin{document}' in latex_code
```


## Complete Example

```python
# Workflow
H1 = nx.path_graph(4)
H2 = nx.complete_graph(4)
H3 = nx.path_graph(8)
H4 = nx.complete_graph(8)
captions = ['Path on 4 nodes', 'Complete graph on 4 nodes', 'Path on 8 nodes', 'Complete graph on 8 nodes']
labels = ['fig2a', 'fig2b', 'fig2c', 'fig2d']
latex_code = nx.to_latex([H1, H2, H3, H4], n_rows=2, sub_captions=captions, sub_labels=labels)
assert 'begin{document}' in latex_code
assert 'begin{figure}' in latex_code
assert latex_code.count('begin{subfigure}') == 4
assert latex_code.count('tikzpicture') == 8
assert latex_code.count('[-]') == 4
```

## Next Steps


---

*Source: test_latex.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*