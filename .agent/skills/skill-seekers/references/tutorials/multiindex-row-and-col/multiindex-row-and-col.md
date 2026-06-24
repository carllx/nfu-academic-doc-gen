# How To: Multiindex Row And Col

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex row and col

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

**Verification:**
```python
assert result == expected
```

### Step 3: Assign unknown = value

```python
df_ext.index, df_ext.columns = (ridx, cidx)
```

### Step 4: Assign expected = dedent(...)

```python
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & \\multicolumn{2}{l}{Z} & Y \\\\\n         &  & a & b & c \\\\\n        \\multirow[b]{2}{*}{A} & a & 0 & -0.61 & ab \\\\\n         & b & 1 & -1.22 & cd \\\\\n        B & c & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
```

### Step 5: Assign styler = df_ext.style.format(...)

```python
styler = df_ext.style.format(precision=2)
```

### Step 6: Assign result = styler.to_latex(...)

```python
result = styler.to_latex(multirow_align='b', multicol_align='l')
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign expected = dedent(...)

```python
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & Z & Z & Y \\\\\n         &  & a & b & c \\\\\n        A & a & 0 & -0.61 & ab \\\\\n        A & b & 1 & -1.22 & cd \\\\\n        B & c & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
```

### Step 8: Assign result = styler.to_latex(...)

```python
result = styler.to_latex(sparse_index=False, sparse_columns=False)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: df_ext

# Workflow
cidx = MultiIndex.from_tuples([('Z', 'a'), ('Z', 'b'), ('Y', 'c')])
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
df_ext.index, df_ext.columns = (ridx, cidx)
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & \\multicolumn{2}{l}{Z} & Y \\\\\n         &  & a & b & c \\\\\n        \\multirow[b]{2}{*}{A} & a & 0 & -0.61 & ab \\\\\n         & b & 1 & -1.22 & cd \\\\\n        B & c & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
styler = df_ext.style.format(precision=2)
result = styler.to_latex(multirow_align='b', multicol_align='l')
assert result == expected
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & Z & Z & Y \\\\\n         &  & a & b & c \\\\\n        A & a & 0 & -0.61 & ab \\\\\n        A & b & 1 & -1.22 & cd \\\\\n        B & c & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
result = styler.to_latex(sparse_index=False, sparse_columns=False)
assert result == expected
```

## Next Steps


---

*Source: test_to_latex.py:274 | Complexity: Advanced | Last updated: 2026-06-02*