import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = os.getenv("SECRET_KEY", default=os.urandom(32))

DEBUG = int(os.getenv("DEBUG", default=1))

ADMIN_ENABLED = int(os.getenv("ADMIN_ENABLED", default=1))

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="127.0.0.1,0.0.0.0").split(",")

# Generic Settings

APPEND_SLASH = True

HTML_MINIFY = True

OTP_TOTP_ISSUER = "Ceiphr"

# Content Security Policy

CSP_IMG_SRC = (
    "'self'",
    "https://*.ceiphr.com",
    "https://*.ceiphr.io",
    "https://*.buysellads.net",
    "https://ad.doubleclick.net",
    "https://scontent.cdninstagram.com",
    "https://disqus.com",
    "https://*.disqus.com",
    "https://*.disquscdn.com",
)

CSP_STYLE_SRC = (
    "'self' 'unsafe-inline'",
    "https://*.cloudflare.com",
    "https://*.carbonads.com",
    "https://*.disquscdn.com",
)

CSP_SCRIPT_SRC = (
    "'self' 'unsafe-eval' 'unsafe-inline'",
    "https://*.ceiphr.com",
    "https://*.carbonads.com",
    "https://*.carbonads.net",
    "https://*.cloudflare.com",
    "https://disqus.com",
    "https://*.disquscdn.com",
    "https://ceiphr.disqus.com",
)

CSP_FONT_SRC = ("'self' data:", "https://*.cloudflare.com")

CSP_FRAME_SRC = ("'self'", "https://disqus.com",)

CSP_CONNECT_SRC = ("'self'", "https://disqus.com",)

CSP_OBJECT_SRC = ("'none'",)

CSP_BASE_URI = ("'none'",)

CSP_WORKER_SRC = ("'self'",)

CSP_FORM_ACTION = "'self'"

CSP_DEFAULT_SRC = ("'self'", "https://disqus.com", "https://*.disquscdn.com",)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "sorl.thumbnail",
    "pipeline",
    "portfolio",
    "blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "csp.middleware.CSPMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.PipelineFinder",
)

ROOT_URLCONF = "ceiphr.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "ceiphr.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "assets"),)

# Pipeline - process and compress assets for optimized use

STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"

PIPELINE = {
    # Convert stylesheet assets into post-processed static content
    "STYLESHEETS": {
        "feed-mobile": {
            "source_filenames": ("sass/feed-mobile.scss",),
            "output_filename": "css/feed-mobile.css",
            "extra_context": {"media": "screen and (max-width: 769px)"},
        },
        "feed-desktop": {
            "source_filenames": ("sass/feed-desktop.scss",),
            "output_filename": "css/feed-desktop.css",
            "extra_context": {"media": "screen and (min-width: 769px)"},
        },
        "article-mobile": {
            "source_filenames": ("sass/article-mobile.scss", "sass/highlight.scss"),
            "output_filename": "css/article-mobile.css",
            "extra_context": {"media": "screen and (max-width: 1024px)"},
        },
        "article-desktop": {
            "source_filenames": ("sass/article-desktop.scss", "sass/highlight.scss"),
            "output_filename": "css/article-desktop.css",
            "extra_context": {"media": "screen and (min-width: 1024px)"},
        },
    },
    # Compress javascript assets
    "JAVASCRIPT": {
        "onload": {
            "source_filenames": (
                "node_modules/lazysizes/lazysizes.js",
                "node_modules/lazysizes/plugins/blur-up/ls.blur-up.js",
                "js/nav.js",
            ),
            "output_filename": "js/onload.js",
            "extra_context": {"defer": True},
        },
    },
}

PIPELINE["CSS_COMPRESSOR"] = "pipeline.compressors.yuglify.YuglifyCompressor"

# Sass compiler for converting scss files to post-processed css

PIPELINE["COMPILERS"] = ("pipeline.compilers.sass.SASSCompiler",)

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"
