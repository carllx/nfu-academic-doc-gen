# How To: To Latex Midrule Location

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to latex midrule location

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
df = DataFrame({'a': [1, 2]})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df.index.name = 'foo'

```python
df.index.name = 'foo'
```

### Step 3: Assign result = df.to_latex(...)

```python
result = df.to_latex(index_names=False)
```

### Step 4: Assign expected = _dedent(...)

```python
expected = _dedent('\n            \\begin{tabular}{lr}\n            \\toprule\n             & a \\\\\n            \\midrule\n            0 & 1 \\\\\n            1 & 2 \\\\\n            \\bottomrule\n            \\end{tabular}\n            ')
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2]})
df.index.name = 'foo'
result = df.to_latex(index_names=False)
expected = _dedent('\n            \\begin{tabular}{lr}\n            \\toprule\n             & a \\\\\n            \\midrule\n            0 & 1 \\\\\n            1 & 2 \\\\\n            \\bottomrule\n            \\end{tabular}\n            ')
assert result == expected
```

## Next Steps


---

*Source: test_to_latex.py:170 | Complexity: Intermediate | Last updated: 2026-06-02*