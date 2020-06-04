from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={"required": "제목을 입력하세요"}, max_length=128, label="제목",
    )
    contents = forms.CharField(
        error_messages={"required": "내용을 입력하세요"}, widget=forms.Textarea, label="내용",
    )  # CharField를 그대로 사용하는 이유는 form 에는 textfield가 없다 , textfield는 models.Model 에서 상속받을수 있다
    # 그러므로 forms의 textarea 위젯을 사용하여 text 입력을 구현한다
    tags = forms.CharField(required=False, label="태그")
    # required=False ->필수가 아님
