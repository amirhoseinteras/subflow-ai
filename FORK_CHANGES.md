# Community fork: changes and attribution

This repository is a **fork** of [sadraahkami/subflow-ai](https://github.com/sadraahkami/subflow-ai), originally developed by its upstream contributors. Their copyright and the original [MIT license](LICENSE) remain intact.

## Added here

- Turkish translations for all 50 desktop-interface messages, kept in `src/core/i18n_tr.py`.
- A three-language interface selector cycling Persian, English and Turkish. Persian remains right-to-left; Turkish and English are left-to-right.
- Five regression tests validating translation coverage, string-format placeholders and language selection.

## Important limits

The original project already supported Turkish **speech transcription** via Whisper; this fork adds **Turkish interface labels**, not a new model or a new transcription capability.

Five new unit tests passed locally on Windows with Python 3.12. The actual desktop interface and packaged executable have not yet been smoke-tested, and this fork does not offer a new signed Windows installer.

## Development and verification

From the repository root:

```bash
python -m unittest tests.test_i18n_tr -v
```

For full application setup, refer to the upstream README. If a new release is provided, verify its source and provenance before installing.

Contributions to the original project should go through the upstream repository. This fork is an independent derivative and is not endorsed by the original authors.
