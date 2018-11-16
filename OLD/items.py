
def create_base_item(name, desc, cost, count=1, max_stack=100, resell=None):
    if resell is None:
        resell = int(cost/2)
    item = {}
    item["item_type"] = "basic"
    item["desc"] = desc
    item["name"] = name
    item["cost"] = cost
    item["resell"] = resell
    item["count"] = count
    item["max_stack"] = max_stack

    return item


def create_weapon(class_for, name, desc, cost, level, stats, count=1, max_stack=100, resell=None):
    if resell is None:
        resell = int(cost/2)

    weapon = create_base_item(name, desc, cost, count, max_stack, resell)
    weapon["item_type"] = "weapon"
    weapon["class_for"] = class_for
    weapon["level"] = level
    weapon["stats"] = stats

    return weapon


def create_boost(name, desc, cost, boosted_stat, val, count=1, max_stack=100, resell=None):
    if resell is None:
        resell = int(cost/2)
    
    potion = create_base_item(name, desc, cost, count, max_stack, resell)
    potion["item_type"] = "potion"
    potion["boosted_stat"] = boosted_stat
    potion["boost"] = val

    return potion

