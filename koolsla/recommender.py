#!/usr/bin/env python

from koolsla import data
from koolsla import tfidf
from koolsla import color_print


def recommend(dish_id: int, recommendation_count: int = 5):
    """Recommends similar dishes.
    Args:
      dish_id (int): Dish id which koolsla recommends similar ones.
      recommendation_count (int): Max recommendation count given by user.
    Returns:
      indice, similarity value (dictionary): Indice & similarity value or None.
    """

    is_valid = data.validate_dish_id(dish_id)
    if is_valid:
        # Import the data
        imported_data = data.import_data()
        # Get the metadatasets
        dataset = data.split_data(imported_data)
        # Train the recommendation engine
        tfidf_matrix = tfidf.train_engine(dataset['names'])
        # Generate recommendations
        recomended_dishes = tfidf.find_similarities(tfidf_matrix, dish_id, recommendation_count)
        # Input dish
        color_print.print_green('Given Dish')
        color_print.print_dish(
                    name=dataset['names'][dish_id],
                    dish_id=dish_id,
                    color=color_print.green)
        # Display the recommended dishes
        color_print.print_yellow('Top ' + str(recommendation_count) + ' Recommendations')
        for i, _ in recomended_dishes:
            color_print.print_green(i)
            color_print.print_dish(
                    name=dataset['names'][i],
                    dish_id=i,
                    color=color_print.yellow)
        return recomended_dishes
    return None
