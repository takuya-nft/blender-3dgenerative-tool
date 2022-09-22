# blender-3d-generative-tool
Blender用の3Dジェネラティブ生成スクリプトです。

[Takuya | 3D ArtistのTwitter](https://twitter.com/takuya_nft)をフォローしていただけると嬉しいです！！

# マニュアル
以下は、blender用の3Dジェネラティブ生成スクリプトのマニュアルとなります。

簡易的なので、自由に改変していただき、ご自身の要件に近づけていただければと思います。

[とりあえず動かしてみたい！！という方は、1.を実施してから、6.へ進んでください。](https://github.com/takuya-nft/blender-3dgenerative-tool#6-scriptsgen_modelpy%E3%82%92%E4%BF%AE%E6%AD%A3%E3%81%99%E3%82%8B)

## 推奨環境
blender 2.8以上

※scripting機能が利用できれば、問題ないはずです。

## フォルダ構造について
フォルダは以下の構造をしています。

```
nft-collectibles
          ∟ outputs
          ∟ parts
          ∟ scripts
```

- outputs : 生成したJSONと画像データが格納されるフォルダです。
- parts : 3Dモデルのパーツを保持するフォルダです。
- scripts : ジェネラティブ生成に利用するpythonスクリプトを保持するフォルダです。

## 1. 本githubページからフォルダをダウンロードする
ページ上段にある緑色のCodeボタンをクリックし、Download ZIPなどでフォルダをダウンロードしてください。

## 2. blenderをインストールする
すでにインストール済みの方はスキップしてください。

以下のサイトからblenderの最新版をインストールできます。

[blender](https://www.blender.org/download/)

## 3. partsフォルダ内にPropatiesフォルダを配置する
サンプルとして、３つのフォルダを配置しています。

```
parts
  ∟ background_color
  ∟ body
  ∟ misc
```

- background_color : 背景パーツを保持するフォルダ
- body : 体パーツを保持するフォルダ
- misc : 照明とカメラを保持するフォルダ

misc以外、それぞれのフォルダは、NFTのPropatiesが持つパーツのカテゴリーとなります。

以下のPropatiesに表示されているような「ACCESSORIES（BODY）」「ACCESSORIES（FACE）」というカテゴリー１つ１つをフォルダにしているイメージです。

<img width="504" alt="Propaties" src="https://user-images.githubusercontent.com/111946287/186344994-c837d93b-8b1e-4e06-92fa-d59527e6d4e4.png">

例えば「目の色」というPropertyを作成し、その中に、赤、青、黄色の目のパーツを作成する場合、「eye_color」のようなフォルダ名を配置します。


## 4. 各Propatiesフォルダにパーツを配置する
bodyフォルダの中に4点blenderのファイルを配置しています。

```
body
  ∟ blue_monkey.blend
  ∟ green_monkey.blend
  ∟ red_monkey.blend
  ∟ white_monkey.blend
```

例えば、「white_monkey.blend」を開くと、白い猿が表示されます。

また、画像の赤枠で示したコレクション名がファイルと一致しています。

**コレクション名とファイル名が一致していないと、3Dアート生成時に認識されないため、注意してください。**

<img width="1440" alt="blender" src="https://user-images.githubusercontent.com/111946287/186355088-2f130a30-d41c-4c49-99e9-29903c015e3c.png">

## 5. scripts/gen_metadata.pyを修正する
ご自身のNFTに利用する際は、コメントのTODOに沿って修正をしてください。

お試しの場合は、コメントだけ読んでみてください。

## 6. scripts/gen_model.pyを修正する
ご自身のNFTに利用する際は、コメントのTODOに沿って修正をしてください。

お試しの場合は、コメントだけ読んでみてください。

## 7. 3Dアートを生成してみる！
では、まずはJSONから生成してみましょう。

サンプルファイルが配置されているため、まずはblenderを起動します。

アイコンをクリックして起動する方法でも問題ないですが、Macユーザーの場合は、コマンドプロンプトから以下のコマンドで起動すると、ログがコマンドプロンプトに表示されます。

Windowsは試していないです、すいません。

```
/Applications/blender.app/Contents/MacOS/blender
```

### scriptingタブを開く
scriptingタブを開くと以下のような画面になります。

<img width="1440" alt="scripting" src="https://user-images.githubusercontent.com/111946287/186357009-a153d707-e633-4c07-bc3b-6ce21c209976.png">

### gen_metadata.pyを指定して実行！
「開く」からgen_metadata.pyを選択すると、ファイルが読み込まれます。

<img width="1440" alt="read file" src="https://user-images.githubusercontent.com/111946287/186388078-b8947bec-8da4-4cd9-9b5b-4df06acb0fc9.png">


あとは実行ボタン「▶︎」をクリックしてみましょう。数秒で、JSONがoutputフォルダに配置されます！

<img width="907" alt="JSON Output" src="https://user-images.githubusercontent.com/111946287/186711206-f127124d-980b-4764-9599-0bbada012122.png">

### gen_model.pyを指定して実行
フォルダアイコンを選択して、gen_metadata.pyと同じようにgen_model.pyを開きます。

実行ボタン「▶︎」をクリックすると、順番に3Dアートが生成されます。

PCスペックに大きく依存するため、気長に待ちましょう。

<img width="910" alt="3D generate" src="https://user-images.githubusercontent.com/111946287/186711568-cb2a0a8e-18d2-426a-b6c9-0ff5413a74a3.png">

# 最後に
本スクリプトは、自由にご利用可能です。

本スクリプトを通して発生した問題などに関しては、一切責任を取りませんため、ご自身の責任範囲でご利用ください。

[Takuya | 3D ArtistのTwitter](https://twitter.com/takuya_nft)をフォローしていただけると嬉しいです！！
