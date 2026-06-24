# How To: Multiindex Row

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex row

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
# Fixtures: df_ext
```

## Step-by-Step Guide

### Step 1: Assign ridx = MultiIndex.from_tuples(...)

```python
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign df_ext.index = ridx

```python
df_ext.index = ridx
```

**Verification:**
```python
assert expected == result
```

### Step 3: Assign expected = dedent(...)

```python
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & A & B & C \\\\\n        \\multirow[c]{2}{*}{A} & a & 0 & -0.61 & ab \\\\\n         & b & 1 & -1.22 & cd \\\\\n        B & c & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
```

### Step 4: Assign styler = df_ext.style.format(...)

```python
styler = df_ext.style.format(precision=2)
```

### Step 5: Assign result = styler.to_latex(...)

```python
result = styler.to_latex()
```

**Verification:**
```python
assert expected == result
```

### Step 6: Assign expected = dedent(...)

```python
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & A & B & C \\\\\n        A & a & 0 & -0.61 & ab \\\\\n        A & b & 1 & -1.22 & cd \\\\\n        B & c & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
```

### Step 7: Assign result = styler.to_latex(...)

```python
result = styler.to_latex(sparse_index=False)
```

**Verification:**
```python
assert expected == result
```


## Complete Example

```python
# Setup
# Fixtures: df_ext

# Workflow
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
df_ext.index = ridx
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & A & B & C \\\\\n        \\multirow[c]{2}{*}{A} & a & 0 & -0.61 & ab \\\\\n         & b & 1 & -1.22 & cd \\\\\n        B & c & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
styler = df_ext.style.format(precision=2)
result = styler.to_latex()
assert expected == result
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & A & B & C \\\\\n        A & a & 0 & -0.61 & ab \\\\\n        A & b & 1 & -1.22 & cd \\\\\n        B & c & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
result = styler.to_latex(sparse_index=False)
assert expected == result
```

## Next Steps


---

*Source: test_to_latex.py:224 | Complexity: Intermediate | Last updated: 2026-06-02*