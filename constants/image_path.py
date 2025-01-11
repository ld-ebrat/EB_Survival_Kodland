import os

base_dir = os.path.dirname(os.path.abspath(__file__))

image_path_player = {
    "path": os.path.join(base_dir, "../public/assets/player","player.png"),
    "size": 35
}
image_path_hotbar = {
    "path": os.path.join(base_dir, "../public/assets/player","inventory.png"),
    "size": 48
}
image_path_nature = {
    0: {
        "path": os.path.join(base_dir,"../public/assets/elements/nature","grass.png"),
        "size": 30
    },
    1: {
        "path": os.path.join(base_dir,"../public/assets/elements/nature","dirt.png"),
        "size": 30
    },
    2: {
        "path": os.path.join(base_dir,"../public/assets/elements/nature","Tree.png"),
        "size": 50
    },
    3: {
        "path": os.path.join(base_dir,"../public/assets/elements/nature","items_nature.png"),
        "size": 30
    },
    4: {
        "path": os.path.join(base_dir,"../public/assets/elements/nature","water.png"),
        "size": 36
    }
}


image_house = {
    "path": os.path.join(base_dir, "../public/assets/elements/objects","House.png"),
    "size": 100
}

image_enmies = {
    6: {
        "path": os.path.join(base_dir, "../public/assets/enemies","Skeleton.png"),
        "size": 40
    },
    7: {
        "path": os.path.join(base_dir, "../public/assets/enemies","Slime_Green.png"),
        "size": 60
    },
    8: {
        "path": os.path.join(base_dir, "../public/assets/enemies","Slime_purple.png"),
        "size": 35
    }
}