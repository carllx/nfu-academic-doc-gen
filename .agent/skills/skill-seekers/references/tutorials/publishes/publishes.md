# How To: Publishes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test publishes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas._config.config`
- `pandas`

**Setup Required:**
```python
# Fixtures: ip
```

## Step-by-Step Guide

### Step 1: Assign ipython = ip.instance(...)

```python
ipython = ip.instance(config=ip.config)
```

**Verification:**
```python
assert set(formatted[0].keys()) == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2]})
```

**Verification:**
```python
assert set(formatted[0].keys()) == expected
```

### Step 3: Assign objects = value

```python
objects = [df['A'], df]
```

### Step 4: Assign expected_keys = value

```python
expected_keys = [{'text/plain', 'application/vnd.dataresource+json'}, {'text/plain', 'text/html', 'application/vnd.dataresource+json'}]
```

### Step 5: Assign opt = cf.option_context(...)

```python
opt = cf.option_context('display.html.table_schema', True)
```

### Step 6: Assign last_obj = None

```python
last_obj = None
```

### Step 7: Assign with_latex = cf.option_context(...)

```python
with_latex = cf.option_context('styler.render.repr', 'latex')
```

### Step 8: Assign expected = value

```python
expected = {'text/plain', 'text/html', 'text/latex', 'application/vnd.dataresource+json'}
```

**Verification:**
```python
assert set(formatted[0].keys()) == expected
```

### Step 9: Assign last_obj = obj

```python
last_obj = obj
```

**Verification:**
```python
assert set(formatted[0].keys()) == expected
```

### Step 10: Assign formatted = ipython.display_formatter.format(...)

```python
formatted = ipython.display_formatter.format(last_obj)
```

### Step 11: Assign formatted = ipython.display_formatter.format(...)

```python
formatted = ipython.display_formatter.format(obj)
```


## Complete Example

```python
# Setup
# Fixtures: ip

# Workflow
ipython = ip.instance(config=ip.config)
df = DataFrame({'A': [1, 2]})
objects = [df['A'], df]
expected_keys = [{'text/plain', 'application/vnd.dataresource+json'}, {'text/plain', 'text/html', 'application/vnd.dataresource+json'}]
opt = cf.option_context('display.html.table_schema', True)
last_obj = None
for obj, expected in zip(objects, expected_keys):
    last_obj = obj
    with opt:
        formatted = ipython.display_formatter.format(obj)
    assert set(formatted[0].keys()) == expected
with_latex = cf.option_context('styler.render.repr', 'latex')
with opt, with_latex:
    formatted = ipython.display_formatter.format(last_obj)
expected = {'text/plain', 'text/html', 'text/latex', 'application/vnd.dataresource+json'}
assert set(formatted[0].keys()) == expected
```

## Next Steps


---

*Source: test_ipython_compat.py:12 | Complexity: Advanced | Last updated: 2026-06-02*