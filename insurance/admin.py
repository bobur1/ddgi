from django.contrib import admin
from insurance.models import *
from django.contrib.auth.admin import UserAdmin


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class UserRoleInline(admin.TabularInline):
    model = UserRole
    verbose_name_plural = 'Roles'
    fk_name = 'user'
    extra = 0


class PermissionUserInline(admin.TabularInline):
    model = PermissionUser
    verbose_name_plural = 'Permissions'
    fk_name = 'user'
    extra = 0


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, UserRoleInline, PermissionUserInline)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code_name', 'title')
    readonly_fields = ('cr_by', 'cr_on', 'up_by', 'up_on')

    def save_model(self, request, obj, form, change):
        if change:
            obj.up_by = request.user
        else:
            obj.cr_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(OfficeWorkers)
class OfficeWorkersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'office')
    readonly_fields = ('cr_by', 'cr_on', 'up_by', 'up_on')


class PermissionRoleInline(admin.TabularInline):
    model = PermissionRole
    fk_name = 'role'
    verbose_name_plural = 'ROLE PERMISSIONS'
    verbose_name = 'PERMISSION'
    extra = 0


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    inlines = (PermissionRoleInline,)


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')

    # readonly_fields = ('cr_by', 'cr_on')

    def save_model(self, request, obj, form, change):
        if change:
            obj.cr_by = request.user
        else:
            obj.cr_by = request.user
        permissions = PermissionRole.objects.filter(role=obj.role)
        for p in permissions:
            PermissionUser.objects.create(permission=p.permission,
                                          user=obj.user,
                                          grant=p.grant,
                                          cr_by=request.user)
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        permission_ids = PermissionRole.objects.filter(role=obj.role).values_list('permission_id')
        PermissionUser.objects.filter(user=obj.user, permission__in=permission_ids).delete()
        obj.delete()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            permission_ids = PermissionRole.objects.filter(role=obj.role).values_list('permission_id')
            PermissionUser.objects.filter(user=obj.user, permission__in=permission_ids).delete()
            obj.delete()


@admin.register(PermissionRole)
class PermissionRoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')

    def save_model(self, request, obj, form, change):
        if change:
            obj.cr_by = request.user
        else:
            obj.cr_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(PermissionUser)
class PermissionUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission', 'grant')

    def save_model(self, request, obj, form, change):
        if change:
            obj.cr_by = request.user
        else:
            obj.cr_by = request.user
        super().save_model(request, obj, form, change)


class GridColsInline(admin.TabularInline):
    model = GridCols
    extra = 0
    fields = ('order_num', 'title', 'data', 'name', 'type', 'className', 'defaultContent',
              'width', 'searchable', 'orderable', 'visible')


@admin.register(Dt_Option)
class GridAdmin(admin.ModelAdmin):
    list_display = ('codeName', 'title')
    inlines = [GridColsInline]


@admin.register(IndividualClient)
class IndividualClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    pass


@admin.register(InsuranceOffice)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'series', 'name')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(LegalClient)
class LegalClientAdmin(admin.ModelAdmin):
    pass


# class SimpleFieldInline(admin.TabularInline):
#     model = SimpleField
#     extra = 0
#     fields = ('name', 'input_type', 'value')


class ProductFieldInline(admin.TabularInline):
    model = ProductField
    extra = 0
    fields = ('field_class', 'input_type', 'is_required', 'name', 'extra_fields', 'value', 'order')


admin.site.register(ProductFieldClass)
admin.site.register(SimpleField)
admin.site.register(VehicleApplicationFormAdditional)
admin.site.register(VehicleApplicationFormHazard)


class ApplicationFieldInline(admin.TabularInline):
    model = ProductApplicationField
    extra = 0
    fields = ('field_class', 'input_type', 'is_required', 'name', 'extra_fields', 'value', 'order')


class VehicleApplicationFormItemInline(admin.TabularInline):
    model = VehicleApplicationItemForm
    extra = 0
    fields = ('model_name', 'release_date', 'state_number', 'passport_tech_number', 'engine_number', 'body_number',
              'lifting_capacity', 'seat_number', 'price', 'awarded_price', 'additional', 'hazards')


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    model = ApplicationForm
    list_display = ('product_type', 'from_time', 'to_time', 'contract_type')
    inlines = [ApplicationFieldInline, VehicleApplicationFormItemInline]


@admin.register(ProductType)
class ProductAdmin(admin.ModelAdmin):
    model = ProductType
    code = model.code
    list_display = ('id', 'name', 'code')
    inlines = [ProductFieldInline]


@admin.register(PoliciesIncome)
class PoliciesIncomeAdmin(admin.ModelAdmin):
    list_display = ['act_number', 'act_date', 'policy_number_from', 'policy_number_to']


@admin.register(PolicySeriesType)
class PolicySeriesType(admin.ModelAdmin):
    list_display = ['code', 'cr_by']


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', str, 'is_free_generated', 'is_active')


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = (str, 'individual', 'legal')


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')


@admin.register(PolicyTransfers)
class PolicyTransfersAdmin(admin.ModelAdmin):
    list_display = ('id', 'to_office', 'cr_by', 'cr_on')


@admin.register(PolicyRetransfer)
class PolicyRetransferAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'transfer', 'to_user', 'cr_on', 'cr_by'
    )


@admin.register(OfficeType)
class OfficeTypeAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'description'
    )


@admin.register(Location)
class RegionAdmin(admin.ModelAdmin):
    list_display = (str,)


@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = (str,)


@admin.register(ClientRequest)
class ClientRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductTypeCode)
class ProductTypeCodeAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'description', 'is_exist'
    )
