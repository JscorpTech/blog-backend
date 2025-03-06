from . import navigation
from django.templatetags.static import static

UNFOLD = {
    "DASHBOARD_CALLBACK": "django_core.views.dashboard_callback",
    "SITE_TITLE": None,
    "SHOW_LANGUAGES": True,
    "SITE_HEADER": None,
    "SITE_URL": "/",
    "STYLES": [
        lambda request: static("css/tailwind.css"),
    ],

    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,
    "BORDER_RADIUS": "10px",
    "COLORS": {
        "base": {
            "50": "250 250 250",
            "100": "244 244 245",
            "200": "228 228 231",
            "300": "212 212 216",
            "400": "161 161 170",
            "500": "113 113 122",
            "600": "82 82 91",
            "700": "63 63 70",
            "800": "39 39 42",
            "900": "24 24 27",
            "950": "9 9 11",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
        "primary": {
            "50": "230 245 255",
            "100": "180 225 255",
            "200": "130 205 255",
            "300": "80 185 255",
            "400": "40 165 255",
            "500": "0 145 255",
            "600": "0 115 204",
            "700": "0 85 153",
            "800": "0 55 102",
            "900": "0 30 51",
            "950": "0 15 25",
        },

    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "uz": "🇺🇿",
                "ru": "🇷🇺",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,
        "navigation": navigation.PAGES,  # Pagelarni qo'lda qo'shish
    },
}
