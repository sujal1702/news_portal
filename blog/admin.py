from django.contrib import admin
from .models import Post, Category
from .models import Ad

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'category', 'date_posted')  # ✅ now valid
    list_filter = ('category', 'date_posted')  # ✅ works if author is ForeignKey

    search_fields = ('title', 'content', 'author__username')
    ordering = ('-date_posted',)


admin.site.register(Category)

# 👇 Customize Admin Panel Header and Titles
admin.site.site_header = "News Portal Admin Panel"
admin.site.site_title = "News Portal Admin"
admin.site.index_title = "Welcome to the News Portal Admin Panel"
from .models import Feedback
admin.site.register(Feedback)
admin.site.register(Ad)
from .models import Subscriber

admin.site.register(Subscriber)
from django.contrib import admin
from .models import Enquiry

admin.site.register(Enquiry)



