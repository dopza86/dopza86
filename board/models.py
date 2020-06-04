from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey(
        "fcusers.Fcusers", on_delete=models.CASCADE, verbose_name="작성자"
    )  # on_delete 을 꼭 설정하자,ForeignKey는 1대N 1명의 사용자가 여러 글을 쓸수있다
    tags = models.ManyToManyField("tag.Tag", verbose_name="태그")
    registerd_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "fastcampus_board"
        verbose_name = "패스트캠퍼스 게시글"
        verbose_name_plural = "패스트캠퍼스 게시글"
