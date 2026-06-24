# How To: Basic Tikz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic tikz

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign expected_tex = '\\documentclass{report}\n\\usepackage{tikz}\n\\usepackage{subcaption}\n\n\\begin{document}\n\\begin{figure}\n  \\begin{subfigure}{0.5\\textwidth}\n  \\begin{tikzpicture}[scale=2]\n      \\draw[gray!90]\n        (0.749, 0.702) node[red!90] (0){0}\n        (1.0, -0.014) node[red!90] (1){1}\n        (-0.777, -0.705) node (2){2}\n        (-0.984, 0.042) node (3){3}\n        (-0.028, 0.375) node[cyan!90] (4){4}\n        (-0.412, 0.888) node (5){5}\n        (0.448, -0.856) node (6){6}\n        (0.003, -0.431) node[cyan!90] (7){7};\n      \\begin{scope}[->,gray!90]\n        \\draw (0) to (4);\n        \\draw (0) to (5);\n        \\draw (0) to (6);\n        \\draw (0) to (7);\n        \\draw (1) to (4);\n        \\draw (1) to (5);\n        \\draw (1) to (6);\n        \\draw (1) to (7);\n        \\draw (2) to (4);\n        \\draw (2) to (5);\n        \\draw (2) to (6);\n        \\draw (2) to (7);\n        \\draw (3) to (4);\n        \\draw (3) to (5);\n        \\draw (3) to (6);\n        \\draw (3) to (7);\n      \\end{scope}\n    \\end{tikzpicture}\n    \\caption{My tikz number 1 of 2}\\label{tikz_1_2}\n  \\end{subfigure}\n  \\begin{subfigure}{0.5\\textwidth}\n  \\begin{tikzpicture}[scale=2]\n      \\draw[gray!90]\n        (0.749, 0.702) node[green!90] (0){0}\n        (1.0, -0.014) node[green!90] (1){1}\n        (-0.777, -0.705) node (2){2}\n        (-0.984, 0.042) node (3){3}\n        (-0.028, 0.375) node[purple!90] (4){4}\n        (-0.412, 0.888) node (5){5}\n        (0.448, -0.856) node (6){6}\n        (0.003, -0.431) node[purple!90] (7){7};\n      \\begin{scope}[->,gray!90]\n        \\draw (0) to (4);\n        \\draw (0) to (5);\n        \\draw (0) to (6);\n        \\draw (0) to (7);\n        \\draw (1) to (4);\n        \\draw (1) to (5);\n        \\draw (1) to (6);\n        \\draw (1) to (7);\n        \\draw (2) to (4);\n        \\draw (2) to (5);\n        \\draw (2) to (6);\n        \\draw (2) to (7);\n        \\draw (3) to (4);\n        \\draw (3) to (5);\n        \\draw (3) to (6);\n        \\draw (3) to (7);\n      \\end{scope}\n    \\end{tikzpicture}\n    \\caption{My tikz number 2 of 2}\\label{tikz_2_2}\n  \\end{subfigure}\n  \\caption{A graph generated with python and latex.}\n\\end{figure}\n\\end{document}'

