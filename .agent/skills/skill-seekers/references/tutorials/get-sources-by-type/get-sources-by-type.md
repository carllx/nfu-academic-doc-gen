# How To: Get Sources By Type

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: get_sources_by_type returns only matching sources.

## Prerequisites

**Required Modules:**
- `sys`
- `unittest`
- `pathlib`
- `skill_seekers.cli.config_validator`


## Step-by-Step Guide

### Step 1: 'get_sources_by_type returns only matching sources.'

```python
'get_sources_by_type returns only matching sources.'
```

### Step 2: Assign config = value

```python
config = {'name': 'test', 'description': 'Test', 'sources': [{'type': 'documentation', 'base_url': 'https://example.com/'}, {'type': 'github', 'repo': 'facebook/react'}, {'type': 'documentation', 'base_url': 'https://foo.com/'}]}
```

### Step 3: Assign validator = UniSkillConfigValidator(...)

```python
validator = UniSkillConfigValidator(config)
```

### Step 4: Call validator.validate()

```python
validator.validate()
```

### Step 5: Assign docs = validator.get_sources_by_type(...)

```python
docs = validator.get_sources_by_type('documentation')
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(len(docs), 2)
```

### Step 7: Assign github = validator.get_sources_by_type(...)

```python
github = validator.get_sources_by_type('github')
```

### Step 8: Call self.assertEqual()

```python
self.assertEqual(len(github), 1)
```


## Complete Example

```python
# Workflow
'get_sources_by_type returns only matching sources.'
config = {'name': 'test', 'description': 'Test', 'sources': [{'type': 'documentation', 'base_url': 'https://example.com/'}, {'type': 'github', 'repo': 'facebook/react'}, {'type': 'documentation', 'base_url': 'https://foo.com/'}]}
validator = UniSkillConfigValidator(config)
validator.validate()
docs = validator.get_sources_by_type('documentation')
self.assertEqual(len(docs), 2)
github = validator.get_sources_by_type('github')
self.assertEqual(len(github), 1)
```

## Next Steps


---

*Source: test_unified_config_validator.py:312 | Complexity: Advanced | Last updated: 2026-06-02*