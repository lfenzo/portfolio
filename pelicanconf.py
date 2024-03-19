AUTHOR = 'Enzo L. Fernandes'
SITENAME = 'Portfolio'
SITEURL = ""

PATH = "content"
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["articles"]
ARTICLE_PATHS = ["articles"]

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "pelican-themes/elegant"

AUTHORS = {
    "Enzo L. Fernandes": {},
}

SITESUBTITLE = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAo"

LANDING_PAGE_TITLE = "Aloha"

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "extract_toc",
    "neighbors",
    "similar_posts",
]
SIMILAR_POSTS_MIN_SCORE = 0.01

READING_TIME_LOWER_LIMIT = 1

PROJECTS_TITLE = "Featured Projects"
PROJECTS = [
    {
        'name': 'Multi-ensemble based approach for Short-term Solar Radiation Forecasting',
        'url': '',
        'description': ''
    },
    {
        'name': 'Impostor.jl',
        'url': '',
        'description': 'A highly versatile synthetic data generator.'
    },
    {
        'name': 'Neovim Fusion',
        'url': '',
        'description': 'The Radioactive Neovim Dark Colorscheme'
    },
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
