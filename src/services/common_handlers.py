"""Contains common handlers classes."""
import random
from typing import Any

from services.data_getters import crm_data
from services.image_handlers import product_image_handler


class CommonHandlers:
    """Contains common handlers."""

    @staticmethod
    async def get_first_three_additional_products(
        region_slug: str, region_products: list[dict[str, Any]]
    ) -> list:
        """
        Get first three additional products from random subcategory 'Present' category.

        WARNING: There is hardcoded name of the "Presents" module in the ZohoCRM.

        :param region_slug: str
        """
        filtered_subcategories_slugs = [
            subcategory["slug"]
            for subcategory in await crm_data.get_subcategories_list()
            if subcategory["category_name"] == "Подарки"
        ]

        filtered_additional_products = [
            product
            for product in region_products
            if product["region_slug"] == region_slug
            and product["subcategory_slug"] in filtered_subcategories_slugs
        ]
        if len(filtered_additional_products) >= 3:
            additional_products = random.sample(
                filtered_additional_products,
                3,
            )
        else:
            additional_products = filtered_additional_products
        return await product_image_handler.embed_products_image(additional_products)


common_handlers = CommonHandlers()
