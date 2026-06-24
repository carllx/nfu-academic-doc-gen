# How To: Mi Styler Comp

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: mi styler comp

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `copy`
- `re`
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`

**Setup Required:**
```python
# Fixtures: mi_styler
```

## Step-by-Step Guide

### Step 1: Assign mi_styler = mi_styler._copy(...)

```python
mi_styler = mi_styler._copy(deepcopy=True)
```

### Step 2: Assign mi_styler.css = value

```python
mi_styler.css = {**mi_styler.css, 'row': 'ROW', 'col': 'COL'}
```

### Step 3: Assign mi_styler.uuid_len = 5

```python
mi_styler.uuid_len = 5
```

### Step 4: Assign mi_styler.uuid = 'abcde'

```python
mi_styler.uuid = 'abcde'
```

### Step 5: Call mi_styler.set_caption()

```python
mi_styler.set_caption('capt')
```

### Step 6: Call mi_styler.set_table_styles()

```python
mi_styler.set_table_styles([{'selector': 'a', 'props': 'a:v;'}])
```

### Step 7: Call mi_styler.hide()

```python
mi_styler.hide(axis='columns')
```

### Step 8: Call mi_styler.hide()

```python
mi_styler.hide([('c0', 'c1_a')], axis='columns', names=True)
```

### Step 9: Call mi_styler.hide()

```python
mi_styler.hide(axis='index')
```

### Step 10: Call mi_styler.hide()

```python
mi_styler.hide([('i0', 'i1_a')], axis='index', names=True)
```

### Step 11: Call mi_styler.set_table_attributes()

```python
mi_styler.set_table_attributes('class="box"')
```

### Step 12: Assign other = mi_styler.data.agg(...)

```python
other = mi_styler.data.agg(['mean'])
```

### Step 13: Assign other.index = MultiIndex.from_product(...)

```python
other.index = MultiIndex.from_product([[''], other.index])
```

### Step 14: Call mi_styler.concat()

```python
mi_styler.concat(other.style)
```

### Step 15: Call mi_styler.format()

```python
mi_styler.format(na_rep='MISSING', precision=3)
```

### Step 16: Call mi_styler.format_index()

```python
mi_styler.format_index(precision=2, axis=0)
```

### Step 17: Call mi_styler.format_index()

```python
mi_styler.format_index(precision=4, axis=1)
```

### Step 18: Call mi_styler.highlight_max()

```python
mi_styler.highlight_max(axis=None)
```

### Step 19: Call mi_styler.map_index()

```python
mi_styler.map_index(lambda x: 'color: white;', axis=0)
```

### Step 20: Call mi_styler.map_index()

```python
mi_styler.map_index(lambda x: 'color: black;', axis=1)
```

### Step 21: Call mi_styler.set_td_classes()

```python
mi_styler.set_td_classes(DataFrame([['a', 'b'], ['a', 'c']], index=mi_styler.index, columns=mi_styler.columns))
```

### Step 22: Call mi_styler.set_tooltips()

```python
mi_styler.set_tooltips(DataFrame([['a2', 'b2'], ['a2', 'c2']], index=mi_styler.index, columns=mi_styler.columns))
```


## Complete Example

```python
# Setup
# Fixtures: mi_styler

# Workflow
mi_styler = mi_styler._copy(deepcopy=True)
mi_styler.css = {**mi_styler.css, 'row': 'ROW', 'col': 'COL'}
mi_styler.uuid_len = 5
mi_styler.uuid = 'abcde'
mi_styler.set_caption('capt')
mi_styler.set_table_styles([{'selector': 'a', 'props': 'a:v;'}])
mi_styler.hide(axis='columns')
mi_styler.hide([('c0', 'c1_a')], axis='columns', names=True)
mi_styler.hide(axis='index')
mi_styler.hide([('i0', 'i1_a')], axis='index', names=True)
mi_styler.set_table_attributes('class="box"')
other = mi_styler.data.agg(['mean'])
other.index = MultiIndex.from_product([[''], other.index])
mi_styler.concat(other.style)
mi_styler.format(na_rep='MISSING', precision=3)
mi_styler.format_index(precision=2, axis=0)
mi_styler.format_index(precision=4, axis=1)
mi_styler.highlight_max(axis=None)
mi_styler.map_index(lambda x: 'color: white;', axis=0)
mi_styler.map_index(lambda x: 'color: black;', axis=1)
mi_styler.set_td_classes(DataFrame([['a', 'b'], ['a', 'c']], index=mi_styler.index, columns=mi_styler.columns))
mi_styler.set_tooltips(DataFrame([['a2', 'b2'], ['a2', 'c2']], index=mi_styler.index, columns=mi_styler.columns))
return mi_styler
```

## Next Steps


---

*Source: test_style.py:46 | Complexity: Advanced | Last updated: 2026-06-02*