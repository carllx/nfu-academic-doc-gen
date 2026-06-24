# How To: Comprehensive

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comprehensive

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`

**Setup Required:**
```python
# Fixtures: df_ext, environment
```

## Step-by-Step Guide

### Step 1: Assign cidx = MultiIndex.from_tuples(...)

```python
cidx = MultiIndex.from_tuples([('Z', 'a'), ('Z', 'b'), ('Y', 'c')])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ridx = MultiIndex.from_tuples(...)

```python
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
```

### Step 3: Assign unknown = value

```python
df_ext.index, df_ext.columns = (ridx, cidx)
```

### Step 4: Assign stlr = value

```python
stlr = df_ext.style
```

### Step 5: Call stlr.set_caption()

```python
stlr.set_caption('mycap')
```

### Step 6: Call stlr.set_table_styles()

```python
stlr.set_table_styles([{'selector': 'label', 'props': ':{fig§item}'}, {'selector': 'position', 'props': ':h!'}, {'selector': 'position_float', 'props': ':centering'}, {'selector': 'column_format', 'props': ':rlrlr'}, {'selector': 'toprule', 'props': ':toprule'}, {'selector': 'midrule', 'props': ':midrule'}, {'selector': 'bottomrule', 'props': ':bottomrule'}, {'selector': 'rowcolors', 'props': ':{3}{pink}{}'}])
```

### Step 7: Call stlr.highlight_max()

```python
stlr.highlight_max(axis=0, props='textbf:--rwrap;cellcolor:[rgb]{1,1,0.6}--rwrap')
```

### Step 8: Call stlr.highlight_max()

```python
stlr.highlight_max(axis=None, props='Huge:--wrap;', subset=[('Z', 'a'), ('Z', 'b')])
```

### Step 9: Assign expected = unknown.replace(...)

```python
expected = '\\begin{table}[h!]\n\\centering\n\\caption{mycap}\n\\label{fig:item}\n\\rowcolors{3}{pink}{}\n\\begin{tabular}{rlrlr}\n\\toprule\n &  & \\multicolumn{2}{r}{Z} & Y \\\\\n &  & a & b & c \\\\\n\\midrule\n\\multirow[c]{2}{*}{A} & a & 0 & \\textbf{\\cellcolor[rgb]{1,1,0.6}{-0.61}} & ab \\\\\n & b & 1 & -1.22 & cd \\\\\nB & c & \\textbf{\\cellcolor[rgb]{1,1,0.6}{{\\Huge 2}}} & -2.22 & \\textbf{\\cellcolor[rgb]{1,1,0.6}{de}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n'.replace('table', environment if environment else 'table')
```

### Step 10: Assign result = stlr.format.to_latex(...)

```python
result = stlr.format(precision=2).to_latex(environment=environment)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: df_ext, environment

# Workflow
cidx = MultiIndex.from_tuples([('Z', 'a'), ('Z', 'b'), ('Y', 'c')])
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
df_ext.index, df_ext.columns = (ridx, cidx)
stlr = df_ext.style
stlr.set_caption('mycap')
stlr.set_table_styles([{'selector': 'label', 'props': ':{fig§item}'}, {'selector': 'position', 'props': ':h!'}, {'selector': 'position_float', 'props': ':centering'}, {'selector': 'column_format', 'props': ':rlrlr'}, {'selector': 'toprule', 'props': ':toprule'}, {'selector': 'midrule', 'props': ':midrule'}, {'selector': 'bottomrule', 'props': ':bottomrule'}, {'selector': 'rowcolors', 'props': ':{3}{pink}{}'}])
stlr.highlight_max(axis=0, props='textbf:--rwrap;cellcolor:[rgb]{1,1,0.6}--rwrap')
stlr.highlight_max(axis=None, props='Huge:--wrap;', subset=[('Z', 'a'), ('Z', 'b')])
expected = '\\begin{table}[h!]\n\\centering\n\\caption{mycap}\n\\label{fig:item}\n\\rowcolors{3}{pink}{}\n\\begin{tabular}{rlrlr}\n\\toprule\n &  & \\multicolumn{2}{r}{Z} & Y \\\\\n &  & a & b & c \\\\\n\\midrule\n\\multirow[c]{2}{*}{A} & a & 0 & \\textbf{\\cellcolor[rgb]{1,1,0.6}{-0.61}} & ab \\\\\n & b & 1 & -1.22 & cd \\\\\nB & c & \\textbf{\\cellcolor[rgb]{1,1,0.6}{{\\Huge 2}}} & -2.22 & \\textbf{\\cellcolor[rgb]{1,1,0.6}{de}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n'.replace('table', environment if environment else 'table')
result = stlr.format(precision=2).to_latex(environment=environment)
assert result == expected
```

## Next Steps


---

*Source: test_to_latex.py:407 | Complexity: Advanced | Last updated: 2026-06-02*