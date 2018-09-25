from django.contrib import admin
from cmdb.models import Test,Contact,Tag

# 将models中的模型在这里注册
# admin.site.register([Test,Contact,Tag])

# 自定义管理页面，来取代默认的页面 比如上面的"add"页面.
# class ContactAdmin(admin.ModelAdmin):
    # fields 属性定义了要显示的字段 我们想只显示name和email部分(不显示age)
    # fields = ('name','email')
# 由于该类对应的是 Contact 数据模型，我们在注册的时候，需要将它们一起注册

class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
admin.site.register(Contact,ContactAdmin)
admin.site.register([Test, Tag])