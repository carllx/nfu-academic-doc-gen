# How To: Returns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test parsing returns.

## Prerequisites

**Required Modules:**
- `typing`
- `pytest`
- `docstring_parser.common`
- `docstring_parser.rest`


## Step-by-Step Guide

### Step 1: 'Test parsing returns.'

```python
'Test parsing returns.'
```

**Verification:**
```python
assert docstring.returns is None
```

### Step 2: Assign docstring = parse(...)

```python
docstring = parse('\n        Short description\n        ')
```

**Verification:**
```python
assert docstring.many_returns is not None
```

### Step 3: Assign docstring = parse(...)

```python
docstring = parse('\n        Short description\n        :returns: description\n        ')
```

**Verification:**
```python
assert len(docstring.many_returns) == 0
```

### Step 4: Assign docstring = parse(...)

```python
docstring = parse('\n        Short description\n        :returns int: description\n        ')
```

**Verification:**
```python
assert docstring.returns is not None
```

### Step 5: Assign docstring = parse(...)

```python
docstring = parse('\n        Short description\n        :returns: description\n        :rtype: int\n        ')
```

**Verification:**
```python
assert docstring.returns.type_name is None
```


## Complete Example

```python
# Workflow
'Test parsing returns.'
docstring = parse('\n        Short description\n        ')
assert docstring.returns is None
assert docstring.many_returns is not None
assert len(docstring.many_returns) == 0
docstring = parse('\n        Short description\n        :returns: description\n        ')
assert docstring.returns is not None
assert docstring.returns.type_name is None
assert docstring.returns.description == 'description'
assert not docstring.returns.is_generator
assert docstring.many_returns == [docstring.returns]
docstring = parse('\n        Short description\n        :returns int: description\n        ')
assert docstring.returns is not None
assert docstring.returns.type_name == 'int'
assert docstring.returns.description == 'description'
assert not docstring.returns.is_generator
assert docstring.many_returns == [docstring.returns]
docstring = parse('\n        Short description\n        :returns: description\n        :rtype: int\n        ')
assert docstring.returns is not None
assert docstring.returns.type_name == 'int'
assert docstring.returns.description == 'description'
assert not docstring.returns.is_generator
assert docstring.many_returns == [docstring.returns]
```

## Next Steps


---

*Source: test_rest.py:329 | Complexity: Intermediate | Last updated: 2026-06-02*