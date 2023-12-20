from django.urls import path

from app18.views import StartPage, BookList, AuthorList, BookCreate, BookDetail, AuthorDetail, BookUpdate,AuthorUpdate, AuthorDelete, BookDelete, AuthorCreate

urlpatterns = [
    path('', StartPage.as_view(), name='start'),
    path('book-list/', BookList.as_view(),name='book_list'),
    path('author-list/', AuthorList.as_view(), name='author_list'),

    path('create-book/', BookCreate.as_view(), name='book_create'),
    path('create-author/', AuthorCreate.as_view(), name='author_create'),

    path('detail-book/<slug:slug>', BookDetail.as_view(), name='book_detail'),
    path('detail-author/<slug:slug>', AuthorDetail.as_view(), name='author_detail'),

    path('update-book/<slug:slug>', BookUpdate.as_view(), name='book_update'),
    path('update-author/<slug:slug>', AuthorUpdate.as_view(), name='author_update'),

    path('detele-book/<slug:slug>', BookDelete.as_view(), name='book_delete'),
    path('delete-author/<slug:slug>', AuthorDelete.as_view(), name='author_delete')

]