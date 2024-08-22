from django.db import models
import uuid


class Page(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    title = models.CharField(max_length=100, verbose_name="제목")
    body = models.TextField(max_length=2000, verbose_name="내용")
    page_date = models.DateField(verbose_name="날짜")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일자")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일자")

    def __str__(self):
        return self.title
