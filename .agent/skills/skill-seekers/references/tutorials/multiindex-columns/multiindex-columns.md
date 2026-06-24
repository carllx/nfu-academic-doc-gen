# How To: Multiindex Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex columns

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
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign cidx = MultiIndex.from_tuples(...)

```python
cidx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
```

**Verification:**
```python
assert expected == s.to_latex()
```

### Step 2: Assign df.columns = cidx

```python
df.columns = cidx
```

**Verification:**
```python
assert expected == s.to_latex(sparse_columns=False)
```

### Step 3: Assign expected = dedent(...)

```python
expected = dedent('        \\begin{tabular}{lrrl}\n         & \\multicolumn{2}{r}{A} & B \\\\\n         & a & b & c \\\\\n        0 & 0 & -0.61 & ab \\\\\n        1 & 1 & -1.22 & cd \\\\\n        \\end{tabular}\n        ')
```

### Step 4: Assign s = df.style.format(...)

```python
s = df.style.format(precision=2)
```

**Verification:**
```python
assert expected == s.to_latex()
```

### Step 5: Assign expected = dedent(...)

```python
expected = dedent('        \\begin{tabular}{lrrl}\n         & A & A & B \\\\\n         & a & b & c \\\\\n        0 & 0 & -0.61 & ab \\\\\n        1 & 1 & -1.22 & cd \\\\\n        \\end{tabular}\n        ')
```

### Step 6: Assign s = df.style.format(...)

```python
s = df.style.format(precision=2)
```

**Verification:**
```python
assert expected == s.to_latex(sparse_columns=False)
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
cidx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
df.columns = cidx
expected = dedent('        \\begin{tabular}{lrrl}\n         & \\multicolumn{2}{r}{A} & B \\\\\n         & a & b & c \\\\\n        0 & 0 & -0.61 & ab \\\\\n        1 & 1 & -1.22 & cd \\\\\n        \\end{tabular}\n        ')
s = df.style.format(precision=2)
assert expected == s.to_latex()
expected = dedent('        \\begin{tabular}{lrrl}\n         & A & A & B \\\\\n         & a & b & c \\\\\n        0 & 0 & -0.61 & ab \\\\\n        1 & 1 & -1.22 & cd \\\\\n        \\end{tabular}\n        ')
s = df.style.format(precision=2)
assert expected == s.to_latex(sparse_columns=False)
```

## Next Steps


---

*Source: test_to_latex.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*