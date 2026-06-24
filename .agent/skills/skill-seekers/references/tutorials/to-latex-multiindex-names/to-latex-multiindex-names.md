# How To: To Latex Multiindex Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to latex multiindex names

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
# Fixtures: name0, name1, axes
```

## Step-by-Step Guide

### Step 1: Assign names = value

```python
names = [name0, name1]
```

**Verification:**
```python
assert observed == expected
```

### Step 2: Assign mi = pd.MultiIndex.from_product(...)

```python
mi = pd.MultiIndex.from_product([[1, 2], [3, 4]])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(-1, index=mi.copy(), columns=mi.copy())
```

### Step 4: Assign idx_names = tuple(...)

```python
idx_names = tuple((n or '' for n in names))
```

### Step 5: Assign idx_names_row = value

```python
idx_names_row = f'{idx_names[0]} & {idx_names[1]} &  &  &  &  \\\\\n' if 0 in axes and any(names) else ''
```

### Step 6: Assign col_names = value

```python
col_names = [n if bool(n) and 1 in axes else '' for n in names]
```

### Step 7: Assign observed = df.to_latex(...)

```python
observed = df.to_latex(multirow=False)
```

### Step 8: Assign expected = value

```python
expected = '\\begin{tabular}{llrrrr}\n\\toprule\n & %s & \\multicolumn{2}{r}{1} & \\multicolumn{2}{r}{2} \\\\\n & %s & 3 & 4 & 3 & 4 \\\\\n%s\\midrule\n1 & 3 & -1 & -1 & -1 & -1 \\\\\n & 4 & -1 & -1 & -1 & -1 \\\\\n2 & 3 & -1 & -1 & -1 & -1 \\\\\n & 4 & -1 & -1 & -1 & -1 \\\\\n\\bottomrule\n\\end{tabular}\n' % tuple(list(col_names) + [idx_names_row])
```

**Verification:**
```python
assert observed == expected
```

### Step 9: Assign unknown.names = names

```python
df.axes[idx].names = names
```


## Complete Example

```python
# Setup
# Fixtures: name0, name1, axes

# Workflow
names = [name0, name1]
mi = pd.MultiIndex.from_product([[1, 2], [3, 4]])
df = DataFrame(-1, index=mi.copy(), columns=mi.copy())
for idx in axes:
    df.axes[idx].names = names
idx_names = tuple((n or '' for n in names))
idx_names_row = f'{idx_names[0]} & {idx_names[1]} &  &  &  &  \\\\\n' if 0 in axes and any(names) else ''
col_names = [n if bool(n) and 1 in axes else '' for n in names]
observed = df.to_latex(multirow=False)
expected = '\\begin{tabular}{llrrrr}\n\\toprule\n & %s & \\multicolumn{2}{r}{1} & \\multicolumn{2}{r}{2} \\\\\n & %s & 3 & 4 & 3 & 4 \\\\\n%s\\midrule\n1 & 3 & -1 & -1 & -1 & -1 \\\\\n & 4 & -1 & -1 & -1 & -1 \\\\\n2 & 3 & -1 & -1 & -1 & -1 \\\\\n & 4 & -1 & -1 & -1 & -1 \\\\\n\\bottomrule\n\\end{tabular}\n' % tuple(list(col_names) + [idx_names_row])
assert observed == expected
```

## Next Steps


---

*Source: test_to_latex.py:1312 | Complexity: Advanced | Last updated: 2026-06-02*