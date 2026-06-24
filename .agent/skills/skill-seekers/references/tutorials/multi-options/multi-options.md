# How To: Multi Options

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multi options

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
assert expected in result
```

### Step 2: Assign ridx = MultiIndex.from_tuples(...)

```python
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
```

**Verification:**
```python
assert ' &  & \\multicolumn{2}{l}{Z} & Y \\\\' in styler.to_latex()
```

### Step 3: Assign unknown = value

```python
df_ext.index, df_ext.columns = (ridx, cidx)
```

**Verification:**
```python
assert '\\multirow[b]{2}{*}{A} & a & 0 & -0.61 & ab \\\\' in styler.to_latex()
```

### Step 4: Assign styler = df_ext.style.format(...)

```python
styler = df_ext.style.format(precision=2)
```

### Step 5: Assign expected = dedent(...)

```python
expected = dedent('     &  & \\multicolumn{2}{r}{Z} & Y \\\\\n     &  & a & b & c \\\\\n    \\multirow[c]{2}{*}{A} & a & 0 & -0.61 & ab \\\\\n    ')
```

### Step 6: Assign result = styler.to_latex(...)

```python
result = styler.to_latex()
```

**Verification:**
```python
assert expected in result
```


## Complete Example

```python
# Setup
# Fixtures: df_ext

# Workflow
cidx = MultiIndex.from_tuples([('Z', 'a'), ('Z', 'b'), ('Y', 'c')])
ridx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
df_ext.index, df_ext.columns = (ridx, cidx)
styler = df_ext.style.format(precision=2)
expected = dedent('     &  & \\multicolumn{2}{r}{Z} & Y \\\\\n     &  & a & b & c \\\\\n    \\multirow[c]{2}{*}{A} & a & 0 & -0.61 & ab \\\\\n    ')
result = styler.to_latex()
assert expected in result
with option_context('styler.latex.multicol_align', 'l'):
    assert ' &  & \\multicolumn{2}{l}{Z} & Y \\\\' in styler.to_latex()
with option_context('styler.latex.multirow_align', 'b'):
    assert '\\multirow[b]{2}{*}{A} & a & 0 & -0.61 & ab \\\\' in styler.to_latex()
```

## Next Steps


---

*Source: test_to_latex.py:338 | Complexity: Intermediate | Last updated: 2026-06-02*