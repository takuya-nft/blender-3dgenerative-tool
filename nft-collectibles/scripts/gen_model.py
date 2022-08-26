import bpy
import json
import random
import shutil
from bpy import data as D

# 生成したいキャラクターの数を指定します。
TOTAL_CHARACTERS = 100

# outputフォルダを指定しています。パスを正しく設定してください。
PARTS_DIR = "/{your_path}/nft-collectibles/parts/"
OUTPUTS_DIR = "/{your_path}/nft-collectibles/outputs/"


# レンダリングの設定を行います。
def set_render_config():

    r = bpy.context.scene.render
    r.engine = "CYCLES" # EEVEEを指定することも可能です。
    r.resolution_x = 1024
    r.resolution_y = 1024
    r.film_transparent = True
    
    c = bpy.context.scene.cycles # EEVEEを指定した場合は削除してください。
    c.device = "GPU" # GPUを保持していないPCの場合は、削除してください。
    c.use_preview_denoising = True
    c.preview_samples = 1024
    c.samples = 1024
    c.adaptive_threshold = 0.1
    

    # outputするファイルフォーマットです。
    r.image_settings.file_format = 'PNG'


# append_XXXは、それぞれのコレクションからJSONに記載されたパーツをもとにファイルを取得しています。
def append_misc():
    path = PARTS_DIR + "misc/" + "misc.blend/Collection/" # コレクションを指定
    collection_name = "misc" # コレクション名
    bpy.ops.wm.append(filename=collection_name, directory=path) # レンダリングするコレクション名とパスを指定。名前とパスがずれていると取得されません。

    cam = bpy.data.objects["camera"] #カメラコンポーネントの名前をcameraにしてください。
    scene = bpy.context.scene
    scene.camera = cam

def append_background_color(trait_value):
    name = trait_value.replace(" ", "_") # ファイル名の認識のために、Propatiesのスペースを_変換し直します。
    name = name.lower() # 頭文字を小文字に変換し直します。

    path = PARTS_DIR + "background_color/" + name + ".blend/Collection/"
    bpy.ops.wm.append(filename=name, directory=path)

def append_body(trait_value):
    name = trait_value.replace(" ", "_")
    name = name.lower()

    path = PARTS_DIR + "body/" + name + ".blend/Collection/"
    bpy.ops.wm.append(filename=name, directory=path)

# TODO 追加する場合はコピペで増やしてください。
# def append_XXX(trait_value):
#    name = trait_value.replace(" ", "_")
#    name = name.lower()
#
#    path = PARTS_DIR + "XXX/" + name + ".blend/Collection/"
#    bpy.ops.wm.append(filename=name, directory=path)


# レンダリング
def render(id):
    # レンダー
    bpy.ops.render.render(write_still=1)

    # 保存
    bpy.data.images['Render Result'].save_render(filepath=OUTPUTS_DIR + id + ".png")


# 生成をしています。
def generate(id, metadata):
    for attr in metadata["attributes"]:
        # Propatiesのカテゴリ名を指定します。
        if attr["trait_type"] == "Background Color" and attr["value"] != "":
            print(attr["value"])
            append_background_color(attr["value"]) #パーツを取得する変数を指定します。
        # Body
        if attr["trait_type"] == "Body" and attr["value"] != "":
            print(attr["value"])
            append_body(attr["value"])
        # TODO 追加する場合はコピペで増やしてください。
        # if attr["trait_type"] == "XXX" and attr["value"] != "":
        #    print(attr["value"])
        #    append_XXX(attr["value"])

    render(str(id))


# 3Dアート生成後に配置したコンポーネントを削除します。メモリリークに対応すべく多くの削除を追加していますが、個別にチューニングをお願いします。
def remove():
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj)
    for col in bpy.data.collections:
        bpy.data.collections.remove(col)

    for block in bpy.data.meshes:
        if block.users == 0:
            bpy.data.meshes.remove(block)

    for block in bpy.data.materials:
        if block.users == 0:
            bpy.data.materials.remove(block)

    for block in bpy.data.textures:
        if block.users == 0:
            bpy.data.textures.remove(block)

    for block in bpy.data.images:
        if block.users == 0:
            bpy.data.images.remove(block)

    for block in D.curves:
        if block.users == 0:
            D.curves.remove(block)


def main():
    print("Start generating models...")
    set_render_config()

    # アートを生成してoutputフォルダに格納します。
    for i in range(TOTAL_CHARACTERS):

        remove()
        append_misc()

        with open(OUTPUTS_DIR + str(i) + ".json", 'r') as metaJson:
            data = json.load(metaJson)
            generate(i, data)
            print("Generated model id: {}\n".format(id))

main()