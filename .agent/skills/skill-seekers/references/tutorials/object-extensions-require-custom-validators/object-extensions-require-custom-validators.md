# How To: Object Extensions Require Custom Validators

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test object extensions require custom validators

## Prerequisites

**Required Modules:**
- `collections`
- `unittest`
- `jsonschema`
- `jsonschema._types`
- `jsonschema.exceptions`
- `jsonschema.validators`


## Step-by-Step Guide

### Step 1: Assign schema = value

```python
schema = {'type': 'object', 'required': ['x']}
```

### Step 2: Assign type_checker = Draft202012Validator.TYPE_CHECKER.redefine(...)

```python
type_checker = Draft202012Validator.TYPE_CHECKER.redefine('object', is_object_or_named_tuple)
```

### Step 3: Assign CustomValidator = extend(...)

```python
CustomValidator = extend(Draft202012Validator, type_checker=type_checker)
```

### Step 4: Assign validator = CustomValidator(...)

```python
validator = CustomValidator(schema)
```

### Step 5: Assign Point = namedtuple(...)

```python
Point = namedtuple('Point', ['x', 'y'])
```

### Step 6: Call validator.validate()

```python
validator.validate(Point(x=4, y=5))
```


## Complete Example

```python
# Workflow
schema = {'type': 'object', 'required': ['x']}
type_checker = Draft202012Validator.TYPE_CHECKER.redefine('object', is_object_or_named_tuple)
CustomValidator = extend(Draft202012Validator, type_checker=type_checker)
validator = CustomValidator(schema)
Point = namedtuple('Point', ['x', 'y'])
with self.assertRaises(ValidationError):
    validator.validate(Point(x=4, y=5))
```

## Next Steps


---

*Source: test_types.py:158 | Complexity: Intermediate | Last updated: 2026-06-02*