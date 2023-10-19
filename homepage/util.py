from .models import Purchase

def bestsell(purchases_df):
    id_counts = {}  # Initialize a dictionary to store the counts

    for purchase in purchases_df:
        for info in purchase.products.all():
            product_id = info.id
            if product_id in id_counts:
                id_counts[product_id] += 1
            else:
                id_counts[product_id] = 1
    sorted_ids = sorted(id_counts.keys(), key=lambda x: id_counts[x], reverse=True)
    return sorted_ids

