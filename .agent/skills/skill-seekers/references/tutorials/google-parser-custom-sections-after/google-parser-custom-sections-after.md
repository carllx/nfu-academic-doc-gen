# How To: Google Parser Custom Sections After

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test parsing an unknown section with custom GoogleParser configuration
that was set at a runtime.

## Prerequisites

**Required Modules:**
- `typing`
- `pytest`
- `docstring_parser.common`
- `docstring_parser.google`


## Step-by-Step Guide

### Step 1: 'Test parsing an unknown section with custom GoogleParser configuration\n    that was set at a runtime.\n    '

```python
'Test parsing an unknown section with custom GoogleParser configuration\n    that was set at a runtime.\n    '
```

**Verification:**
```python
assert docstring.short_description == 'short description'
```

### Step 2: Assign parser = GoogleParser(...)

```python
parser = GoogleParser(title_colon=False)
```

**Verification:**
```python
assert docstring.long_description == 'Note:\n    a note'
```

### Step 3: Call parser.add_section()

```python
parser.add_section(Section('Note', 'note', SectionType.SINGULAR))
```

**Verification:**
```python
assert docstring.short_description == 'short description'
```

### Step 4: Assign docstring = parser.parse(...)

```python
docstring = parser.parse('\n        short description\n\n        Note:\n            a note\n        ')
```

**Verification:**
```python
assert docstring.long_description == 'Note a note'
```

### Step 5: Assign docstring = parser.parse(...)

```python
docstring = parser.parse('\n        short description\n\n        Note a note\n        ')
```

**Verification:**
```python
assert len(docstring.meta) == 1
```

### Step 6: Assign docstring = parser.parse(...)

```python
docstring = parser.parse('\n        short description\n\n        Note\n            a note\n        ')
```

**Verification:**
```python
assert docstring.meta[0].args == ['note']
```


## Complete Example

```python
# Workflow
'Test parsing an unknown section with custom GoogleParser configuration\n    that was set at a runtime.\n    '
parser = GoogleParser(title_colon=False)
parser.add_section(Section('Note', 'note', SectionType.SINGULAR))
docstring = parser.parse('\n        short description\n\n        Note:\n            a note\n        ')
assert docstring.short_description == 'short description'
assert docstring.long_description == 'Note:\n    a note'
docstring = parser.parse('\n        short description\n\n        Note a note\n        ')
assert docstring.short_description == 'short description'
assert docstring.long_description == 'Note a note'
docstring = parser.parse('\n        short description\n\n        Note\n            a note\n        ')
assert len(docstring.meta) == 1
assert docstring.meta[0].args == ['note']
assert docstring.meta[0].description == 'a note'
```

## Next Steps


---

*Source: test_google.py:103 | Complexity: Intermediate | Last updated: 2026-06-02*