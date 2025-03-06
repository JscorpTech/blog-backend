from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Contact"),
                "icon": "contacts",
                "link": reverse_lazy("admin:api_contactmodel_changelist"),
            },
            {
                "title": _("Users"),
                "icon": "group",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
            {
                "title": _("Group"),
                "icon": "group",
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
    {
        "title": _("Portfolio"),
        "separator": True,
        "items": [
            {
                "title": _("Project"),
                "icon": "bookmarks",
                "link": reverse_lazy("admin:api_projectmodel_changelist"),
            },
            {
                "title": _("Education"),
                "icon": "school",
                "link": reverse_lazy("admin:api_educationmodel_changelist"),
            },
            {
                "title": _("Experience"),
                "icon": "science",
                "link": reverse_lazy("admin:api_experiencemodel_changelist"),
            }
        ]
    },
    {
        "title": _("Stack"),
        "separator": True,
        "items": [
            {
                "title": _("Stacks"),
                "icon": "stacks",
                "link": reverse_lazy("admin:api_stackmodel_changelist"),
            },
            {
                "title": _("Stack Categories"),
                "icon": "category",
                "link": reverse_lazy("admin:api_categorymodel_changelist"),
            }
        ]
    },
    {
        "title": _("Blog"),
        "separator": True,
        "items": [
            {
                "title": _("Post"),
                "icon": "post",
                "link": reverse_lazy("admin:api_postmodel_changelist"),
            },
            {
                "title": _("Tag"),
                "icon": "tag",
                "link": reverse_lazy("admin:api_tagmodel_changelist"),
            },
            {
                "title": _("Category"),
                "icon": "category_search",
                "link": reverse_lazy("admin:api_categorymodel_changelist"),
            },
        ]
    },
    {
        "title": _("Faq"),
        "separator": True,
        "items": [
            {
                "title": _("Faq"),
                "icon": "quiz",
                "link": reverse_lazy("admin:api_faqmodel_changelist"),
            },
            {
                "title": _("Faq Category"),
                "icon": "inbox",
                "link": reverse_lazy("admin:api_faqcategorymodel_changelist"),
            }
        ]
    }
]
