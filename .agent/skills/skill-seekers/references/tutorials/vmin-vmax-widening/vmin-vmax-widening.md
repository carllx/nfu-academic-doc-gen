# How To: Vmin Vmax Widening

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test vmin vmax widening

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: df_pos, df_neg, df_mix, values, vmin, vmax, nullify, align
```

## Step-by-Step Guide

### Step 1: Assign df = value

```python
df = {'positive': df_pos, 'negative': df_neg, 'mixed': df_mix}[values]
```

**Verification:**
```python
assert result.items() <= expected.items()
```

### Step 2: Assign vmin = value

```python
vmin = None if nullify == 'vmin' else vmin
```

### Step 3: Assign vmax = value

```python
vmax = None if nullify == 'vmax' else vmax
```

### Step 4: Assign expand_df = df.copy(...)

```python
expand_df = df.copy()
```

### Step 5: Assign unknown = value

```python
expand_df.loc[3, :], expand_df.loc[4, :] = (vmin, vmax)
```

### Step 6: Assign result = value

```python
result = df.style.bar(align=align, vmin=vmin, vmax=vmax, color=['red', 'green'])._compute().ctx
```

### Step 7: Assign expected = value

```python
expected = expand_df.style.bar(align=align, color=['red', 'green'])._compute().ctx
```

**Verification:**
```python
assert result.items() <= expected.items()
```

### Step 8: Assign align = 'left'

```python
align = 'left'
```

### Step 9: Assign align = 'right'

```python
align = 'right'
```


## Complete Example

```python
# Setup
# Fixtures: df_pos, df_neg, df_mix, values, vmin, vmax, nullify, align

# Workflow
if align == 'mid':
    if values == 'positive':
        align = 'left'
    elif values == 'negative':
        align = 'right'
df = {'positive': df_pos, 'negative': df_neg, 'mixed': df_mix}[values]
vmin = None if nullify == 'vmin' else vmin
vmax = None if nullify == 'vmax' else vmax
expand_df = df.copy()
expand_df.loc[3, :], expand_df.loc[4, :] = (vmin, vmax)
result = df.style.bar(align=align, vmin=vmin, vmax=vmax, color=['red', 'green'])._compute().ctx
expected = expand_df.style.bar(align=align, color=['red', 'green'])._compute().ctx
assert result.items() <= expected.items()
```

## Next Steps


---

*Source: test_bar.py:238 | Complexity: Advanced | Last updated: 2026-06-02*