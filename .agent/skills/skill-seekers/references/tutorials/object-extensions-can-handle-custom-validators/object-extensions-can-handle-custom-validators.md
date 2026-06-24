# How To: Object Extensions Can Handle Custom Validators

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test object extensions can handle custom validators

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
schema = {'type': 'object', 'required': ['x'], 'properties': {'x': {'type': 'integer'}}}
```

### Step 2: Assign type_checker = Draft202012Validator.TYPE_CHECKER.redefine(...)

```python
type_checker = Draft202012Validator.TYPE_CHECKER.redefine('object', is_object_or_named_tuple)
```

### Step 3: Assign required = coerce_named_tuple(...)

```python
required = coerce_named_tuple(_keywords.required)
```

### Step 4: Assign properties = coerce_named_tuple(...)

```python
properties = coerce_named_tuple(_keywords.properties)
```

### Step 5: Assign CustomValidator = extend(...)

```python
CustomValidator = extend(Draft202012Validator, type_checker=type_checker, validators={'required': required, 'properties': properties})
```

### Step 6: Assign validator = CustomValidator(...)

```python
validator = CustomValidator(schema)
```

### Step 7: Assign Point = namedtuple(...)

```python
Point = namedtuple('Point', ['x', 'y'])
```

### Step 8: Call validator.validate()

```python
validator.validate(Point(x=4, y=5))
```

### Step 9: Call validator.validate()

```python
validator.validate({'x': 4, 'y': 5})
```

### Step 10: Call validator.validate()

```python
validator.validate(Point(x='not an integer', y=5))
```

### Step 11: Call validator.validate()

```python
validator.validate({'x': 'not an integer', 'y': 5})
```

### Step 12: Assign instance = instance._asdict(...)

```python
instance = instance._asdict()
```


## Complete Example

```python
# Workflow
schema = {'type': 'object', 'required': ['x'], 'properties': {'x': {'type': 'integer'}}}
type_checker = Draft202012Validator.TYPE_CHECKER.redefine('object', is_object_or_named_tuple)

def coerce_named_tuple(fn):

    def coerced(validator, value, instance, schema):
        if is_namedtuple(instance):
            instance = instance._asdict()
        return fn(validator, value, instance, schema)
    return coerced
required = coerce_named_tuple(_keywords.required)
properties = coerce_named_tuple(_keywords.properties)
CustomValidator = extend(Draft202012Validator, type_checker=type_checker, validators={'required': required, 'properties': properties})
validator = CustomValidator(schema)
Point = namedtuple('Point', ['x', 'y'])
validator.validate(Point(x=4, y=5))
with self.assertRaises(ValidationError):
    validator.validate(Point(x='not an integer', y=5))
validator.validate({'x': 4, 'y': 5})
with self.assertRaises(ValidationError):
    validator.validate({'x': 'not an integer', 'y': 5})
```

## Next Steps


---

*Source: test_types.py:176 | Complexity: Advanced | Last updated: 2026-06-02*