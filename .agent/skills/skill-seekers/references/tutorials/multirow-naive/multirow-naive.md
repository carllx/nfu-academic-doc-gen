# How To: Multirow Naive

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multirow naive

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
ridx = MultiIndex.from_tuples([('X', 'x'), ('X', 'y'), ('Y', 'z')])
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign df_ext.index = ridx

```python
df_ext.index = ridx
```

### Step 3: Assign expected = dedent(...)

```python
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & A & B & C \\\\\n        X & x & 0 & -0.61 & ab \\\\\n         & y & 1 & -1.22 & cd \\\\\n        Y & z & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
```

### Step 4: Assign styler = df_ext.style.format(...)

```python
styler = df_ext.style.format(precision=2)
```

### Step 5: Assign result = styler.to_latex(...)

```python
result = styler.to_latex(multirow_align='naive')
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
ridx = MultiIndex.from_tuples([('X', 'x'), ('X', 'y'), ('Y', 'z')])
df_ext.index = ridx
expected = dedent('        \\begin{tabular}{llrrl}\n         &  & A & B & C \\\\\n        X & x & 0 & -0.61 & ab \\\\\n         & y & 1 & -1.22 & cd \\\\\n        Y & z & 2 & -2.22 & de \\\\\n        \\end{tabular}\n        ')
styler = df_ext.style.format(precision=2)
result = styler.to_latex(multirow_align='naive')
assert expected == result
```

## Next Steps


---

*Source: test_to_latex.py:256 | Complexity: Intermediate | Last updated: 2026-06-02*