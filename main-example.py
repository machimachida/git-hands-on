# じゃんけんをするプログラム
# グー、チョキ、パーをそれぞれ0, 1, 2で表す
hands = ["グー", "チョキ", "パー"]


"""
じゃんけんの手を入力する関数
引数: なし
返り値: 0, 1, 2のいずれか
"""
def input_hand():
    print("0: グー")
    print("1: チョキ")
    print("2: パー")
    return int(input("何を出しますか? "))


"""
ランダムにじゃんけんの手を出力する関数
引数: なし
返り値: 0, 1, 2のいずれか
"""
def random_hand():
    import random
    return random.randint(0, 2)


"""
じゃんけんの勝敗を判定する関数
引数: player_hand, computer_hand
返り値: 勝ち、負け、引き分けのいずれか
"""
def judge(player_hand, computer_hand):
    if player_hand == computer_hand:
        return "引き分け"
    elif (player_hand == 0 and computer_hand == 1) or (player_hand == 1 and computer_hand == 2) or (player_hand == 2 and computer_hand == 0):
        return "勝ち"
    else:
        return "負け"


def main():
    print("じゃんけん開始")
    player_hand = input_hand()
    computer_hand = random_hand()
    print("あなたの手: " + hands[player_hand])
    print("コンピュータの手: " + hands[computer_hand])
    print(judge(player_hand, computer_hand))


if __name__ == "__main__":
    main()