from django.contrib import admin
from .models import CompanyInfo, Service, FleetCategory, FleetVehicle

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'updated_at')
    
    # Prevenir que se creen multiples instancias de CompanyInfo si se desea (Singleton)
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon_name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('is_active',)

@admin.register(FleetCategory)
class FleetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)

@admin.register(FleetVehicle)
class FleetVehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'capacity', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'features')
