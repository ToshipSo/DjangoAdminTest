from django.contrib import admin
from .models import SettlementSummary
from django.utils.html import format_html
from django.contrib.auth.models import Group, User


# Register your models here.
class SettlementSummaryAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'view_records_link', 'total_num_transactions', 'settlement_id', 'report_id', 'total_amount',
        'start_date', 'end_date', 'deposit_date')
    # list_display_links = ('transaction_id',)
    list_filter = ('user_id', 'settlement_id')

    def get_queryset(self, request):
        query_set = super(SettlementSummaryAdmin, self).get_queryset(request)
        return query_set.filter(user_id=request.user.id)

    def view_records_link(self, obj):
        url = u'../transaction/?user_id=%d&settlement_id=%s' % (obj.user_id, obj.settlement_id)
        return format_html("<a href='{url}'>View Records</a>", url=url)


admin.site.register(SettlementSummary, SettlementSummaryAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
