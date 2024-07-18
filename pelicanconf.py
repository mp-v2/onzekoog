AUTHOR = 'Morgan Plain'
SITENAME = 'OnzeKoog'
SITEURL = ""

PATH = "content"
#STATIC_PATHS = ['images']

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Disable automatic page menu generation
DISPLAY_PAGES_ON_MENU = False

# Choose which pages go into the menu
MENUITEMS = [
    ('Home', '/'),
    ('Video Tour', '/video-tour.html'),
    ('History', '/history.html'),
    ('Events (de Koog)', '/cultural-events-in-de-koog.html'),
    ('Events (Zaanstad)', '/cultural-events-in-zaanstad.html'),
    ('Redevelopments', '/redevelopment.html'),
    ('Green Resources', '/green-resources.html'),
    ('Playgrounds', '/playgrounds.html'),
    ('Swimming', '/swimming-areas.html'),
    ('Dog parks', '/dog-parks.html'),
    ('News', '/local-news.html'),
    ('Local Organisations', '/local-organisations.html'),
    ('Noticeboards', '/noticeboards.html'),
]

# If you want to use pages generated from Markdown files, make sure you have the following settings:
#PAGE_PATHS = ['/pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'


PLUGIN_PATHS = ['plugins', 'solar-plugins']
PLUGINS = [
    'addressable_paragraphs', 'assets', 'neighbors', 'page_metadata', 'related_posts', 'representative_image',
    'seo', 
    #'deadlinks'
    ]

# SEO plugin
# https://github.com/pelican-plugins/seo
SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = False  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = False # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False # Subfeature of SEO enhancer

SEO_ARTICLES_LIMIT = 10
SEO_PAGES_LIMIT = 20

#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
#SITEMAP_SAVE_AS = 'sitemap.xml'

# Deadlink checker plugin
# https://github.com/pelican-plugins/deadlinks
DEADLINK_VALIDATION = True

DEADLINK_OPTS = {
    'archive':  False,
    'classes': ['custom-class1', 'disabled'],
    'labels':   True,
    'timeout_duration_ms': 1000,
    'timeout_is_error':    False,
}



# Other settings...



# Blogroll
LINKS = (
    ("Zaanstad Municipality", "https://www.zaanstad.nl/"),
    ("Zaan Wiki", "https://www.zaanwiki.nl/"),
)

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )


DEFAULT_PAGINATION = False

# THEMES
#default:
THEME = "/Users/morganplain/Software/pelican/.venv/lib/python3.12/site-packages/pelican/themes/notmyidea"
#THEME = "/Users/morganplain/Software/pelican/.venv/lib/python3.12/site-packages/pelican/themes/notmyidea2"
#lowtechmagizine:
#THEME = "/Users/morganplain/Software/pelican/.venv/lib/python3.12/site-packages/pelican/themes/solar"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True