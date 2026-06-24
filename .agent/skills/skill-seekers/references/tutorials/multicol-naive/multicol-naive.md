# How To: Multicol Naive

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multicol naive

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
# Fixtures: df, multicol_align, siunitx, header
```

## Step-by-Step Guide

### Step 1: Assign ridx = MultiIndex.from_tuples(...)

```python
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('A', 'c')])
```

**Verification:**
```python
assert expected == result
```

### Step 2: Assign df.columns = ridx

```python
df.columns = ridx
```

### Step 3: Assign level1 = value

```python
level1 = ' & a & b & c' if not siunitx else '{} & {a} & {b} & {c}'
```

### Step 4: Assign col_format = value

```python
col_format = 'lrrl' if not siunitx else 'lSSl'
```

### Step 5: Assign expected = dedent(...)

```python
expected = dedent(f'        \\begin{{tabular}}{{{col_format}}}\n        {header} \\\\\n        {level1} \\\\\n        0 & 0 & -0.61 & ab \\\\\n        1 & 1 & -1.22 & cd \\\\\n        \\end{{tabular}}\n        ')
```

### Step 6: Assign styler = df.style.format(...)

```python
styler = df.style.format(precision=2)
```

### Step 7: Assign result = styler.to_latex(...)

```python
result = styler.to_latex(multicol_align=multicol_align, siunitx=siunitx)
```

**Verification:**
```python
assert expected == result
```


## Complete Example

```python
# Setup
# Fixtures: df, multicol_align, siunitx, header

# Workflow
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('A', 'c')])
df.columns = ridx
level1 = ' & a & b & c' if not siunitx else '{} & {a} & {b} & {c}'
col_format = 'lrrl' if not siunitx else 'lSSl'
expected = dedent(f'        \\begin{{tabular}}{{{col_format}}}\n        {header} \\\\\n        {level1} \\\\\n        0 & 0 & -0.61 & ab \\\\\n        1 & 1 & -1.22 & cd \\\\\n        \\end{{tabular}}\n        ')
styler = df.style.format(precision=2)
result = styler.to_latex(multicol_align=multicol_align, siunitx=siunitx)
assert expected == result
```

## Next Steps


---

*Source: test_to_latex.py:318 | Complexity: Intermediate | Last updated: 2026-06-02*