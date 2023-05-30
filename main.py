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

def main():
    print("じゃんけん開始")
    player_hand = input_hand()
    computer_hand = random_hand()
    print("あなたの手: " + hands[player_hand])
    print("コンピュータの手: " + hands[computer_hand])
    print(judge(player_hand, computer_hand))


if __name__ == "__main__":
    main()