#!/bin/bash

# エラーが発生したら即座に終了
set -e

echo "🚀 PyPIパッケージの更新プロセスを開始します..."

# 1. プッシュ
echo "💾 変更をプッシュします..."
git push

# 2. テスト実行
echo "🧪 テストを実行します..."
python -m pytest tests/
python test.py

# 3. ビルド前のクリーンアップ
echo "🧹 古いビルドファイルを削除します..."
rm -rf dist/* kabu_json_lib.egg-info/*
rm -rf __pycache__ kabu_json_lib/__pycache__ tests/__pycache__

# 4. ビルド
echo "🏗️ パッケージをビルドします..."
python -m build

# 5. CIチェック
echo "🔄 CIチェックを待機します..."
while true; do
    status=$(gh run list --repo umihico/kabu-json-lib --json status,name --jq '.[0].status')
    if [ "$status" = "completed" ]; then
        conclusion=$(gh run list --repo umihico/kabu-json-lib --json status,conclusion,name --jq '.[0].conclusion')
        if [ "$conclusion" = "success" ]; then
            echo "✅ CIチェックが成功しました"
            break
        else
            echo "❌ CIチェックが失敗しました: $conclusion"
            exit 1
        fi
    fi
    echo "⏳ CIチェックを待機中... 現在のステータス: $status"
    sleep 30
done

# 6. PyPIアップロード
echo "📤 PyPIにアップロードします..."
twine upload dist/*

echo "🎉 パッケージの更新が完了しました！" 
