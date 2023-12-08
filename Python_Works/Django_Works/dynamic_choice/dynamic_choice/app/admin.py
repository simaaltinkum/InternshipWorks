from django.contrib import admin
from .models import Category, SubCategory, Saved
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource


class SubCategoryResource(resources.ModelResource):
    class Meta:
        model = SubCategory


class SubCategoryAdmin(ImportExportModelAdmin):
    resource_class = SubCategoryResource


class SavedResource(resources.ModelResource):
    class Meta:
        model = Saved


class SavedAdmin(ImportExportModelAdmin):
    resource_class = SavedResource


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Saved, SavedAdmin)
