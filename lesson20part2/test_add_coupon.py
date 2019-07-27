from lesson20part2.utils.db_func import DatabaseConnector


class TestCouponPage:

    def test_add_coupon(self, dashboard_page, delay, db_info, coupon):
        host = db_info.get("host")
        port = db_info.get("port")
        user = db_info.get("username")
        password = db_info.get("password")
        db_name = db_info.get("db_name")
        db_connector = DatabaseConnector(host, port, user, password, db_name)
        db_connector.insert_coupon(coupon.get("name"), coupon.get("code"), coupon.get("type"),
                                   coupon.get("discount"), coupon.get("logged"), coupon.get("shipping"),
                                   coupon.get("total"), coupon.get("date_start"), coupon.get("date_end"),
                                   coupon.get("uses_total"), coupon.get("uses_customers"),
                                   coupon.get("status"), coupon.get("date_added"))
        marketing = dashboard_page.get_marketing_menu(delay)
        marketing.click()
        dashboard_page.click_catalog_item(marketing, "Coupons")
        my_coupon = dashboard_page.get_coupon(coupon.get("code"), delay)
        assert my_coupon
