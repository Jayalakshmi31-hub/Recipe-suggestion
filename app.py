from flask import Flask, render_template, request

app = Flask(__name__)

recipes = {
    "Curries": {
        "paneer butter masala": {
            "ingredients": [
                "200g paneer (cubed)",
                "2 medium tomatoes (chopped)",
                "1 medium onion (chopped)",
                "2 tbsp cream",
                "1 tsp garam masala",
                "1/2 tsp chili powder",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat 2 tbsp oil in a pan and sauté 1 chopped onion and 2 chopped tomatoes until soft.",
                "Add 1 tsp garam masala, 1/2 tsp chili powder, and cook for 2-3 minutes.",
                "Cool and blend the mixture to a smooth paste.",
                "Return the paste to the pan, add 2 tbsp cream and 200g paneer cubes.",
                "Simmer for 5-7 minutes.",
                "Serve hot with roti or rice."
            ]
        },
        "vegetable curry": {
            "ingredients": [
                "2 cups mixed vegetables (carrot, beans, peas, potato, etc.)",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "1 tsp curry powder",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat 2 tbsp oil in a pan and sauté 1 chopped onion until golden.",
                "Add 2 chopped tomatoes and cook until soft.",
                "Add 1 tsp curry powder and mix well.",
                "Add 2 cups chopped mixed vegetables and salt.",
                "Cover and cook until vegetables are tender.",
                "Serve hot."
            ]
        },
        "chicken curry": {
            "ingredients": [
                "500g chicken pieces",
                "2 medium onions (chopped)",
                "2 medium tomatoes (chopped)",
                "2 tsp curry powder",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat 2 tbsp oil in a pan and sauté 2 chopped onions until golden.",
                "Add 2 chopped tomatoes and cook until soft.",
                "Add 500g chicken pieces and 2 tsp curry powder, mix well.",
                "Cook until chicken is done, adding water if needed.",
                "Simmer for 10 minutes.",
                "Serve hot."
            ]
        },
        "fish curry": {
            "ingredients": [
                "400g fish pieces",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "1 tsp fish masala or curry powder",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat 2 tbsp oil in a pan and sauté 1 chopped onion until golden.",
                "Add 2 chopped tomatoes and cook until soft.",
                "Add 1 tsp fish masala and mix well.",
                "Add 400g fish pieces and salt.",
                "Cook until fish is done, adding water if needed.",
                "Serve hot."
            ]
        },
        "egg curry": {
            "ingredients": [
                "4 boiled eggs",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "1 tsp curry powder",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat 2 tbsp oil in a pan and sauté 1 chopped onion until golden.",
                "Add 2 chopped tomatoes and cook until soft.",
                "Add 1 tsp curry powder and mix well.",
                "Add 4 boiled eggs and salt.",
                "Cook for a few minutes.",
                "Serve hot."
            ]
        },
        "mutton curry": {
            "ingredients": [
                "500g mutton pieces",
                "2 medium onions (chopped)",
                "2 medium tomatoes (chopped)",
                "2 tsp curry powder",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat 2 tbsp oil in a pan and sauté 2 chopped onions until golden.",
                "Add 2 chopped tomatoes and cook until soft.",
                "Add 500g mutton pieces and 2 tsp curry powder, mix well.",
                "Cook until mutton is tender, adding water as needed.",
                "Simmer for 15-20 minutes.",
                "Serve hot."
            ]
        },
        "dal": {
            "ingredients": [
                "1 cup dal (lentils)",
                "3 cups water",
                "Salt to taste",
                "1/4 tsp turmeric",
                "1 tbsp oil",
                "1/2 tsp cumin seeds (for tempering)"
            ],
            "process": [
                "Wash 1 cup dal and cook with 3 cups water and 1/4 tsp turmeric until soft.",
                "Mash the dal and add salt.",
                "Heat 1 tbsp oil in a small pan, add 1/2 tsp cumin seeds for tempering.",
                "Pour tempering over dal and mix well.",
                "Serve hot."
            ]
        },
        "sambar": {
            "ingredients": [
                "1/2 cup toor dal",
                "1 lemon-sized tamarind (soaked)",
                "1 cup mixed vegetables (drumstick, carrot, etc.)",
                "2 tbsp sambar powder",
                "Salt to taste",
                "1 tbsp oil",
                "1/2 tsp mustard seeds"
            ],
            "process": [
                "Cook 1/2 cup toor dal until soft and mash it.",
                "Cook 1 cup vegetables with tamarind water and salt.",
                "Add 2 tbsp sambar powder and cooked dal, mix well.",
                "Simmer for 5-10 minutes.",
                "Heat 1 tbsp oil, add 1/2 tsp mustard seeds to splutter, pour over sambar.",
                "Serve hot."
            ]
        },
        "rasam": {
            "ingredients": [
                "2 medium tomatoes (chopped)",
                "1 lemon-sized tamarind (soaked)",
                "1 tbsp rasam powder",
                "Salt to taste",
                "1/2 tsp mustard seeds",
                "1 tbsp oil"
            ],
            "process": [
                "Boil 2 chopped tomatoes and tamarind water together.",
                "Add 1 tbsp rasam powder and salt, simmer for 5 minutes.",
                "Heat 1 tbsp oil, add 1/2 tsp mustard seeds to splutter, pour over rasam.",
                "Serve hot."
            ]
        },
        "palak paneer": {
            "ingredients": [
                "200g paneer (cubed)",
                "2 cups spinach leaves",
                "1 medium onion (chopped)",
                "1 medium tomato (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Blanch 2 cups spinach and blend to a smooth paste.",
                "Heat 1 tbsp oil, sauté 1 chopped onion and 1 chopped tomato until soft.",
                "Add 1 tsp garam masala and spinach paste, cook for 2-3 minutes.",
                "Add 200g paneer cubes and salt, simmer for 5 minutes.",
                "Serve hot."
            ]
        },
        "rajma": {
            "ingredients": [
                "1 cup kidney beans",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "1 tsp rajma masala",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Soak 1 cup kidney beans overnight and cook until soft.",
                "Heat 1 tbsp oil, sauté 1 chopped onion and 2 chopped tomatoes until soft.",
                "Add 1 tsp rajma masala and cooked beans, mix well.",
                "Simmer for 10-15 minutes.",
                "Serve hot."
            ]
        },
        "bhindi masala": {
            "ingredients": [
                "250g okra (cut into pieces)",
                "1 medium onion (chopped)",
                "1 medium tomato (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Wash and dry 250g okra, cut into pieces.",
                "Heat 2 tbsp oil, sauté okra until sliminess is gone.",
                "Add 1 chopped onion and cook until golden.",
                "Add 1 chopped tomato, 1 tsp garam masala, and salt, cook until done.",
                "Serve hot."
            ]
        },
        "gobi manchurian": {
            "ingredients": [
                "1 small cauliflower (florets)",
                "1/2 cup flour",
                "1/4 cup cornflour",
                "2 tbsp soy sauce",
                "1 tsp chili powder",
                "Salt to taste",
                "Oil for frying"
            ],
            "process": [
                "Make a batter of 1/2 cup flour, 1/4 cup cornflour, and water.",
                "Dip cauliflower florets in batter and deep fry until golden.",
                "Heat oil, add fried florets, 2 tbsp soy sauce, and 1 tsp chili powder.",
                "Toss well and cook for 2-3 minutes.",
                "Serve hot."
            ]
        },
        "mushroom masala": {
            "ingredients": [
                "200g mushrooms (sliced)",
                "1 medium onion (chopped)",
                "1 medium tomato (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Clean and slice 200g mushrooms.",
                "Heat 2 tbsp oil, sauté mushrooms until golden.",
                "Add 1 chopped onion and cook until soft.",
                "Add 1 chopped tomato, 1 tsp garam masala, and salt, cook until done.",
                "Serve hot."
            ]
        },
        "malai kofta": {
            "ingredients": [
                "100g paneer (mashed)",
                "2 medium potatoes (boiled and mashed)",
                "2 tbsp cream",
                "1 tsp garam masala",
                "2 medium tomatoes (chopped)",
                "1 medium onion (chopped)",
                "Oil for frying"
            ],
            "process": [
                "Mash 100g paneer and 2 boiled potatoes, shape into balls (kofta) and fry until golden.",
                "Heat oil, sauté 1 chopped onion and 2 chopped tomatoes until soft.",
                "Add 1 tsp garam masala and blend to a smooth paste.",
                "Return paste to pan, add 2 tbsp cream and simmer.",
                "Add fried koftas and cook for 2-3 minutes.",
                "Serve hot."
            ]
        },
        "kadai paneer": {
            "ingredients": [
                "200g paneer (cubed)",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "1 medium capsicum (chopped)",
                "1 tsp kadai masala",
                "2 tbsp oil"
            ],
            "process": [
                "Heat 2 tbsp oil, sauté 1 chopped onion, 2 chopped tomatoes, and 1 chopped capsicum until soft.",
                "Add 1 tsp kadai masala and paneer cubes, mix well.",
                "Cook for 5-7 minutes.",
                "Serve hot."
            ]
        },
        "dal makhani": {
            "ingredients": [
                "1/2 cup black lentils",
                "1/4 cup kidney beans",
                "2 tbsp cream",
                "1 tbsp butter",
                "1 tsp garam masala",
                "Salt to taste"
            ],
            "process": [
                "Soak and cook 1/2 cup black lentils and 1/4 cup kidney beans until soft.",
                "Heat 1 tbsp butter, add cooked lentils and beans.",
                "Add 1 tsp garam masala, salt, and 2 tbsp cream, simmer for 15-20 minutes.",
                "Serve hot."
            ]
        },
        "butter chicken": {
            "ingredients": [
                "500g chicken pieces",
                "2 tbsp butter",
                "2 medium tomatoes (chopped)",
                "2 tbsp cream",
                "1 tsp garam masala",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Marinate 500g chicken in 1 tsp garam masala and 2 tbsp butter for 30 minutes.",
                "Grill or pan-fry chicken until cooked.",
                "Heat 1 tbsp oil, make a sauce with 2 chopped tomatoes, 2 tbsp cream, and salt.",
                "Add cooked chicken to sauce, simmer for 10 minutes.",
                "Serve hot."
            ]
        },
        "chana masala": {
            "ingredients": [
                "1 cup chickpeas",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "2 tsp chana masala",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Soak and cook 1 cup chickpeas until soft.",
                "Heat 1 tbsp oil, sauté 1 chopped onion and 2 chopped tomatoes until soft.",
                "Add 2 tsp chana masala and cooked chickpeas, mix well.",
                "Simmer for 10 minutes.",
                "Serve hot."
            ]
        },
        "aloo matar": {
            "ingredients": [
                "2 medium potatoes (cubed)",
                "1 cup peas",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Heat 1 tbsp oil, sauté 1 chopped onion and 2 chopped tomatoes until soft.",
                "Add 1 tsp garam masala, 2 cubed potatoes, and 1 cup peas, mix well.",
                "Add salt and cook until potatoes are tender.",
                "Serve hot."
            ]
        },
        "methi malai matar": {
            "ingredients": [
                "1 cup fenugreek leaves (chopped)",
                "1 cup peas",
                "2 tbsp cream",
                "1 medium onion (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Heat 1 tbsp oil, sauté 1 chopped onion until golden.",
                "Add 1 cup fenugreek leaves and 1 cup peas, cook for 2-3 minutes.",
                "Add 2 tbsp cream, 1 tsp garam masala, and salt, simmer for 5 minutes.",
                "Serve hot."
            ]
        },
        "kofta curry": {
            "ingredients": [
                "8-10 koftas (fried)",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "1 tsp curry powder",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Fry koftas until golden and set aside.",
                "Heat 1 tbsp oil, sauté 1 chopped onion and 2 chopped tomatoes until soft.",
                "Add 1 tsp curry powder and salt, cook for 2-3 minutes.",
                "Add fried koftas, simmer for 5 minutes.",
                "Serve hot."
            ]
        },
        "egg masala": {
            "ingredients": [
                "4 boiled eggs",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Heat 1 tbsp oil, sauté 1 chopped onion and 2 chopped tomatoes until soft.",
                "Add 1 tsp garam masala and salt, mix well.",
                "Add 4 boiled eggs, cook for 2-3 minutes.",
                "Serve hot."
            ]
        },
        "tomato curry": {
            "ingredients": [
                "3 medium tomatoes (chopped)",
                "1 medium onion (chopped)",
                "1 tsp curry powder",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Heat 1 tbsp oil in a pan and sauté 1 chopped onion until golden.",
                "Add 3 chopped tomatoes and cook until soft.",
                "Add 1 tsp curry powder and salt, mix well.",
                "Cook until oil separates from the mixture.",
                "Serve hot with rice or chapathi."
            ]
        },
    },
    "Sweets": {
        "gulab jamun": {
            "ingredients": [
                "1 cup khoya",
                "1/4 cup flour",
                "2 cups sugar",
                "1/2 tsp cardamom powder",
                "Oil for frying"
            ],
            "process": [
                "Mix 1 cup khoya and 1/4 cup flour to make a soft dough.",
                "Shape into small balls.",
                "Heat oil and fry balls on low heat until golden brown.",
                "Boil 2 cups sugar with 2 cups water and 1/2 tsp cardamom powder to make syrup.",
                "Soak fried balls in warm syrup for 1 hour before serving."
            ]
        },
        "jalebi": {
            "ingredients": [
                "1 cup flour",
                "2 tbsp yogurt",
                "2 cups sugar",
                "A pinch of saffron",
                "Oil for frying"
            ],
            "process": [
                "Mix 1 cup flour and 2 tbsp yogurt with water to make a thick batter. Ferment for 6-8 hours.",
                "Pour batter into a piping bag or squeeze bottle.",
                "Heat oil and pipe spirals into hot oil. Fry until crisp.",
                "Boil 2 cups sugar with 1 cup water and a pinch of saffron to make syrup.",
                "Dip fried jalebis in hot syrup for a few seconds, then serve."
            ]
        },
        "rasgulla": {
            "ingredients": [
                "1 liter milk",
                "2 tbsp lemon juice",
                "1 cup sugar",
                "1/2 tsp cardamom powder"
            ],
            "process": [
                "Boil 1 liter milk, add 2 tbsp lemon juice to curdle.",
                "Drain and wash chenna, knead until smooth.",
                "Shape into small balls.",
                "Boil 1 cup sugar with 4 cups water, add balls and cook for 15 minutes.",
                "Add 1/2 tsp cardamom powder, cool, and serve."
            ]
        },
        "rasmalai": {
            "ingredients": [
                "1 liter milk",
                "1 cup sugar",
                "1/2 tsp cardamom powder",
                "A pinch of saffron",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Prepare rasgullas as above.",
                "Boil 1 liter milk until reduced by half, add 1/2 cup sugar, 1/2 tsp cardamom powder, and a pinch of saffron.",
                "Squeeze syrup from rasgullas and add to thickened milk.",
                "Simmer for 5 minutes, garnish with 2 tbsp chopped nuts, chill and serve."
            ]
        },
        "kheer": {
            "ingredients": [
                "1/4 cup rice",
                "1 liter milk",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Wash and soak 1/4 cup rice for 15 minutes.",
                "Boil 1 liter milk, add rice and cook on low heat until soft.",
                "Add 1/2 cup sugar and 1/2 tsp cardamom powder, simmer until thick.",
                "Add 2 tbsp chopped nuts, serve warm or chilled."
            ]
        },
        "halwa": {
            "ingredients": [
                "1 cup semolina",
                "1/4 cup ghee",
                "3/4 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Heat 1/4 cup ghee, roast 1 cup semolina until golden.",
                "Add 2 cups water, stir to avoid lumps.",
                "Add 3/4 cup sugar and 1/2 tsp cardamom powder, cook until thick.",
                "Add 2 tbsp chopped nuts, mix and serve."
            ]
        },
        "carrot halwa": {
            "ingredients": [
                "2 cups grated carrot",
                "2 cups milk",
                "1/2 cup sugar",
                "2 tbsp ghee",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Heat 2 tbsp ghee, add 2 cups grated carrot and sauté for 5 minutes.",
                "Add 2 cups milk, cook until carrot is soft and milk is absorbed.",
                "Add 1/2 cup sugar and 1/2 tsp cardamom powder, cook until dry.",
                "Add 2 tbsp chopped nuts, mix and serve."
            ]
        },
        "moong dal halwa": {
            "ingredients": [
                "1 cup moong dal",
                "1/2 cup ghee",
                "1 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Soak 1 cup moong dal for 4 hours, grind to a coarse paste.",
                "Heat 1/2 cup ghee, roast dal paste until golden and aromatic.",
                "Add 2 cups water, cook until absorbed.",
                "Add 1 cup sugar and 1/2 tsp cardamom powder, cook until ghee separates.",
                "Add 2 tbsp chopped nuts, mix and serve."
            ]
        },
        "sooji halwa": {
            "ingredients": [
                "1 cup semolina",
                "1/4 cup ghee",
                "3/4 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Heat 1/4 cup ghee, roast 1 cup semolina until golden.",
                "Add 2 cups water, stir to avoid lumps.",
                "Add 3/4 cup sugar and 1/2 tsp cardamom powder, cook until thick.",
                "Add 2 tbsp chopped nuts, mix and serve."
            ]
        },
        "malpua": {
            "ingredients": [
                "1 cup flour",
                "1 cup milk",
                "1/2 cup sugar",
                "1/2 tsp fennel seeds",
                "Oil for frying"
            ],
            "process": [
                "Mix 1 cup flour, 1 cup milk, 1/2 cup sugar, and 1/2 tsp fennel seeds to make a batter.",
                "Pour small amounts into hot oil, fry until golden.",
                "Soak in sugar syrup and serve."
            ]
        },
        "puran poli": {
            "ingredients": [
                "1 cup flour",
                "1 cup chana dal",
                "3/4 cup jaggery",
                "1/2 tsp cardamom powder",
                "2 tbsp ghee"
            ],
            "process": [
                "Make dough with 1 cup flour and water, rest for 30 minutes.",
                "Cook 1 cup chana dal until soft, drain and mash.",
                "Mix mashed dal with 3/4 cup jaggery and 1/2 tsp cardamom powder, cook until thick.",
                "Divide dough and filling, stuff and roll into discs.",
                "Cook on a griddle with 2 tbsp ghee until golden."
            ]
        },
        "modak": {
            "ingredients": [
                "1 cup rice flour",
                "1 cup grated coconut",
                "3/4 cup jaggery",
                "1/2 tsp cardamom powder"
            ],
            "process": [
                "Make dough with 1 cup rice flour and hot water.",
                "Cook 1 cup coconut and 3/4 cup jaggery until thick, add 1/2 tsp cardamom powder.",
                "Shape dough into cups, fill with coconut mixture, seal and shape modaks.",
                "Steam for 10-12 minutes."
            ]
        },
        "sheera": {
            "ingredients": [
                "1 cup semolina",
                "2 cups milk",
                "3/4 cup sugar",
                "2 tbsp ghee",
                "1/2 tsp cardamom powder"
            ],
            "process": [
                "Heat 2 tbsp ghee, roast 1 cup semolina until golden.",
                "Add 2 cups milk, cook until thick.",
                "Add 3/4 cup sugar and 1/2 tsp cardamom powder, mix well.",
                "Serve warm."
            ]
        },
        "mysore pak": {
            "ingredients": [
                "1 cup gram flour",
                "1 cup ghee",
                "2 cups sugar"
            ],
            "process": [
                "Roast 1 cup gram flour in 1 cup ghee until aromatic.",
                "Boil 2 cups sugar with 1 cup water to make syrup.",
                "Add syrup to flour mixture, cook until ghee separates.",
                "Pour into a greased tray, cool and cut into pieces."
            ]
        },
        "laddu": {
            "ingredients": [
                "1 cup gram flour",
                "1/2 cup ghee",
                "3/4 cup sugar",
                "1/2 tsp cardamom powder"
            ],
            "process": [
                "Roast 1 cup gram flour in 1/2 cup ghee until golden.",
                "Cool slightly, add 3/4 cup sugar and 1/2 tsp cardamom powder.",
                "Mix well, shape into balls."
            ]
        },
        "barfi": {
            "ingredients": [
                "2 cups milk",
                "1 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Boil 2 cups milk until thick, add 1 cup sugar and 1/2 tsp cardamom powder.",
                "Cook until mixture leaves sides of pan.",
                "Pour into a greased tray, sprinkle 2 tbsp nuts, cool and cut into pieces."
            ]
        },
        "sandesh": {
            "ingredients": [
                "1 cup paneer",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder"
            ],
            "process": [
                "Knead 1 cup paneer with 1/2 cup sugar and 1/2 tsp cardamom powder until smooth.",
                "Shape into small discs or balls and serve."
            ]
        },
        "chum chum": {
            "ingredients": [
                "1 cup paneer",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder",
                "1/4 cup grated coconut"
            ],
            "process": [
                "Prepare as sandesh, then roll shaped pieces in 1/4 cup grated coconut before serving."
            ]
        },
        "kalakand": {
            "ingredients": [
                "1 liter milk",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder"
            ],
            "process": [
                "Boil 1 liter milk, curdle with lemon juice to make chenna.",
                "Cook chenna with 1/2 cup sugar and 1/2 tsp cardamom powder until thick.",
                "Pour into a tray, cool and cut into pieces."
            ]
        },
        "peda": {
            "ingredients": [
                "1 cup khoya",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder"
            ],
            "process": [
                "Knead 1 cup khoya with 1/2 cup sugar and 1/2 tsp cardamom powder.",
                "Shape into small discs."
            ]
        },
        "shahi tukda": {
            "ingredients": [
                "4 slices bread",
                "2 cups milk",
                "1/2 cup sugar",
                "2 tbsp ghee",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Cut 4 bread slices into triangles, fry in 2 tbsp ghee until golden.",
                "Boil 2 cups milk with 1/2 cup sugar and 1/2 tsp cardamom powder until thick.",
                "Soak fried bread in milk mixture, garnish with 2 tbsp nuts and serve."
            ]
        },
        "double ka meetha": {
            "ingredients": [
                "8 slices bread",
                "4 cups milk",
                "1 cup sugar",
                "4 tbsp ghee",
                "1 tsp cardamom powder",
                "4 tbsp chopped nuts"
            ],
            "process": [
                "Fry 8 bread slices in 4 tbsp ghee until golden.",
                "Boil 4 cups milk with 1 cup sugar and 1 tsp cardamom powder until thick.",
                "Layer fried bread in a dish, pour milk mixture over, garnish with 4 tbsp nuts and serve as pudding."
            ]
        },
        "falooda": {
            "ingredients": [
                "1/2 cup vermicelli",
                "2 cups milk",
                "2 tbsp rose syrup",
                "1 tbsp basil seeds",
                "2 scoops ice cream"
            ],
            "process": [
                "Soak 1 tbsp basil seeds in water for 10 minutes.",
                "Boil 1/2 cup vermicelli until soft, drain.",
                "Layer vermicelli, basil seeds, and 2 tbsp rose syrup in a glass.",
                "Pour 2 cups chilled milk, top with ice cream and serve."
            ]
        },
        "kulfi": {
            "ingredients": [
                "2 cups milk",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Boil 2 cups milk until reduced by half.",
                "Add 1/2 cup sugar, 1/2 tsp cardamom powder, and 2 tbsp nuts.",
                "Pour into molds and freeze until set."
            ]
        },
        "ice cream": {
            "ingredients": [
                "2 cups milk",
                "1 cup cream",
                "1/2 cup sugar",
                "1 tsp vanilla or other flavor"
            ],
            "process": [
                "Mix 2 cups milk, 1 cup cream, 1/2 cup sugar, and 1 tsp flavor.",
                "Churn in an ice cream maker or freeze, stirring every 2 hours until set."
            ]
        },
        "fruit custard": {
            "ingredients": [
                "2 cups milk",
                "2 tbsp custard powder",
                "1/2 cup sugar",
                "1 cup mixed fruits (chopped)"
            ],
            "process": [
                "Mix 2 tbsp custard powder with 1/4 cup milk.",
                "Boil remaining milk, add custard mixture and 1/2 cup sugar, cook until thick.",
                "Cool, add 1 cup chopped fruits, chill and serve."
            ]
        },
        "shrikhand": {
            "ingredients": [
                "2 cups yogurt",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder",
                "A pinch of saffron",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Hang 2 cups yogurt in a muslin cloth for 4 hours to drain.",
                "Mix thick yogurt with 1/2 cup sugar, 1/2 tsp cardamom powder, and saffron.",
                "Garnish with 2 tbsp nuts and serve chilled."
            ]
        },
        "basundi": {
            "ingredients": [
                "2 cups milk",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts",
                "A pinch of saffron"
            ],
            "process": [
                "Boil 2 cups milk until thick, add 1/2 cup sugar, 1/2 tsp cardamom powder, saffron, and 2 tbsp nuts.",
                "Simmer for 10 minutes, cool and serve."
            ]
        },
        "rabri": {
            "ingredients": [
                "2 cups milk",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp chopped nuts",
                "A pinch of saffron"
            ],
            "process": [
                "Boil 2 cups milk, reduce to half.",
                "Add 1/2 cup sugar, 1/2 tsp cardamom powder, saffron, and 2 tbsp nuts.",
                "Simmer for 10 minutes, cool and serve."
            ]
        },
        "kaju katli": {
            "ingredients": [
                "1 cup cashew",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder"
            ],
            "process": [
                "Grind 1 cup cashews to a fine powder.",
                "Cook with 1/2 cup sugar and 1/2 cup water until thick.",
                "Add 1/2 tsp cardamom powder, roll out and cut into pieces."
            ]
        },
        "badam halwa": {
            "ingredients": [
                "1 cup almonds",
                "1/2 cup ghee",
                "1 cup sugar",
                "1/2 tsp cardamom powder",
                "1 cup milk"
            ],
            "process": [
                "Soak 1 cup almonds, peel and grind to a paste.",
                "Heat 1/2 cup ghee, add almond paste and cook for 5 minutes.",
                "Add 1 cup milk and 1 cup sugar, cook until thick.",
                "Add 1/2 tsp cardamom powder, stir until halwa consistency."
            ]
        },
        "anarsa": {
            "ingredients": [
                "1 cup rice flour",
                "3/4 cup jaggery",
                "2 tbsp poppy seeds",
                "2 tbsp ghee"
            ],
            "process": [
                "Mix 1 cup rice flour and 3/4 cup jaggery to make a dough.",
                "Shape into discs, coat with 2 tbsp poppy seeds.",
                "Fry in 2 tbsp ghee until golden."
            ]
        },
    },
    "Snacks": {
        "samosa": {
            "ingredients": [
                "2 cups flour",
                "3 medium potatoes (boiled, mashed)",
                "1/2 cup peas",
                "1 tsp garam masala",
                "1/2 tsp chili powder",
                "Salt to taste",
                "2 tbsp oil",
                "Oil for frying"
            ],
            "process": [
                "Make a dough with 2 cups flour, 2 tbsp oil, salt, and water. Rest 20 min.",
                "Mix mashed potatoes, peas, garam masala, chili powder, and salt for filling.",
                "Divide dough, roll into circles, cut in half, shape cones, fill, and seal.",
                "Fry in hot oil on medium heat until golden."
            ]
        },
        "khandvi": {
            "ingredients": [
                "1 cup gram flour",
                "2 cups yogurt",
                "2 cups water",
                "1/2 tsp turmeric",
                "Salt to taste",
                "1 tbsp oil",
                "1 tsp mustard seeds"
            ],
            "process": [
                "Mix gram flour, yogurt, water, turmeric, and salt to a smooth batter.",
                "Cook on low heat, stirring, until thick.",
                "Spread thin on a greased plate, cool, cut into strips, and roll.",
                "Heat oil, splutter mustard seeds, pour over rolls."
            ]
        },
        "dhokla": {
            "ingredients": [
                "1 cup gram flour",
                "1/2 cup yogurt",
                "1/2 cup water",
                "1 tsp fruit salt (Eno)",
                "1/2 tsp turmeric",
                "Salt to taste",
                "1 tbsp oil",
                "1 tsp mustard seeds"
            ],
            "process": [
                "Mix gram flour, yogurt, water, turmeric, and salt to a batter.",
                "Add fruit salt, mix gently, pour into greased pan.",
                "Steam for 15-20 min. Cool and cut.",
                "Heat oil, splutter mustard seeds, pour over dhokla."
            ]
        },
        "handvo": {
            "ingredients": [
                "1 cup rice",
                "1/2 cup mixed lentils",
                "1 cup grated vegetables (bottle gourd, carrot, etc.)",
                "1/2 cup yogurt",
                "1 tsp ginger-green chili paste",
                "Salt to taste",
                "1/2 tsp turmeric",
                "1 tsp fruit salt",
                "2 tbsp oil"
            ],
            "process": [
                "Soak rice and lentils 4 hours, grind coarsely.",
                "Mix with yogurt, ferment overnight.",
                "Add grated vegetables, ginger-chili paste, turmeric, salt, and fruit salt.",
                "Pour into greased pan, drizzle oil, bake or steam until set and golden."
            ]
        },
        "thepla": {
            "ingredients": [
                "2 cups wheat flour",
                "1 cup chopped fenugreek leaves",
                "1/2 cup yogurt",
                "1/2 tsp turmeric",
                "1/2 tsp chili powder",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Mix flour, fenugreek, yogurt, turmeric, chili powder, salt, and oil to a soft dough.",
                "Rest 10 min. Divide and roll into thin discs.",
                "Cook on a hot griddle with oil until golden spots appear."
            ]
        },
        "patra": {
            "ingredients": [
                "6 colocasia leaves",
                "1 cup gram flour",
                "2 tbsp tamarind pulp",
                "2 tbsp jaggery",
                "1/2 tsp chili powder",
                "Salt to taste",
                "1/2 tsp turmeric",
                "1 tbsp oil"
            ],
            "process": [
                "Mix gram flour, tamarind, jaggery, chili powder, turmeric, salt, and water to a paste.",
                "Spread on leaves, stack, roll tightly, steam 20 min.",
                "Cool, slice, and temper with oil and mustard seeds."
            ]
        },
        "undhiyu": {
            "ingredients": [
                "2 cups mixed vegetables (yam, potato, beans, brinjal, etc.)",
                "1/2 cup methi muthia (optional)",
                "2 tbsp undhiyu masala or mixed spices",
                "Salt to taste",
                "3 tbsp oil"
            ],
            "process": [
                "Cut vegetables, mix with spices and salt.",
                "Heat oil, add vegetables, cover and cook until tender.",
                "Add muthia, mix gently, cook 5 min, serve hot."
            ]
        },
        "dal dhokli": {
            "ingredients": [
                "1 cup wheat flour",
                "1 cup toor dal",
                "1/2 tsp turmeric",
                "1/2 tsp chili powder",
                "Salt to taste",
                "2 tbsp oil",
                "1 tsp cumin seeds"
            ],
            "process": [
                "Make dough with flour, salt, turmeric, and water. Roll and cut into diamonds.",
                "Cook dal with turmeric and salt, bring to boil.",
                "Add dough pieces, cook until soft.",
                "Heat oil, splutter cumin, pour over dal dhokli."
            ]
        },
        "khakra": {
            "ingredients": [
                "2 cups wheat flour",
                "1/2 tsp cumin seeds",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Mix flour, cumin, salt, and oil to a stiff dough.",
                "Roll into thin discs.",
                "Cook on low heat on a griddle, pressing until crisp."
            ]
        },
        "poha": {
            "ingredients": [
                "2 cups flattened rice (poha)",
                "1 medium onion (chopped)",
                "1 medium potato (cubed)",
                "1 green chili (chopped)",
                "1/2 tsp mustard seeds",
                "1/4 tsp turmeric",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Wash and drain poha.",
                "Heat oil, splutter mustard seeds, sauté onion, potato, and chili.",
                "Add turmeric and salt, cook until potato is soft.",
                "Add poha, mix gently, cook 2 min, serve hot."
            ]
        },
        "sabudana khichdi": {
            "ingredients": [
                "1 cup sago (sabudana)",
                "2 medium potatoes (cubed)",
                "1/4 cup peanuts",
                "2 green chilies (chopped)",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Soak sabudana 4-6 hours, drain.",
                "Heat oil, fry peanuts, set aside.",
                "In same oil, sauté potatoes and chilies until potatoes are soft.",
                "Add sabudana and salt, cook until translucent.",
                "Add peanuts, mix and serve."
            ]
        },
        "misal pav": {
            "ingredients": [
                "2 cups mixed sprouts",
                "1 medium onion (chopped)",
                "1 medium tomato (chopped)",
                "2 tsp misal masala or mixed spices",
                "Salt to taste",
                "2 tbsp oil",
                "4 pav buns"
            ],
            "process": [
                "Heat oil, sauté onion and tomato until soft.",
                "Add sprouts, masala, salt, and water. Simmer 10 min.",
                "Serve hot misal with pav."
            ]
        },
        "vada pav": {
            "ingredients": [
                "3 medium potatoes (boiled, mashed)",
                "1 tsp ginger-garlic paste",
                "1/2 tsp turmeric",
                "1/2 tsp chili powder",
                "Salt to taste",
                "1 cup gram flour",
                "Oil for frying",
                "4 pav buns",
                "Chutney as needed"
            ],
            "process": [
                "Mix potatoes, ginger-garlic, turmeric, chili, and salt. Shape into balls.",
                "Make batter with gram flour, salt, and water.",
                "Dip balls in batter, fry until golden.",
                "Serve in pav with chutney."
            ]
        },
        "pav bhaji": {
            "ingredients": [
                "2 cups mixed vegetables (potato, peas, carrot, etc.)",
                "1 medium onion (chopped)",
                "2 medium tomatoes (chopped)",
                "2 tbsp pav bhaji masala",
                "Salt to taste",
                "2 tbsp butter",
                "4 pav buns"
            ],
            "process": [
                "Boil and mash vegetables.",
                "Heat butter, sauté onion and tomato until soft.",
                "Add vegetables, masala, and salt. Mash and cook 5 min.",
                "Toast pav with butter, serve with bhaji."
            ]
        },
        "dabeli": {
            "ingredients": [
                "2 medium potatoes (boiled, mashed)",
                "2 tbsp dabeli masala",
                "Salt to taste",
                "2 tbsp tamarind chutney",
                "2 tbsp roasted peanuts",
                "2 tbsp pomegranate seeds",
                "4 buns"
            ],
            "process": [
                "Mix potatoes, dabeli masala, salt, and chutney.",
                "Stuff mixture in buns, top with peanuts and pomegranate.",
                "Serve."
            ]
        },
        "sev puri": {
            "ingredients": [
                "12 puris",
                "2 medium potatoes (boiled, cubed)",
                "1 small onion (chopped)",
                "2 tbsp green chutney",
                "2 tbsp tamarind chutney",
                "1/2 cup sev"
            ],
            "process": [
                "Arrange puris, top with potato, onion, chutneys, and sev.",
                "Serve immediately."
            ]
        },
        "bhel puri": {
            "ingredients": [
                "2 cups puffed rice",
                "1 small onion (chopped)",
                "1 small tomato (chopped)",
                "2 tbsp green chutney",
                "2 tbsp tamarind chutney",
                "1/2 cup sev"
            ],
            "process": [
                "Mix puffed rice, onion, tomato, chutneys, and sev.",
                "Serve immediately."
            ]
        },
        "ragda pattice": {
            "ingredients": [
                "2 cups white peas (soaked, boiled)",
                "3 medium potatoes (boiled, mashed)",
                "1 small onion (chopped)",
                "2 tbsp ragda masala or mixed spices",
                "Salt to taste",
                "2 tbsp oil",
                "Chutney as needed"
            ],
            "process": [
                "Make patties from mashed potatoes, shallow fry.",
                "Heat oil, sauté onion, add peas, masala, salt, and water. Simmer 10 min.",
                "Serve patties topped with ragda and chutneys."
            ]
        },
        "fish fry": {
            "ingredients": [
                "400g fish fillets",
                "1 tbsp lemon juice",
                "1 tsp chili powder",
                "1/2 tsp turmeric",
                "Salt to taste",
                "Oil for frying"
            ],
            "process": [
                "Marinate fish with lemon, chili, turmeric, and salt for 30 min.",
                "Heat oil, fry fish until golden and cooked."
            ]
        },
        "aloo gobi": {
            "ingredients": [
                "2 medium potatoes (cubed)",
                "1 small cauliflower (florets)",
                "1 medium onion (chopped)",
                "1 medium tomato (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat oil, sauté onion and tomato until soft.",
                "Add potatoes, cauliflower, garam masala, and salt.",
                "Cover and cook until vegetables are tender."
            ]
        },
        "baingan bharta": {
            "ingredients": [
                "1 large eggplant",
                "1 medium onion (chopped)",
                "1 medium tomato (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Roast eggplant, peel and mash.",
                "Heat oil, sauté onion and tomato until soft.",
                "Add mashed eggplant, garam masala, and salt. Cook 5 min."
            ]
        },
        "lauki sabzi": {
            "ingredients": [
                "1 medium bottle gourd (cubed)",
                "1 medium onion (chopped)",
                "1 medium tomato (chopped)",
                "1 tsp cumin seeds",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat oil, splutter cumin, sauté onion and tomato.",
                "Add bottle gourd and salt, cover and cook until soft."
            ]
        },
        "tinda masala": {
            "ingredients": [
                "4 apple gourds (tinda, cubed)",
                "1 medium onion (chopped)",
                "1 medium tomato (chopped)",
                "1 tsp garam masala",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Heat oil, sauté onion and tomato.",
                "Add tinda, garam masala, and salt. Cover and cook until tender."
            ]
        },
        "pakora": {
            "ingredients": [
                "1 cup gram flour",
                "1 medium onion (sliced)",
                "1 medium potato (sliced)",
                "1/2 tsp chili powder",
                "Salt to taste",
                "Oil for frying"
            ],
            "process": [
                "Mix gram flour, chili powder, salt, and water to a thick batter.",
                "Dip onion and potato slices, fry until golden."
            ]
        },
        "mirchi bajji": {
            "ingredients": [
                "6 large green chilies",
                "1 cup gram flour",
                "1/2 tsp chili powder",
                "Salt to taste",
                "Oil for frying"
            ],
            "process": [
                "Slit and deseed chilies.",
                "Mix gram flour, chili powder, salt, and water to a batter.",
                "Dip chilies, fry until golden."
            ]
        },
        "paneer tikka": {
            "ingredients": [
                "200g paneer (cubed)",
                "1/2 cup yogurt",
                "1 tsp chili powder",
                "1 tsp garam masala",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Marinate paneer in yogurt, chili powder, garam masala, and salt for 30 min.",
                "Thread onto skewers, grill or bake until edges are charred."
            ]
        },
        "corn chaat": {
            "ingredients": [
                "1 cup boiled corn",
                "1 small onion (chopped)",
                "1 small tomato (chopped)",
                "1/2 tsp chaat masala",
                "Salt to taste",
                "1 tbsp lemon juice"
            ],
            "process": [
                "Mix corn, onion, tomato, chaat masala, salt, and lemon juice.",
                "Serve."
            ]
        },
        "moong dal chilla": {
            "ingredients": [
                "1 cup moong dal",
                "1/2 tsp chili powder",
                "Salt to taste",
                "Oil for cooking"
            ],
            "process": [
                "Soak moong dal 2-3 hours, grind with chili powder and salt to a batter.",
                "Pour on hot griddle, spread, drizzle oil, cook both sides until golden."
            ]
        },
        "spring rolls": {
            "ingredients": [
                "8 spring roll sheets",
                "1 cup mixed vegetables (shredded)",
                "1 tsp soy sauce",
                "1/2 tsp chili sauce",
                "Salt to taste",
                "Oil for frying"
            ],
            "process": [
                "Sauté vegetables with soy sauce, chili sauce, and salt.",
                "Place filling on sheets, roll and seal.",
                "Fry until golden and crisp."
            ]
        },
    },
    "Beverages": {
        "tea": {
            "ingredients": [
                "2 cups water",
                "2 tsp tea leaves",
                "1/2 cup milk",
                "2 tsp sugar (or to taste)"
            ],
            "process": [
                "Boil 2 cups water in a saucepan.",
                "Add 2 tsp tea leaves and simmer for 2 minutes.",
                "Add 1/2 cup milk and 2 tsp sugar.",
                "Simmer for another 2-3 minutes.",
                "Strain into cups and serve hot."
            ]
        },
        "coffee": {
            "ingredients": [
                "1 cup water",
                "2 tsp coffee powder",
                "1 cup milk",
                "2 tsp sugar (or to taste)"
            ],
            "process": [
                "Boil 1 cup water in a saucepan.",
                "Add 2 tsp coffee powder and stir.",
                "Add 1 cup milk and 2 tsp sugar.",
                "Mix well and bring to a gentle boil.",
                "Pour into cups and serve hot."
            ]
        },
        "lemonade": {
            "ingredients": [
                "2 lemons (juice)",
                "2 cups water",
                "3 tbsp sugar"
            ],
            "process": [
                "Squeeze juice from 2 lemons into a bowl.",
                "Add 2 cups water and 3 tbsp sugar.",
                "Stir until sugar dissolves.",
                "Pour into glasses and serve chilled."
            ]
        },
        "banana smoothie": {
            "ingredients": [
                "2 bananas",
                "1 cup milk",
                "2 tbsp sugar"
            ],
            "process": [
                "Peel and slice 2 bananas.",
                "Add banana, 1 cup milk, and 2 tbsp sugar to a blender.",
                "Blend until smooth.",
                "Pour into glasses and serve chilled."
            ]
        },
        "mango lassi": {
            "ingredients": [
                "1 cup chopped mango",
                "1 cup yogurt",
                "2 tbsp sugar"
            ],
            "process": [
                "Peel and chop mangoes to make 1 cup.",
                "Add mango, 1 cup yogurt, and 2 tbsp sugar to a blender.",
                "Blend until smooth.",
                "Pour into glasses and serve chilled."
            ]
        },
        "buttermilk": {
            "ingredients": [
                "1 cup yogurt",
                "1 cup water",
                "1/4 tsp salt",
                "1/4 tsp roasted cumin powder"
            ],
            "process": [
                "Whisk 1 cup yogurt with 1 cup water until smooth.",
                "Add 1/4 tsp salt and 1/4 tsp roasted cumin powder.",
                "Mix well.",
                "Serve chilled."
            ]
        },
        "lassi": {
            "ingredients": [
                "1 cup yogurt",
                "1/2 cup water",
                "2 tbsp sugar"
            ],
            "process": [
                "Blend 1 cup yogurt, 1/2 cup water, and 2 tbsp sugar until frothy.",
                "Pour into glasses and serve chilled."
            ]
        },
        "jaljeera": {
            "ingredients": [
                "2 cups water",
                "1/4 cup mint leaves",
                "1 tsp cumin powder",
                "1/2 tsp black salt",
                "1/2 tsp chaat masala",
                "1/2 tsp salt"
            ],
            "process": [
                "Blend 1/4 cup mint leaves, 1 tsp cumin powder, 1/2 tsp black salt, 1/2 tsp chaat masala, and 1/2 tsp salt with a little water to make a paste.",
                "Add paste to 2 cups water and mix well.",
                "Strain and serve chilled."
            ]
        },
        "masala chai": {
            "ingredients": [
                "2 cups milk",
                "2 tsp tea leaves",
                "1/2 inch ginger (crushed)",
                "2 cardamom pods (crushed)",
                "2 tsp sugar (or to taste)"
            ],
            "process": [
                "Boil 2 cups milk with 2 tsp tea leaves, 1/2 inch crushed ginger, and 2 crushed cardamom pods.",
                "Add 2 tsp sugar and simmer for a few minutes.",
                "Strain into cups and serve hot."
            ]
        },
        "cold coffee": {
            "ingredients": [
                "2 tsp instant coffee",
                "1 cup milk",
                "2 tbsp sugar",
                "1 cup ice cubes"
            ],
            "process": [
                "Add 2 tsp instant coffee, 1 cup milk, 2 tbsp sugar, and 1 cup ice cubes to a blender.",
                "Blend until frothy.",
                "Pour into glasses and serve chilled."
            ]
        },
        "hot chocolate": {
            "ingredients": [
                "2 cups milk",
                "2 tbsp cocoa powder",
                "2 tbsp sugar"
            ],
            "process": [
                "Mix 2 tbsp cocoa powder and 2 tbsp sugar in a little milk to make a paste.",
                "Heat remaining milk in a pan.",
                "Add cocoa paste and stir well.",
                "Heat until warm and serve."
            ]
        },
        "lemon soda": {
            "ingredients": [
                "1 lemon (juice)",
                "1 cup soda",
                "1/4 tsp salt",
                "1 tbsp sugar"
            ],
            "process": [
                "Squeeze juice of 1 lemon into a glass.",
                "Add 1/4 tsp salt and 1 tbsp sugar, mix well.",
                "Pour 1 cup soda over and stir.",
                "Serve immediately."
            ]
        },
        "aam panna": {
            "ingredients": [
                "2 raw mangoes",
                "4 tbsp sugar",
                "1/2 tsp salt",
                "1/2 tsp roasted cumin powder",
                "2 cups water"
            ],
            "process": [
                "Boil or roast 2 raw mangoes until soft.",
                "Peel and extract pulp.",
                "Blend pulp with 4 tbsp sugar, 1/2 tsp salt, and 1/2 tsp roasted cumin powder.",
                "Add 2 cups water and mix well.",
                "Serve chilled."
            ]
        },
        "badam milk": {
            "ingredients": [
                "2 cups milk",
                "10 almonds",
                "2 tbsp sugar",
                "1/4 tsp cardamom powder"
            ],
            "process": [
                "Soak 10 almonds and peel them.",
                "Grind almonds to a paste.",
                "Boil 2 cups milk and add almond paste.",
                "Add 2 tbsp sugar and 1/4 tsp cardamom powder.",
                "Simmer for a few minutes.",
                "Serve chilled or warm."
            ]
        },
        "rose milk": {
            "ingredients": [
                "2 cups milk",
                "2 tbsp rose syrup",
                "2 tbsp sugar"
            ],
            "process": [
                "Mix 2 tbsp rose syrup and 2 tbsp sugar in 2 cups milk.",
                "Stir well.",
                "Serve chilled."
            ]
        },
        "filter coffee": {
            "ingredients": [
                "2 tbsp coffee powder",
                "1 cup water",
                "1 cup milk",
                "2 tsp sugar"
            ],
            "process": [
                "Brew 2 tbsp coffee powder with 1 cup hot water in a filter.",
                "Boil 1 cup milk separately.",
                "Mix brewed coffee with milk and 2 tsp sugar.",
                "Serve hot."
            ]
        },
        "thandai": {
            "ingredients": [
                "2 cups milk",
                "10 almonds",
                "1 tbsp fennel seeds",
                "1 tbsp poppy seeds",
                "1/4 tsp cardamom powder",
                "2 tbsp sugar"
            ],
            "process": [
                "Soak 10 almonds, 1 tbsp fennel seeds, and 1 tbsp poppy seeds.",
                "Grind to a fine paste with 1/4 tsp cardamom powder.",
                "Mix paste with 2 cups milk and 2 tbsp sugar.",
                "Chill and serve."
            ]
        },
        "kokum sharbat": {
            "ingredients": [
                "10 kokum pieces",
                "2 tbsp sugar",
                "2 cups water",
                "1/4 tsp salt"
            ],
            "process": [
                "Soak 10 kokum pieces in 2 cups water.",
                "Add 2 tbsp sugar and 1/4 tsp salt.",
                "Stir well until dissolved.",
                "Serve chilled."
            ]
        },
        "masala milk": {
            "ingredients": [
                "2 cups milk",
                "1/4 tsp mixed spice powder",
                "2 tbsp sugar",
                "2 tbsp chopped nuts"
            ],
            "process": [
                "Boil 2 cups milk with 1/4 tsp mixed spice powder and 2 tbsp sugar.",
                "Add 2 tbsp chopped nuts.",
                "Simmer for a few minutes.",
                "Serve warm."
            ]
        },
        "sattu drink": {
            "ingredients": [
                "2 tbsp sattu",
                "1 cup water",
                "1 tsp lemon juice",
                "1/4 tsp salt",
                "1/4 tsp cumin powder"
            ],
            "process": [
                "Mix 2 tbsp sattu with 1 cup water.",
                "Add 1 tsp lemon juice, 1/4 tsp salt, and 1/4 tsp cumin powder.",
                "Stir well.",
                "Serve chilled."
            ]
        }
    },
    "Breakfast": {
        "pasta": {
            "ingredients": [
                "2 cups pasta",
                "2 medium tomatoes (chopped)",
                "Salt to taste",
                "2 tbsp oil"
            ],
            "process": [
                "Boil 2 cups pasta in salted water until cooked, drain.",
                "Heat 2 tbsp oil, sauté tomatoes until soft.",
                "Add boiled pasta, mix well, cook for 2 minutes.",
                "Serve hot."
            ]
        },
        "omelette": {
            "ingredients": [
                "2 eggs",
                "Salt to taste",
                "1/4 tsp pepper",
                "1 tbsp oil"
            ],
            "process": [
                "Beat 2 eggs with salt and pepper.",
                "Heat 1 tbsp oil in a pan, pour egg mixture.",
                "Cook until set, fold and serve hot."
            ]
        },
        "grilled cheese": {
            "ingredients": [
                "2 slices bread",
                "2 slices cheese",
                "1 tbsp butter"
            ],
            "process": [
                "Butter one side of each bread slice.",
                "Place cheese between unbuttered sides.",
                "Grill on a pan until golden on both sides."
            ]
        },
        "fruit salad": {
            "ingredients": [
                "1 apple",
                "1 banana",
                "1 orange"
            ],
            "process": [
                "Chop apple, banana, and orange.",
                "Mix in a bowl and serve."
            ]
        },
        "maggi": {
            "ingredients": [
                "1 packet noodles",
                "2 cups water",
                "Salt to taste"
            ],
            "process": [
                "Boil 2 cups water, add noodles and tastemaker.",
                "Cook until soft, serve hot."
            ]
        },
        "pancakes": {
            "ingredients": [
                "1 cup flour",
                "1 cup milk",
                "1 egg",
                "2 tbsp sugar",
                "2 tbsp butter"
            ],
            "process": [
                "Mix flour, milk, egg, and sugar to make a batter.",
                "Heat a pan, add butter, pour batter, cook until bubbles form.",
                "Flip and cook other side, serve with syrup."
            ]
        },
        "salad": {
            "ingredients": [
                "1 cup lettuce (chopped)",
                "1 tomato (chopped)",
                "1 cucumber (chopped)",
                "Salt to taste",
                "1 tbsp oil"
            ],
            "process": [
                "Chop lettuce, tomato, and cucumber.",
                "Mix with salt and oil, serve."
            ]
        },
        "dosa": {
            "ingredients": [
                "1 cup rice",
                "1/2 cup urad dal",
                "Salt to taste",
                "Oil for cooking"
            ],
            "process": [
                "Soak rice and urad dal for 4-6 hours, grind to a smooth batter.",
                "Ferment overnight, add salt.",
                "Spread batter on hot griddle, drizzle oil, cook until golden."
            ]
        },
        "idli": {
            "ingredients": [
                "1 cup rice",
                "1/2 cup urad dal",
                "Salt to taste"
            ],
            "process": [
                "Soak rice and urad dal for 4-6 hours, grind to a smooth batter.",
                "Ferment overnight, add salt.",
                "Pour into molds, steam for 10-12 minutes."
            ]
        },
        "upma": {
            "ingredients": [
                "1 cup sooji (semolina)",
                "1 medium onion (chopped)",
                "Salt to taste",
                "2 tbsp oil",
                "1/2 tsp mustard seeds"
            ],
            "process": [
                "Heat oil, splutter mustard seeds, sauté onion.",
                "Add sooji, roast for 2-3 minutes.",
                "Add 2 cups water and salt, cook until thick."
            ]
        },
        "sandwich": {
            "ingredients": [
                "2 slices bread",
                "2 slices cheese",
                "1 tomato (sliced)",
                "2 lettuce leaves"
            ],
            "process": [
                "Layer cheese, tomato, and lettuce between bread slices.",
                "Grill or toast until golden."
            ]
        },
        "scrambled eggs": {
            "ingredients": [
                "2 eggs",
                "Salt to taste",
                "1 tbsp butter"
            ],
            "process": [
                "Beat eggs with salt.",
                "Melt butter in a pan, add eggs, stir until just set."
            ]
        },
        "aloo paratha": {
            "ingredients": [
                "1 cup wheat flour",
                "2 medium potatoes (boiled, mashed)",
                "Salt to taste",
                "1/2 tsp spices (cumin, chili powder, etc.)",
                "2 tbsp oil"
            ],
            "process": [
                "Make dough with flour, salt, and water.",
                "Mix potatoes with salt and spices for filling.",
                "Stuff dough with filling, roll out, cook on griddle with oil."
            ]
        },
        "curd rice": {
            "ingredients": [
                "1 cup cooked rice",
                "1 cup curd (yogurt)",
                "Salt to taste"
            ],
            "process": [
                "Mix cooked rice with curd and salt.",
                "Serve chilled."
            ]
        },
        "lemon rice": {
            "ingredients": [
                "1 cup rice",
                "1 lemon (juice)",
                "1/4 tsp turmeric powder",
                "1 tsp salt (or to taste)",
                "2 tbsp oil",
                "1 tsp mustard seeds",
                "2 tbsp peanuts"
            ],
            "process": [
                "Cook the rice and let it cool.",
                "Heat oil in a pan, add mustard seeds and let them splutter.",
                "Add peanuts and fry until golden.",
                "Add turmeric powder and salt, mix well.",
                "Add lemon juice and cooked rice.",
                "Mix everything gently and cook for 2-3 minutes.",
                "Serve warm or at room temperature."
            ]
        },
        "ven pongal": {
            "ingredients": [
                "1/2 cup rice",
                "1/2 cup moong dal",
                "2 tbsp ghee",
                "1/2 tsp black pepper",
                "1/2 tsp cumin seeds",
                "1 tsp grated ginger",
                "1 tsp salt (or to taste)",
                "8-10 cashews"
            ],
            "process": [
                "Dry roast moong dal lightly and wash with rice.",
                "Pressure cook rice and dal with 3 cups water, salt, and ginger until soft.",
                "Heat ghee in a pan, add cumin, pepper, and cashews. Fry until cashews are golden.",
                "Pour the tempering over the cooked rice-dal mixture.",
                "Mash slightly, mix well, and serve hot."
            ]
        },
        "medu vada": {
            "ingredients": [
                "1 cup urad dal",
                "1/2 tsp salt",
                "Oil for deep frying",
                "1/2 tsp black pepper (optional)",
                "1 sprig curry leaves (chopped)"
            ],
            "process": [
                "Soak urad dal for 4-5 hours and drain.",
                "Grind dal to a smooth batter, adding little water as needed.",
                "Mix in salt, pepper, and curry leaves.",
                "Wet your hands, shape batter into donuts.",
                "Heat oil and deep fry vadas until golden and crisp.",
                "Drain on paper towels and serve hot."
            ]
        },
        "appam": {
            "ingredients": [
                "1 cup rice",
                "1/2 cup grated coconut",
                "2 tbsp sugar",
                "1/2 tsp salt",
                "1/2 tsp yeast"
            ],
            "process": [
                "Soak rice for 4 hours, then grind with coconut to a smooth batter.",
                "Dissolve yeast in a little warm water with sugar, let it activate.",
                "Mix yeast mixture, salt, and remaining sugar into the batter.",
                "Ferment for 6-8 hours or overnight.",
                "Pour a ladle of batter into a hot appam pan, swirl, cover, and cook until edges are crisp.",
                "Serve hot."
            ]
        },
        "avial": {
            "ingredients": [
                "2 cups mixed vegetables (carrot, beans, potato, etc.)",
                "1/2 cup grated coconut",
                "1/2 cup curd (yogurt)",
                "1 sprig curry leaves",
                "1 tsp salt",
                "1 tbsp oil"
            ],
            "process": [
                "Cut vegetables into strips and cook with salt until tender.",
                "Grind coconut with a little water to a coarse paste.",
                "Add coconut paste and curry leaves to the cooked vegetables.",
                "Cook for 2-3 minutes, then turn off the heat.",
                "Mix in curd and drizzle oil on top.",
                "Serve warm."
            ]
        },
        "payasam": {
            "ingredients": [
                "1 liter milk",
                "1/4 cup rice",
                "1/2 cup sugar",
                "1/2 tsp cardamom powder",
                "2 tbsp cashew nuts",
                "2 tbsp raisins",
                "2 tbsp ghee"
            ],
            "process": [
                "Wash and soak rice for 15 minutes.",
                "Heat ghee in a pan, fry cashew nuts and raisins until golden, set aside.",
                "Boil milk in a heavy pan.",
                "Add soaked rice and cook on low flame, stirring occasionally, until rice is soft.",
                "Add sugar and cardamom powder, mix well and simmer for 5 minutes.",
                "Add fried cashews and raisins.",
                "Serve warm."
            ]
        },
        "biryani": {
            "ingredients": [
                "1 cup basmati rice",
                "250g meat (chicken/mutton)",
                "1 cup sliced onions",
                "1/2 cup chopped tomatoes",
                "2 tbsp biryani masala or spices",
                "1 tsp salt (or to taste)",
                "2 tbsp oil"
            ],
            "process": [
                "Wash and soak rice for 30 minutes.",
                "Marinate meat with spices and salt for 30 minutes.",
                "Cook rice until 70% done, drain and set aside.",
                "Heat oil in a pan, sauté onions until golden.",
                "Add tomatoes and cook until soft.",
                "Add marinated meat and cook until tender.",
                "Layer cooked meat and rice in a pot, sprinkle remaining spices.",
                "Cover and cook on low heat for 15-20 minutes.",
                "Serve hot."
            ]
        },
        "khichdi": {
            "ingredients": [
                "1/2 cup rice",
                "1/2 cup moong dal",
                "1 cup mixed vegetables (carrot, peas, potato, etc.)",
                "1/4 tsp turmeric powder",
                "1 tsp salt (or to taste)",
                "2 tbsp ghee"
            ],
            "process": [
                "Wash rice and moong dal together.",
                "Heat ghee in a pressure cooker, add vegetables and sauté for 2 minutes.",
                "Add rice, dal, turmeric, and salt. Mix well.",
                "Add 3 cups water, close the lid and cook for 3-4 whistles.",
                "Let the pressure release, mash slightly.",
                "Serve hot."
            ]
        },
        "pulao": {
            "ingredients": [
                "1 cup basmati rice",
                "1 cup mixed vegetables (carrot, peas, beans, etc.)",
                "1 tsp cumin seeds",
                "2 tbsp oil",
                "1 tsp salt (or to taste)",
                "2 cups water",
                "1/2 tsp garam masala"
            ],
            "process": [
                "Wash and soak rice for 20 minutes.",
                "Heat oil in a pan, add cumin seeds and let them splutter.",
                "Add vegetables and sauté for 2-3 minutes.",
                "Add soaked rice, salt, and garam masala. Mix gently.",
                "Add water, bring to a boil, then cover and cook on low heat until rice is done.",
                "Fluff with a fork and serve."
            ]
        },
        "chole": {
            "ingredients": [
                "1 cup chickpeas",
                "1 cup chopped onion",
                "1 cup chopped tomato",
                "2 tbsp chole masala or spices",
                "1 tsp salt (or to taste)",
                "2 tbsp oil"
            ],
            "process": [
                "Soak chickpeas overnight and pressure cook until soft.",
                "Heat oil in a pan, sauté onions until golden.",
                "Add tomatoes and cook until soft.",
                "Add spices and salt, mix well.",
                "Add cooked chickpeas and simmer for 10 minutes.",
                "Serve hot."
            ]
        },
        "poori": {
            "ingredients": [
                "2 cups wheat flour",
                "1/2 tsp salt",
                "1 tbsp oil",
                "Water as needed",
                "Oil for deep frying"
            ],
            "process": [
                "Mix flour, salt, and oil in a bowl.",
                "Add water gradually and knead to a stiff dough.",
                "Divide dough into small balls and roll into small discs.",
                "Heat oil in a deep pan.",
                "Fry each disc until puffed and golden.",
                "Drain on paper towels and serve hot."
            ]
        },
        "methi paratha": {
            "ingredients": [
                "2 cups wheat flour",
                "1 cup chopped fenugreek leaves",
                "1/2 tsp salt",
                "1/2 tsp spices (cumin, chili powder, etc.)",
                "1 tbsp oil",
                "Water as needed"
            ],
            "process": [
                "Mix flour, fenugreek leaves, salt, spices, and oil.",
                "Add water and knead to a soft dough.",
                "Divide into balls, roll each into a disc.",
                "Cook on a hot griddle, applying oil on both sides, until golden spots appear.",
                "Serve hot."
            ]
        },
        "besan chilla": {
            "ingredients": [
                "1 cup gram flour (besan)",
                "1/2 cup chopped onion",
                "1/2 cup chopped tomato",
                "1/2 tsp salt",
                "1/2 tsp spices (turmeric, chili powder, etc.)",
                "Water as needed",
                "Oil for cooking"
            ],
            "process": [
                "Mix besan, onion, tomato, salt, and spices in a bowl.",
                "Add water to make a smooth batter.",
                "Heat a non-stick pan, pour a ladle of batter and spread gently.",
                "Drizzle oil around the edges, cook until golden on both sides.",
                "Serve hot."
            ]
        },
        "uttapam": {
            "ingredients": [
                "1 cup rice",
                "1/2 cup urad dal",
                               "1/2 cup chopped onion",
                "1/2 cup chopped tomato",
                "1/2 tsp salt",
                "Oil for cooking"
            ],
            "process": [
                "Soak rice and urad dal for 4-6 hours, grind to a thick batter, and ferment overnight.",
                "Add salt to the batter and mix well.",
                "Heat a griddle, pour a ladle of batter and spread thick.",
                "Top with onions and tomatoes, drizzle oil around the edges.",
                "Cook until golden on both sides.",
                "Serve hot."
            ]
        },
        "moong dal dosa": {
            "ingredients": [
                "1 cup moong dal",
                "1/4 cup rice",
                "1/2 tsp salt",
                "1/2 tsp spices (cumin, chili, etc.)",
                "Oil for cooking"
            ],
            "process": [
                "Soak moong dal and rice for 4 hours, grind to a smooth batter.",
                "Add salt and spices, mix well.",
                "Heat a griddle, pour a ladle of batter and spread thin.",
                "Drizzle oil around the edges, cook until crisp.",
                "Serve hot."
            ]
        },
        "rava idli": {
            "ingredients": [
                "1 cup semolina (rava)",
                "1 cup yogurt",
                "1/2 tsp salt",
                "1/2 tsp baking soda",
                "1 tbsp oil"
            ],
            "process": [
                "Mix semolina, yogurt, salt, and oil in a bowl.",
                "Add a little water to make a thick batter, rest for 10 minutes.",
                "Add baking soda and mix gently.",
                "Pour batter into greased idli molds.",
                "Steam for 10-15 minutes until cooked through.",
                "Serve hot with chutney or sambar."
            ]
        },
        "chapathi": {
            "ingredients": [
                "2 cups wheat flour",
                "1 cup water (as needed)",
                "1/2 tsp salt",
                "1 tbsp oil or ghee"
            ],
            "process": [
                "In a bowl, mix wheat flour and salt.",
                "Gradually add water and knead to form a soft dough.",
                "Cover and let the dough rest for 15-20 minutes.",
                "Divide the dough into small balls.",
                "Roll each ball into a thin disc using a rolling pin.",
                "Heat a griddle (tawa) and cook each disc on both sides until light brown spots appear.",
                "Apply oil or ghee if desired and serve hot."
            ]
        },
        "ragi ball": {
            "ingredients": [
                "1 cup ragi flour",
                "2 cups water",
                "1/4 tsp salt"
            ],
            "process": [
                "Boil water in a pan and add salt.",
                "Reduce the heat and add ragi flour gradually, stirring continuously to avoid lumps.",
                "Cook the mixture on low heat, stirring until it thickens and leaves the sides of the pan.",
                "Once cooked, let it cool slightly and shape into balls.",
                "Serve warm with curry or sambar."
            ]
        }
    }
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipes')
def list_recipes():
    return render_template("recipes.html", recipes=recipes)

@app.route('/section/<section_name>')
def show_section(section_name):
    section = recipes.get(section_name.capitalize())
    if section:
        return render_template("section.html", section_name=section_name.capitalize(), items=section)
    else:
        return "Section not found", 404

@app.route('/recipe/<section>/<recipe_name>')
def show_recipe(section, recipe_name):
    section_obj = recipes.get(section.capitalize())
    if section_obj:
        recipe = section_obj.get(recipe_name.lower())
        if recipe:
            return render_template(
                "recipe.html",
                recipe_name=recipe_name.title(),
                ingredients=recipe["ingredients"],
                process=recipe["process"],
                section=section
            )
    return "Recipe not found", 404

@app.route('/ingredients', methods=['GET'])
def ingredients():
    recipe_name = request.args.get('ingredient', '').strip().lower()
    found_recipe = None
    found_section = None
    if recipe_name:
        for section, recipes_dict in recipes.items():
            if recipe_name in recipes_dict:
                found_recipe = recipes_dict[recipe_name]
                found_section = section
                break
    return render_template(
        "ingredients.html",
        recipe_name=recipe_name if found_recipe else None,
        ingredients=found_recipe["ingredients"] if found_recipe else None,
        section=found_section
    )

@app.route('/process', methods=['GET'])
def process_search():
    recipe_name = request.args.get('recipe', '').strip().lower()
    found_recipe = None
    found_section = None
    if recipe_name:
        for section, recipes_dict in recipes.items():
            if recipe_name in recipes_dict:
                found_recipe = recipes_dict[recipe_name]
                found_section = section
                break
    if found_recipe and isinstance(found_recipe["process"], str):
        process_steps = found_recipe["process"].split('\n')
    else:
        process_steps = found_recipe["process"] if found_recipe else None

    return render_template(
        "process.html",
        recipe_name=recipe_name if found_recipe else None,
        process=process_steps,
        section=found_section
    )

if __name__ == '__main__':
    
    app.run(debug=True, port=5000)