"""
config.py — all the knobs in one place. Secrets come from env / Secret Manager,
never hard-coded here.
"""
import os

CONFIG = {
    "newsletter_name": "The Week in Seed",

    # Model + search budget for the research call.
    "model": "claude-opus-4-8",
    "max_searches": 12,

    # Voice. Leave blank for a clean newsletter voice, or paste your own style
    # guidance / the output of your `bogdan-voice` skill here to write as you.
    "voice_instruction": "",

    # Substack
    "substack_publication_url": os.environ.get("SUBSTACK_PUBLICATION_URL", "https://YOURNAME.substack.com"),
    "substack_cookies_path": os.environ.get("SUBSTACK_COOKIES_PATH"),  # preferred for headless
    "auto_publish": os.environ.get("AUTO_PUBLISH", "false").lower() == "true",  # keep false in phase 1

    # Output
    "output_dir": os.environ.get("OUTPUT_DIR", "./output"),

    # Rolling last-N-issues summary (committed to the repo) used for dedupe.
    "coverage_path": os.environ.get("COVERAGE_PATH", "coverage.json"),
}
