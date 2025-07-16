package models

import "time"

// Weapon represents a weapon in Elden Ring
type Weapon struct {
	ID          int       `json:"id"`
	Name        string    `json:"name"`
	Type        string    `json:"type"`
	Category    string    `json:"category"`
	Tier        string    `json:"tier,omitempty"`
	Skill       string    `json:"skill"`
	Weight      float64   `json:"weight"`
	Requirements Requirements `json:"requirements"`
	Scaling     Scaling   `json:"scaling"`
	Stats       Stats     `json:"stats"`
	AdditionalStats *AdditionalStats `json:"additional_stats,omitempty"`
	Description string    `json:"description"`
	Location    string    `json:"location"`
	ImageURL    string    `json:"image_url,omitempty"`
	CreatedAt   time.Time `json:"created_at"`
	UpdatedAt   time.Time `json:"updated_at"`
}

// Requirements represents the stat requirements to wield a weapon
type Requirements struct {
	Strength     int `json:"strength"`
	Dexterity    int `json:"dexterity"`
	Intelligence int `json:"intelligence"`
	Faith        int `json:"faith"`
	Arcane       int `json:"arcane"`
}

// Scaling represents how weapon damage scales with character stats
type Scaling struct {
	Strength     string `json:"strength"`
	Dexterity    string `json:"dexterity"`
	Intelligence string `json:"intelligence"`
	Faith        string `json:"faith"`
	Arcane       string `json:"arcane"`
}

// Stats represents the base damage and defense stats
type Stats struct {
	Physical     int `json:"physical"`
	Magic        int `json:"magic"`
	Fire         int `json:"fire"`
	Lightning    int `json:"lightning"`
	Holy         int `json:"holy"`
	Critical     int `json:"critical"`
	GuardBoost   int `json:"guard_boost"`
}

// AdditionalStats represents additional weapon properties and status effects
type AdditionalStats struct {
	BloodLoss    int    `json:"blood_loss"`
	Frost        int    `json:"frost"`
	Poison       int    `json:"poison"`
	ScarletRot   int    `json:"scarlet_rot"`
	Sleep        int    `json:"sleep"`
	Madness      int    `json:"madness"`
	Range        string `json:"range"`
	AttackSpeed  string `json:"attack_speed"`
	StaminaCost  string `json:"stamina_cost"`
}

// Category represents weapon categories
type Category struct {
	ID    string `json:"id"`
	Label string `json:"label"`
	Value string `json:"value"`
}

// APIResponse represents the standard API response format
type APIResponse struct {
	Success bool        `json:"success"`
	Data    interface{} `json:"data,omitempty"`
	Message string      `json:"message,omitempty"`
	Error   string      `json:"error,omitempty"`
}