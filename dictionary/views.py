from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from difflib import get_close_matches
from PyDictionary import PyDictionary
from gettext import gettext
import pyttsx3
import googletrans
from googletrans import Translator
import json


def menuView(request):
    return render(request, 'dictionary/menu.html')


def error_500(request):
    return render(request, 'dictionary/500.html')


def tango_nihongo_eigo(request):
    return render(request, 'dictionary/tango_nihongo_eigo.html')


def tango_rosiago_nihongo(request):
    return render(request, 'dictionary/tango_rosiago_nihongo.html')


def tango_eigo_rosiago(request):
    return render(request, 'dictionary/tango_eigo_rosiago.html')


def tango_sonota(request):
    return render(request, 'dictionary/tango_sonota.html')


def bunsho(request):
    return render(request, 'dictionary/bunsho.html')


def imi(request):
    return render(request, 'dictionary/imi.html')


def tango_sentaku(request):
    return render(request, 'dictionary/tango_sentaku.html')


def about(request):
    return render(request, 'dictionary/about.html')


def tango_kekka_nihongo_eigo(request):
    words_japanese_english = {'xxx': 'yyy',
                              'aaa': 'bbb', }
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    dictionary1 = dict([[v, k] for v, k in words_japanese_english.items()])
    dictionary2 = dict([[v, k] for k, v in words_japanese_english.items()])
    translator = Translator()
    translate = translator.translate(text, lang)
    translation = translate.text
    dictionary = {**dictionary1, **dictionary2}
    if text == '':
        return render(request, 'dictionary/tango_nihongo_eigo.html')
    elif text == ' ':
        return render(request, 'dictionary/tango_nihongo_eigo.html')
    else:
        translation_googletrans_view = translation.title
        word_view = text.title()
        translate_word = text.lower()
        if translate_word in dictionary:
            translation_dictionary = dictionary.get(translate_word)
            translation_dictionary_view = translation_dictionary.title()
            context = {
                'word': word_view,
                'translation': translation_dictionary_view
            }
            return render(request, 'dictionary/tango_kekka_nihongo_eigo.html', context)
        elif translate_word.title() in dictionary:
            translation_dictionary_title = dictionary.get(translate_word.title())
            translation_dictionary_title_view = translation_dictionary_title.title
            context_title = {
                'word': word_view,
                'translation': translation_dictionary_title_view
            }
            return render(request, 'dictionary/tango_kekka_nihongo_eigo.html', context_title)
        elif translate_word.upper() in dictionary:
            translation_upper = dictionary.get(translate_word.upper())
            translation_upper_view = translation_upper.title()
            context_upper = {
                'word': word_view,
                'translation': translation_upper_view
            }
            return render(request, 'dictionary/tango_kekka_nihongo_eigo.html', context_upper)
        elif len(get_close_matches(translate_word, dictionary.keys())) > 0:
            translation_close = dictionary[get_close_matches(text, dictionary.keys())[0]]
            translation_close_view = translation_close.title()
            word_close = get_close_matches(text, dictionary)
            word_close_view1 = "".join(word_close)
            word_close_view = word_close_view1.title()
            close_setsu1 = gettext("close_setsu1")
            close_setsu2 = gettext("close_setsu2")
            close_setsu3 = gettext("close_setsu3")
            close_setsu_quotes1 = gettext("close_setsu_quotes1")
            close_setsu_quotes2 = gettext("close_setsu_quotes2")
            context_close = {
                'word': word_close_view,
                'translation': translation_close_view,
                'not_found_word': text,
                'close_setsu1': close_setsu1,
                'close_setsu2': close_setsu2,
                'close_setsu3': close_setsu3,
                'close_setsu_quotes1': close_setsu_quotes1,
                'close_setsu_quotes2': close_setsu_quotes2
            }
            return render(request, 'dictionary/tango_kekka_nihongo_eigo.html', context_close)
        else:
            return render(request, 'dictionary/tango_kekka_nihongo_eigo.html',
                          {'translation': translation_googletrans_view, 'word': word_view})


def tango_kekka_rosiago_nihongo(request):
    words_russian_japanese = {'xxx': 'yyy',
                              'aaa': 'bbb', }
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    dictionary1 = dict([[v, k] for v, k in words_russian_japanese.items()])
    dictionary2 = dict([[v, k] for k, v in words_russian_japanese.items()])
    translator = Translator()
    translate = translator.translate(text, lang)
    translation = translate.text
    dictionary = {**dictionary1, **dictionary2}
    if text == '':
        return render(request, 'dictionary/tango_rosiago_nihongo.html')
    elif text == ' ':
        return render(request, 'dictionary/tango_rosiago_nihongo.html')
    else:
        translation_googletrans_view = translation.title
        word_view = text.title()
        translate_word = text.lower()
        if translate_word in dictionary:
            translation_dictionary = dictionary.get(translate_word)
            translation_dictionary_view = translation_dictionary.title()
            context = {
                'word': word_view,
                'translation': translation_dictionary_view
            }
            return render(request, 'dictionary/tango_kekka_rosiago_nihongo.html', context)
        elif translate_word.title() in dictionary:
            translation_dictionary_title = dictionary.get(translate_word.title())
            translation_dictionary_title_view = translation_dictionary_title.title
            context_title = {
                'word': word_view,
                'translation': translation_dictionary_title_view
            }
            return render(request, 'dictionary/tango_kekka_rosiago_nihongo.html', context_title)
        elif translate_word.upper() in dictionary:
            translation_upper = dictionary.get(translate_word.upper())
            translation_upper_view = translation_upper.title()
            context_upper = {
                'word': word_view,
                'translation': translation_upper_view
            }
            return render(request, 'dictionary/tango_kekka_rosiago_nihongo.html', context_upper)
        elif len(get_close_matches(translate_word, dictionary.keys())) > 0:
            translation_close = dictionary[get_close_matches(text, dictionary.keys())[0]]
            translation_close_view = translation_close.title()
            word_close = get_close_matches(text, dictionary)
            word_close_view1 = "".join(word_close)
            word_close_view = word_close_view1.title()
            close_setsu1 = gettext("close_setsu1")
            close_setsu2 = gettext("close_setsu2")
            close_setsu3 = gettext("close_setsu3")
            close_setsu_quotes1 = gettext("close_setsu_quotes1")
            close_setsu_quotes2 = gettext("close_setsu_quotes2")
            context_close = {
                'word': word_close_view,
                'translation': translation_close_view,
                'not_found_word': text,
                'close_setsu1': close_setsu1,
                'close_setsu2': close_setsu2,
                'close_setsu3': close_setsu3,
                'close_setsu_quotes1': close_setsu_quotes1,
                'close_setsu_quotes2': close_setsu_quotes2
            }
            return render(request, 'dictionary/tango_kekka_rosiago_nihongo.html', context_close)
        else:
            return render(request, 'dictionary/tango_kekka_rosiago_nihongo.html',
                          {'translation': translation_googletrans_view, 'word': word_view})


