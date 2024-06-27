AUTHOR = 'Morgan Plain'
SITENAME = 'OnzeKoog'
SITEURL = ""

PATH = "content"

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
    ('History', '/history.html'),
    ('Events (de Koog)', '/cultural-events-in-de-koog.html'),
    ('Events (Zaanstad)', '/cultural-events-in-zaanstad.html'),
    ('Redevelopments', '/redevelopment.html'),
    ('Green Resources', '/green-resources.html'),
    ('Playgrounds', '/playgrounds.html'),
    ('Swimming', '/swimming-areas.html'),
    ('Dog parks', '/dog-parks.html'),
    ('Noticeboards', '/noticeboards.html'),
]

# If you want to use pages generated from Markdown files, make sure you have the following settings:
#PAGE_PATHS = ['/pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Other settings...



# Blogroll
LINKS = (
    ("Zaanstad Council", "https://www.zaanstad.nl/"),
    ("Zaan Wiki", "https://www.zaanwiki.nl/"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

PLUGIN_PATHS = ['plugins', 'solar-plugins']
PLUGINS = ['addressable_paragraphs', 'assets', 'dither', 'neighbors', 'page_metadata', 'related_posts', 'representative_image']


DEFAULT_PAGINATION = False

# THEMES
#default:
THEME = "/Users/morganplain/Software/pelican/.venv/lib/python3.12/site-packages/pelican/themes/notmyidea"
#lowtechmagizine:
#THEME = "/Users/morganplain/Software/pelican/.venv/lib/python3.12/site-packages/pelican/themes/solar"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True