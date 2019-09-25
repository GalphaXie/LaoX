### django 静态文件
#### 2.静态文件开发环境配置
>   项目中的CSS、图片、js都是静态文件。一般会将静态文件放到一个单独的目录中，以方便管理。在html页面中调用时，也需要指定静态文件的路径，Django中提供了一种解析的方式配置静态文件路径。静态文件可以放在项目根目录下，也可以放在应用的目录下，由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下，方便管理。
为了提供静态文件，需要配置两个参数：
- 先创建目录: static_files
- 在setting.py文件中配置:
    - STATICFILES_DIRS 存放查找静态文件的目录
    - STATIC_URL 访问静态文件的URL前缀

- 示例:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files'),
]
```
- 说明: 此时在static_files添加的任何静态文件都可以使用网址 /static/文件在static_files中的路径 来访问了
- 注意:
    - Django 仅在调试模式下（DEBUG=True）能对外提供静态文件。
    - 当DEBUG=False工作在生产模式时，Django不再对外提供静态文件，需要是用collectstatic命令来收集静态文件并交由其他静态文件服务器来提供。
#### 2.静态文件生产环境部署
> 静态文件除了我们业务之外，django本身还有自己的静态文件，如果rest_framework、admin等。我们需要收集这些静态文件，集中一起放到静态文件服务器中。
- 先创建目录 static
- 在setting.py文件中配置:
    - `STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end/static')`
- 执行收集命令: `python manage.py collectstatic`
- 生产环境静态文件服务器配置(这里采用nginx)
    - 1.打开配置文件,一般是 `sudo vim /usr/local/nginx/conf/nginx.conf`
    - 2.```server {
                 listen       80;
                 server_name  www.meiduo.site;
                 location / {
                     root   /home/python/Desktop/front_end_pc;
                     index  index.html index.htm;
                 }
        // 余下省略}```
    - 3.重启 nginx: `sudo /usr/local/nginx/sbin/nginx -s reload`

## django 自带文件管理系统
### 1.一些特点:
1.默认情况下，Django会将上传的图片保存在本地服务器上，需要配置保存的路径。
2.一般项目本身和业务结合较多的文件, 会配置一个 `MEDIA_ROOT`参数结合 BASE_DIR 来形成一个完整的路径,单独放置在 static 文件目录下;
3.django 会在global_settins中, 默认: MEDIA_ROOT = '' 
4.常见在 ImageField 字段中 `upload_to` 相关联
### 2.自定义django的文件存储系统(类)
- 1.继承: django.core.files.storage.Storage
- 2.Storage 继承 object类, 而且没有 `__init__.py`, 所以实例化的时候不需要参数,也就是说任何配置都应该从django.conf.settings中获取
```python
from django.conf import settings
from django.core.files.storage import Storage

class MyStorage(Storage):
    def __init__(self, base_url=None, client_conf=None):
        if base_url is None:
            base_url = settings.File_SERVER_URL
        self.base_url = base_url
        if client_conf is None:
            client_conf = settings.File_CLIENT_CONF
        self.client_conf = client_conf
```
- 3.存储类中必须实现_open()和_save()方法，以及任何后续使用中可能用到的其他方法。
> _open(name, mode='rb')
被Storage.open()调用，在打开文件时被使用。
_save(name, content)
被Storage.save()调用，name是传入的文件名，content是Django接收到的文件内容，该方法需要将content文件内容保存。
Django会将该方法的返回值保存到数据库中对应的文件字段，也就是说该方法应该返回要保存在数据库中的文件名称信息。
exists(name)
如果名为name的文件在文件系统中存在，则返回True，否则返回False。
url(name)
返回文件的完整访问URL
delete(name)
删除name的文件
listdir(path)
列出指定路径的内容
size(name)
返回name文件的总大小
注意，并不是这些方法全部都要实现，可以省略用不到的方法。

- 4.需要为存储类添加django.utils.deconstruct.deconstructible装饰器

### 3.配置 自定义的文件存储类
- 1.django 默认在global_settings中配置了: `DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'`
- 2.我们这里需要 自己配置 DEFAULT_FILE_STORAGE
- 3.如果是保存到服务器,我们可能还需要配置一些 url port path 等文件存储服务器信息.

### 4.其他静态文件服务器:
- FastDFS
- OSS



