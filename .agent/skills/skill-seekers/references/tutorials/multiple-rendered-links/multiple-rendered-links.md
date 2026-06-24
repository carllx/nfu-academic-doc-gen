# How To: Multiple Rendered Links

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple rendered links

## Prerequisites

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`


## Step-by-Step Guide

### Step 1: Assign links = value

```python
links = ('www.a.b', 'http://a.c', 'https://a.d', 'ftp://a.e')
```

**Verification:**
```python
assert href.format(link) in result
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(['text {} {} text {} {}'.format(*links)])
```

**Verification:**
```python
assert href.format('text') not in result
```

### Step 3: Assign result = df.style.format.to_html(...)

```python
result = df.style.format(hyperlinks='html').to_html()
```

### Step 4: Assign href = '<a href="{0}" target="_blank">{0}</a>'

```python
href = '<a href="{0}" target="_blank">{0}</a>'
```

**Verification:**
```python
assert href.format('text') not in result
```


## Complete Example

```python
# Workflow
links = ('www.a.b', 'http://a.c', 'https://a.d', 'ftp://a.e')
df = DataFrame(['text {} {} text {} {}'.format(*links)])
result = df.style.format(hyperlinks='html').to_html()
href = '<a href="{0}" target="_blank">{0}</a>'
for link in links:
    assert href.format(link) in result
assert href.format('text') not in result
```

## Next Steps


---

*Source: test_html.py:816 | Complexity: Intermediate | Last updated: 2026-06-02*