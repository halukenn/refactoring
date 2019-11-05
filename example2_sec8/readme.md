## リファクタリング前
- Shapクラスは、図形（直線、長方形、楕円）を表すクラスです
- TYPECODE_LINE、TYPECODE_RECTANGLE、TYPECODE_OVALフィールドは、図形のタイプコードを表す定数です
- _typecodeフィールドは、このインスタンスのタイプコードを保持します。このフィールドの値は、上記、TYPECODE_LINE、TYPECODE_RECTANGLE、TYPECODE_OVALのいずれかになります。
- _startx、_starty、_endx、_endyフィールドは、図形の範囲を表すフィールドです。
- get_nameメソッドは、_typecodeに応じて図形の名前を返します。たとえば、TYPECODE_LINEに対しては”LINE”という文字列を返します。
- drawメソッドは、図形を描画します。_typecodeに応じて図形の描画方法が変化することをif〜elif文で表現しています。
- get_nameメソッドとdrawメソッドは、タイプコードに応じて振る舞いが変わるメソッドです。リファクタリングによってこのメソッドがどう変化するかを注目してください。