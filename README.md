# kabu-json-lib

システムトレーディングに必要な計算や便利なPythonライブラリをまとめたパッケージです。

## バージョン
- 最新バージョン: 0.1.9
- リリース日: 2024-03-21

## 機能一覧
- bp関数: パーセント表記をベーシスポイント（bp）に変換します。
- fetch_now関数: 現在の日本時間をdatetimeオブジェクトで返します。
- order_to_one_line関数: 注文情報を1行の文字列にフォーマットします（valueはprice×quantityで自動計算されます）。
- setup_logger関数: アプリケーション全体で使用する共通のロギング設定を提供します。

## インストール方法
```bash
pip install kabu-json-lib
```

## 使い方
```python
from kabu_json_lib import bp, fetch_now, order_to_one_line, setup_logger

# ロギングの設定
logger = setup_logger('my_app')
logger.info('アプリケーション開始')
logger.warning('警告メッセージ')
logger.error('エラーメッセージ')

print(bp(0.05))  # 500
print(bp(None))  # None

now = fetch_now()
print(now)  # 2023-10-01 12:34:56+09:00

# 注文情報のフォーマット例
order = {
    "long_or_short": "LONG",
    "entry_or_exit": "ENTRY",
    "symbol": "AAPL",
    "price": 150.0,
    "quantity": 100,
    "value": 15000,
    "order_type": "MARKET",
    "datetime_obj": now
}
print(order_to_one_line(order))  # [LONG -ENTRY ] AAPL @ 150.0 *   100 (¥    15000) [MARKET] 2024-03-21 12:34:56
```

### ロギング機能の詳細
- 環境変数`LOG_LEVEL`でログレベルを設定可能（デフォルト: INFO）
- INFOレベル以下のメッセージは標準出力へ
- WARNINGレベル以上のメッセージは標準エラー出力へ
- 日本語対応のフォーマット
- 重複設定の防止機能

## リポジトリ
- GitHub: https://github.com/umihico/kabu-json-lib
- PyPI: https://pypi.org/project/kabu-json-lib/
