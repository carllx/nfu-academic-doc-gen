# How To: Tikz Attributes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tikz attributes

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4, create_using=nx.DiGraph)
```

**Verification:**
```python
assert expected == actual
```

### Step 2: Assign pos = value

```python
pos = {n: (n, n) for n in G}
```

**Verification:**
```python
assert output_tex == expected_tex
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 0)
```

### Step 4: Assign unknown = 'Loop'

```python
G.edges[0, 0]['label'] = 'Loop'
```

### Step 5: Assign unknown = 'midway'

```python
G.edges[0, 0]['label_options'] = 'midway'
```

### Step 6: Assign unknown = 'blue'

```python
G.nodes[0]['style'] = 'blue'
```

### Step 7: Assign unknown = 'line width=3,draw'

```python
G.nodes[1]['style'] = 'line width=3,draw'
```

### Step 8: Assign unknown = 'circle,draw,blue!50'

```python
G.nodes[2]['style'] = 'circle,draw,blue!50'
```

### Step 9: Assign unknown = 'Stop'

```python
G.nodes[3]['label'] = 'Stop'
```

### Step 10: Assign unknown = '1st Step'

```python
G.edges[0, 1]['label'] = '1st Step'
```

### Step 11: Assign unknown = 'near end'

```python
G.edges[0, 1]['label_options'] = 'near end'
```

### Step 12: Assign unknown = '3rd Step'

```python
G.edges[2, 3]['label'] = '3rd Step'
```

### Step 13: Assign unknown = 'near start'

```python
G.edges[2, 3]['label_options'] = 'near start'
```

### Step 14: Assign unknown = 'bend left,green'

```python
G.edges[2, 3]['style'] = 'bend left,green'
```

### Step 15: Assign unknown = '2nd'

```python
G.edges[1, 2]['label'] = '2nd'
```

### Step 16: Assign unknown = 'pos=0.5'

```python
G.edges[1, 2]['label_options'] = 'pos=0.5'
```

### Step 17: Assign unknown = '>->,bend right,line width=3,green!90'

```python
G.edges[1, 2]['style'] = '>->,bend right,line width=3,green!90'
```

### Step 18: Assign output_tex = nx.to_latex(...)

```python
output_tex = nx.to_latex(G, pos=pos, as_document=False, tikz_options='[scale=3]', node_options='style', edge_options='style', node_label='label', edge_label='label', edge_label_options='label_options')
```

### Step 19: Assign expected_tex = '\\begin{figure}\n  \\begin{tikzpicture}[scale=3]\n      \\draw\n        (0, 0) node[blue] (0){0}\n        (1, 1) node[line width=3,draw] (1){1}\n        (2, 2) node[circle,draw,blue!50] (2){2}\n        (3, 3) node (3){Stop};\n      \\begin{scope}[->]\n        \\draw (0) to node[near end] {1st Step} (1);\n        \\draw[loop,] (0) to node[midway] {Loop} (0);\n        \\draw[>->,bend right,line width=3,green!90] (1) to node[pos=0.5] {2nd} (2);\n        \\draw[bend left,green] (2) to node[near start] {3rd Step} (3);\n      \\end{scope}\n    \\end{tikzpicture}\n\\end{figure}'

```python
expected_tex = '\\begin{figure}\n  \\begin{tikzpicture}[scale=3]\n      \\draw\n        (0, 0) node[blue] (0){0}\n        (1, 1) node[line width=3,draw] (1){1}\n        (2, 2) node[circle,draw,blue!50] (2){2}\n        (3, 3) node (3){Stop};\n      \\begin{scope}[->]\n        \\draw (0) to node[near end] {1st Step} (1);\n        \\draw[loop,] (0) to node[midway] {Loop} (0);\n        \\draw[>->,bend right,line width=3,green!90] (1) to node[pos=0.5] {2nd} (2);\n        \\draw[bend left,green] (2) to node[near start] {3rd Step} (3);\n      \\end{scope}\n    \\end{tikzpicture}\n\\end{figure}'
```

**Verification:**
```python
assert output_tex == expected_tex
```


## Complete Example

```python
# Workflow
G = nx.path_graph(4, create_using=nx.DiGraph)
pos = {n: (n, n) for n in G}
G.add_edge(0, 0)
G.edges[0, 0]['label'] = 'Loop'
G.edges[0, 0]['label_options'] = 'midway'
G.nodes[0]['style'] = 'blue'
G.nodes[1]['style'] = 'line width=3,draw'
G.nodes[2]['style'] = 'circle,draw,blue!50'
G.nodes[3]['label'] = 'Stop'
G.edges[0, 1]['label'] = '1st Step'
G.edges[0, 1]['label_options'] = 'near end'
G.edges[2, 3]['label'] = '3rd Step'
G.edges[2, 3]['label_options'] = 'near start'
G.edges[2, 3]['style'] = 'bend left,green'
G.edges[1, 2]['label'] = '2nd'
G.edges[1, 2]['label_options'] = 'pos=0.5'
G.edges[1, 2]['style'] = '>->,bend right,line width=3,green!90'
output_tex = nx.to_latex(G, pos=pos, as_document=False, tikz_options='[scale=3]', node_options='style', edge_options='style', node_label='label', edge_label='label', edge_label_options='label_options')
expected_tex = '\\begin{figure}\n  \\begin{tikzpicture}[scale=3]\n      \\draw\n        (0, 0) node[blue] (0){0}\n        (1, 1) node[line width=3,draw] (1){1}\n        (2, 2) node[circle,draw,blue!50] (2){2}\n        (3, 3) node (3){Stop};\n      \\begin{scope}[->]\n        \\draw (0) to node[near end] {1st Step} (1);\n        \\draw[loop,] (0) to node[midway] {Loop} (0);\n        \\draw[>->,bend right,line width=3,green!90] (1) to node[pos=0.5] {2nd} (2);\n        \\draw[bend left,green] (2) to node[near start] {3rd Step} (3);\n      \\end{scope}\n    \\end{tikzpicture}\n\\end{figure}'
for expected, actual in zip(expected_tex.split('\n'), output_tex.split('\n')):
    assert expected == actual
assert output_tex == expected_tex
```

## Next Steps


---

*Source: test_latex.py:6 | Complexity: Advanced | Last updated: 2026-06-02*