# How To: Format With Na Rep

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test format with na rep

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[None, None], [1.1, 1.2]], columns=['A', 'B'])
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == '-'
```

### Step 2: Assign ctx = df.style.format._translate(...)

```python
ctx = df.style.format(None, na_rep='-')._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][2]['display_value'] == '-'
```

### Step 3: Assign ctx = df.style.format._translate(...)

```python
ctx = df.style.format('{:.2%}', na_rep='-')._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][1]['display_value'] == '-'
```

### Step 4: Assign ctx = df.style.format._translate(...)

```python
ctx = df.style.format('{:.2%}', na_rep='-', subset=['B'])._translate(True, True)
```

**Verification:**
```python
assert ctx['body'][0][2]['display_value'] == '-'
```


## Complete Example

```python
# Workflow
df = DataFrame([[None, None], [1.1, 1.2]], columns=['A', 'B'])
ctx = df.style.format(None, na_rep='-')._translate(True, True)
assert ctx['body'][0][1]['display_value'] == '-'
assert ctx['body'][0][2]['display_value'] == '-'
ctx = df.style.format('{:.2%}', na_rep='-')._translate(True, True)
assert ctx['body'][0][1]['display_value'] == '-'
assert ctx['body'][0][2]['display_value'] == '-'
assert ctx['body'][1][1]['display_value'] == '110.00%'
assert ctx['body'][1][2]['display_value'] == '120.00%'
ctx = df.style.format('{:.2%}', na_rep='-', subset=['B'])._translate(True, True)
assert ctx['body'][0][2]['display_value'] == '-'
assert ctx['body'][1][2]['display_value'] == '120.00%'
```

## Next Steps


---

*Source: test_format.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*