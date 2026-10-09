"""Regression tests for Turkish localization in the community fork."""

import string
import unittest

from src.core.i18n import (
    TRANSLATIONS,
    get_current_language,
    set_current_language,
    tr,
)
from src.core.i18n_tr import TR_TRANSLATIONS


def placeholders(message):
    return {field.split(".")[0].split("[")[0] for _, field, _, _ in string.Formatter().parse(message) if field}


class TurkishTranslationTests(unittest.TestCase):
    def test_all_ui_keys_have_turkish_translation(self):
        self.assertEqual(set(TRANSLATIONS), set(TR_TRANSLATIONS))
        for key in TRANSLATIONS:
            with self.subTest(key=key):
                self.assertIsInstance(TR_TRANSLATIONS[key], str)
                self.assertTrue(TR_TRANSLATIONS[key].strip())

    def test_format_placeholders_match_english(self):
        for key, variants in TRANSLATIONS.items():
            with self.subTest(key=key):
                self.assertEqual(
                    placeholders(variants["en"]),
                    placeholders(variants["tr"]),
                )

    def test_switch_and_restore_language(self):
        original = get_current_language()
        try:
            set_current_language("tr")
            self.assertEqual(get_current_language(), "tr")
            self.assertEqual(tr("lang_tr"), "Türkçe")
            self.assertEqual(
                tr("files_selected_count", count=3, size="5 MB"),
                "3 dosya seçildi (5 MB)",
            )
            set_current_language("unsupported")
            self.assertEqual(get_current_language(), "tr")
        finally:
            set_current_language(original)

    def test_turkish_status_placeholders(self):
        actual = tr(
            "transcribing_progress",
            lang="tr",
            current=1,
            total=2,
            percent=50,
            name="audio.mp3",
        )
        self.assertIn("1/2", actual)
        self.assertIn("50%", actual)
        self.assertIn("audio.mp3", actual)

    def test_explicit_language_does_not_change_global_setting(self):
        original = get_current_language()
        self.assertEqual(tr("ready", lang="tr"), "Hazır")
        self.assertEqual(get_current_language(), original)


if __name__ == "__main__":
    unittest.main()
