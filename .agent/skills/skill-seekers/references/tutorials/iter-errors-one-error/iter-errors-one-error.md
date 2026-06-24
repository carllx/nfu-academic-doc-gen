# How To: Iter Errors One Error

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test iter errors one error

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `collections`
- `contextlib`
- `decimal`
- `io`
- `typing`
- `unittest`
- `urllib.request`
- `json`
- `os`
- `sys`
- `tempfile`
- `warnings`
- `attrs`
- `referencing.jsonschema`
- `referencing.exceptions`
- `jsonschema`
- `threading`

**Setup Required:**
```python
self.addCleanup(self.assertEqual, validators._META_SCHEMAS, dict(validators._META_SCHEMAS))
self.addCleanup(self.assertEqual, validators._VALIDATORS, dict(validators._VALIDATORS))
self.meta_schema = {'$id': 'some://meta/schema'}
self.validators = {'fail': fail}
self.type_checker = TypeChecker()
self.Validator = validators.create(meta_schema=self.meta_schema, validators=self.validators, type_checker=self.type_checker)
```

## Step-by-Step Guide

### Step 1: Assign schema = value

```python
schema = {'fail': [{'message': 'Whoops!'}]}
```

### Step 2: Assign validator = self.Validator(...)

```python
validator = self.Validator(schema)
```

### Step 3: Assign expected_error = exceptions.ValidationError(...)

```python
expected_error = exceptions.ValidationError('Whoops!', instance='goodbye', schema=schema, validator='fail', validator_value=[{'message': 'Whoops!'}], schema_path=deque(['fail']))
```

### Step 4: Assign errors = list(...)

```python
errors = list(validator.iter_errors('goodbye'))
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(len(errors), 1)
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(errors[0]._contents(), expected_error._contents())
```


## Complete Example

```python
# Setup
self.addCleanup(self.assertEqual, validators._META_SCHEMAS, dict(validators._META_SCHEMAS))
self.addCleanup(self.assertEqual, validators._VALIDATORS, dict(validators._VALIDATORS))
self.meta_schema = {'$id': 'some://meta/schema'}
self.validators = {'fail': fail}
self.type_checker = TypeChecker()
self.Validator = validators.create(meta_schema=self.meta_schema, validators=self.validators, type_checker=self.type_checker)

# Workflow
schema = {'fail': [{'message': 'Whoops!'}]}
validator = self.Validator(schema)
expected_error = exceptions.ValidationError('Whoops!', instance='goodbye', schema=schema, validator='fail', validator_value=[{'message': 'Whoops!'}], schema_path=deque(['fail']))
errors = list(validator.iter_errors('goodbye'))
self.assertEqual(len(errors), 1)
self.assertEqual(errors[0]._contents(), expected_error._contents())
```

## Next Steps


---

*Source: test_validators.py:81 | Complexity: Advanced | Last updated: 2026-06-02*