# -*- coding: utf-8 -*-
"""
📁 Data Module — Static Game Data, Localization & Constants
𝐝𝐞𝐯 𝐛𝐲 𝟕𝐚𝐦𝐨 © 2026
"""

# ══════════════════════════════════════════════════════════════════════════════
# LOCALIZATION — ARABIC & ENGLISH
# ══════════════════════════════════════════════════════════════════════════════

TRANSLATIONS = {
    "ar": {
        # General
        "welcome": "أهلا وسهلا في لعبة الرول بلاي المصرية!",
        "character_created": "تم إنشاء شخصيتك بنجاح!",
        "error": "حدث خطأ ما!",
        "not_found": "لم يتم العثور على الشخصية!",
        
        # Stats
        "health": "الصحة",
        "hunger": "الجوع",
        "thirst": "العطش",
        "energy": "الطاقة",
        "happiness": "السعادة",
        "hygiene": "النظافة",
        "fun": "المرح",
        "fitness": "اللياقة",
        
        # Economy
        "balance": "الرصيد",
        "wallet": "المحفظة",
        "bank": "البنك",
        "earned": "حصلت على",
        "spent": "أنفقت",
        
        # Jobs
        "work": "العمل",
        "job": "الوظيفة",
        "salary": "الراتب",
        "promoted": "تم ترقيتك!",
        
        # Classes
        "businessman": "رجل أعمال",
        "hacker": "هاكر",
        "athlete": "رياضي",
        "student": "طالب",
        "artist": "فنان",
    },
    "en": {
        # General
        "welcome": "Welcome to the Egyptian RPG!",
        "character_created": "Your character has been created successfully!",
        "error": "An error occurred!",
        "not_found": "Character not found!",
        
        # Stats
        "health": "Health",
        "hunger": "Hunger",
        "thirst": "Thirst",
        "energy": "Energy",
        "happiness": "Happiness",
        "hygiene": "Hygiene",
        "fun": "Fun",
        "fitness": "Fitness",
        
        # Economy
        "balance": "Balance",
        "wallet": "Wallet",
        "bank": "Bank",
        "earned": "Earned",
        "spent": "Spent",
        
        # Jobs
        "work": "Work",
        "job": "Job",
        "salary": "Salary",
        "promoted": "Promoted!",
        
        # Classes
        "businessman": "Businessman",
        "hacker": "Hacker",
        "athlete": "Athlete",
        "student": "Student",
        "artist": "Artist",
    }
}

# ══════════════════════════════════════════════════════════════════════════════
# CHARACTER CLASSES
# ══════════════════════════════════════════════════════════════════════════════

