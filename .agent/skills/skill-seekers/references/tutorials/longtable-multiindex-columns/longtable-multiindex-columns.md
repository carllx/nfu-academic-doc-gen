# How To: Longtable Multiindex Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test longtable multiindex columns

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
# Fixtures: df, sparse, exp, siunitx
```

## Step-by-Step Guide

### Step 1: Assign cidx = MultiIndex.from_tuples(...)

```python
cidx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
```

**Verification:**
```python
assert expected in result
```

### Step 2: Assign df.columns = cidx

```python
df.columns = cidx
```

### Step 3: Assign with_si = '{} & {a} & {b} & {c} \\\\'

```python
with_si = '{} & {a} & {b} & {c} \\\\'
```

### Step 4: Assign without_si = ' & a & b & c \\\\'

```python
without_si = ' & a & b & c \\\\'
```

### Step 5: Assign expected = dedent(...)

```python
expected = dedent(f"        \\begin{{longtable}}{{l{('SS' if siunitx else 'rr')}l}}\n        {exp} \\\\\n        {(with_si if siunitx else without_si)}\n        \\endfirsthead\n        {exp} \\\\\n        {(with_si if siunitx else without_si)}\n        \\endhead\n        ")
```

### Step 6: Assign result = df.style.to_latex(...)

```python
result = df.style.to_latex(environment='longtable', sparse_columns=sparse, siunitx=siunitx)
```

**Verification:**
```python
assert expected in result
```


## Complete Example

```python
# Setup
# Fixtures: df, sparse, exp, siunitx

# Workflow
cidx = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'c')])
df.columns = cidx
with_si = '{} & {a} & {b} & {c} \\\\'
without_si = ' & a & b & c \\\\'
expected = dedent(f"        \\begin{{longtable}}{{l{('SS' if siunitx else 'rr')}l}}\n        {exp} \\\\\n        {(with_si if siunitx else without_si)}\n        \\endfirsthead\n        {exp} \\\\\n        {(with_si if siunitx else without_si)}\n        \\endhead\n        ")
result = df.style.to_latex(environment='longtable', sparse_columns=sparse, siunitx=siunitx)
assert expected in result
```

## Next Steps


---

*Source: test_to_latex.py:685 | Complexity: Intermediate | Last updated: 2026-06-02*