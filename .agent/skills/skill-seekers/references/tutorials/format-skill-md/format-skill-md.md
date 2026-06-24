# How To: Format Skill Md

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test formatting SKILL.md as Weaviate objects.

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

### Step 1: 'Test formatting SKILL.md as Weaviate objects.'

```python
'Test formatting SKILL.md as Weaviate objects.'
```

**Verification:**
```python
assert 'schema' in result
```

### Step 2: Assign skill_dir = value

```python
skill_dir = tmp_path / 'test_skill'
```

**Verification:**
```python
assert 'objects' in result
```

### Step 3: Call skill_dir.mkdir()

```python
skill_dir.mkdir()
```

**Verification:**
```python
assert 'class_name' in result
```

### Step 4: Assign skill_md = value

```python
skill_md = skill_dir / 'SKILL.md'
```

**Verification:**
```python
assert len(result['objects']) == 3
```

### Step 5: Call skill_md.write_text()

```python
skill_md.write_text('# Test Skill\n\nThis is a test skill for Weaviate format.')
```

**Verification:**
```python
assert 'id' in obj
```

### Step 6: Assign refs_dir = value

```python
refs_dir = skill_dir / 'references'
```

**Verification:**
```python
assert 'properties' in obj
```

### Step 7: Call refs_dir.mkdir()

```python
refs_dir.mkdir()
```

**Verification:**
```python
assert 'content' in props
```

### Step 8: Call unknown.write_text()

```python
(refs_dir / 'getting_started.md').write_text('# Getting Started\n\nQuick start.')
```

**Verification:**
```python
assert 'source' in props
```

### Step 9: Call unknown.write_text()

```python
(refs_dir / 'api.md').write_text('# API Reference\n\nAPI docs.')
```

**Verification:**
```python
assert props['source'] == 'test_skill'
```

### Step 10: Assign adaptor = get_adaptor(...)

```python
adaptor = get_adaptor('weaviate')
```

**Verification:**
```python
assert props['version'] == '1.0.0'
```

### Step 11: Assign metadata = SkillMetadata(...)

```python
metadata = SkillMetadata(name='test_skill', description='Test skill', version='1.0.0')
```

**Verification:**
```python
assert 'category' in props
```

### Step 12: Assign objects_json = adaptor.format_skill_md(...)

```python
objects_json = adaptor.format_skill_md(skill_dir, metadata)
```

**Verification:**
```python
assert 'file' in props
```

### Step 13: Assign result = json.loads(...)

```python
result = json.loads(objects_json)
```

**Verification:**
```python
assert 'type' in props
```

### Step 14: Assign categories = value

```python
categories = {obj['properties']['category'] for obj in result['objects']}
```

**Verification:**
```python
assert 'overview' in categories
```

### Step 15: Assign props = value

```python
props = obj['properties']
```

**Verification:**
```python
assert 'getting started' in categories or 'api' in categories
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'Test formatting SKILL.md as Weaviate objects.'
skill_dir = tmp_path / 'test_skill'
skill_dir.mkdir()
skill_md = skill_dir / 'SKILL.md'
skill_md.write_text('# Test Skill\n\nThis is a test skill for Weaviate format.')
refs_dir = skill_dir / 'references'
refs_dir.mkdir()
(refs_dir / 'getting_started.md').write_text('# Getting Started\n\nQuick start.')
(refs_dir / 'api.md').write_text('# API Reference\n\nAPI docs.')
adaptor = get_adaptor('weaviate')
metadata = SkillMetadata(name='test_skill', description='Test skill', version='1.0.0')
objects_json = adaptor.format_skill_md(skill_dir, metadata)
result = json.loads(objects_json)
assert 'schema' in result
assert 'objects' in result
assert 'class_name' in result
assert len(result['objects']) == 3
for obj in result['objects']:
    assert 'id' in obj
    assert 'properties' in obj
    props = obj['properties']
    assert 'content' in props
    assert 'source' in props
    assert props['source'] == 'test_skill'
    assert props['version'] == '1.0.0'
    assert 'category' in props
    assert 'file' in props
    assert 'type' in props
categories = {obj['properties']['category'] for obj in result['objects']}
assert 'overview' in categories
assert 'getting started' in categories or 'api' in categories
```

## Next Steps


---

*Source: test_weaviate_adaptor.py:23 | Complexity: Advanced | Last updated: 2026-06-02*