# How To: Empty Skill Directory

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test handling of empty skill directory.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `pytest`
- `skill_seekers.cli.adaptors`
- `skill_seekers.cli.adaptors.base`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: 'Test handling of empty skill directory.'

```python
'Test handling of empty skill directory.'
```

**Verification:**
```python
assert 'objects' in result
```

### Step 2: Assign skill_dir = value

```python
skill_dir = tmp_path / 'empty_skill'
```

**Verification:**
```python
assert result['objects'] == []
```

### Step 3: Call skill_dir.mkdir()

```python
skill_dir.mkdir()
```

### Step 4: Assign adaptor = get_adaptor(...)

```python
adaptor = get_adaptor('weaviate')
```

### Step 5: Assign metadata = SkillMetadata(...)

```python
metadata = SkillMetadata(name='empty_skill', description='Empty', version='1.0.0')
```

### Step 6: Assign objects_json = adaptor.format_skill_md(...)

```python
objects_json = adaptor.format_skill_md(skill_dir, metadata)
```

### Step 7: Assign result = json.loads(...)

```python
result = json.loads(objects_json)
```

**Verification:**
```python
assert 'objects' in result
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'Test handling of empty skill directory.'
skill_dir = tmp_path / 'empty_skill'
skill_dir.mkdir()
adaptor = get_adaptor('weaviate')
metadata = SkillMetadata(name='empty_skill', description='Empty', version='1.0.0')
objects_json = adaptor.format_skill_md(skill_dir, metadata)
result = json.loads(objects_json)
assert 'objects' in result
assert result['objects'] == []
```

## Next Steps


---

*Source: test_weaviate_adaptor.py:157 | Complexity: Intermediate | Last updated: 2026-06-02*