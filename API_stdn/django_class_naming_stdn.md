# django 类 命名规范

## 1.模型类
- XxModel(Models.Model)
- 表名命名‘tb_app名小写_Xx’
## 2.序列化器类
- XxSerializer(serializer.Serializer) 或 XxModelSerializer(serializer.ModelSerializer) 或 XxAbstractSerializer
## 3.视图类
- XxView(View)
- XxAPIView(APIView)
- XxAPIView(Mixin, GenericAPIView)
- XxViewSet(Mixin, APIView)
- XxModelViewSet(Mixin, GenericAPIView)
- 补充： 要写好类的注释， 和 视图方法的注释
## 4.URL
- 导包： from app import views ， 不要直接导入视图类
- 推荐使用 项目路由 和 app路由 分开的方式
- 写好每个URL的注释，
- 符合：rest API规范， 清楚版本，调用的端，新增的时间

## 5.