def tango_kekka_eigo_rosiago(request):
    words_english_russian = {'xxx': 'yyy',
                             'aaa': 'bbb', }
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    dictionary1 = dict([[v, k] for v, k in words_english_russian.items()])
    dictionary2 = dict([[v, k] for k, v in words_english_russian.items()])
    translator = Translator()
    translate = translator.translate(text, lang)
    translation = translate.text
    dictionary = {**dictionary1, **dictionary2}
    if text == '':
        return render(request, 'dictionary/tango_eigo_rosiago.html')
    elif text == ' ':
        return render(request, 'dictionary/tango_eigo_rosiago.html')
    else:
        translation_googletrans_view = translation.title
        word_view = text.title()
        translate_word = text.lower()
        if translate_word in dictionary:
            translation_dictionary = dictionary.get(translate_word)
            translation_dictionary_view = translation_dictionary.title()
            context = {
                'word': word_view,
                'translation': translation_dictionary_view
            }
            return render(request, 'dictionary/tango_kekka_eigo_rosiago.html', context)
        elif translate_word.title() in dictionary:
            translation_dictionary_title = dictionary.get(translate_word.title())
            translation_dictionary_title_view = translation_dictionary_title.title
            context_title = {
                'word': word_view,
                'translation': translation_dictionary_title_view
            }
            return render(request, 'dictionary/tango_kekka_eigo_rosiago.html', context_title)
        elif translate_word.upper() in dictionary:
            translation_upper = dictionary.get(translate_word.upper())
            translation_upper_view = translation_upper.title()
            context_upper = {
                'word': word_view,
                'translation': translation_upper_view
            }
            return render(request, 'dictionary/tango_kekka_eigo_rosiago.html', context_upper)
        elif len(get_close_matches(translate_word, dictionary.keys())) > 0:
            translation_close = dictionary[get_close_matches(text, dictionary.keys())[0]]
            translation_close_view = translation_close.title()
            word_close = get_close_matches(text, dictionary)
            word_close_view1 = "".join(word_close)
            word_close_view = word_close_view1.title()
            close_setsu1 = gettext("close_setsu1")
            close_setsu2 = gettext("close_setsu2")
            close_setsu3 = gettext("close_setsu3")
            close_setsu_quotes1 = gettext("close_setsu_quotes1")
            close_setsu_quotes2 = gettext("close_setsu_quotes2")
            context_close = {
                'word': word_close_view,
                'translation': translation_close_view,
                'not_found_word': text,
                'close_setsu1': close_setsu1,
                'close_setsu2': close_setsu2,
                'close_setsu3': close_setsu3,
                'close_setsu_quotes1': close_setsu_quotes1,
                'close_setsu_quotes2': close_setsu_quotes2
            }
            return render(request, 'dictionary/tango_kekka_eigo_rosiago.html', context_close)
        else:
            return render(request, 'dictionary/tango_kekka_eigo_rosiago.html',
                          {'translation': translation_googletrans_view, 'word': word_view})


