"""
Django settings for FuGuang project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4zrh=q(t4kz-8lel-#0$ezalvn23lo4dmv(=#7mh%wjj6v(+(k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'rest_framework',
    'multiselectfield',
    'notifications',
    'square',
    'user',
    'channels',
    'message',
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

ROOT_URLCONF = 'fuguang.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fuguang.wsgi.application'

ASGI_APPLICATION = 'fuguang.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)]
        }
    }
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'port': 3306,
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'fuguang',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 指定自定义用户模型
AUTH_USER_MODEL = 'user.user'

#  DRF 的配置
REST_FRAMEWORK = {
    # 配置登录鉴权方式
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT配置
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),  # Access Token的有效期
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),  # Refresh Token的有效期
    # 'CHECK_REVOKE_TOKEN': False,
    # 对于大部分情况，设置以上两项就可以了，以下为默认配置项目，可根据需要进行调整

    # # 是否自动刷新Refresh Token
    # 'ROTATE_REFRESH_TOKENS': False,
    # #刷新Refresh Token时是否将旧Token加入黑名单，如果设置为False，则旧的刷新令牌仍然可以用于获取新的访问令牌。需要将'rest_framework_simplejwt.token_blacklist'加入到'INSTALLED_APPS'的配置中
    # 'BLACKLIST_AFTER_ROTATION': False,
    # 'ALGORITHM': 'HS256',  # 加密算法
    # 'SIGNING_KEY': SECRET_KEY,  # 签名密匙，这里使用Django的SECRET_KEY
    # # 如为True，则在每次使用访问令牌进行身份验证时，更新用户最后登录时间
    # "UPDATE_LAST_LOGIN": False,
    # # 用于验证JWT签名的密钥返回的内容。可以是字符串形式的密钥，也可以是一个字典。
    # "VERIFYING_KEY": "",
    # "AUDIENCE": None,  # JWT中的"Audience"声明,用于指定该JWT的预期接收者。
    # "ISSUER": None,  # JWT中的"Issuer"声明，用于指定该JWT的发行者。
    # "JSON_ENCODER": None,  # 用于序列化JWT负载的JSON编码器。默认为Django的JSON编码器。
    # "JWK_URL": None,  # 包含公钥的URL，用于验证JWT签名。
    # "LEEWAY": 0,  # 允许的时钟偏差量，以秒为单位。用于在验证JWT的过期时间和生效时间时考虑时钟偏差。
    #
    # # 用于指定JWT在HTTP请求头中使用的身份验证方案。默认为"Bearer"
    # "AUTH_HEADER_TYPES": ("Bearer",),
    # # 包含JWT的HTTP请求头的名称。默认为"HTTP_AUTHORIZATION"
    # "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # # 用户模型中用作用户ID的字段。默认为"id"。
    # "USER_ID_FIELD": "id",
    # # JWT负载中包含用户ID的声明。默认为"user_id"。
    # "USER_ID_CLAIM": "user_id",

}

# 后端配置
# AUTHENTICATION_BACKENDS = (
#     # 'django.contrib.auth.backends.ModelBackend',
#     # 'user.wechat_auth.MyJWTAuthentication',
#     # 'rest_framework_simplejwt.authentication.JWTAuthentication',
#     # 'user.backend.MyCustomBackend',
# )

# 文件上传的保存路径
MEDIA_ROOT = BASE_DIR / 'file/image'
MEDIA_URL = 'file/image/'