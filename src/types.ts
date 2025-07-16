export type Weapon = {
  id: number
  name: string
  type: string
  category: string
  tier?: string
  skill: string
  weight: number
  requirements: {
    strength: number
    dexterity: number
    intelligence: number
    faith: number
    arcane: number
  }
  scaling: {
    strength: string
    dexterity: string
    intelligence: string
    faith: string
    arcane: string
  }
  stats: {
    physical: number
    magic: number
    fire: number
    lightning: number
    holy: number
    critical: number
    guard_boost: number
  }
  additional_stats?: {
    blood_loss: number
    frost: number
    poison: number
    scarlet_rot: number
    sleep: number
    madness: number
    range: string
    attack_speed: string
    stamina_cost: string
  }
  description: string
  location: string
  image_url?: string
  created_at: string
  updated_at: string
}

export type Category = {
  id: string
  label: string
  value: string
}

export type APIResponse<T> = {
  success: boolean
  data?: T
  message?: string
  error?: string
}