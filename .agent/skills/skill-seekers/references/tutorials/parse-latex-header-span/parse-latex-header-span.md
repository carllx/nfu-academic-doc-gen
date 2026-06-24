# How To: Parse Latex Header Span

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test parse latex header span

## Prerequisites

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas`
- `pandas.io.formats.style`
- `pandas.io.formats.style_render`


## Step-by-Step Guide

### Step 1: Assign cell = value

```python
cell = {'attributes': 'colspan="3"', 'display_value': 'text', 'cellstyle': []}
```

**Verification:**
```python
assert _parse_latex_header_span(cell, 'X', 'Y') == expected
```

### Step 2: Assign expected = '\\multicolumn{3}{Y}{text}'

```python
expected = '\\multicolumn{3}{Y}{text}'
```

**Verification:**
```python
assert _parse_latex_header_span(cell, 'X', 'Y') == expected
```

### Step 3: Assign cell = value

```python
cell = {'attributes': 'rowspan="5"', 'display_value': 'text', 'cellstyle': []}
```

**Verification:**
```python
assert _parse_latex_header_span(cell, 'X', 'Y') == 'text'
```

### Step 4: Assign expected = '\\multirow[X]{5}{*}{text}'

```python
expected = '\\multirow[X]{5}{*}{text}'
```

**Verification:**
```python
assert _parse_latex_header_span(cell, 'X', 'Y') == '\\bfseries{text}'
```

### Step 5: Assign cell = value

```python
cell = {'display_value': 'text', 'cellstyle': []}
```

**Verification:**
```python
assert _parse_latex_header_span(cell, 'X', 'Y') == 'text'
```

### Step 6: Assign cell = value

```python
cell = {'display_value': 'text', 'cellstyle': [('bfseries', '--rwrap')]}
```

**Verification:**
```python
assert _parse_latex_header_span(cell, 'X', 'Y') == '\\bfseries{text}'
```


## Complete Example

```python
# Workflow
cell = {'attributes': 'colspan="3"', 'display_value': 'text', 'cellstyle': []}
expected = '\\multicolumn{3}{Y}{text}'
assert _parse_latex_header_span(cell, 'X', 'Y') == expected
cell = {'attributes': 'rowspan="5"', 'display_value': 'text', 'cellstyle': []}
expected = '\\multirow[X]{5}{*}{text}'
assert _parse_latex_header_span(cell, 'X', 'Y') == expected
cell = {'display_value': 'text', 'cellstyle': []}
assert _parse_latex_header_span(cell, 'X', 'Y') == 'text'
cell = {'display_value': 'text', 'cellstyle': [('bfseries', '--rwrap')]}
assert _parse_latex_header_span(cell, 'X', 'Y') == '\\bfseries{text}'
```

## Next Steps


---

*Source: test_to_latex.py:498 | Complexity: Intermediate | Last updated: 2026-06-02*