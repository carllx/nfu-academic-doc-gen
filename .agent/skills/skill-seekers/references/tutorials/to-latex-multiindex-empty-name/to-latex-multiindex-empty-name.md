# How To: To Latex Multiindex Empty Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to latex multiindex empty name

## Prerequisites

**Required Modules:**
- `datetime`
- `textwrap`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = pd.MultiIndex.from_product(...)

```python
mi = pd.MultiIndex.from_product([[1, 2]], names=[''])
```

**Verification:**
```python
assert observed == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(-1, index=mi, columns=range(4))
```

### Step 3: Assign observed = df.to_latex(...)

```python
observed = df.to_latex()
```

### Step 4: Assign expected = _dedent(...)

```python
expected = _dedent('\n            \\begin{tabular}{lrrrr}\n            \\toprule\n             & 0 & 1 & 2 & 3 \\\\\n             &  &  &  &  \\\\\n            \\midrule\n            1 & -1 & -1 & -1 & -1 \\\\\n            2 & -1 & -1 & -1 & -1 \\\\\n            \\bottomrule\n            \\end{tabular}\n            ')
```

**Verification:**
```python
assert observed == expected
```


## Complete Example

```python
# Workflow
mi = pd.MultiIndex.from_product([[1, 2]], names=[''])
df = DataFrame(-1, index=mi, columns=range(4))
observed = df.to_latex()
expected = _dedent('\n            \\begin{tabular}{lrrrr}\n            \\toprule\n             & 0 & 1 & 2 & 3 \\\\\n             &  &  &  &  \\\\\n            \\midrule\n            1 & -1 & -1 & -1 & -1 \\\\\n            2 & -1 & -1 & -1 & -1 \\\\\n            \\bottomrule\n            \\end{tabular}\n            ')
assert observed == expected
```

## Next Steps


---

*Source: test_to_latex.py:1054 | Complexity: Intermediate | Last updated: 2026-06-02*