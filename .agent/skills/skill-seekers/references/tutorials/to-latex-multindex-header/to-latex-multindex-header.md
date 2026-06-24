# How To: To Latex Multindex Header

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to latex multindex header

## Prerequisites

**Required Modules:**
- `datetime`
- `textwrap`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [0], 'b': [1], 'c': [2], 'd': [3]})
```

**Verification:**
```python
assert observed == expected
```

### Step 2: Assign df = df.set_index(...)

```python
df = df.set_index(['a', 'b'])
```

### Step 3: Assign observed = df.to_latex(...)

```python
observed = df.to_latex(header=['r1', 'r2'], multirow=False)
```

### Step 4: Assign expected = _dedent(...)

```python
expected = _dedent('\n            \\begin{tabular}{llrr}\n            \\toprule\n             &  & r1 & r2 \\\\\n            a & b &  &  \\\\\n            \\midrule\n            0 & 1 & 2 & 3 \\\\\n            \\bottomrule\n            \\end{tabular}\n            ')
```

**Verification:**
```python
assert observed == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [0], 'b': [1], 'c': [2], 'd': [3]})
df = df.set_index(['a', 'b'])
observed = df.to_latex(header=['r1', 'r2'], multirow=False)
expected = _dedent('\n            \\begin{tabular}{llrr}\n            \\toprule\n             &  & r1 & r2 \\\\\n            a & b &  &  \\\\\n            \\midrule\n            0 & 1 & 2 & 3 \\\\\n            \\bottomrule\n            \\end{tabular}\n            ')
assert observed == expected
```

## Next Steps


---

*Source: test_to_latex.py:1035 | Complexity: Intermediate | Last updated: 2026-06-02*