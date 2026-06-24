# How To: Format Skill Md No Frontmatter

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test format skill md no frontmatter

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `tempfile`
- `zipfile`
- `pathlib`
- `unittest.mock`
- `pytest`
- `skill_seekers.cli.adaptors`
- `skill_seekers.cli.adaptors.base`

**Setup Required:**
```python
# Fixtures: platform
```

## Step-by-Step Guide

### Step 1: Assign adaptor = get_adaptor(...)

```python
adaptor = get_adaptor(platform)
```

**Verification:**
```python
assert not formatted.startswith('---'), 'OpenAI-compatible adaptors should NOT have YAML frontmatter'
```

### Step 2: PLATFORM_EXPECTED[platform]

```python
PLATFORM_EXPECTED[platform]
```

**Verification:**
```python
assert 'You are an expert assistant' in formatted
```

### Step 3: Assign skill_dir = Path(...)

```python
skill_dir = Path(temp_dir)
```

**Verification:**
```python
assert 'test-skill' in formatted
```

### Step 4: Call unknown.mkdir()

```python
(skill_dir / 'references').mkdir()
```

**Verification:**
```python
assert 'Test skill description' in formatted
```

### Step 5: Call unknown.write_text()

```python
(skill_dir / 'references' / 'test.md').write_text('# Test content')
```

### Step 6: Assign metadata = SkillMetadata(...)

```python
metadata = SkillMetadata(name='test-skill', description='Test skill description')
```

### Step 7: Assign formatted = adaptor.format_skill_md(...)

```python
formatted = adaptor.format_skill_md(skill_dir, metadata)
```

**Verification:**
```python
assert not formatted.startswith('---'), 'OpenAI-compatible adaptors should NOT have YAML frontmatter'
```


## Complete Example

```python
# Setup
# Fixtures: platform

# Workflow
adaptor = get_adaptor(platform)
PLATFORM_EXPECTED[platform]
with tempfile.TemporaryDirectory() as temp_dir:
    skill_dir = Path(temp_dir)
    (skill_dir / 'references').mkdir()
    (skill_dir / 'references' / 'test.md').write_text('# Test content')
    metadata = SkillMetadata(name='test-skill', description='Test skill description')
    formatted = adaptor.format_skill_md(skill_dir, metadata)
    assert not formatted.startswith('---'), 'OpenAI-compatible adaptors should NOT have YAML frontmatter'
    assert 'You are an expert assistant' in formatted
    assert 'test-skill' in formatted
    assert 'Test skill description' in formatted
```

## Next Steps


---

*Source: test_openai_compatible_shared.py:115 | Complexity: Intermediate | Last updated: 2026-06-02*