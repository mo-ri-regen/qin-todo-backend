# qin-memo-backend

## 使用技術

- Python(フレームワークは FastAPI)
- postgresql
- Heroku(デプロイ先)
- Docker ver 20.10.10
  - ローカルでのテスト時は Docker Compose ver 1.29.2 を使用
- gitmoji

## セットアップ

### Docker イメージの作成

docker-compose.yml があるディレクトリで下記コマンドを実行します。
すると、Docker Image が作成されます。

```bash
docker-compose build
```

### FastAPI のインストール

依存パッケージをインストールします

```bash
docker-compose run --entrypoint "poetry install" qin-todo
```

新しい Python パッケージを追加した場合は下記コマンドで再ビルドをします

```bash
docker-compose build --no-cache
```

### パッケージのインストール

alembic をインストールする

```bash
docker-compose run --entrypoint "poetry add asyncpg alembic python-dotenv" qin-todo
```

pip コマンドによるパッケージのインストールは requirements.txt に記載する

### マイグレーション

```bash
docker-compose exec qin-todo poetry run python -m api.migrate_db
```

### 実行

- 初回

```bash
docker-compose up
```

- 2 回目実行

```bash
docker-compose up --remove-orphans
```

するとサーバが立ち上がるので

http://localhost:8000/docs にアクセスしてください

サーバが立ち上がった状態で別ウィンドウでターミナルを起動してください

#### Postgresql

##### Docker コンテナにログイン

```bash
docker-compose exec postqresql /bin/bash
```

```bash
# ログインに成功したとき下記のようになります
root@dc7f998a87fd:/#
```

#### DB に接続

root ユーザを指定して DB に接続します

```bash
psql -U root postgres
```

```bash
# ログインに成功したら下記のようになります
postgres=#
```

##### Postgresql コマンド

- ユーザーを指定してデータベースに入る

```bash
# psql -U <USER_NAME> <DB_NAME>
psql -U root postgres
```

- データベースから出る

```bash
# \q
```

### 終了

```bash
docker-compose down
```

### Mocking

作成予定

## 開発について

### Git ブランチルール

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
- ci: CI ツールのファイルの変更を行う場合

## その他

- [デザイン](https://www.figma.com/file/SNPCXNu0V6k6wHS4piYyS2/Qin-Todo?node-id=0%3A1)
- [フロントエンドリポジトリ](https://github.com/mo-ri-regen/qin-todo-frontend)
- [使用相談(プライベートリポジトリ)](https://github.com/qin-salon/qin-todo-backend/issues/1)

### サンプルソース

- [fastapi サンプルソース](https://github.com/takasaki376/fast-task-docker)
- [Django で作成したサンプルソース](https://github.com/gotoh-poclab/docker-django-api)

### 参考

- [FastAPI 入門](https://zenn.dev/sh0nk/books/537bb028709ab9)
- [PostgreSQL の命名規則](https://dev.appswingby.com/sql/postgresql%E3%81%AE%E5%91%BD%E5%90%8D%E8%A6%8F%E5%89%87/)
- [PostgreSQL](よく使うコマンドまとめ)
