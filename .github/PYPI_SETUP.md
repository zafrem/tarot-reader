# PyPI Trusted Publishing Setup

This project uses PyPI's Trusted Publishing feature for secure, token-less publishing.

## Setup Instructions

### 1. Create a PyPI Account
If you don't have one already, create an account at https://pypi.org

### 2. Configure Trusted Publisher on PyPI

1. Go to https://pypi.org/manage/account/publishing/
2. Scroll to "Add a new pending publisher"
3. Fill in the form:
   - **PyPI Project Name**: `tarot-reader`
   - **Owner**: `zafrem` (your GitHub username)
   - **Repository name**: `tarot-reader`
   - **Workflow name**: `ci.yml`
   - **Environment name**: (leave blank)
4. Click "Add"

### 3. Create a Release

Once the trusted publisher is configured, you can create releases:

```bash
# Create and push a tag
git tag v0.1.0
git push origin v0.1.0
```

This will trigger the CI workflow which will:
1. Run all tests
2. Build the package
3. Publish to PyPI (only for tags starting with 'v')

## Notes

- The workflow only publishes when you push a tag matching `v*` (e.g., `v0.1.0`, `v1.2.3`)
- Regular pushes to `main` or `develop` will NOT trigger publishing
- The first publish must be done after configuring the trusted publisher on PyPI
- After the first successful publish, subsequent releases will work automatically

## Troubleshooting

If you get an "invalid-publisher" error:
- Verify the trusted publisher configuration on PyPI matches exactly
- Make sure the repository owner, name, and workflow name are correct
- Check that you're pushing a tag (not just a branch)

For more information, see: https://docs.pypi.org/trusted-publishers/
