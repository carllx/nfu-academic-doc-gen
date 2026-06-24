# How To: References Only

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test skill with references but no SKILL.md.

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

### Step 1: 'Test skill with references but no SKILL.md.'

```python
'Test skill with references but no SKILL.md.'
```

**Verification:**
```python
assert len(result['objects']) == 1
```

### Step 2: Assign skill_dir = value

```python
skill_dir = tmp_path / 'refs_only'
```

**Verification:**
```python
assert result['objects'][0]['properties']['category'] == 'test'
```

### Step 3: Call skill_dir.mkdir()

```python
skill_dir.mkdir()
```

**Verification:**
```python
assert result['objects'][0]['properties']['type'] == 'reference'
```

### Step 4: Assign refs_dir = value

```python
refs_dir = skill_dir / 'references'
```

### Step 5: Call refs_dir.mkdir()

```python
refs_dir.mkdir()
```

### Step 6: Call unknown.write_text()

```python
(refs_dir / 'test.md').write_text('# Test\n\nTest content.')
```

### Step 7: Assign adaptor = get_adaptor(...)

```python
adaptor = get_adaptor('weaviate')
```

### Step 8: Assign metadata = SkillMetadata(...)

```python
metadata = SkillMetadata(name='refs_only', description='Refs only', version='1.0.0')
```

### Step 9: Assign objects_json = adaptor.format_skill_md(...)

```python
objects_json = adaptor.format_skill_md(skill_dir, metadata)
```

### Step 10: Assign result = json.loads(...)

```python
result = json.loads(objects_json)
```

**Verification:**
```python
assert len(result['objects']) == 1
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'Test skill with references but no SKILL.md.'
skill_dir = tmp_path / 'refs_only'
skill_dir.mkdir()
refs_dir = skill_dir / 'references'
refs_dir.mkdir()
(refs_dir / 'test.md').write_text('# Test\n\nTest content.')
adaptor = get_adaptor('weaviate')
metadata = SkillMetadata(name='refs_only', description='Refs only', version='1.0.0')
objects_json = adaptor.format_skill_md(skill_dir, metadata)
result = json.loads(objects_json)
assert len(result['objects']) == 1
assert result['objects'][0]['properties']['category'] == 'test'
assert result['objects'][0]['properties']['type'] == 'reference'
```

## Next Steps


---

*Source: test_weaviate_adaptor.py:172 | Complexity: Advanced | Last updated: 2026-06-02*