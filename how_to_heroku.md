# Heroku CLI のダウンロード

https://devcenter.heroku.com/ja/articles/getting-started-with-python#-2

インストールしたら、コマンドシェルで heroku​ コマンドを使用できます。

heroku login​ コマンドを使って Heroku CLI にログインします。

# アプリケーションを準備する
gunicornはインストールしておくこと。

使用する Python バージョンを指定する runtime.txt、および Python の依存関係マネージャである Pip が使用する requirements.txt​
及びHerokuのプラットフォーム上にあるWebアプリがどのようなコマンドで実行されるのかを記述するファイルであるProcfileを準備する。

- runtime.txtに書く 情報 <br>
`python-3.9.12`
- requirements.txtに書く情報<br>
`docker-compose exec qin-todo poetry export -f requirements.txt -o requirements.txt`
のコマンドを使って、docker-composeで動いているpoetryからrequirements.txtを出力する。
- procfileに書く情報<br>
`web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker api.main:app --log-file -` <br>
最後に--log-file - と記述すれば，HerokuのログでWSGIの挙動のログが出力される。(なくてもOK!!)

- heroku CLIを使ってアップロード
$ heroku login

$ cd my-project/
$ git init
$ heroku git:remote -a myapp

$ git add .
$ git commit -am "make it better"

ローカルリポジトリの非 main​ ブランチ (testbranch​ など) から Heroku にコードをデプロイするには、次の構文を使用して、リモートの main​ ブランチにプッシュされるようにします。
`git push heroku testbranch:main`

