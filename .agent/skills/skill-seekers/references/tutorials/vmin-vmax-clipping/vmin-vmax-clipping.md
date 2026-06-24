# How To: Vmin Vmax Clipping

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test vmin vmax clipping

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
assert result == expected
```

### Step 2: Assign vmin = value

```python
vmin = None if nullify == 'vmin' else vmin
```

### Step 3: Assign vmax = value

```python
vmax = None if nullify == 'vmax' else vmax
```

### Step 4: Assign clip_df = df.where(...)

```python
clip_df = df.where(df <= (vmax if vmax else 999), other=vmax)
```

### Step 5: Assign clip_df = clip_df.where(...)

```python
clip_df = clip_df.where(clip_df >= (vmin if vmin else -999), other=vmin)
```

### Step 6: Assign result = value

```python
result = df.style.bar(align=align, vmin=vmin, vmax=vmax, color=['red', 'green'])._compute().ctx
```

### Step 7: Assign expected = value

```python
expected = clip_df.style.bar(align=align, color=['red', 'green'])._compute().ctx
```

**Verification:**
```python
assert result == expected
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
clip_df = df.where(df <= (vmax if vmax else 999), other=vmax)
clip_df = clip_df.where(clip_df >= (vmin if vmin else -999), other=vmin)
result = df.style.bar(align=align, vmin=vmin, vmax=vmax, color=['red', 'green'])._compute().ctx
expected = clip_df.style.bar(align=align, color=['red', 'green'])._compute().ctx
assert result == expected
```

## Next Steps


---

*Source: test_bar.py:205 | Complexity: Advanced | Last updated: 2026-06-02*