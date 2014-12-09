#! /usr/bin/env python
# coding:utf-8

'''
ぱいてょんよくわかんない
'''
import re

def covconv(ja_JP):
    kv_JP = ja_JP

    #translateのほうがいいんですかね？

    #ひたすら列挙
    kv_JP = kv_JP.replace("アイコン", "ｱｲﾖﾝ")
    kv_JP = kv_JP.replace("アピール", "ｱｯﾋﾟﾙ")
    kv_JP = kv_JP.replace("アルゴリズム", "ｵﾙﾖﾘｽﾞﾑ")
    kv_JP = kv_JP.replace("アルバム", "ｱﾕﾊﾞﾑ")
    kv_JP = kv_JP.replace("アンコール", "ｱﾝｺｯﾙ")
    kv_JP = kv_JP.replace("イった", "ｲed")
    kv_JP = kv_JP.replace("イメージ", "ｲﾒｯｼﾞ")
    kv_JP = re.sub(r"(イヤホン)|(イヤフォン)", "ｲﾔﾋｮﾝ", kv_JP)
    kv_JP = kv_JP.replace("インチ", "ｲﾝﾖ")
    kv_JP = kv_JP.replace("インポータント", "ｲﾝﾎﾟｯﾀﾝｯ")
    kv_JP = kv_JP.replace("ウェブ", "ｳｪｯﾌﾞ")
    kv_JP = kv_JP.replace("エアコン", "ｴｱﾖﾝ")
    kv_JP = kv_JP.replace("エナジードリンク", "ｴﾅﾖｰﾄﾞﾘﾝﾎﾟ")
    kv_JP = kv_JP.replace("エロゲ", "ｴﾖｹﾞ")
    kv_JP = kv_JP.replace("オペレーティング", "ｵﾍﾟﾚｯﾃｨﾝｯ")
    kv_JP = kv_JP.replace("カニクリームコロッケ", "ｺﾆｸﾘｯﾑｶﾗｯｹ")
    kv_JP = kv_JP.replace("カラースキーム", "ｶﾗｰｽｷｯﾑ")
    kv_JP = kv_JP.replace("カップル", "ｶﾌﾟﾙ")
    kv_JP = kv_JP.replace("カーテン", "ｶｯﾃﾝ")
    kv_JP = kv_JP.replace("キーボード", "ｷｰﾎﾞｰﾖ")
    kv_JP = re.sub(r"きめ(.)|キメ(.)", "ｷﾒ\1", kv_JP) #とれない
    kv_JP = kv_JP.replace("キーワード", "ｷｯﾜｰﾖ")
    kv_JP = kv_JP.replace("クリーニング", "ｸﾘﾆﾝｯ")
    kv_JP = kv_JP.replace("ケーブル", "ｹｯﾌﾞﾙ")
    kv_JP = kv_JP.replace("ココア", "ｺｺﾔ")
    kv_JP = kv_JP.replace("コンクリート", "ｺﾝｸﾘｯﾖ")
    kv_JP = kv_JP.replace("コネクション", "ｺﾈｸﾋｮﾝ")
    kv_JP = kv_JP.replace("コンパイラ", "ｺﾝﾊﾟｲﾔ")
    kv_JP = kv_JP.replace("コンパイル", "ｺﾝﾊﾟｲﾕ")
    kv_JP = re.sub(r"(サイコロ)|(さいころ)", "ｻｲｺﾖ", kv_JP)
    kv_JP = kv_JP.replace("サドル", "ｻﾄﾞﾙ")
    kv_JP = kv_JP.replace("サークル", "ｻｯｸﾙ")
    kv_JP = kv_JP.replace("システム", "ｼｽﾖﾑ")
    kv_JP = kv_JP.replace("シュリンク", "ｼｭﾘﾝｸｯ")
    kv_JP = kv_JP.replace("ショップ", "ﾁｮｯﾌﾟ")
    kv_JP = kv_JP.replace("ステーキ", "ｽﾃｯｷ")
    kv_JP = kv_JP.replace("スタック", "ｽﾀｯﾎﾟ")
    kv_JP = kv_JP.replace("スマホ", "ｽﾏﾋｮ")
    kv_JP = kv_JP.replace("スマートフォン", "ｽﾏｰﾖﾋｮﾝ")
    kv_JP = kv_JP.replace("ストリーム", "ｽﾖﾘｰﾑ")
    kv_JP = kv_JP.replace("スパークリング", "ｽﾊﾟｰｸﾘﾝｯ")
    kv_JP = kv_JP.replace("スリープ", "ｽﾘｯﾌﾟ")
    kv_JP = kv_JP.replace("スーツケース", "ｽｰﾕｹｰｽ")
    kv_JP = kv_JP.replace("スーツ", "ｽｯﾂ")
    kv_JP = kv_JP.replace("セックス", "ｾｯｸﾖ")
    kv_JP = re.sub(r"(ソウル)|(ソール)", "ｿｯﾙ", kv_JP)
    kv_JP = kv_JP.replace("ダイヤグラム", "ﾀﾞｲﾔｸﾞﾗﾐｭ")
    kv_JP = kv_JP.replace("ダブルクォーターパウンダー", "ﾀﾞﾌﾞﾕｸｫｯﾀｰﾊﾟｳﾝﾔｰ")
    kv_JP = kv_JP.replace("ダブルチーズバーガー", "ﾀﾞﾌﾞﾕﾁｯｽﾞﾊﾞｯｶﾞｰ")
    kv_JP = kv_JP.replace("ダンボール", "ﾀﾞﾝﾎﾞｯﾙ")
    kv_JP = kv_JP.replace("デスクトップ", "ﾃﾞｽｸﾖｯﾌﾟ")
    kv_JP = kv_JP.replace("テクニカル", "ﾃｸﾆｶﾕ")
    kv_JP = kv_JP.replace("テクニシャン", "ﾃｸﾆﾋｬﾝ")
    kv_JP = kv_JP.replace("テンション", "ﾃﾝﾖﾝ")
    kv_JP = kv_JP.replace("ディスプレイ", "ﾃﾞｨｽﾌﾟﾖｲ")
    kv_JP = kv_JP.replace("テーブル", "ﾃｰﾌﾞﾕ")
    kv_JP = kv_JP.replace("トイレクイックル", "ﾖｲﾚｸｲｯｸﾖ")
    kv_JP = kv_JP.replace("トイレ", "ﾖｲﾚ")
    kv_JP = re.sub(r"(トラックパッド)|(トラックパット)", "ﾄﾗｯｸﾊﾟｯﾖ", kv_JP)
    kv_JP = kv_JP.replace("ドル", "ﾖﾙ")
    kv_JP = kv_JP.replace("トートロジー", "ﾄﾝﾄﾛｼﾞｰ")
    kv_JP = kv_JP.replace("ノートパソコン", "ﾉｰﾖﾊﾟﾖﾖﾝ")
    kv_JP = kv_JP.replace("バイオリン", "ﾊﾞｲﾖﾘﾝ")
    kv_JP = kv_JP.replace("バレーボール", "ﾊﾞﾘﾎﾞｰﾙ")
    kv_JP = kv_JP.replace("ハッカソン", "ﾊｯｶﾖﾝ")
    kv_JP = kv_JP.replace("バックアップ", "ﾊﾞｯﾖｱｯﾌﾟ")
    kv_JP = kv_JP.replace("バッテリー", "ﾊﾞｯﾖﾘｰ")
    kv_JP = kv_JP.replace("バージョン", "ﾊﾞｼﾞﾖﾝ")
    kv_JP = kv_JP.replace("パーセント", "ﾊﾟｯｾﾝﾄ")
    kv_JP = kv_JP.replace("ビデオ", "ｳﾞｨﾃﾞｵ")
    kv_JP = re.sub(r"(ビヤガーデン)|(ビアガーデン)", "ﾋﾞﾔｶﾞﾃﾞｯﾑ", kv_JP)
    kv_JP = kv_JP.replace("ビーフジャーキー", "ﾋﾞｯﾌｼﾞｬｯｷｰ")
    kv_JP = kv_JP.replace("ピロピロ", "ﾋﾟﾛﾋﾟﾛ")
    kv_JP = kv_JP.replace("フラグ", "ﾌﾔｸﾞ")
    kv_JP = kv_JP.replace("ブルートゥース", "ﾌﾞﾙｰﾖｰﾕ")
    kv_JP = kv_JP.replace("ブース", "ﾌﾞｰｽ")
    kv_JP = kv_JP.replace("フロー", "ﾌﾖｰ")
    kv_JP = kv_JP.replace("フィルタリング", "ﾌｨﾙﾀﾘﾝｯ")
    kv_JP = kv_JP.replace("フォロワー", "ﾋｮﾛﾔｰ")
    kv_JP = kv_JP.replace("フォロー", "ﾋｮﾛｰ")
    kv_JP = kv_JP.replace("フォース", "ﾋｮｰｽ")
    kv_JP = kv_JP.replace("プラグイン", "ﾌﾟﾗｷﾞﾝ")
    kv_JP = kv_JP.replace("プログラミング", "ﾌﾟﾖｸﾞﾔﾐﾝｯ")
    kv_JP = kv_JP.replace("プログラム", "ﾌﾟﾖｸﾞﾛﾑ")
    kv_JP = kv_JP.replace("プログレス", "ﾌﾟﾔｸﾞﾚｽ")
    kv_JP = re.sub(r"(プロセッサ)|(プロセッサー)", "ﾌﾟﾖｾｯｻ", kv_JP)
    kv_JP = kv_JP.replace("プロフィール", "ﾌﾟﾛﾌｨｯﾙ")
    kv_JP = kv_JP.replace("プロセス", "ﾌﾟﾖｾｽ")
    kv_JP = kv_JP.replace("プロモーション", "ﾌﾟﾖﾓｯｼｮﾝ")
    kv_JP = kv_JP.replace("ベストエフォート", "ﾍﾞｽﾄｴﾌｫｯﾄ")
    kv_JP = kv_JP.replace("ベビースター", "ﾍﾞﾋﾞｯｽﾔｯ")
    kv_JP = kv_JP.replace("マグロ", "ﾏｸﾞﾛ")
    kv_JP = kv_JP.replace("ミステイク", "ﾐｽﾃｯｸ")
    kv_JP = kv_JP.replace("ミーティング", "ﾒｯﾃｨﾝ")
    kv_JP = kv_JP.replace("メイド", "ﾒｲﾖ")
    kv_JP = kv_JP.replace("メール", "ﾒｰﾕ")
    kv_JP = kv_JP.replace("モンスター", "ﾓﾝｽﾔｰ")
    kv_JP = kv_JP.replace("モーニング", "ﾓｯﾆﾝ")
    kv_JP = kv_JP.replace("ライティング", "ﾗｲﾃｨﾝｯ")
    kv_JP = kv_JP.replace("ラーメン", "ﾗﾒﾝｯ")
    kv_JP = kv_JP.replace("リア充", "ﾘｱｯｼﾞｭ")
    kv_JP = kv_JP.replace("リサイクル", "ﾘｻｲｸﾕ")
    kv_JP = kv_JP.replace("レッドブル", "ﾚｯﾖﾌﾞﾙ")
    kv_JP = kv_JP.replace("ロックスター", "ﾛｯﾌﾟｽﾔｰ")
    kv_JP = kv_JP.replace("ローマ", "ﾖｰﾏ")
    kv_JP = re.sub(r"(ユーザ)|(ユーザー)", "ﾕｰｻﾞ", kv_JP)
    kv_JP = kv_JP.replace("群論", "ｸﾞﾝﾖﾝ")
    kv_JP = kv_JP.replace("圏論", "ｹﾝﾖﾝ")

    #英語に変換する場合
    kv_JP = kv_JP.replace(r"かなり", "ｋａｎａｒｉ")
    kv_JP = kv_JP.replace(r"こわい", "ｋｏｗａｉ")
    kv_JP = kv_JP.replace(r"つらい", "ｔｓｕｒａｉ")
    kv_JP = kv_JP.replace(r"へんたい", "ｈｅｎｎｔａｉ")
    kv_JP = kv_JP.replace(r"べんり", "ｂｅｎｒｉ")
    kv_JP = kv_JP.replace(r"やばい", "ｙａｂａｉ")
    kv_JP = kv_JP.replace(r"やばそう", "ｙａｂａｓｏｕ")
    kv_JP = kv_JP.replace(r"わるい", "ｗａｒｕｉ")
    
    return kv_JP


#test
if __name__ == '__main__':
    a = covconv('エナジードリンク')
    print(a)
