import type { Weapon } from '../types'

export const weapons: Weapon[] = [
  // DAGGERS
  {
    id: 1,
    name: "Dagger",
    tier: "Common",
    category: "Daggers",
    weaponType: "Dagger",
    damageTypes: ["Physical"],
    scaling: {
      "Strength": "D",
      "Dexterity": "C"
    },
    requirements: {
      "Strength": 5,
      "Dexterity": 9
    },
    skill: "Quick Step",
    skillDescription: "Quickly step behind or around the side of foes. Especially effective on foes with shields, and those who are guarding, and when it comes to circling around to their backs.",
    stats: {
      "Physical": 65,
      "Magic": 0,
      "Fire": 0,
      "Lightning": 0,
      "Holy": 0,
      "Critical": 110
    },
    weight: 1.0,
    critical: 110,
    range: 1,
    attackSpeed: "Fast",
    upgradePath: "Standard",
    location: "Starting weapon for Bandit class, or purchase from Twin Maiden Husks",
    description: "A standard dagger. Lightweight and quick, but lacks power. Effective for critical hits.",
    lore: "A simple dagger used by bandits and assassins throughout the Lands Between.",
    dlc: false,
    pvpRating: 6,
    pveRating: 5,
    difficulty: "Easy",
    unique: false,
    buildRecommendations: ["Critical hit builds", "Assassin builds", "Early game"]
  },
  {
    id: 2,
    name: "Black Knife",
    tier: "Legendary",
    category: "Daggers",
    weaponType: "Dagger",
    damageTypes: ["Physical", "Holy"],
    scaling: {
      "Strength": "E",
      "Dexterity": "C",
      "Faith": "D"
    },
    requirements: {
      "Strength": 6,
      "Dexterity": 12,
      "Faith": 18
    },
    skill: "Blade of Death",
    skillDescription: "Imbue the blade with the power of the Black Knife, dealing holy damage and reducing the target's maximum HP.",
    stats: {
      "Physical": 65,
      "Magic": 0,
      "Fire": 0,
      "Lightning": 0,
      "Holy": 78,
      "Critical": 110
    },
    weight: 2.0,
    critical: 110,
    range: 1,
    attackSpeed: "Fast",
    upgradePath: "Unique",
    location: "Dropped by Black Knife Assassin in Altus Plateau",
    description: "A legendary dagger that belonged to the Black Knife Assassins. Its skill reduces enemy max HP.",
    lore: "The Black Knife Assassins were a group of killers who used the power of the Rune of Death to slay the demigods.",
    dlc: false,
    pvpRating: 9,
    pveRating: 8,
    difficulty: "Medium",
    unique: true,
    legendary: true,
    specialEffects: ["Reduces target max HP", "Holy damage"],
    buildRecommendations: ["Faith/Dexterity builds", "Assassin builds", "PvP builds"]
  },
  {
    id: 3,
    name: "Reduvia",
    tier: "Rare",
    category: "Daggers",
    weaponType: "Dagger",
    damageTypes: ["Physical", "Blood"],
    scaling: {
      "Strength": "E",
      "Dexterity": "C",
      "Arcane": "D"
    },
    requirements: {
      "Strength": 5,
      "Dexterity": 13,
      "Arcane": 13
    },
    skill: "Reduvia Blood Blade",
    skillDescription: "Launch a blade of blood from the dagger. The blade deals blood loss build-up and can be fired repeatedly.",
    stats: {
      "Physical": 79,
      "Magic": 0,
      "Fire": 0,
      "Lightning": 0,
      "Holy": 0,
      "Critical": 110
    },
    weight: 2.5,
    critical: 110,
    range: 1,
    attackSpeed: "Fast",
    upgradePath: "Unique",
    location: "Dropped by Bloody Finger Nerijus in Limgrave",
    description: "A dagger that causes blood loss. Its skill fires blood blades.",
    lore: "A dagger that drips with blood. Used by the Bloody Fingers to hunt Tarnished.",
    dlc: false,
    pvpRating: 8,
    pveRating: 7,
    difficulty: "Medium",
    unique: true,
    specialEffects: ["Blood loss build-up", "Ranged blood blade skill"],
    statusEffects: {
      "Blood Loss": 50
    },
    buildRecommendations: ["Arcane/Dexterity builds", "Blood loss builds", "Early game"]
  }
]