CHARACTER_CLASSES = {
    "businessman": {
        "name": "رجل أعمال",
        "en_name": "Businessman",
        "description": "ماهر في التجارة والتفاوض",
        "starting_skill": "trading_skill",
        "starting_bonus": 20,
        "starting_money": 1000,
    },
    "hacker": {
        "name": "هاكر",
        "en_name": "Hacker",
        "description": "خبير التكنولوجيا والبرمجة",
        "starting_skill": "hacking_skill",
        "starting_bonus": 30,
        "starting_money": 500,
    },
    "athlete": {
        "name": "رياضي",
        "en_name": "Athlete",
        "description": "قوي وسريع اللياقة",
        "starting_skill": "fighting_skill",
        "starting_bonus": 25,
        "starting_money": 600,
    },
    "student": {
        "name": "طالب",
        "en_name": "Student",
        "description": "ذكي وسريع التعلم",
        "starting_skill": "programming_skill",
        "starting_bonus": 20,
        "starting_money": 300,
    },
    "artist": {
        "name": "فنان",
        "en_name": "Artist",
        "description": "موهوب وخلاق",
        "starting_skill": "design_skill",
        "starting_bonus": 20,
        "starting_money": 400,
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# NEIGHBORHOODS
# ══════════════════════════════════════════════════════════════════════════════

NEIGHBORHOODS = {
    "downtown": {
        "name": "وسط البلد",
        "en_name": "Downtown",
        "description": "القلب النابض للمدينة، حيث الحياة سريعة والفرص كثيرة",
        "rent": 50,
        "safety": 60,
        "activity": 90,
        "jobs_multiplier": 1.2,
    },
    "zamalek": {
        "name": "الزمالك",
        "en_name": "Zamalek",
        "description": "حي راقي وهادئ للأثرياء",
        "rent": 200,
        "safety": 95,
        "activity": 40,
        "jobs_multiplier": 1.5,
    },
    "giza": {
        "name": "الجيزة",
        "en_name": "Giza",
        "description": "بالقرب من الأهرامات، حي سياحي",
        "rent": 100,
        "safety": 75,
        "activity": 70,
        "jobs_multiplier": 1.1,
    },
    "helwan": {
        "name": "حلوان",
        "en_name": "Helwan",
        "description": "حي شعبي مزدحم",
        "rent": 30,
        "safety": 50,
        "activity": 80,
        "jobs_multiplier": 0.9,
    },
    "new_cairo": {
        "name": "القاهرة الجديدة",
        "en_name": "New Cairo",
        "description": "مدينة حديثة عصرية",
        "rent": 150,
        "safety": 90,
        "activity": 60,
        "jobs_multiplier": 1.3,
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# HOUSE TYPES
# ══════════════════════════════════════════════════════════════════════════════

HOUSE_TYPES = {
    "apartment": {
        "name": "شقة",
        "en_name": "Apartment",
        "base_price": 10000,
        "maintenance": 100,
        "luxury_level": 3,
    },
    "house": {
        "name": "منزل",
        "en_name": "House",
        "base_price": 50000,
        "maintenance": 500,
        "luxury_level": 6,
    },
    "villa": {
        "name": "فيلا",
        "en_name": "Villa",
        "base_price": 200000,
        "maintenance": 2000,
        "luxury_level": 10,
    },
    "penthouse": {
        "name": "شقة فاخرة",
        "en_name": "Penthouse",
        "base_price": 500000,
        "maintenance": 5000,
        "luxury_level": 15,
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# CAR TYPES
# ══════════════════════════════════════════════════════════════════════════════

CAR_TYPES = {
    "bike": {
        "name": "دراجة نارية",
        "en_name": "Motorbike",
        "price": 2000,
        "speed": 80,
        "luxury": 2,
        "maintenance": 50,
    },
    "sedan": {
        "name": "سيارة سيدان",
        "en_name": "Sedan",
        "price": 15000,
        "speed": 160,
        "luxury": 5,
        "maintenance": 300,
    },
    "sports": {
        "name": "سيارة رياضية",
        "en_name": "Sports Car",
        "price": 80000,
        "speed": 240,
        "luxury": 9,
        "maintenance": 1500,
    },
    "luxury": {
        "name": "سيارة فاخرة",
        "en_name": "Luxury Car",
        "price": 200000,
        "speed": 200,
        "luxury": 15,
        "maintenance": 3000,
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# ITEMS & INVENTORY
# ══════════════════════════════════════════════════════════════════════════════

ITEMS = {
    "burger": {
        "name": "برجر",
        "en_name": "Burger",
        "rarity": "common",
        "effect": {"hunger": 30},
        "price": 50,
    },
    "sushi": {
        "name": "سوشي",
        "en_name": "Sushi",
        "rarity": "uncommon",
        "effect": {"hunger": 50},
        "price": 150,
    },
    "laptop": {
        "name": "كمبيوتر محمول",
        "en_name": "Laptop",
        "rarity": "rare",
        "effect": {"programming_skill": 10},
        "price": 3000,
    },
    "diamond_ring": {
        "name": "خاتم الماس",
        "en_name": "Diamond Ring",
        "rarity": "legendary",
        "effect": {"charisma": 20},
        "price": 50000,
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# CRIME ACTIVITIES
# ══════════════════════════════════════════════════════════════════════════════

CRIMES = {
    "pickpocket": {
        "name": "سرقة من الجيوب",
        "en_name": "Pickpocket",
        "min_reward": 100,
        "max_reward": 500,
        "required_skill": "stealth_skill",
        "required_skill_level": 20,
        "danger_level": 2,
        "xp_gain": 30,
    },
    "burglary": {
        "name": "السرقة من المنازل",
        "en_name": "Burglary",
        "min_reward": 1000,
        "max_reward": 5000,
        "required_skill": "hacking_skill",
        "required_skill_level": 50,
        "danger_level": 7,
        "xp_gain": 100,
    },
    "robbery": {
        "name": "السرقة المسلحة",
        "en_name": "Armed Robbery",
        "min_reward": 5000,
        "max_reward": 15000,
        "required_skill": "fighting_skill",
        "required_skill_level": 60,
        "danger_level": 10,
        "xp_gain": 200,
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# ACHIEVEMENTS/BADGES
# ══════════════════════════════════════════════════════════════════════════════

ACHIEVEMENTS = {
    "first_steps": {
        "name": "الخطوات الأولى",
        "en_name": "First Steps",
        "description": "أكمل أول عمل لك",
        "icon": "👣",
    },
    "millionaire": {
        "name": "مليونير",
        "en_name": "Millionaire",
        "description": "اجمع مليون دولار",
        "icon": "💰",
    },
    "max_level": {
        "name": "الحد الأقصى",
        "en_name": "Max Level",
        "description": "وصل للمستوى 100",
        "icon": "👑",
    },
    "master_hacker": {
        "name": "ماستر هاكر",
        "en_name": "Master Hacker",
        "description": "وصل للمستوى 100 في الهاكينج",
        "icon": "🔓",
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTION
# ══════════════════════════════════════════════════════════════════════════════

def translate(key: str, lang: str = "ar") -> str:
    """Get translated string."""
    return TRANSLATIONS.get(lang, {}).get(key, key)
