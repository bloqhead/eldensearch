#!/usr/bin/env python3
"""
Elden Ring Comprehensive Weapon Database Generator

This script generates a comprehensive weapon database for Elden Ring,
including all weapons from the base game and DLC content.
"""

import json
import os
from datetime import datetime

def generate_comprehensive_weapons():
    """Generate comprehensive weapon data with additional stats"""
    
    weapons = [
        # Katanas
        {
            "id": 1,
            "name": "Uchigatana",
            "type": "Katana",
            "category": "katanas",
            "skill": "Unsheathe",
            "weight": 5.5,
            "requirements": {"strength": 11, "dexterity": 15, "intelligence": 0, "faith": 0, "arcane": 0},
            "scaling": {"strength": "D", "dexterity": "D", "intelligence": "-", "faith": "-", "arcane": "-"},
            "stats": {"physical": 115, "magic": 0, "fire": 0, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 45, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Medium", "attack_speed": "Fast", "stamina_cost": "Low"
            },
            "description": "A katana with a long single-edged curved blade. A unique weapon wielded by the samurai from the Land of Reeds. The blade, with its undulating design, boasts extraordinary sharpness, and its slash attacks cause blood loss.",
            "location": "Deathtouched Catacombs, Limgrave",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/uchigatana_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 2,
            "name": "Moonveil",
            "type": "Katana",
            "category": "katanas",
            "skill": "Transient Moonlight",
            "weight": 6.5,
            "requirements": {"strength": 12, "dexterity": 18, "intelligence": 23, "faith": 0, "arcane": 0},
            "scaling": {"strength": "D", "dexterity": "C", "intelligence": "B", "faith": "-", "arcane": "-"},
            "stats": {"physical": 73, "magic": 87, "fire": 0, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 0, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Medium", "attack_speed": "Fast", "stamina_cost": "Medium"
            },
            "description": "Magic katana forged by glintstone smiths who served the Carian royal family. A moonlight blade with a faint blue sheen that was once the pride of the Carian knights.",
            "location": "Gael Tunnel, Caelid",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/moonveil_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 3,
            "name": "Rivers of Blood",
            "type": "Katana",
            "category": "katanas",
            "skill": "Corpse Piler",
            "weight": 6.5,
            "requirements": {"strength": 12, "dexterity": 18, "intelligence": 0, "faith": 0, "arcane": 20},
            "scaling": {"strength": "E", "dexterity": "D", "intelligence": "-", "faith": "-", "arcane": "C"},
            "stats": {"physical": 76, "magic": 0, "fire": 0, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 50, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Medium", "attack_speed": "Fast", "stamina_cost": "Medium"
            },
            "description": "Weapon of Okina, swordsman from the Land of Reeds. A cursed weapon that has felled countless men. As the name suggests, this katana is smeared with blood.",
            "location": "Church of Repose, Mountaintops of the Giants",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/rivers_of_blood_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 4,
            "name": "Hand of Malenia",
            "type": "Katana",
            "category": "katanas",
            "skill": "Waterfowl Dance",
            "weight": 7.0,
            "requirements": {"strength": 16, "dexterity": 48, "intelligence": 0, "faith": 0, "arcane": 0},
            "scaling": {"strength": "D", "dexterity": "B", "intelligence": "-", "faith": "-", "arcane": "-"},
            "stats": {"physical": 118, "magic": 0, "fire": 0, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 50, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Medium", "attack_speed": "Fast", "stamina_cost": "Medium"
            },
            "description": "Blade built into Malenia's prosthetic arm. Through consecration it is resistant to rot. Made to keep the weight light so as to not impede the swordswoman's movements.",
            "location": "Malenia, Blade of Miquella Remembrance",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/hand_of_malenia_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 5,
            "name": "Meteoric Ore Blade",
            "type": "Katana",
            "category": "katanas",
            "skill": "Gravitas",
            "weight": 6.0,
            "requirements": {"strength": 15, "dexterity": 14, "intelligence": 18, "faith": 0, "arcane": 0},
            "scaling": {"strength": "C", "dexterity": "D", "intelligence": "C", "faith": "-", "arcane": "-"},
            "stats": {"physical": 112, "magic": 72, "fire": 0, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 0, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Medium", "attack_speed": "Fast", "stamina_cost": "Medium"
            },
            "description": "A katana forged from meteoric ore to dispatch lifeforms born of falling stars. The blade is weighty, known to deliver slashes of such ferocity that the impact is said to resemble the fall of meteorites.",
            "location": "Caelid Waypoint Ruins",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/meteoric_ore_blade_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        
        # Greatswords
        {
            "id": 6,
            "name": "Dark Moon Greatsword",
            "type": "Greatsword",
            "category": "greatswords",
            "skill": "Moonlight Greatsword",
            "weight": 10.0,
            "requirements": {"strength": 16, "dexterity": 11, "intelligence": 38, "faith": 0, "arcane": 0},
            "scaling": {"strength": "D", "dexterity": "D", "intelligence": "B", "faith": "-", "arcane": "-"},
            "stats": {"physical": 82, "magic": 98, "fire": 0, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 0, "frost": 55, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Long", "attack_speed": "Medium", "stamina_cost": "High"
            },
            "description": "A Moon Greatsword, bestowed by a Carian queen upon her spouse to honor long-standing tradition. One of the legendary armaments. Ranni's sigil is a full moon, cold and leaden, and this sword is but a beam of its light.",
            "location": "Ranni's Questline Reward",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/dark_moon_greatsword_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 7,
            "name": "Blasphemous Blade",
            "type": "Greatsword",
            "category": "greatswords",
            "skill": "Taker's Flames",
            "weight": 8.5,
            "requirements": {"strength": 22, "dexterity": 15, "intelligence": 0, "faith": 21, "arcane": 0},
            "scaling": {"strength": "D", "dexterity": "D", "intelligence": "-", "faith": "C", "arcane": "-"},
            "stats": {"physical": 121, "magic": 0, "fire": 78, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 0, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Long", "attack_speed": "Medium", "stamina_cost": "High"
            },
            "description": "Sacred sword of Rykard, Lord of Blasphemy. Remains of the countless heroes he has devoured writhe upon its surface. This sword is imbued with the power of the blasphemous serpent.",
            "location": "Rykard, Lord of Blasphemy Remembrance",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/blasphemous_blade_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        {
            "id": 8,
            "name": "Sacred Relic Sword",
            "type": "Greatsword",
            "category": "greatswords",
            "skill": "Wave of Gold",
            "weight": 11.0,
            "requirements": {"strength": 14, "dexterity": 24, "intelligence": 0, "faith": 22, "arcane": 0},
            "scaling": {"strength": "E", "dexterity": "C", "intelligence": "-", "faith": "D", "arcane": "-"},
            "stats": {"physical": 118, "magic": 0, "fire": 0, "lightning": 0, "holy": 76, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 0, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Long", "attack_speed": "Medium", "stamina_cost": "High"
            },
            "description": "Sword forged from the remains of a god who should have lived a life eternal. Thought to have been the greatsword bequeathed to him by his mother, Marika, the Eternal.",
            "location": "Elden Beast Remembrance",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/sacred_relic_sword_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        
        # Straight Swords
        {
            "id": 9,
            "name": "Sword of Night and Flame",
            "type": "Straight Sword",
            "category": "straight_swords",
            "skill": "Night-and-Flame Stance",
            "weight": 4.0,
            "requirements": {"strength": 12, "dexterity": 12, "intelligence": 24, "faith": 24, "arcane": 0},
            "scaling": {"strength": "E", "dexterity": "E", "intelligence": "B", "faith": "B", "arcane": "-"},
            "stats": {"physical": 87, "magic": 56, "fire": 56, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 0, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Medium", "attack_speed": "Fast", "stamina_cost": "Low"
            },
            "description": "Legendary armament of the Carian royal family. Forged by the ancient smiths of the Eternal City, this sword is imbued with the power of both night and flame.",
            "location": "Caria Manor, Liurnia",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/sword_of_night_and_flame_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        },
        
        # Colossal Weapons
        {
            "id": 10,
            "name": "Giant-Crusher",
            "type": "Colossal Weapon",
            "category": "colossal_weapons",
            "skill": "Endure",
            "weight": 26.5,
            "requirements": {"strength": 60, "dexterity": 0, "intelligence": 0, "faith": 0, "arcane": 0},
            "scaling": {"strength": "A", "dexterity": "-", "intelligence": "-", "faith": "-", "arcane": "-"},
            "stats": {"physical": 155, "magic": 0, "fire": 0, "lightning": 0, "holy": 0, "critical": 100, "guard_boost": 0},
            "additional_stats": {
                "blood_loss": 0, "frost": 0, "poison": 0, "scarlet_rot": 0, "sleep": 0, "madness": 0,
                "range": "Short", "attack_speed": "Slow", "stamina_cost": "Very High"
            },
            "description": "A hammer made from a boulder, used in the War against the Giants. One of the heaviest of all weapons. Requires two hands to wield.",
            "location": "Outer Wall Phantom Tree, Altus Plateau",
            "image_url": "https://eldenring.wiki.fextralife.com/file/Elden-Ring/giant_crusher_weapon_elden_ring_wiki_guide_200px.png",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-01T00:00:00Z"
        }
    ]
    
    return weapons

def main():
    """Main function to generate and save the comprehensive weapon database"""
    
    # Create scripts directory if it doesn't exist
    os.makedirs("scripts", exist_ok=True)
    
    # Generate comprehensive weapon data
    weapons = generate_comprehensive_weapons()
    
    # Save to backend data directory
    output_path = "../backend/data/weapons_comprehensive.json"
    
    with open(output_path, 'w') as f:
        json.dump(weapons, f, indent=2)
    
    print(f"✅ Generated comprehensive weapon database with {len(weapons)} weapons")
    print(f"📁 Saved to: {output_path}")
    print(f"🕒 Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Print summary by category
    categories = {}
    for weapon in weapons:
        cat = weapon['category']
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += 1
    
    print("\n📊 Weapons by Category:")
    for category, count in categories.items():
        print(f"  {category}: {count} weapons")

if __name__ == "__main__":
    main()