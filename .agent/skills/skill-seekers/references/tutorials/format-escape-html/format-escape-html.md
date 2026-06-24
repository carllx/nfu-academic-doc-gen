# How To: Format Escape Html

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test format escape html

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`

**Setup Required:**
```python
# Fixtures: escape, exp
```

## Step-by-Step Guide

### Step 1: Assign chars = '<>&"%$#_{}~^\\~ ^ \\ '

```python
chars = '<>&"%$#_{}~^\\~ ^ \\ '
```

**Verification:**
```python
assert expected in s.to_html()
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[chars]])
```

**Verification:**
```python
assert expected in s.to_html()
```

### Step 3: Assign s = Styler.format(...)

```python
s = Styler(df, uuid_len=0).format('&{0}&', escape=None)
```

**Verification:**
```python
assert styler._translate(True, True)['head'][0][1]['display_value'] == f'&{chars}&'
```

### Step 4: Assign expected = value

```python
expected = f'<td id="T__row0_col0" class="data row0 col0" >&{chars}&</td>'
```

**Verification:**
```python
assert styler._translate(True, True)['head'][0][1]['display_value'] == f'&{exp}&'
```

### Step 5: Assign s = Styler.format(...)

```python
s = Styler(df, uuid_len=0).format('&{0}&', escape=escape)
```

### Step 6: Assign expected = value

```python
expected = f'<td id="T__row0_col0" class="data row0 col0" >&{exp}&</td>'
```

**Verification:**
```python
assert expected in s.to_html()
```

### Step 7: Assign styler = Styler(...)

```python
styler = Styler(DataFrame(columns=[chars]), uuid_len=0)
```

### Step 8: Call styler.format_index()

```python
styler.format_index('&{0}&', escape=None, axis=1)
```

**Verification:**
```python
assert styler._translate(True, True)['head'][0][1]['display_value'] == f'&{chars}&'
```

### Step 9: Call styler.format_index()

```python
styler.format_index('&{0}&', escape=escape, axis=1)
```

**Verification:**
```python
assert styler._translate(True, True)['head'][0][1]['display_value'] == f'&{exp}&'
```


## Complete Example

```python
# Setup
# Fixtures: escape, exp

# Workflow
chars = '<>&"%$#_{}~^\\~ ^ \\ '
df = DataFrame([[chars]])
s = Styler(df, uuid_len=0).format('&{0}&', escape=None)
expected = f'<td id="T__row0_col0" class="data row0 col0" >&{chars}&</td>'
assert expected in s.to_html()
s = Styler(df, uuid_len=0).format('&{0}&', escape=escape)
expected = f'<td id="T__row0_col0" class="data row0 col0" >&{exp}&</td>'
assert expected in s.to_html()
styler = Styler(DataFrame(columns=[chars]), uuid_len=0)
styler.format_index('&{0}&', escape=None, axis=1)
assert styler._translate(True, True)['head'][0][1]['display_value'] == f'&{chars}&'
styler.format_index('&{0}&', escape=escape, axis=1)
assert styler._translate(True, True)['head'][0][1]['display_value'] == f'&{exp}&'
```

## Next Steps


---

*Source: test_format.py:174 | Complexity: Advanced | Last updated: 2026-06-02*