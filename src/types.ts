export type Weapon = {
  id: number
  name: string
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