from pathlib import Path
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'django.contrib.auth',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'SOLIDIFY.common.apps.CommonConfig',
    'SOLIDIFY.categories.apps.CategoriesConfig',
    'SOLIDIFY.habits.apps.HabitsConfig',
    'SOLIDIFY.routines.apps.RoutinesConfig',
    'SOLIDIFY.accounts.apps.AccountsConfig',
    'SOLIDIFY.schedule.apps.ScheduleConfig',
    'rest_framework',
    "widget_tweaks",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SOLIDIFY.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

JAZZMIN_SETTINGS = {
    "site_title": "SOLIDIFY Admin",
    "site_header": "SOLIDIFY Admin Panel",
    "site_brand": "SOLIDIFY",
    "welcome_sign": "Welcome to SOLIDIFY Admin",
    "copyright": "SOLIDIFY",
    "search_model": ["accounts.AppUser", "routines.Routine"],
    "show_sidebar": True,
    "navigation_expanded": True,
    "site_icon": "images/favicon.ico",
    "site_logo": "images/favicon.ico",
    "show_ui_builder": True,
    "icons": {
        "auth.Group": "fas fa-users-cog",
        "accounts.AppUser": "fas fa-user",
        "routines.Routine": "fas fa-tasks",
        "schedule.ScheduledRoutine": "fas fa-calendar-alt",
    },
    "custom_links": {
        "accounts.AppUser": [{
            "name": "View in App",
            "url": "https://yourapp.com/profile/",
            "icon": "fas fa-external-link-alt",
            "permissions": ["accounts.view_appuser"]
        }]
    },
    "hide_models": ["auth.Permission"],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-gray",
    "accent": "accent-primary",
    "navbar": "navbar-navy navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "sandstone",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

WSGI_APPLICATION = 'SOLIDIFY.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.AppUser'
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('login')
