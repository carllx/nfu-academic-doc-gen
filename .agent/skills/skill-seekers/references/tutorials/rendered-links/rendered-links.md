# How To: Rendered Links

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rendered links

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`

**Setup Required:**
```python
# Fixtures: type, text, exp, found
```

## Step-by-Step Guide

### Step 1: Assign rendered = value

```python
rendered = f'<a href="{found}" target="_blank">{found}</a>'
```

**Verification:**
```python
assert (rendered in result) is exp
```

### Step 2: Assign result = styler.to_html(...)

```python
result = styler.to_html()
```

**Verification:**
```python
assert (text in result) is not exp
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([text])
```

### Step 4: Assign styler = df.style.format(...)

```python
styler = df.style.format(hyperlinks='html')
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame([0], index=[text])
```

### Step 6: Assign styler = df.style.format_index(...)

```python
styler = df.style.format_index(hyperlinks='html')
```


## Complete Example

```python
# Setup
# Fixtures: type, text, exp, found

# Workflow
if type == 'data':
    df = DataFrame([text])
    styler = df.style.format(hyperlinks='html')
else:
    df = DataFrame([0], index=[text])
    styler = df.style.format_index(hyperlinks='html')
rendered = f'<a href="{found}" target="_blank">{found}</a>'
result = styler.to_html()
assert (rendered in result) is exp
assert (text in result) is not exp
```

## Next Steps


---

*Source: test_html.py:802 | Complexity: Intermediate | Last updated: 2026-06-02*