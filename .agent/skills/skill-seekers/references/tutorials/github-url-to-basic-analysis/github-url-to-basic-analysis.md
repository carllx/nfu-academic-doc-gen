# How To: Github Url To Basic Analysis

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: mock

## Overview

Instantiate InsightsStream: Test complete pipeline: GitHub URL → Basic analysis → Merged output

This tests the fast path (1-2 minutes) without C3.x analysis.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `unittest.mock`
- `pytest`
- `skill_seekers.cli.generate_router`
- `skill_seekers.cli.github_fetcher`
- `skill_seekers.cli.merge_sources`
- `skill_seekers.cli.unified_codebase_analyzer`

**Setup Required:**
```python
# Fixtures: mock_fetcher_class, tmp_path
```

## Step-by-Step Guide

### Step 1: Assign insights_stream = InsightsStream(...)

```python
insights_stream = InsightsStream(metadata={'stars': 1234, 'forks': 56, 'language': 'Python', 'description': 'A test project'}, common_problems=[{'title': 'Installation fails on Windows', 'number': 42, 'state': 'open', 'comments': 15, 'labels': ['bug', 'windows']}, {'title': 'Import error with Python 3.6', 'number': 38, 'state': 'open', 'comments': 10, 'labels': ['bug', 'python']}], known_solutions=[{'title': 'Fixed: Module not found', 'number': 35, 'state': 'closed', 'comments': 8, 'labels': ['bug']}], top_labels=[{'label': 'bug', 'count': 25}, {'label': 'enhancement', 'count': 15}, {'label': 'documentation', 'count': 10}])
```


## Complete Example

```python
# Setup
# Fixtures: mock_fetcher_class, tmp_path

# Workflow
insights_stream = InsightsStream(metadata={'stars': 1234, 'forks': 56, 'language': 'Python', 'description': 'A test project'}, common_problems=[{'title': 'Installation fails on Windows', 'number': 42, 'state': 'open', 'comments': 15, 'labels': ['bug', 'windows']}, {'title': 'Import error with Python 3.6', 'number': 38, 'state': 'open', 'comments': 10, 'labels': ['bug', 'python']}], known_solutions=[{'title': 'Fixed: Module not found', 'number': 35, 'state': 'closed', 'comments': 8, 'labels': ['bug']}], top_labels=[{'label': 'bug', 'count': 25}, {'label': 'enhancement', 'count': 15}, {'label': 'documentation', 'count': 10}])
```

## Next Steps


---

*Source: test_e2e_three_stream_pipeline.py:83 | Complexity: Beginner | Last updated: 2026-06-02*