from kabu_json_lib import bp, fetch_now, order_to_one_line
from datetime import datetime


def assert_equal(actual, expected, message):
    if actual != expected:
        raise AssertionError(f"{message}\n期待値: {expected}\n実際値: {actual}")


def test_bp():
    print("=== bp関数のテスト ===")
    assert_equal(bp(0.05), 500, "0.05の変換が不正です")
    assert_equal(bp(0.01), 100, "0.01の変換が不正です")
    assert_equal(bp(0), 0, "0の変換が不正です")
    assert_equal(bp(None), None, "Noneの変換が不正です")
    print("✅ bp関数のテスト完了")


def test_fetch_now():
    print("\n=== fetch_now関数のテスト ===")
    now = fetch_now()
    assert_equal(now.tzinfo.zone, "Asia/Tokyo", "タイムゾーンが不正です")
    print(f"現在時刻: {now}")
    print("✅ fetch_now関数のテスト完了")


def test_buy_order():
    print("\n=== 買い注文のテスト ===")
    buy_order = {
        "long_or_short": "Long",
        "entry_or_exit": "Entry",
        "symbol": "1321",
        "price": 45000,
        "quantity": 16,
        "value": "720,000",
        "order_type": "指値",
        "datetime_obj": datetime(2024, 3, 22, 10, 30, 0)
    }
    expected = "[Long -Entry] 1321 @ 45000 *    16 (¥  720,000) [指値] 2024-03-22 10:30:00"
    actual = order_to_one_line(buy_order)
    assert_equal(actual, expected, "買い注文のフォーマットが不正です")
    print("買い注文:")
    print(actual)
    print("✅ 買い注文のテスト完了")


def test_short_order():
    print("\n=== 空売り注文のテスト ===")
    short_order = {
        "long_or_short": "Short",
        "entry_or_exit": "Entry",
        "symbol": "9984",
        "price": 15000,
        "quantity": 100,
        "value": "1,500,000",
        "order_type": "成行",
        "datetime_obj": datetime(2024, 3, 22, 13, 45, 30)
    }
    expected = "[Short-Entry] 9984 @ 15000 *   100 (¥1,500,000) [成行] 2024-03-22 13:45:30"
    actual = order_to_one_line(short_order)
    assert_equal(actual, expected, "空売り注文のフォーマットが不正です")
    print("空売り注文:")
    print(actual)
    print("✅ 空売り注文のテスト完了")


def test_exit_order():
    print("\n=== 決済注文のテスト ===")
    exit_order = {
        "long_or_short": "Long",
        "entry_or_exit": "Exit",
        "symbol": "9432",
        "price": 8000,
        "quantity": 200,
        "value": "1,600,000",
        "order_type": "IOC指値",
        "datetime_obj": datetime(2024, 3, 22, 15, 0, 0)
    }
    expected = "[Long -Exit ] 9432 @  8000 *   200 (¥1,600,000) [IOC指値] 2024-03-22 15:00:00"
    actual = order_to_one_line(exit_order)
    assert_equal(actual, expected, "決済注文のフォーマットが不正です")
    print("決済注文:")
    print(actual)
    print("✅ 決済注文のテスト完了")


def main():
    test_bp()
    test_fetch_now()
    test_buy_order()
    test_short_order()
    test_exit_order()


if __name__ == "__main__":
    main()
