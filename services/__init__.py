# -*- coding: utf-8 -*-
"""
⚙️ services/__init__.py — Core Game Services
𝐝𝐞𝐯 𝐛𝐲 𝟕𝐚𝐦𝐨 © 2026
"""
from typing import Optional, Dict, List
import random
from datetime import datetime, timedelta

# ══════════════════════════════════════════════════════════════════════════════
# PLAYER SERVICE
# ══════════════════════════════════════════════════════════════════════════════

class PlayerService:
    """Manages player profile, XP, leveling, and statistics."""
    
    @staticmethod
    def calculate_next_level_xp(level: int, base_xp: int = 500, multiplier: float = 1.12) -> int:
        """Calculate XP required for next level."""
        return int(base_xp * (multiplier ** (level - 1)))
    
    @staticmethod
    def add_xp(current_xp: int, current_level: int, xp_to_add: int) -> tuple:
        """Add XP and handle leveling up."""
        new_xp = current_xp + xp_to_add
        new_level = current_level
        
        while new_xp >= PlayerService.calculate_next_level_xp(new_level):
            new_xp -= PlayerService.calculate_next_level_xp(new_level)
            new_level += 1
            if new_level > 100:
                new_level = 100
                new_xp = 0
                break
        
        return new_xp, new_level
    
    @staticmethod
    def decay_stats(stats: Dict[str, int]) -> Dict[str, int]:
        """Apply stat decay (hunger, thirst, hygiene)."""
        decay_rate = {
            "hunger": -5,
            "thirst": -5,
            "hygiene": -3,
            "happiness": -2,
            "energy": -1,
        }
        
        for stat, rate in decay_rate.items():
            if stat in stats:
                stats[stat] = max(0, min(100, stats[stat] + rate))
        
        return stats

# ══════════════════════════════════════════════════════════════════════════════
# ECONOMY SERVICE
# ══════════════════════════════════════════════════════════════════════════════

class EconomyService:
    """Manages money, banking, and transactions."""
    
    @staticmethod
    def add_money(wallet: int, amount: int, max_wallet: int = 1000000) -> int:
        """Add money to wallet (with cap)."""
        return min(wallet + amount, max_wallet)
    
    @staticmethod
    def deduct_money(wallet: int, amount: int) -> tuple:
        """Deduct money, return success and new wallet."""
        if wallet >= amount:
            return True, wallet - amount
        return False, wallet
    
    @staticmethod
    def transfer_to_bank(wallet: int, bank: int, amount: int) -> tuple:
        """Transfer from wallet to bank."""
        if wallet >= amount:
            return True, wallet - amount, bank + amount
        return False, wallet, bank
    
    @staticmethod
    def withdraw_from_bank(wallet: int, bank: int, amount: int) -> tuple:
        """Withdraw from bank to wallet."""
        if bank >= amount:
            return True, wallet + amount, bank - amount
        return False, wallet, bank
    
    @staticmethod
    def calculate_interest(bank: int, rate: float = 0.01) -> int:
        """Calculate daily bank interest."""
        return int(bank * rate)

# ══════════════════════════════════════════════════════════════════════════════
# JOB SERVICE
# ══════════════════════════════════════════════════════════════════════════════

class JobService:
    """Manages jobs, work, and employment."""
    
    JOBS = {
        "cashier": {
            "name": "أمين الصندوق",
            "en_name": "Cashier",
            "base_salary": 200,
            "xp_per_work": 25,
            "energy_cost": 25,
            "cooldown": 3,
            "required_level": 1,
        },
        "programmer": {
            "name": "مبرمج",
            "en_name": "Programmer",
            "base_salary": 500,
            "xp_per_work": 50,
            "energy_cost": 20,
            "cooldown": 4,
            "required_level": 10,
        },
        "manager": {
            "name": "مدير",
            "en_name": "Manager",
            "base_salary": 800,
            "xp_per_work": 75,
            "energy_cost": 30,
            "cooldown": 5,
            "required_level": 25,
        },
        "ceo": {
            "name": "رئيس تنفيذي",
            "en_name": "CEO",
            "base_salary": 2000,
            "xp_per_work": 150,
            "energy_cost": 40,
            "cooldown": 6,
            "required_level": 50,
        },
    }
    
    @staticmethod
    def calculate_salary(job: str, level: int = 1, multiplier: float = 1.0) -> int:
        """Calculate salary based on job and level."""
        job_data = JobService.JOBS.get(job, {})
        base = job_data.get("base_salary", 100)
        return int(base * (1 + level * 0.1) * multiplier)
    
    @staticmethod
    def can_work(energy: int, job: str) -> bool:
        """Check if player has enough energy."""
        job_data = JobService.JOBS.get(job, {})
        energy_cost = job_data.get("energy_cost", 20)
        return energy >= energy_cost
    
    @staticmethod
    def get_cooldown_remaining(last_work: datetime, cooldown_hours: int) -> int:
        """Get remaining cooldown in minutes."""
        cooldown = last_work + timedelta(hours=cooldown_hours)
        remaining = (cooldown - datetime.now()).total_seconds() / 60
        return max(0, int(remaining))

