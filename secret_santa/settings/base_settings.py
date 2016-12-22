"""
Django settings for secret_santa project.

Generated by 'django-admin startproject' using Django .

For more information on this file, see
https://docs.djangoproject.com/en/1.7//topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7//ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, '..'))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aok^0j=-vw6c-7=8$=s%%2eu07u4g-g2c7npev8a-d7et6vy_h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'registration',
    'bootstrap3',
    'debug_toolbar',

    'account',
    'social.apps.django_app.default',
    'djangobower',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'secret_santa.urls'


WSGI_APPLICATION = 'secret_santa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PROJECT_NAME = "secret_santa"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': (
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.core.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'account.context_processors.project_name',
            ),
        },
    },
]

AUTH_USER_MODEL = 'account.Account'
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = (os.path.join(BASE_DIR, 'staticfiles'))
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/accounts/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/accounts/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accounts/'

SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_FORCE_EMAIL_VALIDATION = True
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/accounts/email-sent/'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'apps.account.views.send_validation'

SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['last_name', 'first_name']

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'public_profile']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'email,last_name,first_name,name,id,link'}

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email', 'photo_100']
SOCIAL_AUTH_VK_OAUTH2_EXTRA_DATA = ['photo_100']

SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SCOPE = ['PHOTO_CONTENT']

SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'picture-url', 'public-profile-url']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                                          ('firstName', 'first_name'),
                                          ('lastName', 'last_name'),
                                          ('emailAddress', 'email_address'),
                                          ('pictureUrl', 'picture_url'),
                                          ('publicProfileUrl', 'public_profile_url')]

SOCIAL_AUTH_SLUGIFY_USERNAMES = True


AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'account.pipeline.require_email',
    'account.pipeline.check_for_raccoongang_email',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    # 'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'account.pipeline.save_profile_picture_and_profile_url',
    'social.pipeline.debug.debug',
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    'social.pipeline.disconnect.allowed_to_disconnect',
    'social.pipeline.disconnect.get_entries',
    'social.pipeline.disconnect.revoke_tokens',
    'social.pipeline.disconnect.disconnect',
    'account.pipeline.disconnect',
)

BOWER_INSTALLED_APPS = (
    'bootstrap#3.3.5',
    'bootstrap-switch#3.3.2',
    'https://github.com/malsup/form/archive/master.zip',
    'jquery.validate',
    'jquery#1.11.3',
    'eonasdan-bootstrap-datetimepicker#4.17.42',
    'moment#2.10.5',
    'select2#4.0.0',
    'bootstrap-social#5.1.1',
    # 'bootstrap-theme',
)

BOWER_COMPONENTS_ROOT = STATICFILES_DIRS[0]

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--cover-package=secret_santa',
    '--with-coverage',
]

try:
    from settings_local import *
except ImportError:
    pass