def tango_kekka_sonota(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    if text == '':
        return render(request, 'dictionary/tango_sonota.html')
    elif text == ' ':
        return render(request, 'dictionary/tango_sonota.html')
    else:
        translator = Translator()
        translate = translator.translate(text, lang)
        word_translation = translate.text
        word_view = text.title()
        return render(request, 'dictionary/tango_kekka_sonota.html',
                      {'word': word_view, 'word_translation': word_translation})


def bunsho_kekka(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    if text == '':
        return render(request, 'dictionary/bunsho.html')
    elif text == ' ':
        return render(request, 'dictionary/bunsho.html')
    else:
        translator = Translator()
        translate = translator.translate(text, lang)
        translation = translate.text
        return render(request, 'dictionary/bunsho_kekka.html',
                      {'translation': translation, 'text': text})


def imi_kekka(request):
    words = {'血栓': '血管内で、血液成分が固まって、血管内を閉塞すること。',
             '塞栓': '血管からはがれた血栓の一部や血管外から侵入した異物（空気・脂肪等）が血管を閉塞させること。',
             '除脈': '通常50/分未満の心拍数のこと。',
             '頻脈（タヒ）': '心拍数が１分間に100以上の状態。',
             '結滞・結代': '心臓の期外収縮により、脈拍のリズムが乱れ、脈拍測定した際に脈拍が途切れる（または脈が飛ぶ）こと。',
             '発作（アタック）': '疾病特有の症状または激しい症状が急激に起こること。',
             'うっ血': '　静脈の血液循環が障がいされ、血流が停滞すること。',
             '静脈瘤（バリックス）': '静脈の一部が何らかの要因で薄くなり、その血管が膨らむことで発症する。',
             '急性循環不全（ショック）': '急に全身の末梢循環が障がいされること。生命を維持するには血圧が低すぎる、命に関わる状態。',
             '貧血（アネミー）': '一定量の血液の酸素運搬物質の濃度が低下した状態で、微熱・易疲労感・頭痛・動悸・息切れが起こる。',
             'チアノーゼ': '肺もしくは心臓の機能不全による循環障害により、唇・まぶた・手足の爪等、皮膚が紫藍色または暗青色になること。',
             '虚血': '局所性貧血。組織や臓器への動脈血の流入や酸素供給が減少あるいは途絶えた状態。',
             '壊死（ネクローシス）': '病気や傷により、細胞や組織が致命的な損傷を受けて、局所的に死ぬこと。',
             '壊疽・脱疽 ': '血液供給が無くなり、組織が壊死した所に細菌感染し、腐敗してくること。',
             'DIC（播種性血管内凝固症候群）': '重篤な疾患が引き金となり、全身の血管内で血液凝固反応が起こり血栓ができるため、臓器不全や出血下血を引き起こす。',
             '脱水': '体内の水分が喪失される時に電解質も喪失し、口渇や発熱、痙攣、昏睡などの症状が起こる。',
             '浮腫（エデーマ）': '皮下に組織間液が貯留すること。',
             'ヘルニア': '臓器の一部または全部が隙間や裂け目を通じて異常な位置に脱出すること。（脳・椎間板・ソケイ部等に発生する）',
             '発熱（フィーバー）': '病気が原因で、体温が平常より上昇した場合（３７℃以上）をいう。',
             '悪寒': 'さむけ。感染初期や過激な発熱初期によくみられる不快なさむけ。',
             '戦慄（シバリング）': 'さむけにふるえが伴うもの。',
             '咳嗽': '　咳。肺・気管支・気管から異物・刺激物・分泌物を排除できない場合の防御反応のこと。',
             '血痰': '痰に少量の血が混じっているもの。',
             '喀血': '咳とともに気道または肺から吐き出される鮮紅血の大量出血のこと。',
             '吃逆': 'しゃっくり。横隔膜の痙攣によって生ずる症状。',
             '呻吟': '苦しそうにうなること。',
             '喘鳴': '気管支ぜんそく等で、呼吸時に「ゼーゼー」「ヒューヒュー」というような状態。',
             '嗄声': 'しわがれ声。声帯に病変があるため、音声が異常な状態。',
             'ファイティング': '患者の呼吸と人工呼吸器の補助や強制換気が合わないこと。',
             'バッキング': '気管カニューレ等の刺激や人工呼吸器との呼吸のリズムが合わず、患者の咳嗽反射を誘発して、咳込んだ状態。',
             '胸水': '胸膜腔に貯留した液。通常は少量が胸膜の表面をうるおしているが、胸膜炎・肺がん・肝硬変などの際には増加する。',
             '失禁': '小便・大便・涙等を自分の意思によらず排泄してしまうこと。',
             '尿閉': '膀胱内にたまった尿を上手く排出できない状態。',
             '無尿': '一日の尿量が100ｍｌ以下で膀胱に尿がたまらない状態。',
             '乏尿': '一日尿量が400ｍｌ以下で、排泄する尿が著しく少ない状態。',
             '膿尿': '白血球のまじった尿。尿路に炎症のある場合にみられる。',
             '血尿': '腎臓・膀胱・尿道のいずれかの部位からの出血により、尿に血液が混じって濁ること。',
             '頻尿': '排尿回数の異常な増加をきたす疾患または状態。',
             '多尿': '一日の尿量が3000ｍｌを超えるもの。多量の液体摂取や神経興奮・萎縮腎・糖尿病・尿崩症などが原因。',
             'パーキンソニズム': '　振戦、筋強剛、動作緩慢、姿勢反射などのパーキンソン病類似の症候を呈する病態を指す。',
             '仮面用顔貌': 'パーキンソン症候群の３大症候の一つ。他に運動緩慢及び無動症がある。無表情となり瞬きも少なく、一点を見つめるような顔つきが特徴。',
             '不随意運動': '意思に基づかない不合理な運動のこと。',
             '振戦': '意思とは無関係に、筋肉の収縮、弛緩が繰り返された場合に起こる、リズミカルな振動運動である。',
             '疼痛（ペイン）': 'ずきずき痛むこと。うずき。',
             'ムーンフェイス': '満月様顔貌。ステロイド使用による副作用で、体重増加とともに顔がまん丸になる症状。',
             '回旋': '回す動作のこと。',
             '外旋': '体の外側にひねる動作股関節等。',
             '内旋': '体の内側にひねる動作（股関節等）',
             '外転': '四肢を体正中線より遠ざけるような、冠状面内の動きを指す。',
             '内転': '四肢を体正中線に近づくように内方に向かう関節動作',
             '伸展': '関節を伸ばすこと。',
             '屈曲': '関節を曲げること。',
             '後屈': '体を後ろに曲げること。',
             '前屈': '体を前に曲げること。',
             '側屈': '体を横に曲げること。',
             '背屈': '手首の運動で手背側に曲げること。',
             '掌屈': '手首の運動で、手掌側に曲げること。',
             'ROM（ロム）': '身体の各関節が傷害などが起きないで生理的に運動することができる範囲（角度）のこと。',
             '良肢位': '関節拘縮をきたし、その位置で動かなくなっても日常生活にもっとも支障が少ない手足の位置。',
             '拘縮': '関節動かさないために、次第に関節の動く範囲が狭くなった状態のこと。',
             '内反尖足': '足関節、すなわち足首がピンと伸びて、足の底が内側を向いた麻痺のある足の特有の拘縮の状態',
             '強直': 'かたくこわばること。',
             '固縮・強剛': '身体の筋肉が持続的に強くこわばること。',
             '破行': '片足をひきずるようにして歩くこと。',
             '分回し歩行': '麻痺側の足を前へふり出す時に、つま先が床面にあたらなしように、外側に大回りさせる歩行。',
             'タンデム歩行': 'つぎあし歩行。一側のつま先に対側の踵を接触させながら床面に引いた一直線上を歩行する。応用歩行の一つ。',
             '幻覚': '実際に感覚的刺激や対象がないのに、あるように知覚すること。',
             'せん妄': '意識混濁に加えて、幻覚や錯覚がみられるような状態。我を忘れて意味不明なことを言い出すこと。',
             '妄想': '根拠もなくあれこれと想像すること。事実でないことや根拠の薄いことを強固に確信しており、どんな手段を以てしても訂正できない状態',
             '抑うつ': '気分が沈んで晴れないこと。',
             '焦燥': 'いらいらする、あるいはむしゃくしゃする精神状態。',
             '熱傷（バーン）': 'やけど',
             '挫創': '物にぶつけたりして皮下組織と皮膚の表面に傷口がある場合の怪我のこと。',
             '挫傷': '物にぶつけたりして、皮膚の表面に傷口がなく内部組織が身障する怪我のこと。',
             '擦過傷': 'すりきず。かすり傷。',
             '漿液': '一般的に薄い黄色透明な種々の体液のこと。',
             '膿（アイテル）': 'うみ。炎症部が化膿して生じる黄白色または黄緑色の不透明な粘液。',
             '滲出': '液体が外ににじみでること。',
             '漏出性': 'もれて出ること。',
             'ポケット': '寝たきり等で筋肉量が減り骨が突出した所の皮膚、皮下組織・筋肉が体重で圧迫され血流障がいが起こり、創傷がポケット状となること。',
             'デブリ―ドマン': '創傷治癒の障がいとなる壊死組織や損傷組織を除去すること。',

             'RBC（赤血球）': '貧血や多血症の診断に用いられる。基準値（成人）男性400万～540万/μ ｌ　　女性370万～490万/μ ｌ',
             'WBC（白血球）': '炎症性疾患や血液疾患の診断に用いられる。基準値（成人）4700～8700/μ ｌ',
             'Hb（ヘモグロビン濃度・ハーベー）': '貧血や多血症の診断に用いられる。基準値（成人）男性13.0～17.0ｇ/ｄｌ　女性11.0～15.0ｇ/ｄｌ',
             'Ht（ヘマトクリット）': '貧血や多血症の診断に用いられる。基準値（成人）男性40～50％　　女性35～45％',
             'CRP（C反応性蛋白）': '体内に急性炎症や感染、組織の損傷がある時に、血清中に増えるたんぱく質の一つで、体内の炎症の度合いを見る。',
             'BS・GLU（血糖・グルコース）': '血液中のブドウ糖のこと。食前食後を通して70～140ｍｇ/ｄｌの範囲で保たれている。',
             'TP　(総蛋白）': '血液中の蛋白の量で、栄養状態や腎障害・肝障害を見る。正常値6.7～8.3ｇ/ｄｌ',
             'GOT': '肝臓に多く含まれる酵素で、組織に障がいがあると値が上昇し、肝障害を見る。正常値10～40IU/ｌ',
             'GPT': '肝臓に多く含まれる酵素で、組織に障がいがあると値が上昇し、肝障害を見る。正常値5～45IU/ｌ',
             'AL-P': '骨や肝臓などに多く含まれる酵素で、胆のう・胆管の障がいで上昇する。正常値100～325IU/ｌ',
             'γ-GTP': '肝臓などに分布する酵素で、胆汁うっ滞・アルコール・薬物などの影響で上昇する。正常値男80以下IU/ｌ　女30以下IU/ｌ',
             'LDH': '心筋や肝臓・骨格筋・赤血球等に多く含まれる酵素で、心筋障がいや肝障がいなどが起こると上昇する。正常値120～240IU/ｌ',
             'ZZT': '慢性化燃・肝硬変・慢性炎症や膠原病等で値が上昇する。正常値2.0～12.0U',
             'T-Bil　(総ビリルビン）': '老化した赤血球の破壊により、その血色素がビリルビンとなり、一部は肝臓を経て胆汁中に排泄される。肝・胆道系疾患等で上昇する。正常値1.1以下ｍｇ/ｄｌ',
             'AMY（アミラーゼ）': '膵臓や膵液腺から分泌される酵素で、膵炎や耳下腺炎などの際に上昇する。正常値　血清55～175mu/ml　尿30～950mu/ml',
             'BUN (尿素窒素）': '腎臓の機能が低下すると排泄が十分されず、値が上昇する。値が高値になると、尿毒症を引き起こす。正常値8～23ｍｇ/ｄｌ',
             'CHE（クレアチニン）': '筋肉中のエネルギー源となる物質がクレアチニンに変わって腎臓から排泄される。腎障害があると高値となる。正常値　男0.8～1.3ｍｇ/ｄｌ女2.4～5.8ｍｇ/ｄｌ',
             'UA（尿酸）': '腎臓の排泄機能の低下や尿酸生成の促進によって、値が高値になり痛風等を引き起こす。正常値　男3.8～7.5ｍｇ/ｄｌ　女2.4～5.8ｍｇ/ｄｌ',
             'T-cho（総コレステロール）': '過剰になれば、血管壁に付着して血管が狭くなったり、弾力性を失うなど、動脈硬化の原因となる。　正常値140～199ｍｇ/ｄｌ',
             'TG（中性脂肪）': '過剰になれば、皮下や肝臓に蓄積して、肥満や脂肪肝または動脈硬化も促進される。　正常値30～149ｍｇ/ｄｌ',
             'HDL-C（HDLコレステロール） ': 'コレステロールを末梢血管から肝臓に転送する働き（善玉コレステロール）があり、40以下は動脈硬化を疑う。正常値　男40～70ｍｇ/ｄｌ　女45～75ｍｇ/ｄｌ',
             'FBS（空腹時血糖）': '糖代謝の検査。一般的には朝の空腹時血糖値をもって判定される。正常値70～109ｍｇ/ｄｌ',
             'BS（随時または食後血糖）': '血糖値は食事などにより変動するが、変動幅は一定範囲に止まり、食後であっても140ｍｇ/ｄｌは超えない。正常値　70～139ｍｇ/ｄｌ',
             'Hb A1c（ヘモグロビンA1c）': 'およそ4～8週間の血糖のコントロール状態を反映するため、食事に影響されない。糖代謝の診断に有効な検査。　正常値4.5～5.8％',
             'Tages（ターゲス）': '血糖の日内変動。朝食前・朝食後2時間・昼食前・昼食後2時間・夕食前・夕食後2時間・夜中の血糖値を想定して、その変動を調べる検査。',
             'OGTT（糖不可試験）': '空腹時の血糖値を調べた後、75ｇのブドウ糖水溶液を飲み、その後２時間で血糖値がどの程度変化したかを調べて、糖尿病の判定に利用する血液検査。',
             'CA19-9': '消化器がんの腫瘍マーカーとして広く用いられている。特にすい臓がんの診断に役立つ。基準値　37U/ml以下',
             'CEA': '腫瘍マーカーの一つ。癌細胞が増殖している組織内からつくられるタンパクの一種で、再発や転移の早期発見等、治療効果の特定に有効。基準値5.0/ｎｇ/ｍｌ',
             'U-TP（尿蛋白）': '血液中に含まれる蛋白が尿中にでてきたもの。陽性が続くようなら、ネフローゼ等の腎疾患の可能性がある。正常（-）',
             'U-Glu（尿糖）': '一定量以上の増加により、（+）以上の場合は糖尿病が疑われル。正常値（-）',
             'URO（ウロビリノーゲン）': '血液中のビリルビンという色素が腸内細菌に還元されたのもで、正常（±）強陽性（2+）以上は肝障害を疑う。',
             'RBC（尿潜血） ': '尿中に含まれる血液を検出するもの、腎臓・膀胱・尿道の炎症や結石・腫瘍・前立腺炎等で陽性となる。　正常（-）',
             'PaO2（動脈血酸素分圧）': '動脈血ガス分析を使用した動脈血酸素飽和濃度（動脈血中の酸素と結合しているヘモグロビンの割合のこと）を測定した値。',
             'SaO2・SAT（サチュレーション）': '指先などにクリップのように挟むパルスオキシメーターを使用して、動脈血中の酸素と結合しているヘモグロビンの割合を測定した値。',
             'in,out（水分出納）': 'INは点滴・薬・飲水・食事量等体内に入るもの　OUTは出血量・尿量・汗等の対外に排泄されるもの。',
             'BMI（ボディマス指数）': '肥満度を表す指標。ふつう（BMI:18.5以上25未満）　肥満（BMI:30以上）やせ（BM：18.5未満）　計算式BMI＝体重Kｇ÷（身長ｍ）2　　適性体重＝（身長m）2×22',
             'BMD（骨密度）': 'カルシウムやマグネシウムなどのミネラルの量が骨にどれくらい含まれているか想定する検査。正常80%以上。',

             'xxxxxxxx': 'yyy',
             'apple': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'xxx': 'yyy',
             'VS・TPR　（バイタルサイン）': '生命の徴候。脈拍・心拍・呼吸・体温・血圧・意識などが含まれる。適切な治療や看護法を決定して実施する上で需要な基礎データーとなる。',
             'BT・KT　（体温）': '体内の生化学反応によって発生する熱と体外へ放出される熱との関係で決まる体の温度。正常（成人）は腋下体温で36～37℃',
             'BP　（血圧）': '心臓から送り出された血液が血管の中を通る時、血管にかかる圧力のこと。正常値（成人）最高血圧130ｍｍHg未満、最低血圧85ｍｍHg',
             'R（呼吸）': '息を吸ったり吐いたりすること。正常呼吸（成人）1分間12～20回',
             'P　　（脈拍）': '心臓が規則的に収縮して血液が押し出されるたびに体表近くを走る動脈に伝わる周期的な拍動。正常呼吸（成人）1分間60～90程度。',
             'HR　（心拍数）': '心臓が血液を送り出すために収集する回数のこと。通常1分間の回数をいう。正常値60～90',
             '意識': '頭がはっきりしていて、自分自身や外界のことがわかっている状態。',
             '意識清明　（レベルクリア）': '意識障がいがない状態。',
             '意識混濁': '意識の清明度の低下で、注意・記銘・見当識が障がいされた状態。意識障害の病像の一つ。',
             '明識困難': '注意が散漫となり、自発性がなくなて了解がやや悪い。',
             '傾眠': '周囲からの刺激があれば覚醒するが、すぐうとうとして、意識が混濁する状態。',
             '嗜眠 ': 'はっきりとさめないが、強い刺激に反応する。会話はできない状態。',
             '昏睡　（コーマ）': '　刺激には全く反応せず、瞳孔反射や腱反射も消失した状態。',
             '痙攣': '　ひきつけのように、一時的または急な脳の過剰興奮によって起こる不随意的な発作性運動現象。',
             '見当識障がい ': '場所・時間・おかれた状況等がわからなくなること。',
             '高次脳機能障害': '失行・失語・失認・半側空間無視等、学習や記憶、言語活動のように情報の蓄積と分析、統御に基づいた行動に関する大脳の機能障がい。',
             '失行': '　失調、不随意運動、筋緊張異常などの運動障がいや感覚障がいがなく、行うべき動作または行為を十分了解しているのにできない状態。',
             '失語 ': '　聴覚障がいや運動障がい、および一般的な知能・精神障がいがないのに、脳の病巣により、言語の理解や表出が障がいされたもの。',
             '失認': '以前から熟知しているはずの物や人を認識する能力が、全面的あるいは部分的に喪失してしまうこと。',
             '半側空間無視': '損傷した大脳の部位と反対側の刺激に反応せず、注視した空間の半側に注意を向けたりできない認識障がいの症状。',
             '遂行機能障害': '高次脳機能障がいの一つ。自発的に物事を始めることができない。',
             '瞳孔不同　（アニソコリー）': '病気等により、左右の瞳孔の大きさが異なる状態。正常な人にみられることもある。',
             '半盲 ': '視野の半分が水平または垂直方向に欠けて見えなくなる状態。',
             '血管攣縮　（スパズム） ': '血管の緊張が亢進して、痙攣性の収縮が起こり、臓器や組織の血流が低下し虚血症状を起こす。',
             '血液　（ブラッド）': '全身の組織や臓器の中に網の目のように張り巡らされている血管の中を流れる赤い液体。',
             '血塊　（コアグラ）': '血液が固まったもの。',
             '潜血': '尿や便に微量の血液が混じっている状態のこと',
             '溶血': '赤血球の膜が破れて、中のヘモグロビンが流出する現象。',
             'IVH（中心静脈栄養）': '高カロリー輸液とも呼ばれ、高濃度の栄養輸液を中心静脈から投与することで栄養状態の改善を図る。',
             'TPN（中心静脈栄養）': 'TPN（中心静脈栄養）',
             'PPN（末梢静脈栄養）': '腕などの末梢の血管から栄養輸液を点滴する方法。食べられない期間が比較的短い方に選択される。',
             '腹水': '腹膜の炎症や肝臓・心臓・腎臓の疾患などにより腹腔内にたまった液体。',
             '筋性防御　（デフェンス）': '腹腔内になんらかの急性炎症が起こると、反射的にその部分の腹壁が固くなること。',
             'グル音': '消化している時に、腸が動いて発生する音。',
             '吐血': '食道・胃・十二指腸などから出血した時に、その血液を吐くこと。',
             '下血': '　疾患により消化管内に出た血液が肛門から出ること。',
             '血便 ': '血液の混じった大便。',
             'Actinobacillus': 'грамотрицательные неподвижные овальные или палочковидные клетки. Паразиты и комменсалы человека, млекопитающих и птиц. Основные поражения у человека вызывает A. actinimycetemcomitans, входящая в состав нормальной микрофлоры ротовой полости. Инфекции, вызываемые актинобациллами, носят эндогенный характер. Так как подавляющее большинство инфекций реализуется в ассоциации с A. israelii, то и их проявления идентичны таковым при актиномикозах. Также зарегистрированы раневые инфекции, менингиты, остеомиелиты, эндокардиты (особенно при наличии протезов клапанов), а также поражения мочеполовой системы',
             'Actinomyces': 'род неподвижных споронеобразующих анаэробных или факультативно-анаэробных бактерий (семейство Actinomycetaceae), включающий грамположительные палочки неправильной формы, часто образующие нити. Характерно наличие серных гранул, образующихся при истинном ветвлении при формировании колоний мицелиального типа. Патогенны для человека и/или животных. Типовой вид — A. bovis',
             'Aspergillus': 'род грибов-аскомицетов (леечная плесень), включает множество видов. A. fumigatus — возбудитель аспергиллёза',
             'Blastomyces': 'род паразитических грибов из класса несовершенных грибов; некоторые виды вызывают бластомикозы человека',
             'Borrelia': 'род спирохет, передающихся млекопитающим с укусами членистоногих; B. burgdorferi вызывает болезнь Лайма (хроническую трансмиссивную природно-очаговую инфекцию из группы иксодовых клещевых боррелиозов)',
             'Brucella': 'род капсулированных неподвижных бактерий семейства Brucellaceae. Представлены мелкими, грамотрицательными, палочковидными или кокковидными клетками. Патогенны для человека и домашних животных, проникают в ткани; типовой вид — B. melitensis; вызывают бруцеллёз, который у животных проявляется инфекционными абортами, у человека — длительно протекающими инфекционными поражениями опорно-двигательной системы, нервной и половой систем',
             'Campylobacter': 'род подвижных грамотрицательных, спирально изогнутых бактерий. Типовой вид — C. fetus — возбудитель кишечных заболеваний и инфекционных абортов у теплокровных. C. jejuni — основной этиологический агент кампилобактериозов (диарейного синдрома и «диареи путешественников»)',
             'Candida': 'род повсеместно распространённых дрожжеподобных грибов. Типовой вид — C. albicans — входит в состав нормальной микрофлоры кишечника. При дисбактериозе способна выступать в качестве оппортунистического патогена с развитием локального или генерализованного кандидоза с системными поражениями в виде эндокардита, септицемии и менингита',
             'Chlamydia': 'род грамотрицательных кокковидных бактерий, облигатных внутриклеточных паразитов. Типовой вид — C. trachomatis — возбудитель болезней группы уретрит–трахома–лимфогранулёма. C. psittaci — возбудитель пситтакоза. C. pneumoniae выступает возбудителем респираторных инфекций',
             'Clostridium': 'род анаэробных спорообразующих подвижных грамположительных палочек. Включает ряд высокопатогенных видов, образующих экзотоксины, — C. botulinum (возбудитель ботулизма), C. tetani (возбудитель столбняка) и т.п.',
             'Coxiella': 'род фильтрующихся микроорганизмов порядка Rickettsiales, включающий мелкие короткие палочки или кокковидные грамотрицательные клетки. Типовой вид — C. burnetii — возбудитель Q-лихорадки человека (зоонозная инфекция; у человека протекает как острое лихорадочное заболевание с преимущественным поражением дыхательных путей)',
             'Enterobacter': 'род грамотрицательных условно-патогенных подвижных бактерий. Выделяют из ЖКТ. Способны вызвать диареи, токсикоинфекции, у детей — гнойничковые инфекции и сепсис. Типовой вид — E. cloacae',
             'Escherichia': 'род аэробных или факультативно-анаэробных бактерий, выделяемых из фекалий. Типовой вид — E. coli (кишечная палочка), обычный обитатель кишечника позвоночных и человека, широко распространена в природе, часто может вызывать урогенитальные инфекции и диареи (в основном у детей). Некоторые типы кишечной палочки обладают патогенными свойствами, вызывают энтерит, перитонит, цистит и другие заболевания',
             'Haemophilus': 'род аэробных и факультативно-анаэробных мелких грамотрицательных бактерий, нуждающихся в крови для роста (гемоглобинофильные бактерии). Типовой вид — H. influenzae (палочка Пфайффера) — возбудитель респираторных инфекций, гнойного конъюнктивита и менингита; ранее этот микроорганизм считали возбудителем гриппа (influenza). H. ducreyi (палочка Дюкрея) — возбудитель мягкого шанкра (шанкроида)',
             'Helicobacter pylori': 'грамотрицательная бактерия спиральной формы. Её фермент уреаза приводит к образованию аммиака, нейтрализующего кислую среду желудка. Микроорганизм высевают с поверхности слизистой оболочки желудка при пептических язвах и хронических гастритах',
             'Histoplasma capsulatum': 'диморфный гриб, почвенный сапрофит. Ингаляция спор может привести к развитию гистоплазмоза',
             'HLA-антигены (Аг главного локуса, общие Аг лейкоцитов)': 'Аг, выделенные у человека из лейкоцитов и тромбоцитов, а также клеток многих других тканей. Совместимость по HLA-Аг имеет значение при аллотрансплантации, переливании крови и т.п.',
             'Klebsiella': 'род грамотрицательных капсулированных бактерий, располагающихся одиночно либо короткими цепочками. Типовой вид — K. pneumoniae (палочка Фридлендера) — выделяют из ЖКТ теплокровных и микробных ассоциаций при различных инфекциях. Также клиническое значение имеет K. ozenae (палочка Абеля), возбудитель озены',
             'Legionella': 'род гpамотрицательных бактерий. Типовой вид — L. pneumophila — возбудитель «болезни легионеров»',
             'Leptospira': 'род аэробных бактеpий отряда Spirochaetales, включающий тонкие, плотно скрученные в спираль организмы; типовой вид L. interrogans представлен более чем 100 паразитирующими или сапрофитными серологическими вариантами',
             'livedo (мраморная кожа)': 'патологическое состояние кожи, характеризующееся синевато-фиолетовой её окраской за счёт сетчатого или древовидного рисунка сосудов при пассивной гиперемии',
             'Mycobacterium': 'род аэробных неподвижных грамположительных палочковидных бактерий семейства Mycobacteriaceae. Включает паразитические и сапрофитные виды. Типовой вид — M. tuberculosis',
             'M. avium-intracellulare': 'возбудитель пневмоний у лиц с выраженными иммунодефицитами',
             'M. leprae (палочка Хансена)': 'вид M., облигатный паразит, возбудитель проказы',
             'M. tuberculosis (палочка Коха, туберкулёзная палочка)': 'вид M. — возбудитель туберкулёза человека',
             'Mycoplasma': 'род аэробных или факультативно-анаэробных грамотрицательных, не имеющих истинной клеточной стенки, но обладающих трёхслойной клеточной мембраной бактерий семейства Mycoplasmataceae. Некоторые виды патогенны для человека. Типовой вид — M. mycoides. M. hominis — вид M., выделяемый из мочеполовых путей и прямой кишки человека',
             'Neisseria': 'род аэробных или факультативно-анаэробных грамотрицательных диплококков с выпрямленными смежными краями (семейство Neisseriaceae). Типовой вид — N. gonorrhoeae',
             'N. meningitidis (менингококк)': 'вид N., возбудитель менингококкового менингита. Серологически разделён на группы A, B, C и D по специфичности капсулярных полисахаридов',
             'Parvovirus': 'род вирусов семейcтва Parvoviridae. Типичный парвовирус — парвовирус В19, вызывающий заболевание, приводящее к апластическим кризам, хронической анемии, инфекционной эритеме, водянке плода',
             'Pityrosporum orbiculare': 'микроорганизм рода Pityrosporum (сем. Cryptococcaceae, класс несовершенных грибов), образующий круглые двухконтурные споры и короткие широкие нити мицелия; возбудитель отрубевидного лишая у человека',
             'Proteus': 'род подвижных грамотрицательных бактерий, обитающих в фекальных или разлагающихся органических массах. Типовой вид — P. vulgaris',
             'Pseudomonas': 'род подвижных грамотрицательных бактерий, распространённых в почве, пресной и морской воде. Некоторые виды патогенны для растений и животных. Типовой вид — P. aeruginosa — возбудитель синегнойной инфекции',
             'Salmonella': 'род аэробных и факультативно-анаэробных грамотрицательных бактерий семейства Enterobacteriaceae. Патогенны для людей и животных. Типовой вид — S. choleraesuis',
             'S. enteritidis (палочка Гартнера)': 'вид S., вызывающий пищевые токсикоинфекции у человека',
             'S. pneumoniae (пневмококк)': 'возбудитель долевой пневмонии, менингита, синуситов и прочих инфекций',
             'S. pyogenes': 'пиогенный β-гемолитический стрептококк, вызывающий образование гнойных поражений и септицемий',
             'S. typhimurium (палочка мышиного тифа)': 'вид S., вызывающий пищевые отравления у людей',
             'S. viridans': 'зеленящий α-гемолитический стрептококк. α-Стрептококк, образующий на -гемолиза (неполный гемолиз, затрагивающий только αα-гемолитическую активность проявляют S. pneumoniae, S. mitis, иногда S. faecalis',
             'Serratia': 'род грамотрицательных подвижных бактерий-сапрофитов. Некоторые штаммы капсулированы. Типовой вид — S. marcescens — может вызывать пищевые токсикоинфекции либо бактериемии при использовании инфицированного инструментария.',
             'Shigella': 'род неподвижных грамотрицательных палочек. Могут входить в состав микробных ассоциаций кишечника. Типовой вид — S. dysenteriae (палочка Шига–Крузе) — возбудитель дизентерии',
             'Staphylococcus': 'род грамположительных бактерий, образующих характерные гроздья. Обитают на коже, в кожных железах, на поверхности слизистых оболочек теплокровных, а также пищевых продуктах. Типовой вид — S. aureus, вызывающий фурункулёз, пиемию, остеомиелит, нагноение ран и пищевые отравления',
             'Streptococcus': 'род грамположительных бактерий семейства Streptococcaceae. Включает сферические или овоидные организмы, образующие пары или цепочки. Некоторые виды патогенны для человека. Типовой вид — S. pyogenes',
             'Yersinia': 'род грамотрицательных бактерий, паразитов животных и человека. Типовой вид — Y. pestis (чумная палочка, палочка Китазато) — возбудитель чумы. Y. enterocolitica — возбудитель иерсиниоза',
             'α-глобулины': 'фракция глобулинов сыворотки крови, состоящая из гликопротеидов и липопротеидов, обладающая наибольшей электрофоретической подвижностью (в сравнении с другими фракциями); белки, относящиеся к α-глобулинам, участвуют в транспорте липидов',
             'α-фетопротеин (сывороточные эмбриональные глобулины)': 'глобулины, синтезируемые клетками эмбриональной печени и находящиеся в крови эмбриона; в сыворотке крови взрослого человека α-фетопротеин обнаруживают при печёночно-клеточном раке печени, тератобластоме яичка и яичника и некоторых других опухолях',
             'β-глобулины': 'фракция глобулинов сыворотки крови, состоящая из гликопротеидов, липопротеидов и металлопротеидов (трансферрин, церулоплазмин), обладающая средней между фракциями α- и γ-глобулинов электрофоретической подвижностью',
             'γ-глобулины': 'фракция иммуноглобулинов плазмы крови, содержащая большинство АТ, обладающая наименьшей (по сравнению с α- и β-глобулинами) электрофоретической подвижностью',
             'аборт септический': 'аборт, осложнившийся развитием сепсиса (гематогенной диссеминацией бактерий и/или их токсинов из первичного очага)',
             'абсцесс (гнойник, нарыв)': 'полость, заполненная гноем и отграниченная от окружающих тканей и органов пиогенной мембраной',
             'паратонзиллярный а. (околоминдаликовый абсцесс, перитонзиллярный абсцесс)': 'абсцесс в околоминдаликовой клетчатке в результате предшествующего флегмонозного воспаления',
             'аденокарцинома (железистый рак)': 'злокачественная опухоль из железистого эпителия',
             'акромегалия': 'заболевание, характеризующееся прогрессирующим увеличением размеров кистей, стоп, нижней челюсти, внутренних органов вследствие избыточной секреции соматотропина передней долей гипофиза',
             'активатор тканевой плазминогена': 'одноцепочечный гликопротеин с молекулярной массой в 70 кД, синтезируемый клетками эндотелия; также продукт генной инженерии, вызывающий лизис тромбов, закупоривающих коронарные артерии (используют в терапии инфаркта миокарда)',
             'альвеолит': 'воспаление группы альвеол лёгкого без поражения дыхательных путей',
             'аллергический экзогенный а.': 'пневмокониоз, вызванный гиперчувствительностью вследствие повторного вдыхания органической пыли, спор некоторых видов грибов, некоторых ЛС (обычно расценивают как профессиональное заболевание)',
             'фиброзирующие аа.': 'общий термин для группы заболеваний, характеризующихся диффузной воспалительной инфильтрацией альвеол, обратимым интерстициальным пневмонитом, прогрессирующим до диффузного лёгочного фиброза',
             'аменорея': 'отсутствие менструаций в течение 6 мес и более',
             'аменция': 'форма расстройства сознания с бессвязностью мышления, речи, движений',
             'амилаза': 'один из группы амилолитических ферментов, расщепляющих крахмал, гликоген, родственные полисахариды, а также все α-1,4-глюканы; в клинической практике важно выявление амилазы в моче (амилазурии)',
             'амилоид': 'химически разнообразные протеиды; однородные частицы, состоящие из слоёв фибрилл; встречаются в виде патологических отложений в стенках кровеносных сосудов, оболочках и строме органов (амилоидоз); химическая природа а. зависит от конкретной болезни',
             'амилорея': 'выделение непереваренного крахмала с калом',
             'анафилаксия': 'аллергическая реакция немедленного типа, возникающая при парентеральном поступлении в организм аллергена, характеризующаяся сокращением ГМК и расширением капилляров, вызванными высвобождением фармакологически активных веществ (гистамин, брадикинин, серотонин, медленно действующее вещество а. и др.); индуцируется взаимодействием аллергена с фиксированными на тучных клетках АТ класса IgE',
             'ангина': 'воспаление горла любой природы (в том числе тонзиллит)',
             'ангиография': 'рентгенография сосудов после введения в них рентгеноконтрастного вещества',
             'ангиокардиография (вазокардиография, кардиоангиография, рентгеновазокардиография)': 'рентгенологическое исследование сердца и магистральных сосудов после введения в кровеносное русло контрастного вещества',
             'ангиопульмонография (ангиопневмография)': 'рентгенологическое исследование сосудов малого круга кровообращения после введения в них контрастного вещества',
             'ангиотензин': 'представитель семейства сосудосуживающих пептидов, образующихся из ангиотензиногена под действием ренина',
             'а. I': 'декапептид, образующийся из ангиотензиногена под действием ренина; пептидилдипептидаза (АПФ) отщепляет от а. I ещё два аминокислотных остатка, превращая его в физиологически активную форму а. II',
             'а. II': 'октапептид, образующийся из а. I; сильное сосудосуживающее средство, стимулятор синтеза альдостерона',
             'аневризма': 'локальное расширение просвета кровеносного сосуда или сердца вследствие патологических изменений их стенки или аномалий развития',
             'расслаивающая а.': 'расщепление или расслоение артериальной стенки при прохождении крови через разрыв интимы или при интерстициальном кровоизлиянии; обычно возникает в аорте, клинически характеризуясь выраженным болевым синдромом и тяжёлым состояние больных',
             'сердца а.': 'выпячивание стенки левого желудочка, соответствующее зоне перенесённого крупноочагового инфаркта миокарда и не участвующее в активном сокращении; в половине случаев при пальпации удаётся установить пульсацию участка грудной стенки в месте прилежания к ней аневризмы; на ЭКГ над центром аневризмы обнаруживают отсутствие зубца R, глубокий зубец Q, подъём сегмента ST, с обращённой выпуклостью вверх («застывшая инфарктная кривая»)',
             'анемия свинцовая': 'анемия, развивающаяся при отравлении свинцом; обусловлена гемолитическим действием свинца и угнетением синтеза гемоглобина',
             'а. серповидноклеточная': 'наследственная гемолитическая анемия, обусловленная наличием в эритроцитах патологического гемоглобина S; в условиях гипоксемии такие эритроциты приобретают серповидную форму',
             'анкилоз': 'тугоподвижность, отсутствие движений в суставе; сопровождается фиброзом либо сращением костей',
             'анорексия': 'отсутствие аппетита при наличии физиологической потребности в питании, обусловленное нарушениями деятельности пищевого центра',
             'нервная а.': 'личностное расстройство, проявляющееся чрезмерным отвращением к еде; обычно встречается у девушек, вызывает похудание, аменорею',
             'антиген карциноэмбриональный': 'гликопротеин гликокаликса эмбрионального энтодермального эпителия; не экспрессируется клетками взрослых особей, за исключением клеток некоторых опухолей (при этом Аг присутствует и в сыворотке больных)',
             'антитела моноклональные': 'АТ, продуцируемое клоном или генетически гомогенной популяцией гибридомных клеток; гибридомные клетки специально клонируются для получения клеточных линий, вырабатывающих специфические АТ',
             'антоцианидины': 'вещества, образующиеся из антоцианов (растительных пигментов) под действием ферментов или при кипячении с кислотами; используются в медицине как ЛС, уменьшающие проницаемость капилляров',
             'аортоартериит неспецифический (болезнь Такаясу, синдром Такаясу)': 'хроническое воспалительное заболевание аорты и её основных ветвей, реже ветвей лёгочной артерии с развитием стеноза или окклюзии поражённых сосудов и вторичной ишемией органов и тканей',
             'аортография': 'рентгенологическое исследование аорты и её ветвей после введения в её просвет контрастного вещества',
             'апирексия': 'отсутствие повышенной температуры тела при лихорадочном заболевании; длительность периода апирексии имеет дифференциально-диагностическое значение при некоторых заболеваниях (например, при малярии, возвратном тифе)',
             'аплазия (агенезия)': 'общее название аномалий развития, при которых отсутствует часть тела, орган или его часть, участок какой-либо ткани',
             'АПУД-система (APUD; аббревиатура от Amine Precursor Uptake, Decarboxylase)': 'совокупность эндокринных клеток, секретирующих пептидные гормоны и расположенных в различных органах; клетки системы APUD имеют общие черты: содержат амины, могут in vivo захватывать предшественники этих аминов, содержат декарбоксилазу аминокислот. В настоящее время представление об APUD-системе имеет исторический интерес',
             'артериит': 'воспаление стенки артерии',
             'артериография': 'рентгенологическое исследование артерий после введения в их просвет контрастного вещества',
             'артралгия': 'боль в одном или нескольких суставах',
             'артрит': 'воспаление сустава или некоторых его элементов',
             'псориатический а.': 'хронический артрит у больных псориазом, характеризующийся поражением дистальных межфаланговых суставов с их деформацией, деструкцией и анкилозированием',
             'ревматический а.': 'острый или подострый артрит, наблюдающийся в период острой ревматической лихорадки, характеризующийся экссудативным воспалением синовиальной оболочки и периартикулярных тканей чаще крупных и средних суставов конечностей',
             'ревматоидоподобный а.': 'общее название артритов, по клиническим проявлениям напоминающих ревматоидный артрит, но относящихся к другим нозологическим формам',
             'асистолия': 'полное прекращение деятельности всех отделов сердца или одного из них с отсутствием признаков биоэлектрической активности',
             'ассимиляция (анаболизм)': 'процесс усвоения организмом веществ, поступающих в него из окружающей среды, в результате которого эти вещества становятся составной частью биологических структур или откладываются в организме в виде запасов',
             'асфиксия (удушье)': 'патологическое состояние, обусловленное остро или подостро протекающей гипоксией и гиперкапнией и проявляющееся тяжёлыми расстройствами деятельности нервной системы, дыхания и кровообращения',
             'ателектаз': 'отсутствие газа в части или во всём лёгком вследствие недостаточности растяжения альвеол или транспорта газа из них',
             'компрессионный а.': 'поджатие лёгкого жидкостью или газом, скопившимся в плевральной полости',
             'обтурационный а.': 'спадение лёгкого вследствие закупорки бронха растущей эндобронхиальной опухолью, внешнего сдавления лимфатическим или опухолевым узлом, рубцами',
             'атония': 'расслабленность, вялость, недостаточность тонуса, напряжения',
             'аутопсия (вскрытие трупа, секция)': 'исследование тела умершего, заключающееся в последовательном извлечении и препарировании органов и тканей с выявлением имеющихся в них патологических изменений и установлением причин смерти',
             'афтоз': 'любое состояние, характеризующееся наличием афт',
             'афты': 'поверхностные язвы слизистой оболочки полости рта, часто покрытые серым или белым налётом',
             'ахалазия': 'нарушение способности расслабления гладкомышечных сфинктеров, расположенных в зоне переходных отверстий ЖКТ и мочевой системы',
             'ацидоз': 'состояние, характеризующееся абсолютным или относительным снижением щелочей в жидкостях тела по отношению к содержанию кислот; pH жидкостей тела может быть нормальным или сниженным',
             'а. метаболический (ацидоз обменный)': 'ацидоз, возникающий при нарушениях обмена веществ, сопровождающихся усиленным образованием, недостаточным окислением или связыванием нелетучих кислот -оксимасляной и пр.)β',
             'белок С-реактивный': 'β-глобулин сыворотки крови больных некоторыми воспалительными, дистрофическими и опухолевыми заболеваниями; не являясь специфическим АТ, осаждает in vitro C-углевод, присутствующий во всех типах пневмококков',
             'белок Бенс-Джонса (альбумин Бенс-Джонса)': 'высокотермостабильный б., обнаруживаемый в моче больных миеломой и, иногда, другими болезнями ретикулоэндотелиальной системы; представляет собой лёгкую цепь Ig',
             'бериллиоз': 'профессиональная болезнь, вызываемая сенсибилизирующим и токсическим действием бериллия и его соединений, характеризующаяся развитием в лёгких гранулематозного процесса и диффузного пневмосклероза',
             'бессвязность мышления (ассоциативная бессвязность, инкогерентность мышления)': 'отсутствие логической и ассоциативной последовательности мыслительного процесса с развитием спутанности представлений и понятий',
             'биливердин': 'зелёный пигмент жёлчи, образующийся при окислении билирубина',
             'билирубин': 'жёлто-красный пигмент жёлчи, продукт восстановления биливердина в печени и других органах',
             'биопсия': '(1) прижизненное взятие небольшого объёма ткани для микроскопического исследования с диагностической целью; (2) микроскопическое исследование прижизненно иссечённых или изъятых другим способом тканей и органов с диагностической целью',
             'биоптат': 'материал, полученный путём биопсии',
             'Гоше б.': 'наследственная болезнь, характеризующаяся накоплением глюкоцереброзидов в клетках РЭС (в селезёнке, печени и костном мозге); наследуется по аутосомно-доминантному типу',
             'Лайма б. (лаймский артрит, лаймоборрелиоз)': 'трансмиссивное природно-очаговое заболевание, передающееся клещами, с поражением кожи, сердца, нервной системы и суставов',
             'накопления бб. (болезни депонирования, тезаурисмозы)': 'наследственные болезни, вызванные нарушениями обмена, проявляющимися прогрессирующим отложением веществ определённого типа в клетках различных тканей, например гликогенозы, метахроматическая лейкодистрофия, фукозидоз и пр.',
             'пятая б. (инфекционная эритема)': 'острая инфекционная болезнь неясной этиологии с воздушно-капельным путём передачи; характеризуется лихорадкой и высыпанием сливающихся пятен; типична эритема на щеках и спинке носа в виде крыльев бабочки',
             'Райтера* б. (уретро-окуло-синовиальный синдром)': ' инфекционно-аллергическая болезнь, характеризующаяся сочетанием острого уретрита, конъюнктивита, а также обычно множественного артрита, поражающего в основном крупные суставы ног, а иногда и суставы позвоночника; возникает преимущественно на фоне генетической предрасположенности у лиц, переболевших неспецифическим уретритом, дизентерией или иерсиниозом',
             'Уилсона–Коновалова б. (болезнь Вестфаля–Уилсона–Коновалова, гепатоцеребральная дистрофия, гепатолентикулярная дегенерация)': 'наследственная болезнь, обусловленная нарушением обмена белков и меди, характеризующаяся поражением печени с развитием цирроза и вторичным поражением головного мозга (преимущественно дистрофическим процессом в чечевицеобразных ядрах); проявляется экстрапирамидной ригидностью, гиперкинезами, бульбарными и мозжечковыми расстройствами и изменениями психики на фоне признаков нарушения функций печени; наследуется по аутосомно-рецессивному типу',
             'Уиппла б. (липогранулематоз брыжейки, кишечная липодистрофия)': 'болезнь неясной, возможно инфекционной, этиологии, в основе которой лежит нарушение резорбции жиров с накоплением липидно-мукополисахаридных комплексов в протоплазме гистиоцитов слизистой оболочки и лимфатических узлов брыжейки тонкой кишки, образованием липогранулём и блокадой лимфооттока: проявляется стеатореей, похуданием, анемией',
             'Хиршспрунга б. (врождённый аганглиоз толстой кишки)': 'врождённое вздутие и гипертрофия стенки толстой кишки, вызванное отсутствием (аганглиоз) или значительным уменьшением (гипоганглиоз) количества ганглиозных нейронов в нервных сплетениях прямой кишки и вышележащих отделах толстой кишки. Дефекты онкогена RET (хромосома 10q11.2) в ряде случаев приводят к развитию этой б.',
             'брадикинин': 'нонапептид, получаемый из декапептида (каллидина II, брадикининогена), который, в свою очередь, синтезируется из α2-глобулина под действием калликреина; присутствует в крови в неактивной форме; по действию аналогичен трипсину; один из кининов плазмы — потенциальный вазодилататор; один из физиологических медиаторов анафилаксии, высвобождается из тучных клеток, покрытых цитофильными АТ при взаимодействии последних со специфичным Аг (аллергеном)',
             'брадипноэ': 'редкое дыхание (с частотой 12 дыхательных актов в минуту и менее)',
             'бронхография': 'рентгенографическое исследование бронхиального дерева после введения в его просвет контрастного вещества',
             'бронхоскопия (трахеобронхоскопия)': 'исследование нижних дыхательных путей, основанное на осмотре внутренней поверхности трахеи и бронхов с помощью бронхоскопа; при трахеобронхоскопии производят также удаление инородных тел и бронхиального секрета, биопсию или удаление новообразований, местное воздействие ЛС и т.п.',
             'бруцеллёз (средиземноморская лихорадка)': 'инфекционная болезнь из группы бактериальных зоонозов, вызываемая микроорганизмами рода Brucella, передающаяся от больных животных человеку алиментарным или контактным путём; обычно протекает по типу хрониосепсиса с полиморфной клинической картиной, рецидивами и обострениями',
             'бурсит': 'воспаление синовиальной сумки, сопровождающееся скоплением в её полости экссудата',
             'вагинит (кольпит, эндокольпит)': 'воспаление слизистой оболочки влагалища',
             'ваготомия': 'хирургическая операция пересечения блуждающего нерва или его отдельных ветвей; применяется для лечения язвенной болезни',
             'вальвулопластика': 'общее название хирургических операций, направленных на восстановление функции какого-либо клапана сердца при его недостаточности',
             'варикоцеле': 'расширение и удлинение вен семенного канатика, сопровождающееся болью и чувством тяжести в области яичка',
             'васкулит (ангиит)': 'воспаление стенок кровеносных сосудов',
             'токсигенный в.': 'васкулит, возникающий в связи с воздействием токсичных веществ и некоторых ЛС вследствие их повреждающего действия на ткани или токсико-аллергических реакций',
             'велоэргометрия': 'метод функционального исследования с применением дозированной физической нагрузки, заключающейся во вращении ногами или руками педалей велоэргометра; применяют для выявления латентной коронарной недостаточности, для определения показателей ФВД и т.п.',
             'Эпстайна–Барр в. (вирус инфекционного мононуклеоза)': 'вирус из семейства герпесвирусов, являющийся возбудителем инфекционного мононуклеоза человека; существует предположение об этиологической связи вируса Эпстайна–Барр с лимфомой Беркитта',
             'водянка': 'скопление транссудата в какой-либо полости тела',
             'волчанка красная': 'болезнь из группы коллагенозов, характеризующаяся поражением суставов, серозных оболочек, кожи, внутренних органов, ЦНС, в патогенезе которой определяющую роль играет образование аутоантител, в том числе к ДНК; выделяют форму в.к. с преимущественным поражением кожи, доброкачественным течением (дискоидная в.к.) и генерализованную форму (системная в.к.), рассматриваемые как отдельные нозологические единицы',
             'воспаление рожистое (рожа)': 'cпецифическое острое воспалительное заболевание, обусловленное гемолитическими стрептококками; характеризуется быстро возникающими поражениями кожи, сопровождается тяжёлой общей симптоматикой',
             'герпеса в.': 'род вирусов; вирионы диаметром 100–150 нм, состоят из нуклеокапсида и липопротеиновой оболочки, геном представлен двунитчатой ДНК; включает вирус простого герпеса и близкородственные вирусы, патогенные для человека и животных',
             }
    dictionary1 = dict([[v, k] for v, k in words.items()])
    dictionary2 = dict([[v, k] for k, v in words.items()])
    dictionary = {**dictionary1, **dictionary2}
    word = request.GET.get('imi')
    dictionary3 = PyDictionary()
    if word == '':
        return render(request, 'dictionary/imi.html')
    elif word == ' ':
        return render(request, 'dictionary/imi.html')
    elif word is not None:
        search_word = word.lower()
        word_view = word.title()
        if search_word in dictionary:
            meaning = dictionary.get(search_word)
            meaning_view = meaning.title()
            context = {
                'word': word_view,
                'meaning': meaning_view
            }
            return render(request, 'dictionary/imi_kekka.html', context)
        elif search_word.title() in dictionary:
            meaning_title = dictionary.get(search_word.title())
            meaning_view = meaning_title.title()
            context_title = {
                'word': word_view,
                'meaning': meaning_view
            }
            return render(request, 'dictionary/imi_kekka.html', context_title)
        elif search_word.upper() in dictionary:
            meaning_upper = dictionary.get(search_word.upper())
            meaning_view = meaning_upper.title()
            context_upper = {
                'word': word_view,
                'meaning': meaning_view
            }
            return render(request, 'dictionary/imi_kekka.html', context_upper)
        elif len(get_close_matches(search_word, dictionary.keys())) > 0:
            meaning_close = dictionary[get_close_matches(word, dictionary.keys())[0]]
            meaning_close_title = meaning_close.title()
            word_view1 = get_close_matches(word, dictionary)
            word_view2 = "".join(word_view1)
            word_view = word_view2.title()
            close_setsu1 = gettext("close_setsu1")
            close_setsu2 = gettext("close_setsu2")
            close_setsu3 = gettext("close_setsu3")
            close_setsu_quotes1 = gettext("close_setsu_quotes1")
            close_setsu_quotes2 = gettext("close_setsu_quotes2")
            context_close = {
                'word': word_view,
                'meaning': meaning_close_title,
                'not_found_word': word,
                'close_setsu1': close_setsu1,
                'close_setsu2': close_setsu2,
                'close_setsu3': close_setsu3,
                'close_setsu_quotes1': close_setsu_quotes1,
                'close_setsu_quotes2': close_setsu_quotes2
            }
            return render(request, 'dictionary/imi_kekka.html', context_close)
        else:
            meaning = dictionary3.meaning(search_word)
            serialized = json.dumps(meaning)
            meaning_view1 = serialized.replace('[', '')
            meaning_view2 = meaning_view1.replace(']', '')
            meaning_view3 = meaning_view2.replace('{', '')
            meaning_view4 = meaning_view3.replace('}', '')
            meaning_view5 = meaning_view4.replace('"', '')
            meaning_view6 = meaning_view5.replace(', Noun: ', '. Noun: ')
            meaning_view7 = meaning_view6.replace(', Adjective: ', '. Adjective: ')
            meaning_view8 = meaning_view7.replace(', Pronoun: ', '. Pronoun: ')
            meaning_view9 = meaning_view8.replace(', Adverb: ', '. Adverb: ')
            meaning_view10 = meaning_view9.replace(', Numerals: ', '. Numerals: ')
            meaning_view = meaning_view10.replace(', Verb: ', '. Verb: ')
            context_pydictionary = {
                'word': word_view,
                'meaning': meaning_view,
            }
            return render(request, 'dictionary/imi_kekka.html', context_pydictionary)
