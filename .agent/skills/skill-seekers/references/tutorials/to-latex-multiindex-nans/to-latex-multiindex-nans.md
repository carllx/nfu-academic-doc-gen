# How To: To Latex Multiindex Nans

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to latex multiindex nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `textwrap`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: one_row
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [None, 1], 'b': [2, 3], 'c': [4, 5]})
```

**Verification:**
```python
assert observed == expected
```

### Step 2: Assign observed = df.set_index.to_latex(...)

```python
observed = df.set_index(['a', 'b']).to_latex(multirow=False)
```

### Step 3: Assign expected = _dedent(...)

```python
expected = _dedent('\n            \\begin{tabular}{llr}\n            \\toprule\n             &  & c \\\\\n            a & b &  \\\\\n            \\midrule\n            NaN & 2 & 4 \\\\\n            ')
```

**Verification:**
```python
assert observed == expected
```

### Step 4: Assign df = value

```python
df = df.iloc[[0]]
```


## Complete Example

```python
# Setup
# Fixtures: one_row

# Workflow
df = DataFrame({'a': [None, 1], 'b': [2, 3], 'c': [4, 5]})
if one_row:
    df = df.iloc[[0]]
observed = df.set_index(['a', 'b']).to_latex(multirow=False)
expected = _dedent('\n            \\begin{tabular}{llr}\n            \\toprule\n             &  & c \\\\\n            a & b &  \\\\\n            \\midrule\n            NaN & 2 & 4 \\\\\n            ')
if not one_row:
    expected += '1.000000 & 3 & 5 \\\\\n'
expected += '\\bottomrule\n\\end{tabular}\n'
assert observed == expected
```

## Next Steps


---

*Source: test_to_latex.py:1346 | Complexity: Intermediate | Last updated: 2026-06-02*