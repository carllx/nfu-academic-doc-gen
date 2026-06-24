# How To: To Latex Longtable Position

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to latex longtable position

## Prerequisites

**Required Modules:**
- `datetime`
- `textwrap`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign the_position = 't'

```python
the_position = 't'
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
```

### Step 3: Assign result = df.to_latex(...)

```python
result = df.to_latex(longtable=True, position=the_position)
```

### Step 4: Assign expected = _dedent(...)

```python
expected = _dedent('\n            \\begin{longtable}[t]{lrl}\n            \\toprule\n             & a & b \\\\\n            \\midrule\n            \\endfirsthead\n            \\toprule\n             & a & b \\\\\n            \\midrule\n            \\endhead\n            \\midrule\n            \\multicolumn{3}{r}{Continued on next page} \\\\\n            \\midrule\n            \\endfoot\n            \\bottomrule\n            \\endlastfoot\n            0 & 1 & b1 \\\\\n            1 & 2 & b2 \\\\\n            \\end{longtable}\n            ')
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
the_position = 't'
df = DataFrame({'a': [1, 2], 'b': ['b1', 'b2']})
result = df.to_latex(longtable=True, position=the_position)
expected = _dedent('\n            \\begin{longtable}[t]{lrl}\n            \\toprule\n             & a & b \\\\\n            \\midrule\n            \\endfirsthead\n            \\toprule\n             & a & b \\\\\n            \\midrule\n            \\endhead\n            \\midrule\n            \\multicolumn{3}{r}{Continued on next page} \\\\\n            \\midrule\n            \\endfoot\n            \\bottomrule\n            \\endlastfoot\n            0 & 1 & b1 \\\\\n            1 & 2 & b2 \\\\\n            \\end{longtable}\n            ')
assert result == expected
```

## Next Steps


---

*Source: test_to_latex.py:881 | Complexity: Intermediate | Last updated: 2026-06-02*