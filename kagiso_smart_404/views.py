from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render

from .utils import get_instant_redirect, suggest_page_from_misspelled_slug


def not_found(request):  # pragma: no cover
    slug = request.path
    root_page = request.site.root_page.specific

    page_redirect = get_instant_redirect(slug, root_page)
    if page_redirect:
        return HttpResponsePermanentRedirect(redirect_to=page_redirect.url)

    suggested_pages = suggest_page_from_misspelled_slug(slug, root_page)

    data = {'suggested_pages': suggested_pages}
    return render(request, '404.html', data, status=404)
