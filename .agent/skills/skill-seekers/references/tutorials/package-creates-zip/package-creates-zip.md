# How To: Package Creates Zip

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test package creates zip

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
assert package_path.exists()
```

### Step 2: PLATFORM_EXPECTED[platform]

```python
PLATFORM_EXPECTED[platform]
```

**Verification:**
```python
assert str(package_path).endswith('.zip')
```

### Step 3: Assign skill_dir = value

```python
skill_dir = Path(temp_dir) / 'test-skill'
```

**Verification:**
```python
assert 'system_instructions.txt' in names, f'system_instructions.txt missing for {platform}'
```

### Step 4: Call skill_dir.mkdir()

```python
skill_dir.mkdir()
```

**Verification:**
```python
assert any((f'{platform}_metadata.json' in n for n in names)), f'metadata missing for {platform}'
```

### Step 5: Call unknown.write_text()

```python
(skill_dir / 'SKILL.md').write_text('You are an expert assistant')
```

**Verification:**
```python
assert any(('knowledge_files' in n for n in names))
```

### Step 6: Call unknown.mkdir()

```python
(skill_dir / 'references').mkdir()
```

### Step 7: Call unknown.write_text()

```python
(skill_dir / 'references' / 'test.md').write_text('# Reference')
```

### Step 8: Assign output_dir = value

```python
output_dir = Path(temp_dir) / 'output'
```

### Step 9: Call output_dir.mkdir()

```python
output_dir.mkdir()
```

### Step 10: Assign package_path = adaptor.package(...)

```python
package_path = adaptor.package(skill_dir, output_dir)
```

**Verification:**
```python
assert package_path.exists()
```

### Step 11: Assign names = zf.namelist(...)

```python
names = zf.namelist()
```

**Verification:**
```python
assert 'system_instructions.txt' in names, f'system_instructions.txt missing for {platform}'
```


## Complete Example

```python
# Setup
# Fixtures: platform

# Workflow
adaptor = get_adaptor(platform)
PLATFORM_EXPECTED[platform]
with tempfile.TemporaryDirectory() as temp_dir:
    skill_dir = Path(temp_dir) / 'test-skill'
    skill_dir.mkdir()
    (skill_dir / 'SKILL.md').write_text('You are an expert assistant')
    (skill_dir / 'references').mkdir()
    (skill_dir / 'references' / 'test.md').write_text('# Reference')
    output_dir = Path(temp_dir) / 'output'
    output_dir.mkdir()
    package_path = adaptor.package(skill_dir, output_dir)
    assert package_path.exists()
    assert str(package_path).endswith('.zip')
    with zipfile.ZipFile(package_path, 'r') as zf:
        names = zf.namelist()
        assert 'system_instructions.txt' in names, f'system_instructions.txt missing for {platform}'
        assert any((f'{platform}_metadata.json' in n for n in names)), f'metadata missing for {platform}'
        assert any(('knowledge_files' in n for n in names))
```

## Next Steps


---

*Source: test_openai_compatible_shared.py:150 | Complexity: Advanced | Last updated: 2026-06-02*