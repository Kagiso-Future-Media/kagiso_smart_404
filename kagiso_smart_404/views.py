from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect

from .utils import suggest_page_from_misspelled_slug, get_instant_redirect


def not_found(request):  # pragma: no cover
    slug = request.path
    root_page = request.site.root_page.specific
    print(request)

    page_redirect = get_instant_redirect(slug, root_page)
    if page_redirect:
        return HttpResponsePermanentRedirect(redirect_to=page_redirect.url)

    suggested_pages = suggest_page_from_misspelled_slug(slug, root_page)

    data = {'suggested_pages': suggested_pages}
    return render(request, '404.html', data, status=404)
