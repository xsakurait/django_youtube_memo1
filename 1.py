from typing import ValuesView


# レンダリング　テンプレートをアクセスごとに置き換える
# 変数　{{変数　}}
# タグ　{% タグ　% }
# フィルタ　{　値 | フィルた　}
# staticフォルダに入れたせい的ファイルは　staticタグじゃないと呼び出せない
# staticだけロードする必要あるのは
# htmlでcss使わなくても実行できるから

# テンプレートビュー使いたいときは
class based view


class a(TemplateView):

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt['name'] = 'a'
        return ctxt


template
{{user}}  # デフォルトのやつ
{{name}}  # a
