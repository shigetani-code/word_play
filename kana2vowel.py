def kana2vowel(text):
    """
    カタカナを母音に変換するユーザー関数。

    Returns
    ---------
    text : string
        母音に変換したカタカナの文字列
    """
    #大文字とゥの変換リスト
    large_tone = {
        'ア' :'ア', 'イ' :'イ', 'ウ' :'ウ', 'エ' :'エ', 'オ' :'オ',
        'ゥ': 'ウ', 'ヴ': 'ウ',
        'カ' :'ア', 'キ' :'イ', 'ク' :'ウ', 'ケ' :'エ', 'コ' :'オ',
        'サ' :'ア', 'シ' :'イ', 'ス' :'ウ', 'セ' :'エ', 'ソ' :'オ',
        'タ' :'ア', 'チ' :'イ', 'ツ' :'ウ', 'テ' :'エ', 'ト' :'オ',
        'ナ' :'ア', 'ニ' :'イ', 'ヌ' :'ウ', 'ネ' :'エ', 'ノ' :'オ',
        'ハ' :'ア', 'ヒ' :'イ', 'フ' :'ウ', 'ヘ' :'エ', 'ホ' :'オ',
        'マ' :'ア', 'ミ' :'イ', 'ム' :'ウ', 'メ' :'エ', 'モ' :'オ',
        'ヤ' :'ア', 'ユ' :'ウ', 'ヨ' :'オ',
        'ラ' :'ア', 'リ' :'イ', 'ル' :'ウ', 'レ' :'エ', 'ロ' :'オ',
        'ワ' :'ア', 'ヲ' :'オ', 'ン' :'ン', 'ヴ' :'ウ',
        'ガ' :'ア', 'ギ' :'イ', 'グ' :'ウ', 'ゲ' :'エ', 'ゴ' :'オ',
        'ザ' :'ア', 'ジ' :'イ', 'ズ' :'ウ', 'ゼ' :'エ', 'ゾ' :'オ',
        'ダ' :'ア', 'ヂ' :'イ', 'ヅ' :'ウ', 'デ' :'エ', 'ド' :'オ',
        'バ' :'ア', 'ビ' :'イ', 'ブ' :'ウ', 'ベ' :'エ', 'ボ' :'オ',
        'パ' :'ア', 'ピ' :'イ', 'プ' :'ウ', 'ペ' :'エ', 'ポ' :'オ'
    }

    #ト/ド+'ゥ'をウに変換
    for k in 'トド':
        while k+'ゥ' in text:
            text = text.replace(k+'ゥ','ウ')
    #テ/デ+ィ/ュをイ/ウに変換
    for k in 'テデ':
        for k2,v in zip('ィュ','イウ'):
            while k+k2 in text:
                text = text.replace(k+k2,v)

    #大文字とゥを母音に変換
    text = list(text)
    for i, v in enumerate(text):
        if v in large_tone:
            text[i] = large_tone[v]
    text = ''.join(text)

    #ウーをウウに変換
    while 'ウー' in text:
        text = text.replace('ウー','ウウ')

    #ウ+ヮ/ァ/ィ/ェ/ォを母音に変換
    for k,v in zip('ヮァィェォ','アアイエオ'):
        text = text.replace('ウ'+k,v)

    #イー/ィーをイイ/ィイに変換
    for k in 'イィ':
        while k+'ー' in text:
            text = text.replace(k+'ー',k+'イ')

    #イ/ィ+ャ/ュ/ェ/ョを母音に変換
    for k,v in zip('ャュェョ','アウエオ'):
        text = text.replace('イ'+k, v).replace('ィ'+k, v)

    #残った小文字を母音に変換
    for k,v in zip('ヮァィェォャュョ','アアイエオアウオ'):
        text = text.replace(k,v)

    #ー（長音）を母音に変換する
    for k in 'アイウエオ':
        while k+'ー' in text:
            text = text.replace(k+'ー',k+k)

    return text