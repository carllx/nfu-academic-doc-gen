# How To: Extend Idof

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Extending a validator preserves its notion of schema IDs.

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

### Step 1: '\n        Extending a validator preserves its notion of schema IDs.\n        '

```python
'\n        Extending a validator preserves its notion of schema IDs.\n        '
```

### Step 2: Assign correct_id = 'the://correct/id/'

```python
correct_id = 'the://correct/id/'
```

### Step 3: Assign meta_schema = value

```python
meta_schema = {'$id': 'the://wrong/id/', '__test__': correct_id}
```

### Step 4: Assign Original = validators.create(...)

```python
Original = validators.create(meta_schema=meta_schema, validators=self.validators, type_checker=self.type_checker, id_of=id_of)
```

### Step 5: Call self.assertEqual()

```python
self.assertEqual(Original.ID_OF(Original.META_SCHEMA), correct_id)
```

### Step 6: Assign Derived = validators.extend(...)

```python
Derived = validators.extend(Original)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(Derived.ID_OF(Derived.META_SCHEMA), correct_id)
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
'\n        Extending a validator preserves its notion of schema IDs.\n        '

def id_of(schema):
    return schema.get('__test__', self.Validator.ID_OF(schema))
correct_id = 'the://correct/id/'
meta_schema = {'$id': 'the://wrong/id/', '__test__': correct_id}
Original = validators.create(meta_schema=meta_schema, validators=self.validators, type_checker=self.type_checker, id_of=id_of)
self.assertEqual(Original.ID_OF(Original.META_SCHEMA), correct_id)
Derived = validators.extend(Original)
self.assertEqual(Derived.ID_OF(Derived.META_SCHEMA), correct_id)
```

## Next Steps


---

*Source: test_validators.py:266 | Complexity: Intermediate | Last updated: 2026-06-02*