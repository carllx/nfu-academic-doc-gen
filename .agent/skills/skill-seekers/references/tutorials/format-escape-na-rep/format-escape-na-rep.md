# How To: Format Escape Na Rep

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test format escape na rep

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
df = DataFrame([['<>&"', None]])
```

**Verification:**
```python
assert ex in s.to_html()
```

### Step 2: Assign s = Styler.format(...)

```python
s = Styler(df, uuid_len=0).format('X&{0}>X', escape='html', na_rep='&')
```

**Verification:**
```python
assert expected2 in s.to_html()
```

### Step 3: Assign ex = '<td id="T__row0_col0" class="data row0 col0" >X&&lt;&gt;&amp;&#34;>X</td>'

```python
ex = '<td id="T__row0_col0" class="data row0 col0" >X&&lt;&gt;&amp;&#34;>X</td>'
```

**Verification:**
```python
assert ctx['head'][0][1]['display_value'] == 'X&&lt;&gt;&amp;&#34;>X'
```

### Step 4: Assign expected2 = '<td id="T__row0_col1" class="data row0 col1" >&</td>'

```python
expected2 = '<td id="T__row0_col1" class="data row0 col1" >&</td>'
```

**Verification:**
```python
assert ctx['head'][0][2]['display_value'] == '&'
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['<>&"', None])
```

### Step 6: Assign styler = Styler(...)

```python
styler = Styler(df, uuid_len=0)
```

### Step 7: Call styler.format_index()

```python
styler.format_index('X&{0}>X', escape='html', na_rep='&', axis=1)
```

### Step 8: Assign ctx = styler._translate(...)

```python
ctx = styler._translate(True, True)
```

**Verification:**
```python
assert ctx['head'][0][1]['display_value'] == 'X&&lt;&gt;&amp;&#34;>X'
```


## Complete Example

```python
# Workflow
df = DataFrame([['<>&"', None]])
s = Styler(df, uuid_len=0).format('X&{0}>X', escape='html', na_rep='&')
ex = '<td id="T__row0_col0" class="data row0 col0" >X&&lt;&gt;&amp;&#34;>X</td>'
expected2 = '<td id="T__row0_col1" class="data row0 col1" >&</td>'
assert ex in s.to_html()
assert expected2 in s.to_html()
df = DataFrame(columns=['<>&"', None])
styler = Styler(df, uuid_len=0)
styler.format_index('X&{0}>X', escape='html', na_rep='&', axis=1)
ctx = styler._translate(True, True)
assert ctx['head'][0][1]['display_value'] == 'X&&lt;&gt;&amp;&#34;>X'
assert ctx['head'][0][2]['display_value'] == '&'
```

## Next Steps


---

*Source: test_format.py:242 | Complexity: Advanced | Last updated: 2026-06-02*