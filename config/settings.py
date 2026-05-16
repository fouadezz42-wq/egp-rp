# -*- coding: utf-8 -*-
"""
⚙️ config/settings.py — Configuration Management
𝐝𝐞𝐯 𝐛𝐲 𝟕𝐚𝐦𝐨 © 2026 — Professional Edition
"""
from __future__ import annotations
import os
from enum import Enum
from typing import Optional

# ══════════════════════════════════════════════════════════════════════════════
# CORE BOT SETTINGS
# ══════════════════════════════════════════════════════════════════════════════

class Environment(Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"

# Environment Detection
ENV = Environment(os.getenv("APP_ENV", "development"))
DEBUG = ENV == Environment.DEVELOPMENT

# Discord Bot
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "YOUR_BOT_TOKEN_HERE")
BOT_PREFIX = os.getenv("BOT_PREFIX", "!")
BOT_INTENTS = {
    "message_content": True,
    "members": True,
    "guilds": True,
    "dm_messages": True,
    "presences": True,
}

# ══════════════════════════════════════════════════════════════════════════════
# DATABASE CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

# Database URL (PostgreSQL recommended for production)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///egp_rp.db" if DEBUG else "postgresql://user:pass@localhost/egp_rp"
)

# Database Options
DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "20"))
DB_MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", "40"))
DB_ECHO = DEBUG
DB_POOL_RECYCLE = 3600  # Recycle connections after 1 hour

# ══════════════════════════════════════════════════════════════════════════════
# CACHE CONFIGURATION (Redis)
# ══════════════════════════════════════════════════════════════════════════════

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CACHE_TTL = 3600  # 1 hour default
CACHE_ENABLED = os.getenv("CACHE_ENABLED", "true").lower() == "true"

# ══════════════════════════════════════════════════════════════════════════════
# BRANDING & LOCALIZATION
# ══════════════════════════════════════════════════════════════════════════════

OWNER_BRAND = "𝐝𝐞𝐯 𝐛𝐲 𝟕𝐚𝐦𝐨 © 2026"
BOT_NAME = "Egyptian RPG — Professional Edition"
DEFAULT_LANGUAGE = "ar"  # Arabic
SUPPORTED_LANGUAGES = ["ar", "en"]

# ══════════════════════════════════════════════════════════════════════════════
# DISCORD COLORS
# ══════════════════════════════════════════════════════════════════════════════

class Colors:
    GOLD = 0xF1C40F
    RED = 0xE74C3C
    GREEN = 0x2ECC71
    BLUE = 0x3498DB
    PURPLE = 0x9B59B6
    ORANGE = 0xE67E22
    PINK = 0xE91E63
    DARK = 0x2C3E50
    CYAN = 0x1ABC9C
    LIGHT_GRAY = 0x95A5A6
    DARK_GRAY = 0x34495E
    WHITE = 0xFFFFFF
    BLACK = 0x000000

# ══════════════════════════════════════════════════════════════════════════════
# GAME CONSTANTS
# ══════════════════════════════════════════════════════════════════════════════

# Player Stats
class StatLimits:
    MIN = 0
    MAX = 100
    DEFAULT = 100

# Experience & Levels
STARTING_XP = 0
LEVEL_XP_BASE = 500
LEVEL_XP_MULTIPLIER = 1.12  # Each level costs 12% more
MAX_LEVEL = 100

# Money Constants
STARTING_MONEY = 500
STARTING_BANK = 0
DAILY_REWARD_BASE = 200
DAILY_REWARD_BONUS_LEVEL_7 = 500

# Energy System
ENERGY_RECOVERY_PER_HOUR = 8
ENERGY_PER_ACTION = {
    "work": 25,
    "steal": 30,
    "sports": 25,
    "gym": 20,
    "freelance": 15,
}

# Cooldown Times (hours)
COOLDOWN_WORK = 3
COOLDOWN_DAILY = 20
COOLDOWN_CRIME = 3
COOLDOWN_SPORTS = 3

# ══════════════════════════════════════════════════════════════════════════════
# PLAYER FIELDS & VALIDATION
# ══════════════════════════════════════════════════════════════════════════════

STAT_FIELDS = {
    "health", "hunger", "thirst", "energy", "happiness",
    "hygiene", "fun", "fitness",
}

SKILL_FIELDS = {
    "programming_skill", "design_skill", "hacking_skill",
    "fighting_skill", "stealth_skill", "cooking_skill",
    "trading_skill", "football_skill", "streaming_skill",
    "music_skill", "acting_skill", "driving_skill", "charisma",
}

ALL_PLAYER_FIELDS = STAT_FIELDS | SKILL_FIELDS | {
    "user_id", "username", "display_name", "char_class", "gender", "age_group", "age",
    "job", "job_xp", "job_rank", "money", "bank", "crypto",
    "xp", "level", "house", "car", "neighborhood",
    "married_to", "gang", "gang_rank", "reputation", "wanted_level", "jail_until",
    "daily_streak", "total_earnings", "total_spent",
    "created_at", "updated_at",
}

# ══════════════════════════════════════════════════════════════════════════════
# LOGGING CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO" if not DEBUG else "DEBUG")
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
LOG_FILE = "egp_rp.log"

# ══════════════════════════════════════════════════════════════════════════════
# FEATURE FLAGS
# ══════════════════════════════════════════════════════════════════════════════

FEATURES = {
    "npc_ai": os.getenv("FEATURE_NPC_AI", "true").lower() == "true",
    "world_events": os.getenv("FEATURE_WORLD_EVENTS", "true").lower() == "true",
    "economy_inflation": os.getenv("FEATURE_INFLATION", "true").lower() == "true",
    "crime_system": os.getenv("FEATURE_CRIME", "true").lower() == "true",
    "relationships": os.getenv("FEATURE_RELATIONSHIPS", "true").lower() == "true",
}

# ══════════════════════════════════════════════════════════════════════════════
# RATE LIMITING
# ══════════════════════════════════════════════════════════════════════════════

RATE_LIMIT_COMMANDS = 5  # Max commands per 5 seconds
RATE_LIMIT_WINDOW = 5

# ══════════════════════════════════════════════════════════════════════════════
# VALIDATION
# ══════════════════════════════════════════════════════════════════════════════

if not DISCORD_TOKEN or DISCORD_TOKEN == "YOUR_BOT_TOKEN_HERE":
    raise ValueError(
        "❌ DISCORD_TOKEN not set!\n"
        "   Set it: export DISCORD_TOKEN='your_token_here'"
    )

if ENV == Environment.PRODUCTION and DATABASE_URL.startswith("sqlite"):
    raise ValueError("❌ SQLite not allowed in production! Use PostgreSQL.")
