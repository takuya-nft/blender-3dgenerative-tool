import bpy 
import json
import random

# 生成したいキャラクターの数を指定します。（少し多めに設定してください。）
TOTAL_CHARACTERS = 120

# outputフォルダを指定しています。パスを正しく設定してください。
OUTPUTS_DIR = "/{your_path}/nft-collectibles/outputs/"

# パーツのリストです。(すべてのファイル名(コレクション名)が以下のリストに含まれるようにしてください。)
list_background_color = [ # 背景リスト
    "white",
    "blue",
    "green",
    "light_blue",
    "light_green",
    "orange",
    "pink",
    "purple",
    "red",
    "yellow"
]
list_background_color_weight = [ # 背景のうち、多めに生成するもの、少なめに生成するものを重み付けしています。
    10, 7, 7, 7, 7, 7, 7, 7, 7, 7
]
list_body = [ # 体リスト
    "white_monkey",
    "green_monkey",
    "blue_monkey",
    "red_monkey"
]
list_body_weight = [ # 体のうち、多めに生成するもの、少なめに生成するものを重み付けしています。
    10, 8, 6, 4
]

# TODO 追加する場合はコピペで増やしてください。
# list_XXX = [
#    "XXX"
# ]
# list_XXX_weight = [
#    1
#]


class random_list:
    random_background_color_list = []
    random_body_list = []


def generate_random_list():
    # 重み付けで生成したリストを作成しています。
    random_list.random_background_color_list = random.choices(list_background_color, k=120, weights = list_background_color_weight)
    random_list.random_body_list = random.choices(list_body, k=120, weights = list_body_weight)

    # TODO 追加する場合はコピペで増やしてください。
    # random_list.random_XXX_list = random.choices(list_XXX, k=120, weights = list_XXX_weight)
    
def random_attributes(i):    
    # アンダーバーをスペースに変換し、頭文字を大文字にします。 (e.g. "head_rabbit" -> "Head Rabbit")
    random_background_color = random_list.random_background_color_list[i].replace("_", " ").title()
    random_body = random_list.random_body_list[i].replace("_", " ").title()
    
    # TODO 追加する場合はコピペで増やしてください。
    # random_XXX = random_list.random_XXX_list[i].replace("_", " ").title()

    # attributes(Propaties)を生成します。
    attributes = [
        {
            "trait_type": "Body", # この名称がそのままPropatiesの名称となります。パーツのフォルダ名(コレクション名)の_をスペースに変換、頭文字を大文字にした文字列で指定してください。
            "value": random_body
        },
        {
            "trait_type": "Background Color",
            "value": random_background_color
        }
        # TODO 追加する場合はコピペで増やしてください。
        #,{
        #    "trait_type": "XXX",
        #    "value": random_XXX # 上記で作成したrandom_XXXを指定してください。(例: random_body)
        #}        
    ]

    return attributes


def main():
    print("Start generating metadata...")

    # 一時的な重み付けされたリストを格納します。
    dict_list = []
    
    # 一時的な重み付けされたリストを生成します。
    generate_random_list()

    # ループして希望するキャラクター数を生成します。
    for i in range(TOTAL_CHARACTERS):
        attributes = random_attributes(i)
        d = { "attributes": attributes }
        dict_list.append(d)

    # 重複を排除します。
    unique_list = list(map(json.loads, set(map(json.dumps, dict_list))))
    # 重複が見つかった場合は、処理を停止します。希望以下のキャラクター数の場合は再実行するかパーツを増やしてください。
    
    if len(unique_list) <= TOTAL_CHARACTERS:
        # JSONファイルをoutputフォルダに保存します。
        for i, attr_dict in enumerate(unique_list):
            # JSONを生成します。
            obj = {
                "name": "SAMPLE #" + str(i), # NFTコレクションの名前を指定してください。
                "description": "", # NFTコレクションの説明を記載してください。
                "image": "https://example.com/"+ str(i) + ".png", # 将来的に画像データを保存したリンクになります。 後日修正するで良いと思います。
                "external_url": "https://example2.com/", # ホームページなどのリンクを指定してください。
                "attributes": attr_dict["attributes"] # ランダムに生成されたPropatiesが配置されます。
            }
            with open(OUTPUTS_DIR + str(i) + ".json", 'w') as outjson:
                json.dump(obj, outjson, indent=4)

            print("Generated metadata id: {}\n".format(i))

main()