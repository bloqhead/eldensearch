export type Weapon = {
  id: number
  weapon: string
  tier: string
  scaling: [
    {
      [key: string]: string
    }
  ]
  skill: string
  stats: {
    [key: string]: number
  }
}