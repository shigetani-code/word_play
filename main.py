import jaconv
import kana2vowel

"""
適当な文字列（ひらがな）が入力されたら、母音に変換。
解析した母音とboin.txtにある母音が一致する場合、行数を取得。
goi.txtから取得した行数にある文字を表示。
"""
# try~except文。KeyboardInterruptでCtrl+C押されるまでwhile True
try:
    while True:
        # input()で標準入力
        input_val = input("なんか言ってみて：")
        #文字種変換ライブラリjaconvでひらがな->カタカナ
        kata_val = jaconv.hira2kata(input_val)
        #kana2vowel.pyのkana2vowel関数(ユーザー関数)でカタカナから母音に変換
        hira_val = kana2vowel.kana2vowel(kata_val)
        #print(hira_val)

        """
        ファイル内の特定文字を見つける
        """
        #boin.txtを開く
        with open('./boin.txt') as f:
            #enumerate()でインデックスと要素の両方を取り出す
            for row, text in enumerate(f):
                # 文字列の末尾の\nを除去(replaceでも可)
                text = text.rstrip()
                #解析した母音と一致するテキストを見つける
                if text == hira_val:
                    # 母音と一致する行数
                    dst_row = row
                else:
                    #それ以外の場合無視
                    pass

        """
        指定された行のテキストを表示する
        """
        #goi.txtを開く
        with open("./goi.txt") as f:
            # goi.txtで見つけた行を読み込む
            data = f.readlines()[dst_row]
            # 2行目以降から\nが含まれるのでreplace()で除去
            data = data.replace("\n", "")
        print(data + "？\n")
except KeyboardInterrupt:
    print("\nBREAK")