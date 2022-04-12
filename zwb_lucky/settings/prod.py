import os
from .dev import *

DEBUG = False
ALLOWED_HOSTS = [os.getenv("ALLOWED_HOSTS")]

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_NAME'),  # 数据库名，先前创建的
        'USER': os.getenv('MYSQL_USER'),     # 用户名，可以自己创建用户
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),  # 密码
        'HOST': os.getenv('MYSQL_HOST'),  # mysql服务所在的主机ip
        'PORT': os.getenv('MYSQL_PORT'),         # mysql服务端口
    }
}

# 下面就是logging的配置
LOGGING = {
    'version': 1,  # 指明dictConnfig的版本，目前就只有一个版本，哈哈
    'disable_existing_loggers': False,  # 表示是否禁用所有的已经存在的日志配置
    'formatters': {  # 格式器
        'verbose': {  # 详细
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'standard': {  # 标准
            'format': '[%(asctime)s] [%(levelname)s] %(message)s'
        },
    },
    # handlers：用来定义具体处理日志的方式，可以定义多种，"default"就是默认方式，"console"就是打印到控制台方式。file是写入到文件的方式，注意使用的class不同
    'handlers': {  # 处理器，在这里定义了两个个处理器
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            # 文件重定向的配置，将打印到控制台的信息都重定向出去 python manage.py runserver >> /home/aea/log/test.log
            # 'stream': open('/home/aea/log/test.log','a'),  #虽然成功了，但是并没有将所有内容全部写入文件，目前还不清楚为什么
            'formatter': 'standard'  # 制定输出的格式，注意 在上面的formatters配置里面选择一个，否则会报错
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/webroot/logs/zwb_lucky.log',  # 这是将普通日志写入到日志文件中的方法，
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/webroot/logs/default.log',  # 日志输出文件
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份份数
            'formatter': 'standard',  # 使用哪种formatters日志格式
        },
        # 上面两种写入日志的方法是有区别的，前者是将控制台下输出的内容全部写入到文件中，这样做的好处就是我们在views代码中的所有print也会写在对应的位置
        # 第二种方法就是将系统内定的内容写入到文件，具体就是请求的地址、错误信息等，小伙伴也可以都使用一下然后查看两个文件的异同。
    },
    'loggers': {  # log记录器，配置之后就会对应的输出日志
        # django 表示就是django本身默认的控制台输出，就是原本在控制台里面输出的内容，在这里的handlers里的file表示写入到上面配置的file-/home/aea/log/jwt_test.log文件里面
        # 在这里的handlers里的console表示写入到上面配置的console-/home/aea/log/test.log文件里面
        'django': {
            'handlers': ['console', 'file'],
            # 这里直接输出到控制台只是请求的路由等系统console，当使用重定向之后会把所有内容输出到log日志
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request ': {
            'handlers': ['console', 'file'],
            'level': 'WARNING',  # 配合上面的将警告log写入到另外一个文件
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['file'],  # 指定file handler处理器，表示只写入到文件
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

STATIC_ROOT = os.getenv('STATIC_ROOT', '/webroot/static')

if os.getenv('CSRF_TRUSTED_ORIGINS') is not None:
    CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS').split(',')

