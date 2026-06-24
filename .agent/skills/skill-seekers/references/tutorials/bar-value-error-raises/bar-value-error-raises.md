# How To: Bar Value Error Raises

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bar value error raises

## Prerequisites

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [-100, -60, -30, -20]})
```

### Step 2: Assign msg = "`align` should be in {'left', 'right', 'mid', 'mean', 'zero'} or"

```python
msg = "`align` should be in {'left', 'right', 'mid', 'mean', 'zero'} or"
```

### Step 3: Assign msg = '`width` must be a value in \\[0, 100\\]'

```python
msg = '`width` must be a value in \\[0, 100\\]'
```

### Step 4: Assign msg = '`height` must be a value in \\[0, 100\\]'

```python
msg = '`height` must be a value in \\[0, 100\\]'
```

### Step 5: Call df.style.bar.to_html()

```python
df.style.bar(align='poorly', color=['#d65f5f', '#5fba7d']).to_html()
```

### Step 6: Call df.style.bar.to_html()

```python
df.style.bar(width=200).to_html()
```

### Step 7: Call df.style.bar.to_html()

```python
df.style.bar(height=200).to_html()
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [-100, -60, -30, -20]})
msg = "`align` should be in {'left', 'right', 'mid', 'mean', 'zero'} or"
with pytest.raises(ValueError, match=msg):
    df.style.bar(align='poorly', color=['#d65f5f', '#5fba7d']).to_html()
msg = '`width` must be a value in \\[0, 100\\]'
with pytest.raises(ValueError, match=msg):
    df.style.bar(width=200).to_html()
msg = '`height` must be a value in \\[0, 100\\]'
with pytest.raises(ValueError, match=msg):
    df.style.bar(height=200).to_html()
```

## Next Steps


---

*Source: test_bar.py:300 | Complexity: Intermediate | Last updated: 2026-06-02*