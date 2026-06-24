# How To: To Latex Multiindex Multirow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to latex multiindex multirow

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
mi = pd.MultiIndex.from_product([[0.0, 1.0], [3.0, 2.0, 1.0], ['0', '1']], names=['i', 'val0', 'val1'])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(index=mi)
```

### Step 3: Assign result = df.to_latex(...)

```python
result = df.to_latex(multirow=True, escape=False)
```

### Step 4: Assign expected = _dedent(...)

```python
expected = _dedent('\n            \\begin{tabular}{lll}\n            \\toprule\n            i & val0 & val1 \\\\\n            \\midrule\n            \\multirow[t]{6}{*}{0.000000} & \\multirow[t]{2}{*}{3.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{2-3}\n             & \\multirow[t]{2}{*}{2.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{2-3}\n             & \\multirow[t]{2}{*}{1.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{1-3} \\cline{2-3}\n            \\multirow[t]{6}{*}{1.000000} & \\multirow[t]{2}{*}{3.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{2-3}\n             & \\multirow[t]{2}{*}{2.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{2-3}\n             & \\multirow[t]{2}{*}{1.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{1-3} \\cline{2-3}\n            \\bottomrule\n            \\end{tabular}\n            ')
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
mi = pd.MultiIndex.from_product([[0.0, 1.0], [3.0, 2.0, 1.0], ['0', '1']], names=['i', 'val0', 'val1'])
df = DataFrame(index=mi)
result = df.to_latex(multirow=True, escape=False)
expected = _dedent('\n            \\begin{tabular}{lll}\n            \\toprule\n            i & val0 & val1 \\\\\n            \\midrule\n            \\multirow[t]{6}{*}{0.000000} & \\multirow[t]{2}{*}{3.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{2-3}\n             & \\multirow[t]{2}{*}{2.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{2-3}\n             & \\multirow[t]{2}{*}{1.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{1-3} \\cline{2-3}\n            \\multirow[t]{6}{*}{1.000000} & \\multirow[t]{2}{*}{3.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{2-3}\n             & \\multirow[t]{2}{*}{2.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{2-3}\n             & \\multirow[t]{2}{*}{1.000000} & 0 \\\\\n             &  & 1 \\\\\n            \\cline{1-3} \\cline{2-3}\n            \\bottomrule\n            \\end{tabular}\n            ')
assert result == expected
```

## Next Steps


---

*Source: test_to_latex.py:1389 | Complexity: Intermediate | Last updated: 2026-06-02*