```python
expected_tex = '\\documentclass{report}\n\\usepackage{tikz}\n\\usepackage{subcaption}\n\n\\begin{document}\n\\begin{figure}\n  \\begin{subfigure}{0.5\\textwidth}\n  \\begin{tikzpicture}[scale=2]\n      \\draw[gray!90]\n        (0.749, 0.702) node[red!90] (0){0}\n        (1.0, -0.014) node[red!90] (1){1}\n        (-0.777, -0.705) node (2){2}\n        (-0.984, 0.042) node (3){3}\n        (-0.028, 0.375) node[cyan!90] (4){4}\n        (-0.412, 0.888) node (5){5}\n        (0.448, -0.856) node (6){6}\n        (0.003, -0.431) node[cyan!90] (7){7};\n      \\begin{scope}[->,gray!90]\n        \\draw (0) to (4);\n        \\draw (0) to (5);\n        \\draw (0) to (6);\n        \\draw (0) to (7);\n        \\draw (1) to (4);\n        \\draw (1) to (5);\n        \\draw (1) to (6);\n        \\draw (1) to (7);\n        \\draw (2) to (4);\n        \\draw (2) to (5);\n        \\draw (2) to (6);\n        \\draw (2) to (7);\n        \\draw (3) to (4);\n        \\draw (3) to (5);\n        \\draw (3) to (6);\n        \\draw (3) to (7);\n      \\end{scope}\n    \\end{tikzpicture}\n    \\caption{My tikz number 1 of 2}\\label{tikz_1_2}\n  \\end{subfigure}\n  \\begin{subfigure}{0.5\\textwidth}\n  \\begin{tikzpicture}[scale=2]\n      \\draw[gray!90]\n        (0.749, 0.702) node[green!90] (0){0}\n        (1.0, -0.014) node[green!90] (1){1}\n        (-0.777, -0.705) node (2){2}\n        (-0.984, 0.042) node (3){3}\n        (-0.028, 0.375) node[purple!90] (4){4}\n        (-0.412, 0.888) node (5){5}\n        (0.448, -0.856) node (6){6}\n        (0.003, -0.431) node[purple!90] (7){7};\n      \\begin{scope}[->,gray!90]\n        \\draw (0) to (4);\n        \\draw (0) to (5);\n        \\draw (0) to (6);\n        \\draw (0) to (7);\n        \\draw (1) to (4);\n        \\draw (1) to (5);\n        \\draw (1) to (6);\n        \\draw (1) to (7);\n        \\draw (2) to (4);\n        \\draw (2) to (5);\n        \\draw (2) to (6);\n        \\draw (2) to (7);\n        \\draw (3) to (4);\n        \\draw (3) to (5);\n        \\draw (3) to (6);\n        \\draw (3) to (7);\n      \\end{scope}\n    \\end{tikzpicture}\n    \\caption{My tikz number 2 of 2}\\label{tikz_2_2}\n  \\end{subfigure}\n  \\caption{A graph generated with python and latex.}\n\\end{figure}\n\\end{document}'
```

**Verification:**
```python
assert expected == actual
```

### Step 2: Assign edges = value

```python
edges = [(0, 4), (0, 5), (0, 6), (0, 7), (1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7)]
```

**Verification:**
```python
assert output_tex == expected_tex
```

### Step 3: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 4: Call G.add_nodes_from()

```python
G.add_nodes_from(range(8))
```

### Step 5: Call G.add_edges_from()

```python
G.add_edges_from(edges)
```

### Step 6: Assign pos = value

```python
pos = {0: (0.7490296171687696, 0.702353520257394), 1: (1.0, -0.014221357723796535), 2: (-0.7765783344161441, -0.7054170966808919), 3: (-0.9842690223417624, 0.04177547602465483), 4: (-0.02768523817180917, 0.3745724439551441), 5: (-0.41154855146767433, 0.8880106515525136), 6: (0.44780153389148264, -0.8561492709269164), 7: (0.0032499953371383505, -0.43092436645809945)}
```

### Step 7: Assign rc_node_color = value

```python
rc_node_color = {0: 'red!90', 1: 'red!90', 4: 'cyan!90', 7: 'cyan!90'}
```

### Step 8: Assign gp_node_color = value

```python
gp_node_color = {0: 'green!90', 1: 'green!90', 4: 'purple!90', 7: 'purple!90'}
```

### Step 9: Assign H = G.copy(...)

```python
H = G.copy()
```

