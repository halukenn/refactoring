## リファクタリング前
- サンプルプログラムは「ユーザー名とメールアドレスの組みをファイルに保存する」という簡単なアプリケーションです。
- AddressFileクラスはDatabaseクラスを用いてユーザ名とメールアドレスの組をファイルに保存するクラスです。
- _databaseフィールドは、Databaseクラスのインスタンスを保持します。このフィールドはコンストラクタで初期化されます。
- getDatabaseメソッドは、_databaseフィールドに対するgetterメソッドです。このメソッドがあるために、クライアントクラス（Mainクラス）は、AddressFileクラスの移譲先であるDatabaseクラスに直接アクセスできることになります。このメソッドは1回目のリファクタリングで削除されます。
- namesメソッドは、ユーザ名の一覧をEnumerationとして取り出すためのメソッドです。このメソッドは、2回目のリファクタリングで書き換えます。