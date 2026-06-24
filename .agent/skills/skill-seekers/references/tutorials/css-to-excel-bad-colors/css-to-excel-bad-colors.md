# How To: Css To Excel Bad Colors

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test css to excel bad colors

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `pytest`
- `pandas.errors`
- `pandas._testing`
- `pandas.io.formats.excel`

**Setup Required:**
```python
# Fixtures: input_color
```

## Step-by-Step Guide

### Step 1: Assign css = value

```python
css = f'border-top-color: {input_color}; border-right-color: {input_color}; border-bottom-color: {input_color}; border-left-color: {input_color}; background-color: {input_color}; color: {input_color}'
```

**Verification:**
```python
assert expected == convert(css)
```

### Step 2: Assign expected = value

```python
expected = {}
```

### Step 3: Assign unknown = value

```python
expected['fill'] = {'patternType': 'solid'}
```

### Step 4: Assign convert = CSSToExcelConverter(...)

```python
convert = CSSToExcelConverter()
```

**Verification:**
```python
assert expected == convert(css)
```


## Complete Example

```python
# Setup
# Fixtures: input_color

# Workflow
css = f'border-top-color: {input_color}; border-right-color: {input_color}; border-bottom-color: {input_color}; border-left-color: {input_color}; background-color: {input_color}; color: {input_color}'
expected = {}
if input_color is not None:
    expected['fill'] = {'patternType': 'solid'}
with tm.assert_produces_warning(CSSWarning):
    convert = CSSToExcelConverter()
    assert expected == convert(css)
```

## Next Steps


---

*Source: test_to_excel.py:311 | Complexity: Intermediate | Last updated: 2026-06-02*