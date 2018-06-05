from rest_framework.routers import DefaultRouter
from words.views import TextbookViewSet, NoteViewSet, WordViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

textbooks_router = router.register('textbooks', TextbookViewSet)
textbooks_router.register(
    'notes', NoteViewSet,
    base_name='textbook-note',
    parents_query_lookups=['textbook']) \
    #     .register(
#     'words', WordViewSet,
#     base_name='textbook-note-word',
#     parents_query_lookups=['textbook__note', 'word']
# )

# router.register('authors', AuthorViewSet)
notes_router = router.register('notes', NoteViewSet)
notes_router.register(
    'words', WordViewSet,
    base_name='note-word',
    parents_query_lookups=['note']
    # base_name='textbook-note-word',
    # parents_query_lookups=['textbook__note', 'word']
)
router.register('words', WordViewSet)
