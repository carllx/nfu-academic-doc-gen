# How To: Referencing Suite

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test referencing suite

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pathlib`
- `json`
- `os`
- `pytest`
- `referencing`
- `referencing.exceptions`
- `referencing.jsonschema`

**Setup Required:**
```python
# Fixtures: test_path, subtests
```

## Step-by-Step Guide

### Step 1: Assign dialect_id = value

```python
dialect_id = DIALECT_IDS[test_path.relative_to(SUITE).parts[0]]
```

**Verification:**
```python
assert resolved.contents == test['target']
```

### Step 2: Assign specification = referencing.jsonschema.specification_with(...)

```python
specification = referencing.jsonschema.specification_with(dialect_id)
```

**Verification:**
```python
assert resolved.contents == then['target']
```

### Step 3: Assign loaded = json.loads(...)

```python
loaded = json.loads(test_path.read_text())
```

### Step 4: Assign registry = value

```python
registry = loaded['registry']
```

### Step 5: Assign registry = Registry.with_resources(...)

```python
registry = Registry().with_resources(((uri, specification.create_resource(contents)) for uri, contents in loaded['registry'].items()))
```

### Step 6: Assign resolver = registry.resolver(...)

```python
resolver = registry.resolver(base_uri=test.get('base_uri', ''))
```

### Step 7: Call pytest.xfail()

```python
pytest.xfail('APIs need to change for proper URL support.')
```

### Step 8: Assign resolved = resolver.lookup(...)

```python
resolved = resolver.lookup(test['ref'])
```

**Verification:**
```python
assert resolved.contents == test['target']
```

### Step 9: Assign then = test.get(...)

```python
then = test.get('then')
```

### Step 10: Call resolver.lookup()

```python
resolver.lookup(test['ref'])
```

### Step 11: Assign then = then.get(...)

```python
then = then.get('then')
```

### Step 12: Assign resolved = resolved.resolver.lookup(...)

```python
resolved = resolved.resolver.lookup(then['ref'])
```

**Verification:**
```python
assert resolved.contents == then['target']
```


## Complete Example

```python
# Setup
# Fixtures: test_path, subtests

# Workflow
dialect_id = DIALECT_IDS[test_path.relative_to(SUITE).parts[0]]
specification = referencing.jsonschema.specification_with(dialect_id)
loaded = json.loads(test_path.read_text())
registry = loaded['registry']
registry = Registry().with_resources(((uri, specification.create_resource(contents)) for uri, contents in loaded['registry'].items()))
for test in loaded['tests']:
    with subtests.test(test=test):
        if 'normalization' in test_path.stem:
            pytest.xfail('APIs need to change for proper URL support.')
        resolver = registry.resolver(base_uri=test.get('base_uri', ''))
        if test.get('error'):
            with pytest.raises(Unresolvable):
                resolver.lookup(test['ref'])
        else:
            resolved = resolver.lookup(test['ref'])
            assert resolved.contents == test['target']
            then = test.get('then')
            while then:
                with subtests.test(test=test, then=then):
                    resolved = resolved.resolver.lookup(then['ref'])
                    assert resolved.contents == then['target']
                then = then.get('then')
```

## Next Steps


---

*Source: test_referencing_suite.py:38 | Complexity: Advanced | Last updated: 2026-06-02*