### Step 10: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, rc_node_color, 'color')
```

### Step 11: Call nx.set_node_attributes()

```python
nx.set_node_attributes(H, gp_node_color, 'color')
```

### Step 12: Assign sub_captions = value

```python
sub_captions = ['My tikz number 1 of 2', 'My tikz number 2 of 2']
```

### Step 13: Assign sub_labels = value

```python
sub_labels = ['tikz_1_2', 'tikz_2_2']
```

### Step 14: Assign output_tex = nx.to_latex(...)

```python
output_tex = nx.to_latex([G, H], [pos, pos], tikz_options='[scale=2]', default_node_options='gray!90', default_edge_options='gray!90', node_options='color', sub_captions=sub_captions, sub_labels=sub_labels, caption='A graph generated with python and latex.', n_rows=2, as_document=True)
```

**Verification:**
```python
assert output_tex == expected_tex
```


## Complete Example

```python
# Workflow
expected_tex = '\\documentclass{report}\n\\usepackage{tikz}\n\\usepackage{subcaption}\n\n\\begin{document}\n\\begin{figure}\n  \\begin{subfigure}{0.5\\textwidth}\n  \\begin{tikzpicture}[scale=2]\n      \\draw[gray!90]\n        (0.749, 0.702) node[red!90] (0){0}\n        (1.0, -0.014) node[red!90] (1){1}\n        (-0.777, -0.705) node (2){2}\n        (-0.984, 0.042) node (3){3}\n        (-0.028, 0.375) node[cyan!90] (4){4}\n        (-0.412, 0.888) node (5){5}\n        (0.448, -0.856) node (6){6}\n        (0.003, -0.431) node[cyan!90] (7){7};\n      \\begin{scope}[->,gray!90]\n        \\draw (0) to (4);\n        \\draw (0) to (5);\n        \\draw (0) to (6);\n        \\draw (0) to (7);\n        \\draw (1) to (4);\n        \\draw (1) to (5);\n        \\draw (1) to (6);\n        \\draw (1) to (7);\n        \\draw (2) to (4);\n        \\draw (2) to (5);\n        \\draw (2) to (6);\n        \\draw (2) to (7);\n        \\draw (3) to (4);\n        \\draw (3) to (5);\n        \\draw (3) to (6);\n        \\draw (3) to (7);\n      \\end{scope}\n    \\end{tikzpicture}\n    \\caption{My tikz number 1 of 2}\\label{tikz_1_2}\n  \\end{subfigure}\n  \\begin{subfigure}{0.5\\textwidth}\n  \\begin{tikzpicture}[scale=2]\n      \\draw[gray!90]\n        (0.749, 0.702) node[green!90] (0){0}\n        (1.0, -0.014) node[green!90] (1){1}\n        (-0.777, -0.705) node (2){2}\n        (-0.984, 0.042) node (3){3}\n        (-0.028, 0.375) node[purple!90] (4){4}\n        (-0.412, 0.888) node (5){5}\n        (0.448, -0.856) node (6){6}\n        (0.003, -0.431) node[purple!90] (7){7};\n      \\begin{scope}[->,gray!90]\n        \\draw (0) to (4);\n        \\draw (0) to (5);\n        \\draw (0) to (6);\n        \\draw (0) to (7);\n        \\draw (1) to (4);\n        \\draw (1) to (5);\n        \\draw (1) to (6);\n        \\draw (1) to (7);\n        \\draw (2) to (4);\n        \\draw (2) to (5);\n        \\draw (2) to (6);\n        \\draw (2) to (7);\n        \\draw (3) to (4);\n        \\draw (3) to (5);\n        \\draw (3) to (6);\n        \\draw (3) to (7);\n      \\end{scope}\n    \\end{tikzpicture}\n    \\caption{My tikz number 2 of 2}\\label{tikz_2_2}\n  \\end{subfigure}\n  \\caption{A graph generated with python and latex.}\n\\end{figure}\n\\end{document}'
edges = [(0, 4), (0, 5), (0, 6), (0, 7), (1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7)]
G = nx.DiGraph()
G.add_nodes_from(range(8))
G.add_edges_from(edges)
pos = {0: (0.7490296171687696, 0.702353520257394), 1: (1.0, -0.014221357723796535), 2: (-0.7765783344161441, -0.7054170966808919), 3: (-0.9842690223417624, 0.04177547602465483), 4: (-0.02768523817180917, 0.3745724439551441), 5: (-0.41154855146767433, 0.8880106515525136), 6: (0.44780153389148264, -0.8561492709269164), 7: (0.0032499953371383505, -0.43092436645809945)}
rc_node_color = {0: 'red!90', 1: 'red!90', 4: 'cyan!90', 7: 'cyan!90'}
gp_node_color = {0: 'green!90', 1: 'green!90', 4: 'purple!90', 7: 'purple!90'}
H = G.copy()
nx.set_node_attributes(G, rc_node_color, 'color')
nx.set_node_attributes(H, gp_node_color, 'color')
sub_captions = ['My tikz number 1 of 2', 'My tikz number 2 of 2']
sub_labels = ['tikz_1_2', 'tikz_2_2']
output_tex = nx.to_latex([G, H], [pos, pos], tikz_options='[scale=2]', default_node_options='gray!90', default_edge_options='gray!90', node_options='color', sub_captions=sub_captions, sub_labels=sub_labels, caption='A graph generated with python and latex.', n_rows=2, as_document=True)
for expected, actual in zip(expected_tex.split('\n'), output_tex.split('\n')):
    assert expected == actual
assert output_tex == expected_tex
```

## Next Steps


---

*Source: test_latex.py:87 | Complexity: Advanced | Last updated: 2026-06-02*