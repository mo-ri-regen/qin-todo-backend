# qin-memo-backend

## 使用技術

- [Django](https://www.djangoproject.com/)


## セットアップ
作成予定


### Mocking
作成予定

## 開発する

## Git ブランチルール

`main`

- マージされると本番に自動反映されます。

`develop`

- 本番反映前に確認するための環境（ステージング環境）。
- 常駐しているブランチで、feature からの変更を受け付け、main にマージする。

`hotfix`

- 本番で発生した緊急のバグに対処するためのブランチ。
- 必ず main から分岐し、main と develop にマージする。

`feature/あなたのGitHub名-*`

- 開発にはここを用いる。
- 必ず develop から分岐し、develop にマージする。
- 「あなたの GitHub 名」にはアカウント名を入力。
- `*` は開発するものを簡易的に記入。
- 例: feature/lightsound-add-about-page

`main`, `develop`, `hotfix` に直接 push してはいけません。基本的に皆さんが触って良いのは `feature/あなたのGitHub名_*` ブランチだけです。

## Git コミットルール

Conventional Commits に従う。

- fix: コードベースのバグにパッチを当てる場合（セマンティックバージョン管理における PATCH に相当)
- feat: コードベースに新しい機能を追加した場合(セマンティックバージョン管理における MINOR に相当)
- BREAKING CHANGE: 本文または脚注に BREAKING CHANGE:が存在する、または型、範囲の直後に!が追加されているコミットは、API の破壊的変更を意味します。(セマンティックバージョン管理における MAJOR に相当) BREAKING CHANGE はあらゆる型のコミットに含めることができます。
- docs: ドキュメントの生成や修正を行う場合
- refactor: ロジックの変化は行わず、内部構造を整理のみを行う場合
- test: テストの追加、及び修正を行う場合
- ci: CIツールのファイルの変更を行う場合
