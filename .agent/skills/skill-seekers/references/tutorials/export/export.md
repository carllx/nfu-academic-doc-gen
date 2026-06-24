# How To: Export

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test export

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
# Fixtures: mi_styler_comp, mi_styler
```

## Step-by-Step Guide

### Step 1: Assign exp_attrs = value

```python
exp_attrs = ['_todo', 'hide_index_', 'hide_index_names', 'hide_columns_', 'hide_column_names', 'table_attributes', 'table_styles', 'css']
```

**Verification:**
```python
assert not (all(check) if hasattr(check, '__iter__') and len(check) > 0 else check)
```

### Step 2: Assign export = mi_styler_comp.export(...)

```python
export = mi_styler_comp.export()
```

**Verification:**
```python
assert all(check) if hasattr(check, '__iter__') and len(check) > 0 else check
```

### Step 3: Assign used = mi_styler.use(...)

```python
used = mi_styler.use(export)
```

### Step 4: Call used.to_html()

```python
used.to_html()
```

### Step 5: Assign check = value

```python
check = getattr(mi_styler, attr) == getattr(mi_styler_comp, attr)
```

**Verification:**
```python
assert not (all(check) if hasattr(check, '__iter__') and len(check) > 0 else check)
```

### Step 6: Assign check = value

```python
check = getattr(used, attr) == getattr(mi_styler_comp, attr)
```

**Verification:**
```python
assert all(check) if hasattr(check, '__iter__') and len(check) > 0 else check
```


## Complete Example

```python
# Setup
# Fixtures: mi_styler_comp, mi_styler

# Workflow
exp_attrs = ['_todo', 'hide_index_', 'hide_index_names', 'hide_columns_', 'hide_column_names', 'table_attributes', 'table_styles', 'css']
for attr in exp_attrs:
    check = getattr(mi_styler, attr) == getattr(mi_styler_comp, attr)
    assert not (all(check) if hasattr(check, '__iter__') and len(check) > 0 else check)
export = mi_styler_comp.export()
used = mi_styler.use(export)
for attr in exp_attrs:
    check = getattr(used, attr) == getattr(mi_styler_comp, attr)
    assert all(check) if hasattr(check, '__iter__') and len(check) > 0 else check
used.to_html()
```

## Next Steps


---

*Source: test_style.py:369 | Complexity: Intermediate | Last updated: 2026-06-02*