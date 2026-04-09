from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, ChaiCertifcate

# Inline reviews
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

# ChaiVarity admin
class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

# Store admin
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)

# Certificate admin
class ChaiCertifcateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'date_issued', 'valid_until')

# Register models
admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(ChaiReview)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertifcate, ChaiCertifcateAdmin)