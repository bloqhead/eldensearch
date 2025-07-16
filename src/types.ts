export type Weapon = {
  id: number
  name: string
  tier: string
  category: string
  weaponType: string
  damageTypes: string[]
  scaling: {
    [key: string]: string
  }
  requirements: {
    [key: string]: number
  }
  skill: string
  skillDescription?: string
  stats: {
    [key: string]: number
  }
  weight: number
  durability?: number
  critical?: number
  range?: number
  attackSpeed?: string
  upgradePath?: string
  infusion?: string
  location?: string
  description?: string
  lore?: string
  dlc?: boolean
  dlcName?: string
  imageUrl?: string
  videoUrl?: string
  notes?: string[]
  buildRecommendations?: string[]
  pvpRating?: number
  pveRating?: number
  difficulty?: string
  unique?: boolean
  remembrance?: boolean
  legendary?: boolean
  specialEffects?: string[]
  statusEffects?: {
    [key: string]: number
  }
  guardBoost?: number
  guardDamageNegation?: {
    [key: string]: number
  }
  attackDamageNegation?: {
    [key: string]: number
  }
}