# -*- coding: utf-8 -*-
# (c) 2009-2011 Ruslan Popov <ruslan.popov@gmail.com>

from django.conf import settings
from django import template
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages.models import FlatPage

from shop import models, Cart

register = template.Library()

@register.inclusion_tag('shop/inclusion/categories_list.html')
def categories_list_tag():
    return {
        'categories': models.Category.objects.filter(parent__isnull=True, is_active=True)
    }

@register.inclusion_tag('shop/inclusion/categories_select.html')
def categories_select_tag():
    return {
        'categories': models.Category.objects.filter(parent__isnull=True, is_active=True)
    }

@register.inclusion_tag('shop/inclusion/producers.html')
def producers_tag():
    return {
        'manufacturers': models.Producer.objects.all(),
    }

@register.inclusion_tag('shop/inclusion/flatpage_list.html')
def flatpage_list_tag():
    return {
        'object_list': FlatPage.objects.all(),
    }

@register.inclusion_tag('shop/inclusion/cart.html', takes_context=True)
def cart_tag(context):
    return Cart().state(context['request'])

@register.inclusion_tag('shop/inclusion/item_list.html')
def recommendation_tag():
    limit = getattr(settings, 'SHOP_ITEMS_RECOMMENDED', 5)
    return {
        'widget_title': _(u'Good choice'),
        'product_list': models.Product.objects.filter(is_recommend=True, is_active=True)[:limit],
    }

@register.inclusion_tag('shop/inclusion/item_list.html')
def favorites_tag():
    limit = getattr(settings, 'SHOP_ITEMS_FAVORITES', 10)
    return {
        'widget_title': _(u'Favorites'),
        'product_list': models.Product.objects.filter(is_recommend=True, is_active=True)[:limit], # fixme
    }
