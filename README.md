# git-hands-on

Git講習用のリポジトリです。

## 演習 - じゃんけんゲームを作ろう

main.py上に関数を作成し、じゃんけんゲームを実装してください。

main関数を見ると、
- input_hand()
- random_hand()
- judge()

という3つの関数が必要であることがわかります。
これらを分担して、実装してみましょう。

### フロー

1. requirements.txtからライブラリをインストールしてください。
  - pytestがインストールされます。
2. 作業ブランチをわけましょう。
  - input_hand()なら`feature/input`
  - random_hand()なら`feature/random`
  - judge()なら`feature/judge`
3. 関数を実装しましょう。
4. 関数についてユニットテストを実行しましょう。
  - 自分の実装が合っているか確かめられます。
  - test_main.pyから、自分の実装した関数に該当するテスト関数のコメントアウトを外してください。
  - `pytest ./test_main.py::test_[自分の実装した関数名]`でテストできます。
    - 1 passedと表示されたらOKです。
5. `git add`でファイルをステージングします。
  - `git add main.py test_main.py`です。
6. `git commit`でファイルをコミットします。
  - `git commit -m "[自分の作業がどんなものかわかりやすいメッセージ]"
7. `git push`でコミットをリモートリポジトリに送信します。
  - `git push origin [自分の作業ブランチ名]



### プログラムを考えるのがめんどくさい方へ

main-example.py に回答例があります。