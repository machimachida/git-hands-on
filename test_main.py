"""
じゃんけんの手を入力する関数のユニットテスト

テスト対象関数input_handについて
引数: なし
返り値: 0, 1, 2のいずれか
"""
#def test_input_hand():
#    from main import input_hand
#    from unittest.mock import patch
#    with patch("builtins.input", return_value="0"):
#        assert input_hand() == 0
#    with patch("builtins.input", return_value="1"):
#        assert input_hand() == 1
#    with patch("builtins.input", return_value="2"):
#        assert input_hand() == 2


"""
ランダムにじゃんけんの手を出力する関数のユニットテスト

テスト対象関数random_handについて
引数: なし
返り値: 0, 1, 2のいずれか
"""
#def test_random_hands():
#    from main import random_hand
#    assert random_hand() in [0, 1, 2]


"""
じゃんけんの勝敗を判定する関数

テスト対象関数judgeについて
引数: player_hand, computer_hand
返り値: 勝ち、負け、引き分けのいずれか
"""
#def test_judge():
#    from main import judge
#    assert judge(0, 0) == "引き分け"
#    assert judge(0, 1) == "勝ち"
#    assert judge(0, 2) == "負け"
#    assert judge(1, 0) == "負け"
#    assert judge(1, 1) == "引き分け"
#    assert judge(1, 2) == "勝ち"
#    assert judge(2, 0) == "勝ち"
#    assert judge(2, 1) == "負け"
#    assert judge(2, 2) == "引き分け"