# ══════════════════════════════════════════════════════════════════════════════
# CRIME SERVICE
# ══════════════════════════════════════════════════════════════════════════════

class CrimeService:
    """Manages crimes, heists, and illegal activities."""
    
    CRIMES = {
        "pickpocket": {
            "name": "سرقة من الجيوب",
            "min_reward": 100,
            "max_reward": 500,
            "success_rate": 0.7,
            "danger": 2,
        },
        "burglary": {
            "name": "سرقة من المنازل",
            "min_reward": 1000,
            "max_reward": 5000,
            "success_rate": 0.5,
            "danger": 7,
        },
        "robbery": {
            "name": "السرقة المسلحة",
            "min_reward": 5000,
            "max_reward": 15000,
            "success_rate": 0.3,
            "danger": 10,
        },
    }
    
    @staticmethod
    def attempt_crime(crime: str, skill_level: int) -> tuple:
        """Attempt a crime and return success, reward, wanted_level."""
        crime_data = CrimeService.CRIMES.get(crime, {})
        base_success = crime_data.get("success_rate", 0.5)
        
        # Add skill bonus
        success_rate = min(0.95, base_success + (skill_level / 1000))
        
        if random.random() < success_rate:
            reward = random.randint(
                crime_data.get("min_reward", 100),
                crime_data.get("max_reward", 500)
            )
            wanted = 0
            return True, reward, wanted
        else:
            danger = crime_data.get("danger", 1)
            return False, 0, danger * random.randint(1, 3)

# ══════════════════════════════════════════════════════════════════════════════
# INVENTORY SERVICE
# ══════════════════════════════════════════════════════════════════════════════

class InventoryService:
    """Manages player inventory and items."""
    
    ITEMS = {
        "burger": {"name": "برجر", "rarity": "common", "price": 50},
        "sushi": {"name": "سوشي", "rarity": "uncommon", "price": 150},
        "laptop": {"name": "كمبيوتر محمول", "rarity": "rare", "price": 3000},
        "ring": {"name": "خاتم", "rarity": "legendary", "price": 50000},
    }
    
    @staticmethod
    def buy_item(item: str, quantity: int, wallet: int) -> tuple:
        """Buy items from inventory."""
        item_data = InventoryService.ITEMS.get(item, {})
        price = item_data.get("price", 0)
        total_cost = price * quantity
        
        if wallet >= total_cost:
            return True, wallet - total_cost
        return False, wallet
    
    @staticmethod
    def use_item(item: str) -> Dict[str, int]:
        """Use item and get effects."""
        effects = {
            "burger": {"hunger": 30},
            "sushi": {"hunger": 50},
            "laptop": {"programming_skill": 10},
            "ring": {"charisma": 20},
        }
        return effects.get(item, {})

# ══════════════════════════════════════════════════════════════════════════════
# WORLD EVENT SERVICE
# ══════════════════════════════════════════════════════════════════════════════

class EventService:
    """Manages random world events."""
    
    EVENTS = {
        "lottery_win": {
            "title": "🎰 لقيت بطاقة يانصيب رابحة!",
            "reward": 500,
            "probability": 0.05,
        },
        "robbery_victim": {
            "title": "😱 تم سرقتك!",
            "reward": -500,
            "probability": 0.03,
        },
        "bonus_xp": {
            "title": "⭐ حصلت على مكافأة XP!",
            "xp": 100,
            "probability": 0.08,
        },
        "energy_boost": {
            "title": "⚡ شعرت بطاقة جديدة!",
            "energy": 50,
            "probability": 0.06,
        },
    }
    
    @staticmethod
    def trigger_random_event() -> Optional[Dict]:
        """Randomly trigger an event."""
        for event_name, event_data in EventService.EVENTS.items():
            if random.random() < event_data.get("probability", 0):
                return {
                    "name": event_name,
                    **event_data
                }
        return None

# ══════════════════════════════════════════════════════════════════════════════
# SKILL SERVICE
# ══════════════════════════════════════════════════════════════════════════════

class SkillService:
    """Manages skill leveling and training."""
    
    @staticmethod
    def increase_skill(skill_level: int, xp_gained: int, max_level: int = 100) -> int:
        """Increase skill level based on XP."""
        new_level = skill_level + int(xp_gained / 50)
        return min(max_level, new_level)
    
    @staticmethod
    def get_skill_bonus(skill_level: int) -> float:
        """Get damage/success bonus from skill level."""
        return 1.0 + (skill_level / 100)

# ══════════════════════════════════════════════════════════════════════════════
# RELATIONSHIP SERVICE
# ══════════════════════════════════════════════════════════════════════════════

class RelationshipService:
    """Manages relationships and marriage."""
    
    @staticmethod
    def propose(player1_id: int, player2_id: int, ring_owned: bool = False) -> bool:
        """Propose marriage to another player."""
        if not ring_owned:
            return False
        # Further logic would go here
        return True
    
    @staticmethod
    def get_relationship_status(married_to: Optional[int]) -> str:
        """Get relationship status text."""
        if married_to:
            return "متزوج"
        return "عازب"
